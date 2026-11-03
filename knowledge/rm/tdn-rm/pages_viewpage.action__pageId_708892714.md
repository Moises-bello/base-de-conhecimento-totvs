---
content_hash: 9feb617dd26a2676bfd3f57f0f6569e6dc3be44f0cf7b282679dadd0e2e5700e
fetched_at: '2026-06-29T00:11:25.469524+00:00'
page_id: '708892714'
product: rm
source: tdn-rm
title: Alterações S-2210  Leiaute S1.1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708892714
version: 11
---

false

**A partir das Versões:**

* 12.1.34.232
* 12.1.2205.175
* 12.1.2209.117
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2210 para o leiaute do eSocial Versão S-1.1.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo{cat}: incluído o campo ultDiaTrab | - | Último dia trabalhado. Validação: Preenchimento obrigatório se dtAcid >=[2023-01-16]). Se informada, deve ser uma data igual ou anterior à data atual e igual ou posterior à data de admissão do trabalhador. Se tpCat = [2], deve ser informada data posterior à data preenchida no evento de CAT anterior, quando informada em nrRecCatOrig. |
| Grupo{cat}: incluído o campo houveAfast | - | Houve afastamento? Valores válidos: S - Sim N - Não Validação: Preenchimento obrigatório se dtAcid >= [[2023-01-16]). |

  XML:

Mais informações em:

[S-2210 - Comunicação de Acidente de Trabalho](https://tdn.totvs.com/pages/viewpage.action?pageId=364908460)

[Evento S-2210](https://tdn.totvs.com/display/LRM/Evento+S-2210)
