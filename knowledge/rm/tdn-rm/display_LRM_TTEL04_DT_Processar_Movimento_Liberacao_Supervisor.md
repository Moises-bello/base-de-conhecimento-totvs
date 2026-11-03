---
content_hash: 959cf16d0d1960852f94b3307426bbf30ab2c2d8d134949b01aa73c4dd405698
fetched_at: '2026-06-29T00:06:11.149983+00:00'
page_id: '203766925'
product: rm
source: tdn-rm
title: TTEL04_DT_Processar_Movimento_Liberacao_Supervisor
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEL04_DT_Processar_Movimento_Liberacao_Supervisor
version: 4
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Processar Grupo de Movimentos, Gerar Financeiro |
| **Situação/Requisito:** | Ao fazer uso do processo “Processar Grupo de Movimentos”, se o cliente relacionando tem lançamento em atraso e está parametrizado para bloquear esse tipo de situação não é possível dar prosseguimento. É necessário incluir a opção de autorização do supervisor para esse tipo de operação. |
| **Solução/Implementação:** | Ao fazer uso do processo “Processar Grupo de Movimentos”, se o cliente relacionando tem lançamento em atraso e está parametrizado para bloquear esse tipo de situação, agora vai ser possível liberar através da autorização do supervisor. Essa opção só vai estar disponível quando o parâmetro "Liberar o bloqueio de cliente / fornecedor com a senha de supervisor (Cliente em atraso, Cliente vencidos e Limite de crédito)" estiver ativo.  A mesma regra de exibição agora é aplicada ao processo Gerar Financeiro. |
| **Conversores e Parâmetros:** | NA |
| **Chamados relacionados:** | NA |
| **Requisito (ISSUE):** | NA |
| **Versões/Release:** | 12.1.8 |
