---
article_id: 360051144973
category: ADVPL - Classe e Função
content_hash: 56586c683c25fda684bb2d6c9871002871bfdd561b223091900449cd6d123902
fetched_at: '2026-06-28T22:40:19.512763+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - FwMsPrinter: Alterar
  a seleção do setup'
type: support-article
updated_at: '2022-01-11T17:15:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051144973-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-FwMsPrinter-Alterar-a-sele%C3%A7%C3%A3o-do-setup
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Tem como alterar a impressora que já vem pré-selecionada quando usado a classe FwMsPrinter()  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Não há como ter valores pré-selecionados, pois a tela de **setup** envia os valores selecionados para a **FWMSPrinter**, o contrário não ocorre.  
Você pode optar por não chamar o **método setup**, responsável por exibir a tela de seleção de impressora, mas para isso você deverá informar qual a impressora de destino, no parâmetro ***cPrinter*** do **método *new*.**

**Saiba mais**[FWMsPrinter](https://tdn.totvs.com/display/public/PROT/FWMsPrinter)
