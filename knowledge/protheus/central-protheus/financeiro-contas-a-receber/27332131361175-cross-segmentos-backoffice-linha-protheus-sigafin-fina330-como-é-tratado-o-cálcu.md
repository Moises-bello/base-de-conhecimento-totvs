---
article_id: 27332131361175
category: Financeiro - Contas a Receber
content_hash: 1404030e0999fad2a36f516e3b7a5b185ee39b55a00a89e9eae60cdb07028974
fetched_at: '2026-06-28T22:38:13.995703+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA330 - Como é tratado
  o cálculo dos impostos na compensação de um título NCC
type: support-article
updated_at: '2024-10-25T17:34:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27332131361175-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA330-Como-%C3%A9-tratado-o-c%C3%A1lculo-dos-impostos-na-compensa%C3%A7%C3%A3o-de-um-t%C3%ADtulo-NCC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27332133247255) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como é tratado o cálculo dos impostos na compensação de um título NCC?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice Linha Protheus - Financeiro - FINA330 - Todas as versões

**Solução**

Ao efetuar a compensação de **títulos a receber (FINA330)** de nota de crédito ao cliente (**E1\_TIPO=NCC**), há algumas regras a serem consideras quando o(s) título(s) de contrapartida possuírem cálculo de impostos:

* Para os impostos **calculados na baixa (tipo PIS, COF, CSL, IRF, etc.)**:
  + Como a **compensação da NCC** não possui fato gerador dos impostos (não houve pagamento), o valor desses impostos não serão abatidos do valor da movimentação (**E5\_VALOR**), e o saldo da **NCC** (**E1\_SALDO**) não deve ficar com os valores desses impostos após a compensação;
* Para os impostos **calculados na emissão (tipo IR-, PI-, CO-, etc.)**:
  + Nas perguntas da rotina (tecla **F12**), a pergunta **"Considera Abatimentos/Impostos?"** deve ser configurada para definir se os impostos **calculados na emissão** (**abatimentos**) devem influenciar ou não sobre o valor a ser compensado. Se configurado "**Sim**", o **saldo da NCC** deve ficar com o valor dos impostos da emissão após a compensação.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27332133248279)](https://centraldeatendimento.totvs.com/hc/article_attachments/27332133248279)

**Saiba mais:**

**[Tratamento de impostos sobre NCC](https://tdn.totvs.com/pages/releaseview.action?pageId=770942537)**

**[Compensação a Receber](https://tdn.totvs.com/pages/releaseview.action?pageId=505768648)**
