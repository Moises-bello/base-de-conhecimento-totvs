---
content_hash: c2ac8f60849177c6c53c3b6b7401b6f8a022b677ac2c01ea0bc8fcf4e18dd43a
fetched_at: '2026-06-29T00:09:13.493107+00:00'
page_id: '421366090'
product: rm
source: tdn-rm
title: O que fazer quando o movimento do funcionário não foi distribuido por Tomador?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421366090
version: 8
---

# Objetivo:

---

O objetivo deste documento é informar o funcionamento do parâmetro: "Desconsiderar  movimento por tomador para funcionários que não possui distribuição na geração do XML".

---

Com este parâmetro **Marcado** ao gerar o XML dos eventos S-1200, S-2299 e S-2399 para funcionário que não possui distribuição por Tomador, o sistema irá considerar o tomador informado no cadastro do funcionário, caso não exista tomador no funcionário o sistema irá considerar o tomador empresa cadastrado no parametrizador.

**Observações:**

* Este parâmetro ficará habilitado somente quando utilizar cálculo por tomador.
* Com este parâmetro desmarcado o sistema não irá gerar o XMLs para funcionários que não tiveram a movimentação distribuída por tomador.
* Se tiver pelo menos um evento distribuído na movimentação do funcionário o sistema irá desconsiderar este parâmetro.

 Ao gerar o XML sem fazer a distribuição e o parâmetro estiver marcado, o sistema irá apresentar a mensagem abaixo:

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |
| 12.1.19 |

falsefalse

**Status: Pendente**

false

**Data:**

false

**Autor:**
