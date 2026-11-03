---
article_id: 1500004187121
category: NFe - Nota Fiscal Eletrônica
content_hash: bba08b3fe3682eb033d13c0e4e25b451e0b626223a467ed621123eeb3852d53f
fetched_at: '2026-06-28T22:40:03.213506+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  441 Rejeição :
  Descrição do pagamento obrigatória para meio de pagamento 99 outros'
type: support-article
updated_at: '2025-06-17T19:35:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004187121-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-441-Rejei%C3%A7%C3%A3o-Descri%C3%A7%C3%A3o-do-pagamento-obrigat%C3%B3ria-para-meio-de-pagamento-99-outros
---

**Dúvida**Como solucionar a rejeição abaixo:

441 Rejeição: Descrição do pagamento obrigatória para meio de pagamento 99 outros ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Caso a forma de pagamento **não seja 99 Outros:**

1- Informe uma forma de **pagamento diferente de 99 Outros, para isto há os links abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG tPag (forma de pagamento / duplicata / fatura)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004985571)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar fatura (forma de pagamento / duplicata / fatura) no XML e no Danfe ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025467193)

Caso seja 99 **Outros:**

1 - Realizar as **atualizações, abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.006](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052959634)

2- Crie os **parâmetros abaixo:**

Para inclusão/alteração dos parâmetros, acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **incluir** e informar:

**Parâmetro****utilizado em operações de saída (Faturamento):**

Nome de Var.: **MV\_MFATIPR**

Tipo: **1 - Caractere**

Cont. Por: **"Negociacao Futura"**

![](https://tdn.totvs.com.br/download/attachments/626650334/image2021-6-29_20-3-17.png?version=1&modificationDate=1625007797530&api=v2)

**Parâmetro****utilizado em operações de entrada (Compras):**

Nome de Var.: **MV\_TPAGCOM**

Tipo: **1 - Caractere**

Cont. Por: **"Negociacao Futura"**

![](https://tdn.totvs.com.br/download/attachments/626650334/image2021-6-29_20-3-47.png?version=1&modificationDate=1625007828070&api=v2)

* **Importante**

Caso informado um texto fixo, o mesmo deverá ser informado entre aspas ("), conforme exemplo acima.

Os dois parâmetros quando acionados no código fonte, são macro executados. Desta forma possibilitando em sua configuração o uso de funções especificas/customizadas.

Apenas como exemplo, segue utilização do parâmetro como função:

![](https://tdn.totvs.com.br/download/attachments/626650334/image2021-6-29_20-27-5.png?version=1&modificationDate=1625009225277&api=v2)

Função codificada e compilada em ambiente

![](https://tdn.totvs.com.br/download/attachments/626650334/image2021-6-29_20-31-17.png?version=1&modificationDate=1625009477284&api=v2)

3 - **Exclua a nota** e gere novamente.

* **Importante:**

Caso utilize o **TOTVS Colaboração 2.0** há uma ISSUE  liberada pelo desenvolvimento:

**DSERTSS1-17604**

Realizar as **atualizações no ERP, abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.006](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052959634)

* ***Saiba mais:***

Segue abaixo o parecer da ***consultoria de segmentos referente as formas de pagamentos:***

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=636720599)

* **Validação da Sefaz:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005358221)**
