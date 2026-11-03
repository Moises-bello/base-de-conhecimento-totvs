---
content_hash: 3fcb383baf7d4a021d9e29eb833d3fa045653c6463b56918e105a8289c246ac5
fetched_at: '2026-06-29T00:08:03.405438+00:00'
page_id: '235320362'
product: rm
source: tdn-rm
title: TUOG70_DT_Validacao_Liberacao_Competencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOG70_DT_Validacao_Liberacao_Competencia
version: 119
---

# VALIDAÇÃO DA LIBERAÇÃO DE COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Validação da liberação de competência* |
| **Situação/Requisito:** | Ao Liberar a Competência é apresentado o erro: Erro ao atualizar Base de FGTS para funcionários afastados no mês: Chave duplicada .  Erro é apresentado quando existem funcionários afastados pelo tipo T,M ou O e existe no envelope o evento de CC315 zerado, na Liberação o sistema tenta Inserir o evento CC 315 com valor porém é retornado o erro de Chave Duplicada. |
| **Solução/Implementação:** | Implementada, na validação da liberação de competência, regra para validar e informar ao usuário  possíveis funcionários com eventos de código de cálculo 315 com valor zerado, o que gera inconsistência na liberação de competência |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TUOG70* |
| **Requisito (ISSUE):** |  |

divs
