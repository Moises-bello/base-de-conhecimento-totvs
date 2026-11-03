---
article_id: 360019339412
category: Contabilidade Gerencial - Contabilização txt
content_hash: 03c5f3eeecbbd2d181e96f5a002f1a033982e048378df04da364eed25745ff80
fetched_at: '2026-06-28T22:40:55.453089+00:00'
product: protheus
section_id: 1500001537521
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA500 PE para Validação
  do arquivo txt '
type: support-article
updated_at: '2021-09-28T14:16:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019339412-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA500-PE-para-Valida%C3%A7%C3%A3o-do-arquivo-txt
---

**Dúvida**Como realizar a validação do arquivo txt na rotina CTBA500?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus-  Contabilidade Gerencial - 12.1.17  
  
  
**Solução**O ponto de entrada CTB500VLD é utilizado na Importação off-line .TXT para validar o arquivo a ser importado no processamento.

O ponto de entrada, ira validar o arquivo texto a ser importado na rotina de contabilizacao TXT. Se o retorno do PE for .T. o sistema prossegue com a contailizacao, se .F. a contabilizcao sera interrompida.

## Ponto de Entrada

|  |  |
| --- | --- |
| **Descrição:** | Valida o arquivo TXT a ser importado na contabilizacao TXT. |
| **Eventos:** | If lCTB500VLD  lContinua := ExecBlock("CTB500VLD",.F.,.F.) Endif |
| **Programa Fonte:** | CTBA500 |
| **Retorno:** | Logico |

Exemplo:

#Include '[Protheus.ch](http://protheus.ch/)'

User Function CTB500VLD()

Local lRet  := .T.

/\*  Se lRet for .T. , continua a contabilizacao

    se lRet fot .F. , contabiliza;'ao interrompida \*/

Return lRet

**Saiba Mais**<http://tdn.totvs.com/display/PROT/DT_PE_CTB500VLD_Valida+arquivo.TXT>
