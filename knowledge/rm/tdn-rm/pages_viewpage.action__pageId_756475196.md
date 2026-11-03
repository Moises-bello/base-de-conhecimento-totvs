---
content_hash: e7e03fba68323a50acc45638127a0ccc94ac4c0647bb8841520f766977b05ce8
fetched_at: '2026-06-29T00:11:33.361284+00:00'
page_id: '756475196'
product: rm
source: tdn-rm
title: API - Relatórios - Portal do Cliente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=756475196
version: 5
---

O TCGI permite a geração dos Relatórios de [Ficha Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=435105053) e [Informe de Pagamentos](https://tdn.totvs.com/display/LRM/Informe+de+pagamentos+-+IR) via API para facilitar a integração com outros produtos.

Seguem os exemplos de geração para:

##### **RELATÓRIO DE FICHA FINANCEIRA:**

| Título | **API para Geração de Relatório de Ficha Financeira** |
| --- | --- |
| Endpoint | [http://localhost:8051/api/imb/v1/reports/[COLIGADA]/[TIPO\_RELATORIO]/[NUMERO\_VENDA]](http://localhost:8051/api/imb/v1/reports/1/[TIPO_RELATORIO]/[NUMERO_VENDA) |
| Verbo | Get |
| Parameters | no parameters |
| Descrição | Api para solicitar a geração do relatório de Ficha Financeira, sendo obrigatório a passagem de usuário e senha para autenticação, além das seguintes informações:  Coligada: **#** - Formato numérico, sem zeros à esquerda;  Tipo de Relatório: ***FF****;*  Número Venda: ***####** - Formato numérico, sem zeros à esquerda.*  Exemplo: <http://localhost:8051/api/imb/v1/reports/1/FF/10022> |
| Parâmetros  do TCGI | [Totvs Incorporação - Parâmetros - Portal do Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047) |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue

##### **RELATÓRIO DE INFORME DE PAGAMENTOS:**

| Título | **API para Geração de Relatório de Informe de Pagamentos** |
| --- | --- |
| Endpoint | [http://localhost:8051/api/imb/v1/reports/[COLIGADA]/[TIPO\_RELATORIO]/[NUMERO\_VENDA]?[ANOBASE=####]](http://localhost:8051/api/imb/v1/reports/1/IP/10022?ANOBASE=2022) |
| Verbo | Get |
| Parameters | | Key | Value | | --- | --- | | ANOBASE | Informe o ano base para geração do informe | |
| Descrição | Api para solicitar a geração do relatório de Informe de Pagamentos, sendo obrigatório a passagem de usuário e senha para autenticação, além das seguintes informações:  Coligada: **#** - Formato numérico, sem zeros à esquerda;  Tipo de Relatório: ***IP****;*  Número Venda: ***####** - Formato numérico, sem zeros à esquerda.*  Exemplo: <http://localhost:8051/api/imb/v1/reports/1/IP/10022?ANOBASE=2022> |
| Parâmetros  do TCGI | [Totvs Incorporação - Parâmetros - Portal do Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047) |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue

Para conferir os PDFs gerados no retorno desta API, sugerimos utilizar o site Base64.Guru, cujo link pode ser encontrado nos buscadores da internet.
