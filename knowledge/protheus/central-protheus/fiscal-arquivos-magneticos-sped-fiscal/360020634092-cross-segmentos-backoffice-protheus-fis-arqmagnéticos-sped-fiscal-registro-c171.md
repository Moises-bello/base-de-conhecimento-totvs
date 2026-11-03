---
article_id: 360020634092
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 52b16d6572c402484d9883ff85cbddd37ef156acecfb086a9dbbfaeb34c1efb0
fetched_at: '2026-06-28T22:42:03.632877+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Registro C171 Armazenamento de Combustíveis no Sped Fiscal?
type: support-article
updated_at: '2024-06-24T20:13:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020634092-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Registro-C171-Armazenamento-de-Combust%C3%ADveis-no-Sped-Fiscal
---

**Dúvida**Como gerar o registro **Registro C171 (Armazenamento de Combustíveis (Códigos 01 e 55)** no Sped Fiscal?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão **12.1.25**  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

Este registro contém a especificação do tanque e volume envolvido na operação de entrada com combustíveis. As informações **complementares para combustíveis** podem ser lançadas pela rotina **Complementos dos documentos Fiscais** e é composto de notas fiscais dos seguintes modelos:

* **Nota Fiscal Modelo 1 ou 1-A – Espécie “NF ou NFE”**
* **Nota Fiscal Eletrônica, Modelo 55 – Espécie “SPED”**

Será necessário configurar o parâmetro **MV\_COMBUS** com um grupo de produto**:**

**![MV_COMBUST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24401627215255)**

Após configurar o parâmetro, configure o campo **B1\_GRUPO** - **Grupo** do seu produto com o mesmo conteúdo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24401645129879)

Realize a inclusão da sua nota de entrada com uma das espécies citadas nesta documentação:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12320537329559)

Acesse - **Outras Ações > Complementos Fiscais > Combustível** - Preencha os campos da aba:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12320480023319)

Salve e gere o arquivo Sped Fiscal, o registro será apresentado:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12320560893207)
