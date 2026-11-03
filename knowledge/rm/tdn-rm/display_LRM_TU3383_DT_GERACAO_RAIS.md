---
content_hash: cf0b0667c501de84223bd3e477fdd9a25926bc6b8aaf5912a8c0905766da5468
fetched_at: '2026-06-29T00:06:23.063882+00:00'
page_id: '223931505'
product: rm
source: tdn-rm
title: TU3383_DT_GERACAO_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TU3383_DT_GERACAO_RAIS
version: 125
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | Ao gerar a RAIS em arquivo, dentro dos parâmetros da coligada, aba Seção é marcado o campo "Seção Sindicalizada", porém no arquivo - Registro tipo 1, posição 452, a informação está incorreta. O campo está preenchido com 2 (Não), quando o correto seria 1(Sim). |
| **Solução/Implementação:** | Caso 1: Ajuste na rotina da Rais para considerar valor de aviso previo indenizado quando demissão ocorrer anterior ao ano base e a data de projeção for no ano base. Exemplo: Ano base 2015 - Data desligamento em dezembro de 2014 e data de projeção em janeiro de 2015 Caso 2: Ajuste na rotina da Rais para considerar valor de aviso previo indenizado quando demissão ocorrer no ano base e a data de projeção também for no ano base. Exemplo: Ano base 2015 - Data desligamento em novembro de 2015 e data de projeção em dezembro de 2015 |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TU3383 TUAJA6 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.9* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
