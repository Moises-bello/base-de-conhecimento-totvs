---
article_id: 360045698333
category: NFe - Nota Fiscal Eletrônica
content_hash: c2deded1127128f9b95346379221cfd0e704cb079beb90d3d6ecad67383a0c6f
fetched_at: '2026-06-28T22:40:03.725808+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema na Tag IPI'
type: support-article
updated_at: '2025-06-12T18:21:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045698333-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-IPI
---

**Dúvida**Como solucionar a falha de Schema referente a TAG IPI ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar a  **rotina de transmissão SPEDNFE;**

![nfesefaz.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17324840793111)

2. Clique em **Outras ações -> Monitor -> faixa ->** Digite o número e série da nota;

**![monitor_faixa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17324840801559)**

3. Clique no**botão Schema; Copie e Cole o conteúdo completo do XML.**

![546_rejeicao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17324840807703)

4. Verifique se o CST***da TAG IPI***  gerou conforme o exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062660134)

5. Conforme o XML acima não foi preenchido a situação tributária do **IPI** que é obrigatória.

6. Para a correção preencher o CST do IPI, campo no TES **F4\_CTIPI** deve estar preenchido **Cod. trib. IPI**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17324847040791)

7. Após isso, exclua a nota e gere novamente.
