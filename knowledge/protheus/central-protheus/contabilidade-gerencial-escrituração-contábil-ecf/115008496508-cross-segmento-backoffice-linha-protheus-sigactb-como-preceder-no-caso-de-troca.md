---
article_id: 115008496508
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 1ad49bf58d55b242883a5cd411afa330cd06ee59a4c1a1e58843f1c0f2946cbc
fetched_at: '2026-06-28T22:40:47.485388+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- Como preceder no caso
  de troca de contador ou alteração no plano de contas durante o período da ECF a
  ser entregue
type: support-article
updated_at: '2021-12-09T14:59:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008496508-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-preceder-no-caso-de-troca-de-contador-ou-altera%C3%A7%C3%A3o-no-plano-de-contas-durante-o-per%C3%ADodo-da-ECF-a-ser-entregue
---

**Ocorrência**

Como preceder no caso de troca de Contador, ou alteração no Plano de Contas durante o período da ECF a ser entregue?

**Ambiente**

Microsiga Protheus  – Contabilidade Gerencial – A partir da versão 11.80

**Solução**

Não é possível transmitir duas ou mais ECF no caso de mudança de  contador  no  período  ou  mudança  de  plano  de  contas  no período. A ECF deve ser transmitida em arquivo único, a menos que ocorra alguma das situações especiais previstas no Registro 0000.  Caso  a  entidade  tenha  que  recuperar  os  dados  da  ECD,  devem ser recuperados os dois arquivos da ECD transmitidos (um para cada contador ou um para cada plano de contas). Contudo, para  que  a  ECF  recupere  os  dados  corretamente  é  necessário  que  os  saldos  finais  das  contas  que  aparecem  no  primeiro  arquivo (primeiro contador ou primeiro plano de contas) sejam iguais aos saldos iniciais dessas mesmas contas que aparecem no  segundo  arquivo  (segundo  contador  ou  segundo  plano  de  contas).  Se  isso  não  ocorrer,  a  ECF  recuperará  somente  os  dados do segundo arquivo e os ajustes necessários deverão ser realizados na própria ECF ou na ECD, por meio de substituição.

Veja também :

* [Mudança no plano de contas (CT1) como proceder?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018544191-MP-SIGACTB-CTBA020-Mudan%C3%A7a-no-plano-de-contas-CT1-como-proceder-?source=search)
* [I157 O PROTHEUS ESTÁ HABILITADO PARA GERAR AS INFORMAÇÕES DO REGISTRO ( TRANSFERÊNCIA DE SALDOS DE PLANO DE CONTAS ANTERIOR)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003409082-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-gerar-o-registro-I157-da-ECD?source=search)
