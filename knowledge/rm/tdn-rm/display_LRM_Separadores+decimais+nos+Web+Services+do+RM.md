---
content_hash: 2abb428fba9e5337d22cd2e7bc6f20d8aeedf0b0aba0be46d2ab079803847657
fetched_at: '2026-06-29T00:08:28.707831+00:00'
page_id: '271845552'
product: rm
source: tdn-rm
title: Separadores decimais nos Web Services do RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Separadores+decimais+nos+Web+Services+do+RM
version: 14
---

# Índice:

---

.\*ndice:

# WsProcess:

---

     Nos processos utilizando o método ExecuteWithParams (descontinuado, conforme documentado no endereço: [TBC - Web Service Process](http://tdn.totvs.com/display/LRM/TBC+-+Web+Service+Process)) sempre é utilizada a mesma cultura do sistema operacional do servidor.

     Nos processos executados utilizando o método ExecuteWithXMLParams, o separador decimal é o ponto (.).

# WsDataServer:

---

     Nas operações que utilizam o método WsDataServer, o separador decimal é o mesmo da cultura definida no sistema operacional, entretanto, esta pode ser alterada através do arquivo .config do Host (RM.Host.exe.config ou RM.Host.Service.exe.config). Para isso inclua a tag "WebServiceCulture" exemplificado hem: [Como Expor os Web Services do RM através do Host](http://tdn.totvs.com/pages/viewpage.action?pageId=89620766)

     Abaixo três colunas, a primeira referencia a forma como a tag WebServiceCulture é utilizada, a segunda o seu formato de schema e terceira o separador decimal que será utilizado de acordo com as definições da tag e Schema.

|  |  |  |
| --- | --- | --- |
| **WebServiceCulture** | **Schema** | **Separador** |
| Desabilitada | Tipado | Ponto |
| Desabilitada | String | Vírgula |
| Desabilitada | Não Utiliza | Vírgula |
| value="Invariant" | Não Utiliza | Ponto |
| value="Invariant" | Tipado | Ponto |
| value="Invariant" | String | Ponto |

     Coluna "Schema": Diz respeito a utilização do Schema do DataServer juntamente ao XML contendo os dados do registro. O Schema do DataServer pode ser obtido pelo método GetSchema do serviço WsDataServer, que retorna o schema do Data Server tipado, ou pelo aplicativo [Totvs Web Service Client](http://tdn.totvs.com/x/yBdFCg) (TotvsWSClient.exe) que retorna as informações setadas com o tipo string.

---

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e Superiores

false

**Processo:** Separadores decimais nos Web Services do RM

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
