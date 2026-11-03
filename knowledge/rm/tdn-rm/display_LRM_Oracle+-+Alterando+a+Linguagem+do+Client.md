---
content_hash: d937fa2944cebb570d4aa12e5862d95992897797ac24c14815c6b7b624e8644e
fetched_at: '2026-06-29T00:10:35.588679+00:00'
page_id: '531022507'
product: rm
source: tdn-rm
title: Oracle - Alterando a Linguagem do Client
type: documentation
url: https://tdn.totvs.com/display/LRM/Oracle+-+Alterando+a+Linguagem+do+Client
version: 3
---

WE8ISO8859P15

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Banco de Dados |
| **Versão RM** | : | Qualquer Versão |
| **Banco de Dados** | : | Oracle |
| **Processo** | : | Alterando a Linguagem do Client |
| **Sub Processo** | : | Manutenção |

---

**NLS\_DATABASE\_PARAMETERS**

No padrão Corpore a linguagem padrão para o SGBD Oracle é o NLS\_LANG **WE8ISO8859P15**. Certifique que a linguagem do Oracle da estação esteja igual a do servidor.   
  
Para isso, execute na estação a seguinte consulta:

*SELECT \* FROM NLS\_DATABASE\_PARAMETERS (irá listar a linguagem do servidor)*  
*SELECT \* FROM NLS\_SESSION\_PARAMETERS (irá listar a linguagem da estação)*

No caso de estarem diferentes do padrão, siga os passos do exemplo abaixo:

Na instalação do Oracle o idioma escolhido foi Brazilian e deveria ser American na estação, conforme o servidor.

Recomendamos que os passos abaixo sejam aplicados pelo DBA ou responsável pelo Banco de Dados da empresa:  
  
a) Acessar o regedit;  
b) Localizar a home do Oracle:

*HKEY\_LOCAL\_MACHINE\SOFTWARE\ORACLE\KEY\_OraDb\_home1*  
*HKEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Oracle\KEY\_OraDb\_home1*  
  
c) Incluir a chave *NLS\_DATE\_FORMAT* com o valor DD/MM/YYYY.  
d) Acertar o parâmetro *NLS\_LANG* para AMERICAN\_AMERICA.WE8ISO8859P15;  
  
Por que fazer isso:  
  
A exceção do Oracle **ORA-01843** normalmente é apresentada no CorporeRM, quando a parametrização de Formato de Data ou Linguagem está fora do padrão recomendado pela Totvs.  
Caso utilize ambiente 3 camadas, a alteração deve ser realizada no Servidor de APP.  
  
  
Caso a inconsistência persista, favor incluir a tag <add key="ORACLELANGUAGE" value="pt-BR" />. Configuração para alterar o idioma da sessão de conexão com o Oracle  
O idioma da sessão de conexão do RM com uma base Oracle pode ser alterar através da tag de configuração chamara OracleLanguage no arquivo RM.exe.config:  
  
*<add key="OracleLanguage" value="en-US" />*  
  
O valor padrão desta chave é pt-BR. O sistema deve considerar a linguagem en-US do banco Oracle para na configuração do Server utilizando a tag ORACLELANGUAGE.   
  
Após inserir a tag, reinicie o serviço de host, reabra a aplicação e execute o processo novamente.  
  
Observações:

* Só devem ser alterados os parâmetros NLS\_LANG listados que tiverem com o valor Brazilian, os registros que estiverem com N/A não devem ser alterados.
* Essa inconsistência pode ser apresentada por outros motivos, sendo assim, caso a inconsistência persista, recomendamos um contato com o suporte do módulo onde o erro foi apresentado
