---
content_hash: 587b9fbe7e8e10f417a61dde793ea8efee199a6f6eb14e9f064a55279ab3d040
fetched_at: '2026-06-29T00:08:21.055942+00:00'
page_id: '268810475'
product: rm
source: tdn-rm
title: TWAKMC_DT_Lançamento_Alteração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268810475
version: 113
---

# Lançamento - Alteração

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Lançamento - Alteração |
| **Situação/Requisito:** | Ao gerar reajuste de parcelas de um contrato (componentes de juros e CM pos entrega),  o sistema acusa a existência de parcelas em atraso e não executa o processo. |
| **Solução/Implementação:** | Ajustado o serviço de alteração de lançamentos para não cancelar o reajuste de lançamentos,  onde o cliente está em atraso e o sistema financeiro estiver parametrizado para  "Controlar cliente em atraso" e não "Bloquear cliente em atraso" |
| **Conversores e Parâmetros:** | Ambiente | parâmetros | Totvs Gestão Financeira | Avançar | Contas A Receber | Avançar | Etapa "Situação Cliente" | Habilitar a opção "Controla Clientes em Atraso - 2 dias" e desabilitar a opção "Bloquear Clientes em Atraso". |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000045 |

divs
