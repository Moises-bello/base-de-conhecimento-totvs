---
content_hash: e9a0aac9c481760687a769d226debc6952ad7f71d80c8527d417008df6e52963
fetched_at: '2026-06-29T00:06:20.068829+00:00'
page_id: '221547483'
product: rm
source: tdn-rm
title: TSSUVM_FOLHA_ANALITICA_QUEBRA_SECAO
type: documentation
url: https://tdn.totvs.com/display/LRM/TSSUVM_FOLHA_ANALITICA_QUEBRA_SECAO
version: 1
---

# Folha Analítica

|  |  |
| --- | --- |
| **Linha de Produto:** | *Construção e Projetos* |
| **Segmento:** | *RM* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Emissão Folha Analítica em* *Vídeo* |
| **Situação/Requisito:** | Ao gerar Folha Analítica ocorre inconsistência na quebra da página, onde o funcionário de uma determinada seção saí agrupado na seção anterior e que não possui movimentação. É necessário uma condição muito especifica. A folha analítica Delphi deve ser em vídeo, a seção deve ter funcionário mas todos os funcionários não ter movimentação e o parâmetro "Imprime func sem movimentação" deve estar desmarcado. O Funcionário da seção posterior deve ter apenas um evento de provento ou um evento de desconto e este deve estar sendo impresso nas ultimas três linhas. |
| **Solução/Implementação:** | A folha analítica Delphi passa a não imprimir seções que não possui funcionários impressos. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSSUVM |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
