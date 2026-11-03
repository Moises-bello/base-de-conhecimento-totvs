---
content_hash: b4a7453c962e66ea25903589430a8287e2f173f429121b3264554de1fc3b1550
fetched_at: '2026-06-29T00:12:08.463962+00:00'
page_id: '934636053'
product: rm
source: tdn-rm
title: FISCAL01-25556 - DT - NFS-e - Falha de Cancelamento // Barueri /SP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=934636053
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25556 |

## **02. SITUAÇÃO/REQUISITO**

Inconsistência ao enviar o cancelamento de nota fiscal para Barueri/SP.

É apresentada a seguinte mensagem no processo de cancelamento e o mesmo não é processado:  
"Erro ao Cancelar NFS-e(s) da Coligada: 1 e Filial: 8. Motivo: Erro na execução do serviço [GERAARQIMPARR]. Motivo: É necessário inicializar o WebService antes de utilizar os serviços"

## **03. SOLUÇÃO**

Ajustado processo de cancelamento para não gerar mais o erro.

Foram feitas também alguns ajustes para melhorar a performance das chamadas ao TSS nos métodos gerararqimp e monitorx:

1. O método gerararqimp era chamado 1 vez com todas as notas sendo processadas o que gerava uma grande carga no servidor do TSS. Com a mudança o método passa a ser chamado em lotes de até 50 notas.
2. O método monitorx era chamado 1 vez para cada nota. Com a mudança ele passa a ser chamado em lotes de até 50 notas.

Disponível a partir da biblioteca 12.1.2406
