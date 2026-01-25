import pandas as pd
import psycopg2
from psycopg2 import sql

# CSV 파일 읽기
csv_file = r"c:\Python\work\표준도메인(7차-2024).csv"
df = pd.read_csv(csv_file, sep='^', encoding='utf-8')

# 데이터프레임 정보 출력
print("CSV 파일 로드 완료")
original_rows = len(df)
print(f"원본 행 수: {original_rows}")
print(f"컬럼: {list(df.columns)}")
print(f"컬럼 수: {len(df.columns)}")

# 데이터 정제: 'no' 컬럼이 숫자가 아니면 제거
print(f"\n데이터 정제 시작...")

try:
    df['no'] = pd.to_numeric(df['no'], errors='coerce')
    df = df.dropna(subset=['no']).reset_index(drop=True)
    df['no'] = df['no'].astype(int)
except Exception as e:
    print(f"정제 오류: {e}")

print(f"정제 후 행 수: {len(df)}")
print(f"제거된 행: {original_rows - len(df)}")
print(f"\n정제된 데이터 첫 3행:\n{df.head(3)}")

# PostgreSQL 연결 정보
conn_params = {
    'host': 'localhost',
    'port': 25433,
    'database': 'postgres',
    'user': 'postgres',
    'password': 'dhwoan'
}

# 테이블 이름과 스키마
schema = 'std_db'
table_name = 'standard_domains'

try:
    # PostgreSQL 연결
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    print(f"\nPostgreSQL 연결 성공")
    
    # 스키마 생성 (이미 존재하면 무시)
    cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema};")
    print(f"스키마 '{schema}' 준비 완료")
    
    # 기존 테이블이 있으면 삭제
    cursor.execute(f"DROP TABLE IF EXISTS {schema}.{table_name};")
    print(f"기존 테이블 삭제 완료")
    
    # SQL 테이블 생성 쿼리
    create_table_query = f"""
    CREATE TABLE {schema}.{table_name} (
        no INTEGER PRIMARY KEY,
        turns VARCHAR(50),
        domain_grp VARCHAR(100),
        domain_clsf VARCHAR(100),
        domain_nm VARCHAR(100),
        domain_expln TEXT,
        dt_type VARCHAR(50),
        dt_size VARCHAR(50),
        dt_dcpt_len VARCHAR(50),
        save_type VARCHAR(100),
        frm VARCHAR(100),
        unit VARCHAR(50),
        prm_vl VARCHAR(255)
    );
    """
    
    cursor.execute(create_table_query)
    conn.commit()
    print(f"테이블 '{schema}.{table_name}' 생성 완료")
    
    # 데이터 삽입
    insert_query = f"""
    INSERT INTO {schema}.{table_name} 
    (no, turns, domain_grp, domain_clsf, domain_nm, domain_expln, dt_type, dt_size, dt_dcpt_len, save_type, frm, unit, prm_vl)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    success_count = 0
    error_count = 0
    
    # 처리할 컬럼명 (마지막 두 개의 빈 컬럼 제외)
    columns_to_use = df.columns[:13]  # 첫 13개 컬럼만 사용
    
    # 데이터프레임의 데이터를 튜플로 변환하여 삽입
    for idx, row in df[columns_to_use].iterrows():
        try:
            # NaN 값을 None으로 변환
            data = tuple(None if pd.isna(x) else x for x in row)
            cursor.execute(insert_query, data)
            success_count += 1
        except Exception as e:
            error_count += 1
            print(f"행 {idx} 삽입 실패: {e}")
    
    conn.commit()
    print(f"\n데이터 삽입 완료")
    print(f"성공: {success_count}행, 실패: {error_count}행")
    
    # 테이블 확인
    cursor.execute(f"SELECT COUNT(*) FROM {schema}.{table_name};")
    count = cursor.fetchone()[0]
    print(f"\n테이블 '{schema}.{table_name}'의 총 행 수: {count}")
    
    # 샘플 데이터 확인
    cursor.execute(f"SELECT no, domain_nm, domain_grp, dt_type FROM {schema}.{table_name} LIMIT 3;")
    rows = cursor.fetchall()
    print(f"\n샘플 데이터 (처음 3행):")
    for row in rows:
        print(f"  번호: {row[0]}, 도메인: {row[1]}, 그룹: {row[2]}, 타입: {row[3]}")
    
    cursor.close()
    conn.close()
    print("\n✅ PostgreSQL 연결 종료 - 작업 완료!")
    
except psycopg2.Error as e:
    print(f"❌ PostgreSQL 오류: {e}")
except Exception as e:
    print(f"❌ 오류 발생: {e}")
