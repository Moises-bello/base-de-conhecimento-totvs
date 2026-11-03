---
article_id: 360018103692
category: Contabilidade Gerencial - Reprocessamento
content_hash: c16e67d4eca525c8813aeceb0a3d355114e90d5651fcf7e4fe8856ce02050263
fetched_at: '2026-06-28T22:40:42.016141+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: Como habilitar a consulta
  padrão case sensitive?'
type: support-article
updated_at: '2022-07-18T18:48:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018103692-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-habilitar-a-consulta-padr%C3%A3o-case-sensitive
---

**Dúvida**Como habilitar a consulta padrão case sensitive?

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80 **Solução**

**Para a correta pesquisa considerando case sensitive, devemos ter as configurações:**

**- Cadastro de usuário:**

O usuário deve ter acesso a pesquisa por**Case Sensitive**, portanto, no cadastro do usuário o acesso **155**deve estar habilitado:

![](http://tdn.totvs.com/download/attachments/361450078/1.jpg?version=1&modificationDate=1526476188000&api=v2)

**- Banco de dados:**

Verificar o Collation do banco de dados, conforme documentação:

<http://tdn.totvs.com/display/tec/Character+Set+x+Collation+para+DBAccess>

![](http://tdn.totvs.com/download/attachments/361450078/2.jpg?version=1&modificationDate=1526476188000&api=v2)

![](http://tdn.totvs.com/download/attachments/361450078/3.jpg?version=1&modificationDate=1526476188000&api=v2)

**- Configuração do campo a ser pesquisado**

Na execução da pesquisa é aplicado a Picture ao conteúdo pesquisado, então, se for utilizar a pesquisa por maiúscula\minuscula deve utilizar a Picture **@X** ao invés da **@!**. (Este procedimento é opcional, mas para input dos dados nos  cadastros em maiúscula ou minuscula terá que ser alterado a picture desta forma)

**Importante** :  Alterando a Picture **@X**  o sistema permitirá  também a inclusão da descrição maiúscula\minuscula.

![](http://tdn.totvs.com/download/attachments/361450078/image2018-5-16_10-8-43.png?version=1&modificationDate=1526476188000&api=v2)
