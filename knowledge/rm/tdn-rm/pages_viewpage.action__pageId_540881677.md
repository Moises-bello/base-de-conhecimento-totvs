---
content_hash: e842d1f61735052424d274dfb1ab0c185112a41c75be37ca1893f158e6008eb8
fetched_at: '2026-06-29T00:10:37.703012+00:00'
page_id: '540881677'
product: rm
source: tdn-rm
title: Instalação e configuração do TDE no SQL Server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540881677
version: 6
---

Para avaliar a viabilidade de utilização do TDE (Transparent Data Encrytion) no SQL Server com os produtos da Linha RM utilizamos a configuração a seguir.

Existem outras formas de configuração, armazenamento das chaves de criptografia e instalação do SGBD. Não é objetivo deste documento capacitar para instalação ou configuração do TDE, se atendo apenas na apresentação do ambiente avaliado.

## Configuração do ambiente avaliado

* Crie uma chave mestra

| USE master;  GO  CREATE MASTER KEY ENCRYPTION BY PASSWORD = '<UseStrongPasswordHere>';  GO |
| --- |

* Crie ou obtenha um certificado protegido pela chave mestra

| CREATE CERTIFICATE MyServerCert WITH SUBJECT = 'My DEK Certificate';  GO |
| --- |

* Crie uma chave de criptografia de banco de dados e proteja-a com o certificado

| USE Nome\_da\_base\_de\_dados;  GO  CREATE DATABASE ENCRYPTION KEY WITH ALGORITHM = AES\_128 ENCRYPTION BY SERVER CERTIFICATE MyServerCert;  GO |
| --- |

* Defina o banco de dados para usar criptografia

| ALTER DATABASE Nome\_da\_base\_de\_dados SET ENCRYPTION ON;  GO |
| --- |

Feito isso, é possível verificar a criptografia utilizando o seguinte comando:

| SELECT name, encryption\_state, encryptor\_type  FROM sys.dm\_database\_encryption\_keys a, sys.databases b  WHERE a.database\_id = b.database\_id |
| --- |

Também é possível realizar o backup do certificado. Para isso, rode o script a seguir, alterando os caminhos especificados para o local em que será armazenado o backup:

| BACKUP CERTIFICATE CertificadoProd TO FILE = 'C:\MSSQL\certificate\CertificadoProd’  WITH PRIVATE KEY (file='C:\MSSQL\certificate\CertificadoProd.pvk',  ENCRYPTION BY PASSWORD='<UseStrongPasswordHere>')  GO |
| --- |

Para mais informações sobre essa funcionalidade, favor consultar a página: <https://docs.microsoft.com/pt-br/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver15>
