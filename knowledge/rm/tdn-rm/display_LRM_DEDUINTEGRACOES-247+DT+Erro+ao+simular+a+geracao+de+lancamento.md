---
content_hash: 5a458febdf812d6aa99d4020b9b7b518771f5a4f5740a3dac656035f810f674f
fetched_at: '2026-06-29T00:08:40.885188+00:00'
page_id: '286516054'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-247 DT Erro ao simular a geracao de lancamento
type: documentation
url: https://tdn.totvs.com/display/LRM/DEDUINTEGRACOES-247+DT+Erro+ao+simular+a+geracao+de+lancamento
version: 102
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Simular a geração de lançamentos financeiros |
| **Situação/Requisito:** | Quando o sistema está parametrizado para utilizar a data do contrato como data de emissão, e o contrato não possui uma data informada, a simulação de geração de lançamento não é executada corretamente, já que é emitido uma exceção impedindo a correta execução da funcionalidade. Isto também impacta na geração de contabilização do contrato. |
| **Solução/Implementação:** | Ajustes na obtenção de data de emissão do lançamento quando o sistema estiver parametrizado para obter a data do contrato. Quando o processo for executado via simulação da geração de lançamento a exceção informando que o contrato não possui uma data cadastrada não será lançada. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
