---
content_hash: 2cf2387c877eee09bb9de256b7d14a27e22bcf60e44bf6ed71937fac74fb71af
fetched_at: '2026-06-29T00:10:23.238104+00:00'
page_id: '500290207'
product: rm
source: tdn-rm
title: S-1299 – Como gerar a tag evtAqProd com valor S quando não envio o evento S-1250
  pelo TOTVS Folha de Pagamento?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=500290207
version: 8
---

false

**A partir das Versões:**

* 12.1.23.210
* 12.1.24.148
* 12.1.25.101

# Objetivo:

---

       O objetivo deste documento é trazer informações de como gerar a tag evtAqProd (Possui informações sobre a aquisição de produtor rural de pessoas físicas) com valor S (Sim) no evento S-1299 (Fechamento dos Eventos Periódicos) quando não é enviado o evento S-1250 pelo TOTVS Folha de Pagamento.

---

**Atenção: é necessário executar o RM.Atualizador para que o parâmetro "Possui informação sobre a aquisição de produto rural de pessoas físicas" fique disponível na tela.**

Para gerar a tag evtAqProd com o valor S no evento S-1299, é necessário marcar o parâmetro **"Possui informação sobre a aquisição de produto rural de pessoas físicas"** dentro do cadastro de Período de Apuração:

Ao gerar o evento S-1299 a tag evtAqProd foi gerada com o valor S:
