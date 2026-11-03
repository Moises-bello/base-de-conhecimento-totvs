---
article_id: 360048656053
category: NFe - Nota Fiscal Eletrônica
content_hash: b7c8d4f5d06380d006d6c3b2dc306116b3d904873a0e8157619b3670fc26574e
fetched_at: '2026-06-28T22:40:03.680293+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Nota técnica 2020.002
type: support-article
updated_at: '2025-08-11T23:50:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048656053-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-t%C3%A9cnica-2020-002
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2020.002 ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Conforme o link abaixo foi lançada a ***nota técnica** **2020.002:***

[Nota Técnica 2020.002 - v.1.00 - Publicada em 18/05/2020](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=2aYIAayNJAU=)

No qual, foram acrescentados novos códigos na Tabela de Enquadramento de IPI  ***os códigos 163,164 e 165.***

Sendo assim, será necessário incluir na ***consulta padrão dos campos no TES no campo Enq. IPI "F4\_GRPCST"*** e no cadastro de produto no campo **Enq. IPI "B1\_GRPCST":**

1. Para que seja criado os **novos códigos  163,164 e 165** aplicar a patch e **RODAR O U\_IMPSPED:**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074171353)

2. Após isso, verifique na tabela  **F08 no campo  F08\_CODIGO = ('163','164', '165') e se aparece as opções no cadastro de produto e do TES.**

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070624254)**
