---
content_hash: 5a70f72df94b111dc61091f799a3051fc0876f770c0f6bfedf59e7c182fba6c4
fetched_at: '2026-06-29T00:10:58.835040+00:00'
page_id: '607330690'
product: rm
source: tdn-rm
title: Habilitando criptografia SSL entre o Totvs e o banco de dados Oracle
type: documentation
url: https://tdn.totvs.com/display/LRM/Habilitando+criptografia+SSL+entre+o+Totvs+e+o+banco+de+dados+Oracle
version: 4
---

Para habilitar a criptografia SSL entre o Totvs e o banco de dados Oracle é necessário configurar os seguintes passos:

1- Configurar o banco de dados para trafegar informações via protocolo SSL, este passo é feito através do service, do listener e da wallet.

2- Utilizar um certificado digital assinado por uma autoridade certificadora (CA).

3- Estar o tempo todo com a Wallet aberta, em estado OPEN.

4- Configurar o client na máquina do cliente com os mesmos arquivos e certificados da wallet do servidor.

Habilitando a criptografia SSL.

* Listener

* Service

* Profile - Authentication

* Profile - Other Params

* Profile - Integrity

* Profile - Encryption

* Profile - SSL

\*Colocar no campo Wallet Directory: O diretório da wallet com o certificado.

**WALLET**

Criar uma pasta e colocar o certificado dentro dela.

Indicar nos comandos de criação de KEY esta mesma pasta.

* **ADMINISTER KEY MANAGEMENT CREATE KEYSTORE '**C:\Wallet**' IDENTIFIED BY TOTVS12345;**
* **ADMINISTER KEY MANAGEMENT SET KEYSTORE OPEN IDENTIFIED BY TOTVS12345; (**comando para abrir a WALLET, ela deve estar aberta o tempo todo para que a criptografia funcione**).**

Com o comando: select \* from v$encryption\_wallet; É possivel checar o status da wallet.

**CONFIGURAÇÕES DO LADO DO CLIENT.**

Baixar e instalar o client do Oracle de mesma versão e adicionar o Oracle Net Manager:

Configurar o Oracle Net Manager na aba SSL, com o diretório do wallet e o radio button "Cliente".

* Na pasta wallet deve estar o mesmo certificado que na wallet do servidor.

**Referências:**

**Comandos úteis:**

sqlplus /nolog

conn sys/TOTVS@EXEMPLO1 as sysdba

select \* from v$encryption\_wallet;

ADMINISTER KEY MANAGEMENT SET KEYSTORE OPEN IDENTIFIED BY TOTVS12345;

ADMINISTER KEY MANAGEMENT CREATE KEYSTORE 'C:\Users\engenhariasoftware\Downloads\ORACLE\admin\EXEMPLO1\Wallet' IDENTIFIED BY TOTVS12345;

ADMINISTER KEY MANAGEMENT SET KEY IDENTIFIED BY TOTVS12345 WITH BACKUP USING 'tde\_key\_backup';

**Links para documentação de referência:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=543078195>

<https://docs.oracle.com/cd/F49540_01/DOC/network.815/a67766/09_ssl.htm#1010933>

<https://cloudstacks.wordpress.com/2016/12/22/ora-28353-failed-to-open-wallet/>
