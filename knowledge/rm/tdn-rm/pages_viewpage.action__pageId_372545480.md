---
content_hash: 7dda789a8195596ee5e74d1ab0b3ca45e2436438f3ce747e6c62c4fc8fe39f5e
fetched_at: '2026-06-29T00:09:01.101068+00:00'
page_id: '372545480'
product: rm
source: tdn-rm
title: 98149 MATESTCNTFTOF01-43 DT Alteração no Relatório da Ficha Física Financeira
  - Quebra por Código do Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372545480
version: 5
---

# FICHA FÍSICA FINANCEIRO DEFININDO QUEBRA POR CÓDIGO DO PRODUTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Ficha Física Financeira. |
| **Situação/Requisito:** | Ao emitir o relatório da Ficha Física Financeira marcando o parâmetro para **Definir Quebra por Código Produto** e **Totalizar por Quebra**, o sistema está emitindo o cabeçalho com as informações dos Totalizadores para cada um dos produtos do Grupo de Quebra definido.  Com isso, dependendo da quantidade de registros na base de dados, eram geradas informações desnecessárias no relatório com impressão do cabeçalho. |
| **Solução/Implementação:** | Realizado o ajuste para o relatório em .Net ter o mesmo comportamento do relatório em Delphi.  A partir de agora, o cabeçalho será impresso por **Local de Estoque** quando definido para **Quebrar por Código do Produto**, e este for do tipo **Sintético**. |
| **Conversores e Parâmetros:** | **Importar relatório Ficha Física Financeira**   * Acesse menu Gestão | RM Reports. * Selecione opção de Filtro. * Na visão RM Reports acesse Processos | Importar Estrutura de Relatório. Selecione o relatório e marque a opção Sobrescrever Existente.     Estoque | Consultas e Relatórios | Relatório de Ficha Física Financeira.  Sintético | Definir Quebra por Código Produto. |
| **Tickets relacionados:** | 98149, 101842. |
| **Requisito:** | Ficha Física Financeira. |
| **Documento de Referência:** | Não se aplica. |

## Descrição

1. Acessar Estoque | Consultas e Relatórios | Relatório de Ficha Física Financeira e informar os parâmetros:
2. Relatório gerado com as informações do cabeçalho por Local de Estoque:  
   **Local 01:**  
     
     
   **Local 02:**
