---
content_hash: 2eb3627e5c81a5fc57b0aa4f20f2db7a147b647571741e722caeef02386e133c
fetched_at: '2026-06-29T00:09:11.479309+00:00'
page_id: '404916475'
product: rm
source: tdn-rm
title: Como realizar a geração do evento S-1202?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=404916475
version: 16
---

false

**A partir das Versões:**

* + 12.1.32.249
  + 12.1.33.194
  + 12.1.34.108

---

# Objetivo:

---

O objetivo deste documento é trazer as formas de geração do evento "S-1202-Remuneração de servidor vinculado a Regime Próprio de Previd. Social" que é utilizado para transmitir ao governo informações referente ao pagamento de servidores filiados ao RPPS-Regime Próprio de Previdência Social.

Sua geração se dá pela rotina de "Gerar XML Eventos Periódicos", onde será identificado todos os funcionários (S-2200 e S-2300) que atendam algumas condições.

---

11Tipos de TrabalhadoresTipos de Trabalhadores11Servidores (3XX)Servidores

Serão considerados os funcionários associados a categoria dos servidores "3XX (301, 302 e etc.)" e com o tipo de regime previdenciário "Regime próprio de Previdência Social - RPPS".

* Categoria:

* Tipo de Regime Previdenciário:

2CedidoCedido

Serão considerados os funcionários associados a categoria "410 - Trabalhador cedido - Informação prestada pelo Cessionário" e o tipo de regime previdenciário "Regime próprio de Previdência Social - RPPS" e o tipo de regime previdenciário "Regime próprio de Previdência Social - RPPS".

* Categoria:

* Tipo de Regime Previdenciário:

3Dirigente Sindical - informação prestada pelo SindicatoDirigente Sindical - informação prestada pelo Sindicato

Funcionários associados a categoria "401 - Dirigente Sindical - informação prestada pelo Sindicato" e o tipo de regime previdenciário "Regime próprio de Previdência Social - RPPS"..

* Categoria:

* Tipo de Regime Previdenciário:

2Lançamento Lançamento 11MensalMensal

Acesse RH | eSocial | Gerar XML

213° Salário13° Salário

Acesse RH | eSocial | Gerar XML

falseImportante!

Evento correspondente a verba de 13° salário lançado no envelope de pagamento para o estatutario precisa ter o CC 102, para correto funcionamento da geração do evento S-1202 como anual para o eSocial.
