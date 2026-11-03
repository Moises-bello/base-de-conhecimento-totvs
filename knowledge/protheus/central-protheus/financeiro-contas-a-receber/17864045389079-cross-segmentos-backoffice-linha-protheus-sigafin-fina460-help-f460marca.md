---
article_id: 17864045389079
category: Financeiro - Contas a Receber
content_hash: 8cab6a0d23cbf9765b76fd5e7f039cda3a2d64dfa48a1dff8d14b3857c671f0d
fetched_at: '2026-06-28T22:38:14.081950+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA460 - Help: F460MARCA '
type: support-article
updated_at: '2023-09-28T15:16:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17864045389079-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA460-Help-F460MARCA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17877992406551) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Ao realizar a liquidação ou reliquidar títulos o sistema apresenta a seguinte mensagem: Help: F460MARCA Problema: Registro selecionado por outro usuário na liquidação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17863937927063)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33

**Causa**A mensagem é apresenta quando o campo **E1\_TIPOLIQ** está preenchido, se estiver preenchido com **"LIQ"** por exemplo, ele retorna a mensagem  
  
**Solução**

Avalie o se o campo campo **E1\_TIPOLIQ** está com conteúdo, se estiver preenchido com **"LIQ"** por exemplo, ele retorna a mensagem e não permite efetuar liquidações daqueles títulos. 

**Importante**

O compartilhamento das **tabelas FO0**, **FO1** e **F02**, em relação ao compartilhamento da tabela **SE1**, precisam ter o mesmo modo de compartilhamento, indicado na documentação oficial da rotina.

[**FINA460 - Liquidação a receber - P12**](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275)
