---
content_hash: 4e05a245b3b6e9458e3d6c87f482e484023df7df188d23b8e120fade19c613c4
fetched_at: '2026-06-29T00:08:18.889669+00:00'
page_id: '266973283'
product: rm
source: tdn-rm
title: TVVZ35_DT_Relatório_Salário_Contribuição_Competência_Atual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266973283
version: 112
---

# RELATÓRIO SALÁRIO DE CONTRIBUIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Relatório Salário de Contribuição* |
| **Situação/Requisito:** | *Ao Gerar o relatório Salário de contribuição (AAS) para funcionário demitido no mês, não busca as verbas relacionadas a sua rescisão mesmo com o parâmetro Imprime competência atual marcado.*  *Segundo o manual do sistema o parâmetro Imprime competência atual:*  *Marcando este parâmetro será impresso no relatório de salário de contribuição os valores do mês corrente para funcionários demitidos, ou seja, valores registrados na demissão. Este campo é calculado no momento da impressão do Salário de Contribuição e somente será guardado na tabela após a liberação da competência.* |
| **Solução/Implementação:** | *Adicionada a movimentação do mês corrente de funcionários demitidos quando o parâmetro "Imprime Competência atual" estiver selecionado.* |
| **Chamados relacionados:** | *TVVZ35* |

divs
