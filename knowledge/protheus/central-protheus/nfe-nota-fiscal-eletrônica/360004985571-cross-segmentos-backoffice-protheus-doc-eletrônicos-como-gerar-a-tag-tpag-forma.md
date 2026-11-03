---
article_id: 360004985571
category: NFe - Nota Fiscal Eletrônica
content_hash: 6f95c69a5a21cd742773b56e4fc15a9d1f6a14ae7dccb1d0ce2356eebc0a4af5
fetched_at: '2026-06-28T22:40:00.080653+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG
  tPag (forma de pagamento / duplicata / fatura)
type: support-article
updated_at: '2025-06-11T11:49:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004985571-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-tPag-forma-de-pagamento-duplicata-fatura
---

**Dúvida**Como gerar a TAG tPag (forma de pagamento / duplicata / fatura)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12  
  
**Solução**

Se necessário outras formas de pagamento, indicamos:

1. Por padrão, para que seja levada as duplicatas no XML é necessário que o campo esteja preenchido **E4\_FORMA.**

**![20201117_152020.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/23473882642839)**

* **Saiba mais:**

Caso o campo não apareça na condição de pagamento**,** verifique se o campo **está visível para o módulo no configurador:**

**![E4_FORMA_1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23473912603287)**

**![E4_FORMA_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23473882680983)**

**![E4_FORMA_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23473882706327)**

* **Importante:**

Caso a empresa transmita nota de entrada com formulário próprio = Sim, selecionar também o **módulo do SIGACOM, para que o campo E4\_FORMA seja apresentado na condição de pagamento.**

Lembrando que é necessário verificar a forma de pagamento escolhida no campo **E4\_FORMA**nessa condição de pagamento:

* Novas formas de pagamento **acrescentadas na NT 2020.06:**

Devem ser incluída através do configurador em tabelas **Genéricas -> Tabela 24**

**![tabela_24.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/23473882717079)**

**Observação 2:** Caso necessário a inclusão de Formas de Pagamento (Sem Pagamento). Efetuar a inclusão através do Configurador, em Tabelas Genéricas (**24**).

Exemplo: SPG= Sem Pagamento e VC = Vale combustível

![FORMAS_NOVAS_DE_PG.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/23473882740247)

* **Saiba mais:**

Se o campo **E4\_FORMA** ficar em branco **e não tiver duplicata (F4\_DUPLIC = NÃO), será gerado 99 - Outros e Caso tenha duplicata será gerado 15 - Boleto.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403487179671)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403500852503)

**Otherwise:**

Define um bloco de instruções a ser executado caso nenhuma das cláusulas CASE <condição> seja avaliada como verdadeira.

<https://tdn.totvs.com.br/display/framework/DO+CASE>

* ***Ponto de Entrada:***

A utilização do ponto de entrada **PE01NFESEFAZ.**

Segue link com exemplo:

[PE01NFESEFAZ - Manipulação em dados do Grupo Detalhamento da Forma de Pagamento](http://tdn.totvs.com/pages/viewpage.action?pageId=348298539)

Observação: Caso queira deixar o valor padrão **(tag <tPag>)**, não há necessidade de alterações nos valores do array 'AdetPag'.
