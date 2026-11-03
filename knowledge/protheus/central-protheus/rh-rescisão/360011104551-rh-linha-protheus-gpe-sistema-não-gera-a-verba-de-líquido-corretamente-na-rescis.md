---
article_id: 360011104551
category: RH - Rescisão
content_hash: c82f0b89308c5e6004133753f496960e3103781b05c30983e99937f9febb2926
fetched_at: '2026-06-28T22:43:54.463715+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não gera a verba de líquido corretamente
  na rescisão complementar quando esta ocorre no mesmo mês da original
type: support-article
updated_at: '2025-06-26T11:49:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011104551-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-gera-a-verba-de-l%C3%ADquido-corretamente-na-rescis%C3%A3o-complementar-quando-esta-ocorre-no-mesmo-m%C3%AAs-da-original
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33067299244439)**Tempo aproximado para leitura:**00:02:30 min**

**Dúvida** **GPEM040** - Sistema não está gerando a verba de líquido corretamente na rescisão complementar no mesmo mês da original  
  
**Ambiente**Protheus – Gestão de Pessoal – A partir da versão 11.80  
  
**Solução**Processo de parametrização:  
  
**Cadastro de verbas:**  
![](http://tdn.totvs.com/download/attachments/385860535/image2018-7-31_17-41-14.png?version=1&modificationDate=1533070044000&api=v2)  
![](http://tdn.totvs.com/download/attachments/385860535/image2018-7-31_17-41-41.png?version=1&modificationDate=1533070044000&api=v2)  
  
Cálculo da **Rescisão** Original:![](https://totvssuporte.zendesk.com/attachments/token/p9jNjDkIpozNdDlkJyeuhsL3q/?name=inline-189878455.png)  
  
**Rescisão Complementar**:![](https://totvssuporte.zendesk.com/attachments/token/Wpvi71jYXufcl9cpAJcVvG2SO/?name=inline527815886.png)  
  
**Lançamento por funcionário**:![](https://totvssuporte.zendesk.com/attachments/token/U0JtR4r6lEJa03RgVnrtFus1E/?name=inline1144645789.png)  
  
Integrado com o **roteiro** de **Rescisão** - F7  
Calcular a **Rescisão** - F6:![](https://totvssuporte.zendesk.com/attachments/token/FlYsCgYF2BrRzg1hdgcEFknSm/?name=inline198859673.png)  
  
Resumo do cálculo:  
(Verba 528) 1.528,08 - Rescisão original.  
(Verba 542) 1.526,08 - Rescisão original sendo apresentada na complementar com o intuito de abater o valor já pago.  
(Verba 215) 350,00 - Lançada na rescisão complementar para pagamento - (verba 508) 0,93 = (verba 528) 349,09.  
(Verba 528) 349,09 - Líquido, diferença a ser paga na rescisão complementar.  
  
**Saiba mais**  
Para adquirir informações adicionais, acesse o *link*: [MP - GPE0849 - GPEM040 - Sistema não está gerando a verba de líquido corretamente na rescisão complementar no mesmo mês da original](http://tdn.totvs.com/pages/viewpage.action?pageId=385860535)
