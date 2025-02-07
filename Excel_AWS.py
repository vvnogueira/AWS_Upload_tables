import pandas as pd
import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# Carregar o arquivo Excel
df = pd.read_excel('C:/Users/Acer/Documents/Projeto_GIT/salary_data.xlsx')

# Exibir as primeiras 5 linhas para verificar
print(df.head())

# Salvar o DataFrame em um arquivo temporário (por exemplo, arquivo Excel)
output_file = 'C:/Users/Acer/Documents/Projeto_GIT/temp_file.xlsx'
df.to_csv(output_file, index=False)

# Criando um s3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
)

print("Escrevendo no posts no AWS")
bucket_name = os.environ.get("AWS_S3_BUCKET_NAME")
s3.upload_file(output_file,bucket_name, f"Arquivos/excel")

# Excluir o arquivo temporário após o upload (se não for necessário mais)
import os
os.remove(output_file)

print("Arquivo carregado com sucesso no S3!")