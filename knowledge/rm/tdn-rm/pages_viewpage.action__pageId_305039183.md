---
content_hash: 8b3b8a84ca93cb0ba882e29199f7d2fa83b42119d33cbcc611e6addebb918a1b
fetched_at: '2026-06-29T00:08:43.606019+00:00'
page_id: '305039183'
product: rm
source: tdn-rm
title: 1223350 MATESTCNTFTOF01-629 DT NFe complementar de Preço - Quantidade igual
  a 0(zero)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=305039183
version: 97
---

# FICHA FÍSICA FINANCEIRA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Ficha Física Financeira. |
| **Situação/Requisito:** | Ao incluir um movimento de NF Complementar de valor utilizando motivo 27 (NF Complementar com Cópia de Itens) informando quantidade (zero), a Ficha Física Financeira a Movimentação de entrada que foi realizada o Saldo Financeiro está sendo apresentado na coluna Tot.Saída  porém o mesmo deveria ser apresentado na coluna Tot.Entrada pois a movimentação trata-se de uma entrada. |
| **Solução/Implementação:** | Quando o movimento de NF Complementar Permitir Item com Quantidade Zero e o Efeito Saldo for igual a Aumenta e o Valor Financeiro com Sinal for maior que zero, serão atualizados os dados de entrada na tabela Ficha Física/Financeira dos Produtos. |
| **Conversores e Parâmetros:** | Configurações necessárias no Tipo de Movimento de NF Complementar:  Acesse **BackOffice > Gestão de Estoque, Compras e Faturamento > Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento.**  Selecione o movimento de código 1.2.XX e clique em **Parametrizar** e configure os seguinte parâmetros:   | Etapa | Parâmetro | Valor | | --- | --- | --- | | Mov - Outros Dados | Usar Cópia de Movimentos por referência | Marcado | | Motivo de Referência | 27 - NF Complementar com Cópia de Itens. | | Item - Identificação 2/2 | Permitir Item com Quantidade Zero | Marcado | | Item - Preços | Editar Preço Total | Marcado  Não Calcular Preço Unitário | | Aceitar Preço Zero | Marcado | | Estoque - Estoque 1/3 | 2 - Saldo Atual | Aumenta | | Estoque - Estoque 2/3 | Saldo Financeiro Efeito sobre o Saldo Atual | Aumenta | | Fórmula do Valor Financeiro | Valor Total do Item. Conteúdo da fórmula: TABITM ('VALORTOTALITEM' , 'V') | |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | Relatório de Ficha Física Financeira; Regerar Saldos e Custos. |

divs
