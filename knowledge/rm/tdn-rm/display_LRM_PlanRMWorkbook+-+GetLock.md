---
content_hash: 2c8385e0782ed8ac03e0dd562beb40e0edd923b03b8ac8e3ff4b8625451df986
fetched_at: '2026-06-29T00:05:58.988479+00:00'
page_id: '189307062'
product: rm
source: tdn-rm
title: PlanRMWorkbook - GetLock
type: documentation
url: https://tdn.totvs.com/display/LRM/PlanRMWorkbook+-+GetLock
version: 3
---

GetLock()

## Descrição

---

Interrompe os cálculo em segundo plano e adquire uma trava exclusiva sobre a planilha.

## Observação

---

A função GetLock sempre deve ser utilizada em par com a  função ReleaseLock. Uma vez adquirido a trava da planilha, nenhuma outra thread conseguirá obtê-la e terá que aguardar até que ela seja liberada. Recomenda-se o uso da função GetLock antes de um bloco Try-Finally em que a chamada do ReleaseLock esteja declarada no finally.

## Exemplo

---

Travas na planilhatruec#1Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)
