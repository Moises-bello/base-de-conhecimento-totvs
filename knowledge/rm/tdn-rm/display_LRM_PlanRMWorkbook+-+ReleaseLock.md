---
content_hash: 98d4354a3ab54424d9282285fb12af4e51f1fc4a5741d24e0781c2f3ba549211
fetched_at: '2026-06-29T00:05:58.991211+00:00'
page_id: '189307065'
product: rm
source: tdn-rm
title: PlanRMWorkbook - ReleaseLock
type: documentation
url: https://tdn.totvs.com/display/LRM/PlanRMWorkbook+-+ReleaseLock
version: 5
---

ReleaseLock()

## Descrição

---

Libera a trava adquirida pelo método GetLock e reinicia os cálculos em segundo plano.

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
