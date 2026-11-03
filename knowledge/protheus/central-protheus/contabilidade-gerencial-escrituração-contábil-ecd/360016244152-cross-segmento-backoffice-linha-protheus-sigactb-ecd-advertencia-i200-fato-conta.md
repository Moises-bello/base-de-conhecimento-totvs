---
article_id: 360016244152
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: a493b4820f818dfe82e9c8d1b945a8ca2c0c9bfae5a0ef5b375af6a557bc5760
fetched_at: '2026-06-28T22:40:45.717846+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus -SIGACTB - ECD ADVERTENCIA I200|
  FATO CONTABIL
type: support-article
updated_at: '2023-03-24T17:50:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016244152-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-ADVERTENCIA-I200-FATO-CONTABIL
---

**Dúvida**PORQUE OCORRE A ADVERTÊNCIA : UM LANÇAMENTO PODE TER VÁRIOS REGISTROS A DÉBITO A VÁRIOS CRÉDITOS SOMENTE QUANDO RELATIVOS AO MESMO FATO CONTÁBIL ( ***Resolução CFC1299/2010***)?

**Ambiente**Microsiga Protheus  - Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

A Advertência I200 é a soma das partidas do lançamento a crédito, caso tenha diferença do valor informado, no registro do Lançamento Contábil. Ela ocorre devido ao fato do validador interpretar as informações do lote contábil por operação/processo, que não era validado.

A advertência informa ainda que os lançamentos de quarta fórmula (vários débitos para vários créditos) devem se referir a um mesmo fato contábil.

Veja se os lançamentos informados se referem ao mesmo fato, caso a resposta for positiva, orientamos que entre em contato com a Receita Federal e solicite os procedimentos para realizar a validação desta advertência.

Fatos contábeis são ocorrências que alteram, qualitativa e/ou quantitativamente, o patrimônio. Esta validação ocorre porque em um mesmo lançamento (I200) que aparecem várias (I250) contas debitadas e várias contas creditadas, na resolução CFC-1299/10 , ao utilizar esta modalidade de lançamentos só pode se referir a um único fato contábil.

Caso observe, que a orientação abaixo já está na Resolução:

Lançamento contábil

1. O lançamento contábil deve ter como origem um único fato contábil e conter:

(a) um registro a débito e um registro a crédito; ou

(b) um registro a débito e vários registros a crédito; ou

(c) vários registros a débito e um registro a crédito; ou

(d) vários registros a débito e vários registros a crédito, quando relativos ao mesmo fato contábil.

Esta advertência é apenas para verificar se os lotes estão corretos, servindo para alertar em relação ao fato de um lançamento ter várias contas debitadas e creditadas, pois não possível o PVA validar se pertencem ao mesmo fato contábil.

Foi liberada a melhoria que pode minimizar a advertência dependendo de como  foi realizada a contabilização do lote :  [MV\_CTBSDOC (Clique Aqui)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025883891-MP-SIGACTB-ECD-I200-PORQUE-N%C3%83O-ESTA-CONSIDERANDO-O-NUMERO-DO-LOTE?source=search)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069905514/mceclip0.png)Dependendo de como estive contabilizado o lançamento o sistema irá somente minimizar as advertência. Se o lançamento contábil não estiver exatamente conforme exemplo apresentado no link acima, o parâmetro não terá efeito, com isso para alguns lotes a advertência continuará ser apresentada

Saiba mais:

[MP-SIGACTB - ECD - 4-VL\_LCTO - REGISTRO I200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008353712-MP-SIGACTB-ECD-4-VL-LCTO-REGISTRO-I200?source=search)

[MP - SIGACTB - Erro no validador registro I200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028621892-MP-SIGACTB-Erro-no-validador-registro-I200?source=search)

[MP-SIGACTB ECD I250 O REGISTRO LIDO TEM QUANTIDADE DE CAMPOS DIFERENTE DO ESPECIFICADO NO LAYOUT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047283673-MP-SIGACTB-ECD-I250-O-REGISTRO-LIDO-TEM-QUANTIDADE-DE-CAMPOS-DIFERENTE-DO-ESPECIFICADO-NO-LAYOUT?source=search)
