---
article_id: 360049190014
category: ADVPL - Classe e Função
content_hash: 8389c40b13c325d1b17dbed9bb32055a129f66cfe421a72aefc3daf401c59c08
fetched_at: '2026-06-28T22:40:16.971393+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - LGPD LGPD (Lei Geral
  de Proteção de Dados) em Customizações
type: support-article
updated_at: '2021-08-05T20:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049190014-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-LGPD-LGPD-Lei-Geral-de-Prote%C3%A7%C3%A3o-de-Dados-em-Customiza%C3%A7%C3%B5es
---

**Dúvida**Como devo tratar as customizações de acordo com LGPD?  
  
**Ambiente**Protheus – ADVPL – A partir da versão 12  
  
**Solução**

## O que é LGPD?

A **Lei Geral de Proteção de Dados Pessoais (LGPD ou LGPDP)**, Lei nº 13.709/2018, é a legislação brasileira que regula as atividades de tratamento de dados pessoais e que também altera os artigos 7º e 16 do [Marco Civil da Internet](https://pt.wikipedia.org/wiki/Marco_Civil_da_Internet "Marco Civil da Internet").

A partir de agosto de 2020, entrará em vigor no Brasil, a Lei 13.709 de 2018, a chamada Lei Geral de Proteção de Dados (“LGPD”), que estabelece regras, direitos e obrigações relativas aos dados pessoais. A nova legislação mudará a forma como privacidade e dados pessoais serão tratados no Brasil.

## O que a LGPD determina?

Agora que você já sabe **o que significa LGPD**, falaremos sobre suas principais determinações. Para facilitar a vida tanto de quem utiliza os dados como de quem fornece as informações, apresentamos a estrutura dos termos que compõem a Lei Geral de Proteção de Dados:

* **Dados pessoais;**
* **Dados sensíveis;**
* **Tratamento de dados;**
* **Titular dos dados;**
* **Consentimento aos dados;**
* **Anonimização e pseudoanonimização;**
* **Controlador e processador.**

Detalhes sobre cada item em **Saiba Mais.**

## O que acontece com quem desobedecer a LGPD?

Em caso de comprovação de infração quanto ao uso de forma ilegal, a multa pode chegar a R$ 50 milhões. A sanção também pode ser aplicada diariamente no pagamento de um valor até que a situação seja resolvida.

## Como aplicar LGPD em customizações?

Existem dois tipos de tratamentos que damos para os dados considerados como sensíveis ou pessoal que são eles: a anonimização e o ofuscamento.

Mais detalhes em **Saiba Mais**

O ofuscamento é o recurso de não exibir a informação para o usuário que não tem direito de acesso à ela. Nesse caso, a informação é ofuscada no componente de exibição da informação, seja ele um browser ou um relatório, e os componentes da Lib fazem isso de forma automática.

Com então à customizações que utilizam os componente da Lib, não é necessário se preocupar com essa questão, pois a exibição será feita de acordo com a configuração do campo e com o acesso do usuário.

Já as customizações que fazem acesso direto à informação no banco deverão tratar a exibição de acordo com as configurações. Na verdade as informações não estão criptografadas e então a questão não é na recuperação da informação e sim na exibição.

Para fazer esses tratamentos temos a **FwProtectedDataUtil** que disponibiliza vários métodos. Mais detalhes **Saiba Mais**

**Saiba Mais**:  
**[Dados Protegidos](https://tdn.totvs.com/display/framework/Dados+Protegidos)  
[FwProtectedDataUtil](https://tdn.totvs.com/display/public/PROT/FwProtectedDataUtil)  
[Anonimização de Dados Protegidos](https://tdn.totvs.com/pages/viewpage.action?pageId=532024154)  
[LGPD: Entenda tudo sobre a Lei Geral de Proteção de Dados](https://www.totvs.com/blog/negocios/lgpd-o-manual-para-compreender-a-lei-geral-de-protecao-de-dados/)**
