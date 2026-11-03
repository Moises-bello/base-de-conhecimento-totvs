---
article_id: 360056032674
category: Materiais - Compras (SIGACOM)
content_hash: 8945808f1eb0857ca496b6c4096e3dbebe3ba8774eb87bc3a1fb2bef070943c0
fetched_at: '2026-06-28T22:41:24.264352+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual campo compõe a
  descrição do produto na Solicitação de Compras ?
type: support-article
updated_at: '2023-02-01T11:35:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056032674-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-campo-comp%C3%B5e-a-descri%C3%A7%C3%A3o-do-produto-na-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**

Qual campo compõe a descrição do produto na Solicitação de Compras ?

**Ambiente**Microsiga Protheus – Compras – A partir da versão 12  
  
**Solução**Através dos parâmetros F12 da Rotina de Solicitação de Compras (MATA110) poderá ser configurado de duas formas de onde será buscada a descrição do Produto da SC, conforme abaixo:

1.Aperte o F12 na rotina de Solicitação de Compras (MATA110) no exemplo abaixo inseri B5\_CEME.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097366273/mceclip0.png)

Acesse a rotina Complemento de Produto (MATA180) e cadastre o produto e o Nome Cientifico (B5\_CEME)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095069954/mceclip1.png)

Ao selecionar o produto na Solicitação de Compras observe que trouxe a descrição do campo B5\_CEME

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097367753/mceclip2.png)

2. A outra forma de configurar é selecionando nos parâmetros o campo Descrição do produto do cadastro de produtos (B1\_DESC)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097367993/mceclip3.png)

Acesse o Cadastro de Produtos e verifique a Descrição do Produto(B1\_DESC) rotina (MATA110)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097368313/mceclip4.png)

Ao importar o produto para Solicitação de Compras a Descrição apresentada na solicitação será do campo Descrição do Produto( B1\_DESC) conforme definido nos parâmetros F12 da rotina MATA110.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095071794/mceclip5.png)

**Obs:**

Esta configuração do parâmetro F12 da rotina MATA110 exemplificada, é configurada por usuário.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
