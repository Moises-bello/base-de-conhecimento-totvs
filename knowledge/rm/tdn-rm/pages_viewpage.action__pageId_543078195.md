---
content_hash: 50b11796a6a5d6472bd7cf4aaa2373ca2d1a5ffede5d26d3f4c46e6de9a00a51
fetched_at: '2026-06-29T00:10:38.042588+00:00'
page_id: '543078195'
product: rm
source: tdn-rm
title: Instalação e configuração do TDE  no Oracle 12c e 18c
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543078195
version: 5
---

Para avaliar a viabilidade de utilização do TDE (Transparent Data Encrytion) no Oracle12c e 18c com os produtos da Linha RM utilizamos a configuração a seguir.

Existem outras formas de configuração, armazenamento das chaves de criptografia e instalação do Oracle. Não é objetivo deste documento capacitar para instalação ou configuração do TDE, se atendo apenas na apresentação do ambiente avaliado.

## Configuração do ambiente avaliado

* **Criação da carteira**

 Adicionar o parâmetro encryotion\_`WALLET_LOCATION`no arquivo sqlnet.ora.

| ENCRYPTION\_WALLET\_LOCATION = (SOURCE =(METHOD = FILE)(METHOD\_DATA = (DIRECTORY = C:\app\leonardo.costa\virtual\oradata\RM\wallet))) |
| --- |

Este parâmetro também pode ser usado para identificar o local da carteira.

* ****O comando a seguir cria e abre a carteira.****

| ADMINISTER KEY MANAGEMENT CREATE KEYSTORE 'C:\app\leonardo.costa\virtual\oradata\RM\wallet' IDENTIFIED BY TOTVS12345; |
| --- |

* **As carteiras devem ser reabertas após o reinício de uma instância e podem****ser****fechadas para impedir o acesso****ao****dados criptografados.**

| ADMINISTER KEY MANAGEMENT SET KEYSTORE OPEN IDENTIFIED BY TOTVS12345;  ADMINISTER KEY MANAGEMENT SET KEYSTORE CLOSE IDENTIFIED BY TOTVS12345; |
| --- |

* **Verificar o status da carteira**

|  |
| --- |

* **Criar a tablespaces**

 A instrução a seguir cria um espaço de tabela criptografado nomeando explicitamente o algoritmo de criptografia

'AES256' na `USING`cláusula

| **CREATE TABLESPACE TOTVSAUDIT\_DADOS** **DATAFILE 'C:\app\leonardo.costa\virtual\admin\rm\adump\TOTVSAUDITDADOS1.DAT' SIZE 120M AUTOEXTEND ON NEXT 10M** **ENCRYPTION USING 'AES256'** **DEFAULT STORAGE ( ENCRYPT );** |
| --- |

* **Comando para visualizar as tablespaces que utilizam encrypted na tabela que está ou não criptografado**

|  |
| --- |

Para mais informações sobre essa funcionalidade, favor consultar a página:<https://docs.oracle.com/database/121/ASOAG/configuring-transparent-data-encryption.htm#ASOAG10285>
