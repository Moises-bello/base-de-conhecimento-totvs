---
content_hash: 4bf78c106916f59b22d48cab01af439d903ce954920d178903384280eda9688f
fetched_at: '2026-07-02T19:24:20.407620+00:00'
page_id: '244933014'
product: protheus
source: tdn-tec
title: Configuração para uso do codepage 1251
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244933014
version: 7
---

|  |  |
| --- | --- |
| Descrição | Russian - howto |
| Observações | Este documento explica como como configurar o true, true e true. |

**Configuração do true**

| Configuração | Observação |
| --- | --- |
| RPOLanguage=russian | O valor preferencialmente deve ser lower case. |
| StringCodePage=1 | Utilizado em funções que manipulam string. |

**Configuração do true**

* Para utilizar o true com ODBC, não há necessidade de configuração adicional.
* Para utilizar o true com a OCI do Oracle, foram criadas 3 chaves no arquivo de configuração do DBAccess, que obrigatoriamente devem estar dentro da seção ORACLE:

| Configuração | Observação |
| --- | --- |
| CODEPAGE=CL8MSWIN1251 | Configura no nível da OCI o codepage como CP1251. |
| ALTERSESSION=SET nls\_language='RUSSIAN' nls\_sort='BINARY' | Esta chave tem influência no idioma das strings que são retornadas pela OCI do ORACLE. |

**Configuração da base de dados**

* O banco deve ser criado com o encoding 1251.

**Configuração do true**

* Para utilizar o true com o codepage 1251, é necessário carregar o SmartClient com o parâmetro -L=4, por exemplo:

./smartclient -L=4

* O parâmetro -L=4, pode ser utilizado em conjunto com outros parâmetros, por exemplo:

./smartclient -L=4 -M
