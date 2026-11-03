---
article_id: 360025467193
category: NFe - Nota Fiscal Eletrônica
content_hash: d23fb0838dd097db1c79e393d164abe8456d000b210c21d075060aabb5a75fa9
fetched_at: '2026-06-28T22:40:06.728302+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar fatura
  (forma de pagamento / duplicata / fatura)  no XML e no Danfe
type: support-article
updated_at: '2024-08-14T20:52:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025467193-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-fatura-forma-de-pagamento-duplicata-fatura-no-XML-e-no-Danfe
---

**Dúvida**Como gerar fatura no XML e no Danfe ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Para gerar a **fatura** é necessário que tenha registro na tabela **SE1 ou SE2** além disso:  
  
  
2- Verifique se o parâmetro está habilitado **MV\_GRUPCOB = .T.** Caso não tenha Crie e habilite o parâmetro:

**![20201117_153009.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099750833)**

3- Verifique se o parâmetro está configurado conforme o link abaixo, Caso não tenha Crie e configure o parâmetro: **MV\_LJTPNFE  
  
Conforme o link:**<http://tdn.totvs.com/pages/releaseview.action?pageId=244424303>

![20201117_153527.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099751273)

 4- Por padrão, para que seja levada as duplicatas no XML é necessário que o campo esteja preenchido **E4\_FORMA. Na TES é necessário que seja definido o campo Gera Dupl (F4\_DUPLIC) igual Sim.**

**![20201117_152020.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360097443954)**

* **Saiba mais:**

Caso o campo não apareça na condição de pagamento**,** verifique se o campo **está visível para o módulo no configurador:**

**![E4_FORMA_1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097441914)**

**![E4_FORMA_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360099746013)**

**![E4_FORMA_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360099746033)**

* **Importante:**

Caso a empresa transmita nota de entrada com formulário próprio = Sim, selecionar também o **módulo do SIGACOM, para que o campo E4\_FORMA seja apresentado na condição de pagamento.**

Lembrando que é necessário verificar a forma de pagamento escolhida no campo **E4\_FORMA**nessa condição de pagamento:

* Novas formas de pagamento **acrescentadas na NT 2020.06:**

Devem ser incluída através do configurador em tabelas **Genéricas -> Tabela 24**

**![tabela_24.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4407198900119)**

**Observação 2:** Caso necessário a inclusão de Formas de Pagamento (Sem Pagamento). Efetuar a inclusão através do Configurador, em Tabelas Genéricas (**24**).

Exemplo: SPG= Sem Pagamento e VC = Vale combustível

![FORMAS_NOVAS_DE_PG.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11653798866071)

* **Saiba mais:**

Se o campo ficar em branco **E4\_FORMA não tiver duplicata será gerado 99 - Outros e Caso tenha duplicata será gerado 15 - Boleto.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25654966995607)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25654972704407)

**Otherwise:**

Define um bloco de instruções a ser executado caso nenhuma das cláusulas CASE <condição> seja avaliada como verdadeira.

<https://tdn.totvs.com.br/display/framework/DO+CASE>

* ***Ponto de Entrada:***

A utilização do ponto de entrada **PE01NFESEFAZ.**

Segue link com exemplo:

[PE01NFESEFAZ - Manipulação em dados do Grupo Detalhamento da Forma de Pagamento](http://tdn.totvs.com/pages/viewpage.action?pageId=348298539)

Observação: Caso queira deixar o valor padrão **(tag <tPag>)**, não há necessidade de alterações nos valores do array 'AdetPag'.
