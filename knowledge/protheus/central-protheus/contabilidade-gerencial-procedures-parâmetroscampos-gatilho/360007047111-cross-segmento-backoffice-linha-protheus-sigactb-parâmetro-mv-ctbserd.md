---
article_id: 360007047111
category: Contabilidade Gerencial - Procedures, Parâmetros,Campos, Gatilho
content_hash: 101f4831b799d333377fe3cf81d9204757933d86234af8ddb239a96809589d40
fetched_at: '2026-06-28T22:41:01.418142+00:00'
product: protheus
section_id: 1500001537361
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Parâmetro MV_CTBSERD
type: support-article
updated_at: '2021-09-15T17:09:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007047111-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Par%C3%A2metro-MV-CTBSERD
---

**Ocorrência**Não possui em seu SX6 o parâmetro MV\_CTBSERD, como criar.

**Ambiente**Cross Segmento - Backoffice Linha Protheus  – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

O parâmetro MV\_CTBSERD possibilita excluir (fisicamente) o arquivo temporário utilizado no controle de semáforo.

| MV\_CTBSERD = .T. | O arquivo é criado na pasta system na execução do controle de semáforo, porém cada vez que o controle for executado o sistema exclui e recria novamente o mesmo. |
| --- | --- |
| **MV\_CTBSERD = .F.** | **A cada execução do controle de semáforo o sistema reaproveita o arquivo, ou seja, não exclui e consequentemente não o recria.** |

Visualizando a pasta system do ambiente, ordenada por data de modificação:

![](https://tdn.totvs.com/download/attachments/286009617/image2017-8-4%2014%3A35%3A33.png?version=1&modificationDate=1501868134000&api=v2)

Habilitando o parâmetro **MV\_CTBSERD**:

![](https://tdn.totvs.com/download/attachments/286009617/image2017-8-4%2014%3A37%3A11.png?version=1&modificationDate=1501868232000&api=v2)

Para simular o controle de semaforo iremos incluir um lançamento contábil:

![](https://tdn.totvs.com/download/attachments/286009617/image2017-8-4%2014%3A39%3A31.png?version=1&modificationDate=1501868372000&api=v2)

Veja que no diretório system é criado o arquivo **\_CTBPROC99.dbf**.

Obs.: O número \_CTBPROC**99** se refere a empresa logada.

![](https://tdn.totvs.com/download/attachments/286009617/image2017-8-4%2014%3A40%3A39.png?version=1&modificationDate=1501868439000&api=v2)

<http://tdn.totvs.com/display/public/PROT/CTB0143_Parametro_MV_CTBSERD>

**Saiba mais**

[4047757\_DSERCTR1-15359 -DT Mensagem do semáforo ao ter concorrência nos lançamento contábeis](http://tdn.totvs.com/pages/viewpage.action?pageId=425443672)
