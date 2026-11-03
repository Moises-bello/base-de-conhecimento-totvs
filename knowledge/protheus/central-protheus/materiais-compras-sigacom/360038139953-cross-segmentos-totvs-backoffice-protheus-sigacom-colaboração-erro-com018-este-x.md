---
article_id: 360038139953
category: Materiais - Compras (SIGACOM)
content_hash: 844603dd5fd6f725ab501e3aab56e8cbfdb9ea90f3d9e0c197be453bee2d1678
fetched_at: '2026-06-28T22:41:07.523795+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - COLABORAÇÃO Erro COM018
  - Este XML possui um código de serviço que não está cadastrado em um produto na
  empresa/filial corrente
type: support-article
updated_at: '2022-01-11T19:29:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038139953-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-COLABORA%C3%87%C3%83O-Erro-COM018-Este-XML-possui-um-c%C3%B3digo-de-servi%C3%A7o-que-n%C3%A3o-est%C3%A1-cadastrado-em-um-produto-na-empresa-filial-corrente
---

**Dúvida**

Erro COM018 - Nota de Serviço NFs - Este XML possui um código de serviço que não está cadastrado em um produto na empresa/filial corrente

**Ambiente**Protheus – Compras – A partir da versão 12

**Solução**

Sistema apresenta código de erro no monitor do TOTVS Colaboração e na tabela **CKOCOL** ao tentar importar XML de Nota Fiscal de Serviço (**NFS**):

**COM018** *- Este XML possui um código de serviço que não está cadastrado em um produto na empresa/filial corrente.*

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050288173/mceclip2.png)

É necessário consultar a TAG ***<CodigoServico>*** no XML que precisa importar e identificar o código:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050288893/mceclip3.png)

No cadastro do produto, informar o código do serviço conforme exemplo abaixo:

***Observação: Caso não tenha o código do serviço cadastrado, acesse a SX5, filtre a tabela 60 e realize o cadastro.***

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049400674/mceclip4.png)

- Após executar o processo realize execução de importação novamente para que seja apresentado no monitor do TOTVS Colaboração:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050290613/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049402314/mceclip6.png)

- No Documento de Entrada ficará conforme abaixo:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049403054/mceclip7.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050292013/mceclip8.png)

***Saiba Mais :***

[Códigos de erro](https://tdn.totvs.com/pages/releaseview.action?pageId=271663193)

[Ponto de Entrada para manipular o código de serviço na geração da NF de Serviço](https://tdn.totvs.com/pages/releaseview.action?pageId=284475863)

[CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
