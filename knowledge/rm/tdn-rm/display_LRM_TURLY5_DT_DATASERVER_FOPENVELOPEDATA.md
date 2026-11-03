---
content_hash: ad31514235e729c523f159acc8c192ba27bef3b27b6259379ce5c3445136e7fb
fetched_at: '2026-06-29T00:08:10.768334+00:00'
page_id: '240981015'
product: rm
source: tdn-rm
title: TURLY5_DT_DATASERVER_FOPENVELOPEDATA
type: documentation
url: https://tdn.totvs.com/display/LRM/TURLY5_DT_DATASERVER_FOPENVELOPEDATA
version: 114
---

# WEBSERVICES - FOPENVELOPEDATA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Webservices - FopEnvelopeData* |
| **Situação/Requisito:** | Ao tentar acessar o dataserver FopEnvelopeData via webservices, eram exibidos diversos erros de referência de objeto |
| **Solução/Implementação:** | *Foram adicionados os tratamentos necessários para que o dataserver funcione via webservices. Ao passar no envelope SOAP o nome do dataserver, deve-se passar também a informação se a visão é por centro de custo ou não, ficando da seguinte forma:*  *<tot:DataServerName>FopEnvelopeData/porcentrodecusto=false</tot:DataServerName>*  *ou*  *<tot:DataServerName>FopEnvelopeData/porcentrodecusto=true</tot:DataServerName>*   Atenção: apenas as funções de GetSchema, ReadRecord e ReadView estão disponíveis para esse dataserver. |
| **Chamados relacionados:** | TURLY5 |

divs
