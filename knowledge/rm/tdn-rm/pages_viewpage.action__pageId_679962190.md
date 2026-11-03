---
content_hash: 2d3c6fdd1a62db62ae7aefc4c90a059a180bbca90dc74e9203012d3d205dd7b5
fetched_at: '2026-06-29T00:11:17.391274+00:00'
page_id: '679962190'
product: rm
source: tdn-rm
title: Fazer Integração de Lote Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679962190
version: 8
---

A atividade para fazer a Integração de Lote Contábil. As principais propriedades existentes nela são:

* **CodColigada:** Código da coligada.
* **CodLote:** Código do lote. Essa propriedade deve receber um valor fixo (2020 por exemplo) ou deve estar associada a uma atividade que irá gerar o código do lote. Se o código não existir ele será criado.
* **DataContabilInicial:** Data inicial do Período do lançamento a ser integrado.
* **DataContabilFinal:** Data final do Período do lançamento a ser integrado.
* **FiltroGenerico:** Filtro genérico criado pelo usuário.
* **ParamsFiltroGenerico:** Parametros do Filtro genérico criado pelo usuário
* **Usuario:** Usuário que está executando a integração de Lote
* **PermiteLoteDuplicado:** Informa que o lote que já foi integrado anteriormente pode ser integrado novamente.
* **PodeExcluiLote:** Identifica se o lote deverá ser excluído na integração.
* **LogProcessamentoAtivado:** Informa se ao término do processo será mostrado o LOG de processamento mostrando o tempo gasto em cada etapa.
* **ListLancamentosParaDesbloquear:** Lista de Lançamentos para desbloquear. O controle de bloqueio por lançamento na integração vai acontecer somente quando o parâmetro. "ControlaBloqueioNoProcessoPorLancamento" estiver habilitado.

Segue um exemplo com a atividade configurada.
