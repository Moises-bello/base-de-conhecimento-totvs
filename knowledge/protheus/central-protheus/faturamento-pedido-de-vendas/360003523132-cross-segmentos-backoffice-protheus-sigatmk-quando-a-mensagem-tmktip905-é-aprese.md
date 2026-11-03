---
article_id: 360003523132
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: c2271d9e7b2f78a3b2d799fc0c0fa03f3e5824962a2821d114377ddb9f04f16f
fetched_at: '2026-06-28T22:38:41.014703+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Quando a mensagem TMKTIP905
  é apresentada
type: support-article
updated_at: '2024-04-25T12:34:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003523132-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Quando-a-mensagem-TMKTIP905-%C3%A9-apresentada
---

**Dúvida**

Quando a mensagem **TMKTIP905** é apresentada?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Solução**

A mensagem apresentada **TMKTIP905** indica que a quantidade de parcelas não esta compatível com a quantidade de parcelas informada no parâmetro **MV\_NUMPARC** e os campos referentes às parcelas e vencimentos para a condição de pagamento **Tipo 9**.

Isto ocorre quando são criados novos campos de número de parcelas na base de dados.

É necessário realizar as seguintes verificações:

1. Se no parâmetro **MV\_NUMPARC** consta o mesmo número de parcelas conforme os campos novos que foram criados, lembrando que no padrão é 4 e as parcelas padrões no sistema são **CJ\_PARC4, CJ\_DATA4, C5\_DATA4 e C5\_PARC4**.
2. Se (os) campo (os) existe (em) tanto no **SX3** como na nas tabelas **SCJ** e **SC5**, caso não, é necessário rever a estrutura destas ou criar o campo.
3. Se existir, verificar se o campo esta em uso e se o nível é equivalente ao do usuário corrente. Este é um campo customizado sendo utilizado somente na condição de pagamento do tipo 9.
4. Valide se a nomenclatura da 10 parcela em diante está escrita em alfanumérico, exemplo **c5\_PARCA, C5\_DATAA**.

**Para maiores informações acesse a FAQ no TDN: [FAT0033 Mensagem TMKTIP905](http://tdn.totvs.com/pages/viewpage.action?pageId=225950783)**
