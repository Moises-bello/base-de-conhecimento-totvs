---
content_hash: f3542a3f80f002c3896e975eff51ef9a247561f3fc47caba583028c42c2d88bc
fetched_at: '2026-06-29T00:12:00.693688+00:00'
page_id: '886028762'
product: rm
source: tdn-rm
title: Processo Imprimir Requisição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=886028762
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

No menu Movimentação de Estoque, o processo “Imprimir requisição” irá imprimir o relatório configurado conforme o tipo da requisição.

Action = SauVisualizaImprimePrescricaoMedicaProcAction

- O relatório necessita conter parâmetros: CODCOLIGADA, CODREQUISICAO

- O código do relatório que será impresso encontrasse nos Parâmetros do Gestão Hospitalar.

- No momento, não imprime requisições do tipo CME.

Segue os tipos de requisição que este processo imprime:

|  |  |
| --- | --- |
| **Tipo de Requisição** | **Parâmetro do Relatório** |
| 1 Requisição para Paciente  2 Devolução | Requisição |
| 3 Prescrição | Requisições originadas de Prescrição |
| 6 Folha de Sala | Folha de sala |
| 7 Requisição para centro de custo  9 Devolução de centro de custo | Baixa por centro de custo Prescrição (na tela 2/4) |
| 8 Transferência | Transferência |

## **02. EXEMPLO DE UTILIZAÇÃO**

Parâmetros do Gestão Hospitalar - Item Relatórios

|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
