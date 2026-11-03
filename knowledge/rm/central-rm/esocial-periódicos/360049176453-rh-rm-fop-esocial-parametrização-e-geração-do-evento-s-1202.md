---
article_id: 360049176453
category: esocial - Periódicos
content_hash: f04a8fb80399130e21828b2118dadd81445b55127f8d4dec26fcc19c2d8f2e66
fetched_at: '2026-06-28T22:47:09.444714+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Parametrização e geração do evento S-1202
type: support-article
updated_at: '2023-07-10T17:30:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049176453-RH-RM-FOP-eSocial-Parametriza%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-do-evento-S-1202
---

**Dúvida**Como parametrizar e gerar o evento **S-1202 - Remuneração de servidor vinculado a Regime Próprio de Previd. Social**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O evento **S-1202** é utilizado para levar as informações da remuneração de cada servidor/militar no mês de referência.

Este evento deve ser utilizado para os servidores filiados ao **Regime Próprio de Previdência Social – RPPS** pertencentes as categorias 301, 303 (sub judice no STF para parlamentares estaduais), 305 (desde que seja servidor público efetivo oriundo de ente que possua RPPS) e 307 (Militar).

Será gerado na fila de eventos quando o [cadastro do funcionário](https://tdn.totvs.com/pages/releaseview.action?pageId=452719153) contemplar uma das seguintes combinações:

1. Quando o campo **Código da Categoria eSocial** for igual a 3XX (301, 302, etc.) e o **Tipo de Regime Previdenciário** for igual **Regime próprio de Previdência Social - RGPS** ou **Regime de Previdência Social no Exterior**;  
2. Quando o **Código da Categoria eSocial** for igual a 410 e;  
   • O **Tipo de Regime Previdenciário** presente na aba **Situação** for **Regime Próprio de Previdência Social - RPPS**, ou;  
   • Na aba **Dados da Cessão**, o campo **Tipo de Regime Previdenciário** for igual **Regime Próprio de Previdência Social - RPPS**, ou;  
   • O **Tipo de Regime Previdenciário** for igual a **Regime de Previdência Social no Exterior** e a **Categoria de origem** na aba **Dados da Cessão** for igual a 3XX (301, 302 e etc).

Apos a parametrização acima no cadastro do funcionário, basta ir na no menu **eSocial | Eventos periódicos | Gerar XML** e selecionar o evento S-1202.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071695894)

**Saiba mais**  
Para mais informações acesse:  
      • [Mapeamento do S-1202](https://tdn.totvs.com/display/public/LRM/Evento+S-1202)  
      • [Como realizar a geração do evento S-1202?](https://tdn.totvs.com/pages/releaseview.action?pageId=404916475)
