---
content_hash: cec524dc29f0b3c2b76e28041e077ecccc2306c3a98dc2c16bdf8c3b39121c6b
fetched_at: '2026-06-29T00:08:42.212539+00:00'
page_id: '287061658'
product: rm
source: tdn-rm
title: 1318075 CONTROLADORIA01-460 DT Tela Parâmetros Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287061658
version: 101
---

# Tela de parâmetros dos relatórios

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatórios contábeis |
| **Situação/Requisito:** | Ao acessar os relatórios nativos do módulo de gestão contábil a tela congela travando todo o sistema, a exemplo dos relatórios razão e balancete. |
| **Solução/Implementação:** | Ajuste na geração do relatório Diário para que o número do livro seja incrementado corretamente quando a opção "Não reiniciar a contagem de páginas a cada mudança de livro" é marcada. |
| **Conversores e Parâmetros:** | Ao selecionar um relatório contábil a tela congelava, pois estavam sendo carregados um número muito grande de filiais e departamentos. Para amenizar o problema a rotina responsável por retornar essas informações foi reescrita, permitindo que a tela seja carregada em um intervalo de tempo aceitável. Também foi liberada a seleção de coligadas sem precisar informar as filiais. Neste caso serão retornadas todas as filiais e departamentos pertencentes a coligada, porém na abertura da tela de parâmetros apenas a coligada precisará ser carregada, permitindo que a tela seja carregada rapidamente. |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
