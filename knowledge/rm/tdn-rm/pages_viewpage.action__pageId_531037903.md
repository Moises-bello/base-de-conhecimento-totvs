---
content_hash: 0b3c0778499c9751a8f59277070a5f71b36b156150cddaa42c6582deef4f4ee3
fetched_at: '2026-06-29T00:10:36.235915+00:00'
page_id: '531037903'
product: rm
source: tdn-rm
title: Função SomaCampoEtapa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531037903
version: 2
---

# Objetivo

---

Esta função de fórmula tem por objetivo retornar o somatório dos campos informados: AulasDadas, Nota e Faltas;

# Descrição

---

A função de fórmula SomaCampoEtapa poderá ser utilizada por todo o sistema, não possuindo restrição de uso. Na validação será considerado os campos:

("AULASDADAS","NOTA","FALTAS")

Exemplos: SomaCampoEtapa("AULASDADAS");

                 SomaCampoEtapa("NOTA");

                 SomaCampoEtapa("FALTAS");

# Retorno da função

---

Esta função de fórmula irá retornar a soma do campo informado em todas as etapas exceto a etapa final.
