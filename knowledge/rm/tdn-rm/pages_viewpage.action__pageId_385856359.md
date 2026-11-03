---
content_hash: a17cf84b15f2fa0b43376f98fbd1d91fe2f8f5bbc6c149a6ad189b2ccfbf374c
fetched_at: '2026-06-29T00:09:07.910336+00:00'
page_id: '385856359'
product: rm
source: tdn-rm
title: Como gerar valores para saldo de banco de horas?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385856359
version: 1
---

Para o envio de informações de saldo de banco de horas, foram criadas as seguintes funções:

* **Função SALDOBANCOHORASCHRONUS**

Retorna o valor do saldo de banco de horas do funcionário até a data informada.  
**SALDOBANCOHORASCHRONUS('DATA')**

* **Função SALDOCOMPBANCOHORASCHRONUS**

Retorna o valor de Extras que foram utilizadas na Compensação de Banco de Horas até a data informada.  
**SALDOCOMPBANCOHORASCHRONUS('DATA')**

* **Função BANCOHORASPERIODOCHRONUS**

Retorna o valor de saldo de banco de horas que do funcionário dentro de um intervalo informado.  
**BANCOHORASPERIODOCHRONUS('DATA','DATA')**

* **Função COMPBANCOHORASPERIODOCHRONUS**

Retorna o valor de Extras que foram utilizadas na compensação de Banco de Horas dentro de um intervalo informado.  
**COMPBANCOHORASPERIODOCHRONUS('DATA','DATA')**
