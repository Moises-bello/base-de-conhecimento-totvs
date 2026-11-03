---
content_hash: 432a9a2c29d10ac0bdb8ffd99e818bf02ae6fbb22fe0da67ba4df562df17ebaa
fetched_at: '2026-06-29T00:10:38.037681+00:00'
page_id: '543077424'
product: rm
source: tdn-rm
title: Instalação e configuração do TDE no Oracle 11G
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543077424
version: 11
---

Para avaliar a viabilidade de utilização do TDE (Transparent Data Encrytion) no Oracle12c e 18c com os produtos da Linha RM utilizamos a configuração a seguir.

Existem outras formas de configuração, armazenamento das chaves de criptografia e instalação do Oracle. Não é objetivo deste documento capacitar para instalação ou configuração do TDE, se atendo apenas na apresentação do ambiente avaliado.

## Configuração do ambiente avaliado

* **Criação da carteira**

 Adicionar o parâmetro `WALLET_LOCATION`no arquivo sqlnet.ora.

| WALLET\_LOCATION= (SOURCE=(METHOD=FILE)(METHOD\_DATA= (DIRECTORY=C:\app\leonardo.costa\admin\orcl\wallet))) |
| --- |

Este parâmetro também pode ser usado para identificar o local da carteira.

* **O comando a seguir cria e abre a carteira.**

| ```  CONN bh-eng-vm04/ORCL AS SYSDBA ALTER SYSTEM SET ENCRYPTION KEY IDENTIFIED BY "myPassword"; ``` |
| --- |

* **As carteiras devem ser reabertas após o reinício de uma instância e podem****ser**

**fechadas para impedir o acesso**

**ao****dados criptografados.**

| ```  ALTER SYSTEM SET ENCRYPTION WALLET OPEN IDENTIFIED BY "myPassword";  ALTER SYSTEM SET ENCRYPTION WALLET CLOSE; ``` |
| --- |

* **Criar a tablespaces**

 A instrução a seguir cria um espaço de tabela criptografado nomeando explicitamente o algoritmo de criptografia

'AES256' na `USING`cláusula

| CREATE TABLESPACE RM\_DADOS DATAFILE 'C:\app\leonardo.costa\admin\orcl\adump\RMDADOS1.DAT' SIZE 120M AUTOEXTEND ON NEXT 10M ENCRYPTION USING 'AES256' DEFAULT STORAGE ( ENCRYPT ); |
| --- |

* **Comando para visualizar as tablespaces que utilizam encrypted na tabela que está ou não criptografado**

|  |
| --- |

**Por critério de segurança se carteira estiver fechada não será possível realizar o expdp:**

Para mais informações sobre essa funcionalidade, favor consultar a página: <https://oracle-base.com/articles/11g/tablespace-encryption-11gr1#tablespace_creation>
