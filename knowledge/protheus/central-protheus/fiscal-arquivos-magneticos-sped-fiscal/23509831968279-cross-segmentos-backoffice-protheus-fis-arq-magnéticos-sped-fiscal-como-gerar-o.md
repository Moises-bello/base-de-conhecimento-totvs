---
article_id: 23509831968279
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: c72c0435c25c4f1fa0269c01307bbf4ab0c76a848b4da6551f78eaed39c4d86b
fetched_at: '2026-06-28T22:42:01.154607+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro 0206 no Sped Fiscal?
type: support-article
updated_at: '2024-05-15T18:27:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23509831968279-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-0206-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23509831882135) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como gerar o registro **0206** no txt do **Sped Fiscal**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos:

**1**. Preencha o conteúdo do campo **B1\_GRUPO** com segmento para **Combustível** (crie um grupo especifico para essa questão):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23509831885591)

**2**. Após isso, preencha o parâmetro **MV\_COMBUS** com o mesmo conteúdo apontado no campo **B1\_GRUPO**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23509831891607)

**3**. Realize a escrituração do documento que amarre este produto:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23509831895831)

**4**. Ao salvar a Nota Fiscal, clique em **Outras Ações > Complementos Fiscais**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23509841645079)

**5**. Acesse a aba de **Combustível**, preencha todos os campos da tabela **CD6**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23509831905303)

**6**. Ao concluir, salve o complemento e gere um novo **Sped Fiscal**, segue apresentação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23509841654295)
