---
article_id: 10784734204951
category: RH - 13º salário
content_hash: 91c1f1b510061f475909424cb90d5e0a182fb536afb8232663c8d306ccdae74b
fetched_at: '2026-06-28T22:44:00.772375+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Desconto de pensão alimentícia na 2º Parcela, quando
  já ocorreu desconto na 1° Parcela
type: support-article
updated_at: '2025-07-23T12:32:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10784734204951-RH-Linha-Protheus-GPE-Desconto-de-pens%C3%A3o-aliment%C3%ADcia-na-2%C2%BA-Parcela-quando-j%C3%A1-ocorreu-desconto-na-1-Parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17646565832727) Tempo aproximado para leitura: **00:03:00 min** **Dúvida** Desconto de pensão alimentícia na 2º Parcela, quando já ocorreu desconto na 1° Parcela  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

**1.**No **cadastro de verbas** (Atualizações>Definições de Cálculo>Cadastro de Verbas) crie duas verbas de **Desconto** sem id de cálculo. Uma verba para a 1° Parcela e uma verba para a 2° Parcela.  
As verbas devem estar com o campo **Pensão Alim = Não, REF13 = SIM** na aba incidências, no cadastro de verbas.

O calculo vai ser realizado conforme já parametrizado no cadastro do Beneficiário para o desconto de pensão na FOLHA.   
A verba de Desconto da 1° Parcela não deve ter incidências.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19584720337431)  
A verba de Desconto da 2° Parcela, deve ter incidência para IR

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19584744277399)

OBS. a verba de **ID 0183 (Desconto Antecipação 13° Salario na segunda parcela)** deve estar com o campo Pensão Alim = **NÃO**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19584744288791)  
  
**Cadastro do****Beneficiário**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19584744294679)  
  
**Calculo roteiro 131**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19584744299159)

**Calculo roteiro 132**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19584744307607)  
  
**Saiba Mais**[RH - Linha Protheus - GPE - Desconto de pensão alimentícia na 1º Parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10771368342551-RH-Linha-Protheus-GPE-Desconto-de-pens%C3%A3o-aliment%C3%ADcia-na-1%C2%BA-Parcela-do-13%C2%BA-Sal%C3%A1rio?source=search)  
[RH - Linha Protheus - GPE - Desconto de pensão alimentícia na 2º Parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016145152-RH-Linha-Protheus-GPE-Desconto-de-pens%C3%A3o-aliment%C3%ADcia-na-2%C2%BA-Parcela-do-13%C2%BA-Sal%C3%A1rio?source=search)Essas documentações também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
