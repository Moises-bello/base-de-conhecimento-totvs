---
content_hash: 9c65d565239e6b5947aa2df4bdca41deaf51dbff183021a2a81e84cda22d9871
fetched_at: '2026-06-29T00:05:47.276994+00:00'
page_id: '1010252598'
product: rm
source: tdn-rm
title: DT - Adequação do arquivo AEJ para contemplar as informações do REP-A e REP-P
  do PontoWeb e REP-A e REP-C do Suricato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1010252598
version: 8
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Arquivo AEJ |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-8383](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-8383) |

## **02. REQUISITO**

Adequar o arquivo AEJ para que exiba corretamente as informações referentes ao REP-A e REP-P do PontoWeb e ao REP-A e REP-C do Suricato.

## **03. SOLUÇÃO**

O arquivo AEJ foi ajustado para receber e exibir corretamente as informações dos REP's provenientes das integrações com o PontoWeb e Suricato.

O arquivo apresenta adequadamente os dados dos REP’s correspondentes.

11AEJ - PontoWeb REP-A

A informação do **REP-A** é obtida da tabela **AAFDT**, campo **CONVCOLETIVA**.

Ao gerar o AEJ, será exibido o **REP do tipo 2**, correspondente ao REP-A, com o número encontrado no campo **CONVCOLETIVA** da tabela **AAFDT**.

2AEJ - PontoWeb REP-P

A informação do **REP-P** (número de registro no INPI) é obtida da tabela **AINTEGRACAOBATIDAS**, campo **CODREP**.

Ao gerar o AEJ, será exibido o **REP do tipo 3**, correspondente ao REP-P, com o número contido no campo **CODREP** da tabela **AINTEGRACAOBATIDAS**.

3AEJ - Suricato REP-A

A informação do **REP-A** é obtida da tabela **AAFDT**, campo **CONVCOLETIVA**.

Ao gerar o AEJ, será exibido o **REP do tipo 2**, correspondente ao REP-A, com o número encontrado no campo **CONVCOLETIVA** da tabela **AAFDT**.

3AEJ - Suricato REP-C

A informação do **REP-C** (número de fabricação do REP) é obtida da tabela **AHSTIMPORTACAO**, campo **NUMEROREP**.

Ao gerar o AEJ, será exibido o **REP do tipo 1**, correspondente ao REP-C, com o número encontrado no campo **NUMEROREP** da tabela **AHSTIMPORTACAO**.

## **04. VERSÕES**

A partir dos patches:

* 12.1.2510.114 e superiores.
* 12.1.2502.232
* 12.1.2506.181
