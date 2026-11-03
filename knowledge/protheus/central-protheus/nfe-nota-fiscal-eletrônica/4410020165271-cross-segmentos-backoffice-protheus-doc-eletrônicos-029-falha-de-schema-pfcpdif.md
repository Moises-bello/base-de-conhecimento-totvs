---
article_id: 4410020165271
category: NFe - Nota Fiscal Eletrônica
content_hash: ff006e7a844607a3e74ba0c10898eb7d8d7a9e38510da4106ffdedfdc80bdd1c
fetched_at: '2026-06-28T22:40:03.734438+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema pFCPDif'
type: support-article
updated_at: '2025-07-28T18:54:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410020165271-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-pFCPDif
---

**Dúvida**Como solucionar a falha de Schema referente a TAG pFCPDif ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

*1 - Ao gerar falha de Schema **referente ao pFCPDif** verifique se o seu XML gerou conforme o **exemplo abaixo:***

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410019368343)**

*2- Verifique se está atualizado todos **os fontes conforme o link abaixo:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

*3- O conteúdo dessa **TAG é obrigatória pFCPDif** verifique qual opção do diferimento foi utilizado e usou as opções corretas:*

* Por isso, é necessário verificar se foi configurado corretamente no sistema a nota de diferimento:

* **No Protheus há 7 tipos de configuração de ICMS diferido conforme o link abaixo:**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=654111155)

*4- Após isso, **exclua a nota e gere novamente.***

*5- Caso tenha que gerar o calculo, do **FECP com Diferimento** realizar o procedimento abaixo:*

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gravar os campos CD2\_VFCPDI e CD2\_VFCPEF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408539014935)

*6- Após isso, **exclua a nota e gere novamente.***
