---
article_id: 360007158672
category: NFe - Nota Fiscal Eletrônica
content_hash: 9d057a6aaefd7a1f6b4e9e599d2906208b66a918a4215a50fb30fe901702c049
fetched_at: '2026-06-28T22:39:59.992800+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  871 Rejeição :
  O campo Forma de Pagamento deve ser preenchido com a opcao ''Sem Pagamento'''
type: support-article
updated_at: '2025-06-23T12:00:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007158672-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-871-Rejei%C3%A7%C3%A3o-O-campo-Forma-de-Pagamento-deve-ser-preenchido-com-a-opcao-Sem-Pagamento
---

**Dúvida**

**Como solucionar a rejeição abaixo ?**

Rejeição: 871 O campo Forma de Pagamento deve ser preenchido com a opcao 'Sem Pagamento'

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Quando possui a finalidade de Ajuste (finNFe = 3) ou Devolução (finNFe = 4)  independente da condição de pagamento informada, será aplicada a regra de validação onde a tag < tPag> será gerada **com a opção 90 - Sem Pagamento, conforme sugerido na NT 2016\_002.**

1. Por padrão, para que seja levada as formas de pagamento no XML é necessário que o campo esteja preenchido Forma Pgto. **E4\_FORMA.**

![20220405_085238.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986245994903)

* **Saiba mais:**

Caso o campo não apareça na condição de pagamento**,** verifique se o campo **está visível para o módulo no configurador:**

**![E4_FORMA_1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/32986252868759)**

**![E4_FORMA_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/32986252868887)**

**![E4_FORMA_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/32986245998103)**

**Importante:**

**Caso seja nota de entrada, habilitar o campo no módulo do SIGACOM.**

Lembrando que é necessário verificar a forma de pagamento escolhida no campo **E4\_FORMA**nessa condição de pagamento:

2. Novas formas de pagamento **acrescentadas na NT 2020.06:**

Devem ser incluída através do configurador em tabelas **Genéricas -> Tabela 24**

**![tabela_24.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986252869271)**

3. Cadastrar **a chave = SPG**

![20220405_091053.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986245999127)

4. Após isso, exclua a nota e **gere novamente.**
