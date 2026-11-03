---
content_hash: ac3a9bf706064c6e4ea1d7bcd84c7026553a0e1de04e3880b9b4640cb0d359a6
fetched_at: '2026-06-29T00:09:35.876964+00:00'
page_id: '425459407'
product: rm
source: tdn-rm
title: Backoffice Protheus x TOTVS Incorporação - Pré-Requisitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459407
version: 4
---

**Pré-Requisitos da Integração Backoffice Protheus x TOTVS Incorporação**

---

Para a utilização da integração Backoffice Protheus x TOTVS Incorporação é necessário que as pré-condições abaixo sejam  atendidas.  
     
 **Pré-requisitos RM**  
     
 1- Ter restaurado uma base de dados Sql Server ou Oracle com a versão  11.82.26.108 ou superior  
 2- Ter instalado a Biblioteca RM com a versão  11.82.26.108 ou superior  
 3- Ter instalado e configurado o Webservice da Integração através do TOTVS Business Connect com a versão  11.82.26.108 ou superior  
     
 **Pré-requisitos Protheus**  
    
 1- Ter criado uma base de dados  sem tabelas  
 2- -Ter criado uma fonte de dados ODBC para bases de dados Sql Server.  
 3- Ter instalado o TOTVS DBAccess  
 4- Ter instalado o sistema TOTVS Protheus na versão  11.7 ou superior  
 5- Ter configurado o arquivo de configuração do Protheus(appserver.ini)  
 6- Ter incluído no arquivo de configuração do Protheus as informações do Webservice do EAI(http)  
 7- Criar a configuração do TOTVS DBAccess utilizando o mesmo nome do ambiente Protheus informado no arquivo de configuração appserver.ini  
    
 **Observação:** Para base de dados Oracle, é necessária a configuração do arquivo de configuração do TOTVS DBAccess, informando o caminho do arquivo oci.dll do SGBD Oracle.
