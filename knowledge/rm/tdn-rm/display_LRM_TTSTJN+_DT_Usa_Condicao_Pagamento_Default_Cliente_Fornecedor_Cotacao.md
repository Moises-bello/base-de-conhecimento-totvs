---
content_hash: 453570db086aca81f2cc704b0d7785d93302bb9dbcc0e790d95b8a24594d122c
fetched_at: '2026-06-29T00:06:21.979799+00:00'
page_id: '223909723'
product: rm
source: tdn-rm
title: TTSTJN _DT_Usa_Condicao_Pagamento_Default_Cliente_Fornecedor_Cotacao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTSTJN+_DT_Usa_Condicao_Pagamento_Default_Cliente_Fornecedor_Cotacao
version: 3
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque Compras e Faturamento |
| **Função:** | Definir condição de pagamento default para o cliente fornecedor na cotação |
| **Situação/Requisito:** | Após registrar orçamento da cotação o sistema não preenche o valor default para a condição de pagamento.  Parametrização necessária da cotação:  Definição de Escopo-Filial --- Definições Gerais 1/4 --- Marcar condição de pagamento por fornecedor.  No cadastro do cliente fornecedor definir uma condição de pagamento default  Criar um movimento com este fornecedor  Criar a cotação para o movimento criado anteriormente, no processo de cotação não definir condição de pagamento  Concluindo o registro orçado, a condição de pagamento definida como default não foi a condição definida no anexo do cliente fornecedor. |
| **Solução/Implementação:** | Ajuste no processo de cotação para buscar default a condição de pagamento do cliente fornecedor. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Chamados relacionados:** | Não se aplica |
| **Requisito (ISSUE):** | Não se aplica |
| **Versões/Release:** | 11.82.43 |
