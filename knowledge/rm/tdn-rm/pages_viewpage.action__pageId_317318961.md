---
content_hash: e43ad4041ceaaf207b9f3027f03d361e7177d9e209718ea2a00173dadf6bf1e3
fetched_at: '2026-06-29T00:08:47.000083+00:00'
page_id: '317318961'
product: rm
source: tdn-rm
title: CONTROLADORIA01-782  DT Relatório Balancete Conta Gerencial Inativa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317318961
version: 3
---

# Relatório Balancete Conta Gerencial Inativa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatório Balancete Conta Gerencial Inativa |
| **Situação/Requisito:** | 1 - Verificar o comportamento do filtro de conta inativa no Balancete em Delphi, quando é marcado o Tipo de Balancete "Gerencial" e "Gerencial\Contábil". 2 - Quando marcada a opção de Não exibir as Inativas ele filtra as Contas Contábeis? Neste caso, alteraríamos para filtrar as Contas Gerenciais |
| **Solução/Implementação:** | 1 - No Delphi a opção não faz efeito para os dois tipos de relatório pois, por padrão eles não retornam contas gerenciais que estejam Inativas, Sem Movimentação e Sem Saldo. No relatório .Net é necessário manter pois o tipo de balancete Gerencial mostra todo o plano de contas gerencial o que torna a usabilidade do parâmetro necessária.  2 - Quando a opção é marcada as contas apenas não são exibidas porém não deixam de serem incluídas nas consultas para que não ocorra diferença no saldo de outras contas. No Caso o campo funciona para não exibir as contábeis quando o tipo do balancete é Contábil e gerencial quando o tipo do relatório é Gerencial não sendo necessário alteração no comportamento do parâmetro.    Melhoria no Relatório Balancete relacionado a implementação do processo de Inativação/Ativação de conta Gerencial. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
