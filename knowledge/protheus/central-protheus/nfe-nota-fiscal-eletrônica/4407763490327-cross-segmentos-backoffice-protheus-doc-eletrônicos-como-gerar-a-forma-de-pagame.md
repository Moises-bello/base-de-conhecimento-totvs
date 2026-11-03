---
article_id: 4407763490327
category: NFe - Nota Fiscal Eletrônica
content_hash: a72df4b3b3303b40364040029f990e79ef31295fe5f99de008dd3725046967b0
fetched_at: '2026-06-28T22:40:03.521427+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar a forma
  de pagamento 90 - Sem pagamento
type: support-article
updated_at: '2025-06-17T12:13:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407763490327-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-forma-de-pagamento-90-Sem-pagamento
---

**Dúvida**Como gerar a forma de pagamento 90 - Sem pagamento  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Quando possui a finalidade de Ajuste (finNFe = 3) ou Devolução (finNFe = 4)  independente da condição de pagamento informada, será aplicada a regra de validação onde a tag < tPag> será gerada **com a opção 90 - Sem Pagamento, conforme sugerido na NT 2016\_002.**

* Conforme o parecer do link abaixo, **a opção 90** é apenas para nota de **Ajuste, Complemento e Devolução:**

[Parecer da consultoria](https://tdn.totvs.com/pages/releaseview.action?pageId=599041541)

[Parecer da Consultoria](https://tdn.totvs.com/pages/releaseview.action?pageId=636720599)

![SEM_PAGAMENTO.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/15422719259031)

1 - Para notas de devolução com **FINNFE = 4, não é necessário ter condição de pagamento.**  
  
  
2- Para não informar a forma de pagamento é necessário utilizar um **CFOP com finalidade de devolução.**  
  
  
3- É possível consultar a **nota técnica 2015.003\_v\_1.22** página 130 para saber quais são os CFOPs com finalidade de devolução:  
  
<http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=>  
  
  
4- Ou a nota com  CFOP que não tem finalidade de devolução precisa ter finalidade de **Ajuste** **FINNFE = 3** no TES o campo **F4\_AJUSTE -> Ajuste CIAP = S, além disso as configurações do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Inclusão de Nota de Estorno e Estorno de Devolução (NF de devolução emitida com erros)](https://totvssuporte.zendesk.com/hc/pt-br/articles/360020898192)

* **Saiba mais:**

Se desejar utilizar para notas que não seja de **devolução ou ajuste** abrir um ticket no suporte com a legislação para análise.

A única UF que temos a informação que é prevista essa operação é SE.

* **Link do TDN:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=606095368>

* **Importante:**

Caso seja necessário gerar realmente **90 Sem pagamento:**

1- Por padrão, para que seja levada as formas de pagamento no XML é necessário que o campo esteja preenchido Forma Pgto. **E4\_FORMA.**

![20220405_085238.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5242038623895)

* **Saiba mais:**

Caso o campo não apareça na condição de pagamento**,** verifique se o campo **está visível para o módulo no configurador:**

**![E4_FORMA_1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15422719263511)**

**![E4_FORMA_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15422761854103)**

**![E4_FORMA_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15422761856279)**

**Importante:**

**Caso seja nota de entrada, habilitar o campo no módulo do SIGACOM.**

Lembrando que é necessário verificar a forma de pagamento escolhida no campo **E4\_FORMA**nessa condição de pagamento:

2- Novas formas de pagamento **acrescentadas na NT 2020.06:**

Devem ser incluída através do configurador em tabelas **Genéricas -> Tabela 24**

**![tabela_24.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15422761857559)**

3 - Cadastrar **a chave = SPG**

![20220405_091053.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5242370625047)

4 - Após isso, exclua a nota e **gere novamente.**
