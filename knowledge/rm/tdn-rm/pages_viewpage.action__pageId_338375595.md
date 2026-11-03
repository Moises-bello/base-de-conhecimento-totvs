---
content_hash: 025f95748a9d1b28809c22062da10d3eeca9c8b9ff1bc9296cbb31156422bc55
fetched_at: '2026-06-29T00:08:51.989622+00:00'
page_id: '338375595'
product: rm
source: tdn-rm
title: 2261869 EDUCACIONAL01-4087 DT Inscrição de candidato em prova
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338375595
version: 93
---

# INSCRIÇÃO DE CANDIDATO EM PROVA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Avaliação e Pesquisa |
| **Função:** | Inscrição de candidato em prova |
| **Situação/Requisito:** | Ao tentar realizar a inscrição de um candidato, via webservice, o sistema não calcula o identificador de execução da prova. |
| **Solução/Implementação:** | Foi realizada uma alteração no sistema para que o código de identificação de execução da prova seja gerado independentemente da origem da solicitação de inscrição.  Quando a chamada é realizada via webservice, alguns campos são necessários no XML da solicitação:    Dataserver: ***TstProvasAnexoCandidatosData*** XML  1 04  N  62 ]]]]>]]> Os campos **ID** e **IDEXECPROVA** não precisam conter valores, pois são gerados automaticamente. Porém as tags precisam existir no XML.    Obs.: Caso sejam informados os valores ***vazio***, ***"0"*** ou ***"-1"*** na tag **IDEXECPROVA**, ela terá o mesmo comportamento de quando não houver nada informado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
