---
content_hash: bc875f09451ba30089493c3f13a9737d96a30fa106c8011ffd309912589bcac5
fetched_at: '2026-06-29T00:11:56.470528+00:00'
page_id: '866527882'
product: rm
source: tdn-rm
title: Requisições de Substituição - Integração com TOTVS RH Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866527882
version: 3
---

Ao habilitar a integração entre o **TOTVS RH Orçamento** e o **TOTVS Gestão de Pessoas**, a aba **"Integração com TOTVS RH Orçamento**" será exibida na requisição de **Substituição,** conforme ilustrado na imagem abaixo. Além disso, essa aba também estará visível nos pareceres das requisições.

Como a integração habilitada, **todas** as requisição de substituição serão enviadas para o **orçamento** independente da requisição pai (sendo ela de alteração de dados funcionais, transferência, transferência com alteração de dados ou desligamento) ter sido enviada para o orçamento.

Na requisição de substituição, deverão ser enviados os campos *Centro de Custo (CODCCUSTO), Item Contábil (IDITEMCONTABIL) e Classe de Valor* *(IDCLASSEVALOR)* com os valores existentes para o funcionário que originou a requisição de acordo com a prioridade:

**1** **-** Verificar se existe valor preenchido no cadastro de funcionário

**2 -** Caso não exista, verificar se há valor preenchido no rateio fixo do funcionário, considerando o **centro de custo com o maior percentual**.

**3 -** Caso ainda não exista, verificar se há valor preenchido na seção do funcionário.

**Avisos Importantes:**

* A aba **"Integração com TOTVS RH Orçamento"** será habilitada somente quando a integração estiver habilitada.
  + Para obter mais informações sobre a parametrização da integração, consulte o link a seguir: [Habilitar Integração TOTVS RH Orçamentos com TOTVS Gestão de Pessoas](https://tdn.totvs.com/pages/viewpage.action?pageId=859075333)
* O campo "Permite Exceção" nunca será habilitado pois irá refletir o retorno do TOTVS RH Orçamento, onde somente será marcado, caso no TOTVS RH Orçamento esteja habilitada a possibilidade de Exceção quando de uma negativa.
* Para as requisições do tipo **Substituição** os campos não poderão ser alterados, pois os dados são oriundos de outra requisição (requisição pai).
