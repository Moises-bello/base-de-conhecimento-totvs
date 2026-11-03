---
content_hash: 9ab8e1aac208e13d6cd61f591254affe42fd4b79900ad2bef621ddaa31e46150
fetched_at: '2026-06-29T00:06:13.589712+00:00'
page_id: '208344618'
product: rm
source: tdn-rm
title: TTKD87_DT_FA_TOMADOR_GERADOR_DELPHI
type: documentation
url: https://tdn.totvs.com/display/LRM/TTKD87_DT_FA_TOMADOR_GERADOR_DELPHI
version: 1
---

# Relatório 2.001.004-Folha Analítica por Tomador Gerador Delphi

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Emissão do relatório 2.001.004-Folha Analítica por Tomador* |
| **Situação/Requisito:** | *Não emiti os dados do Tomador e os totais não conferem com os tomadores e funcionários contantes no relatório* |
| **Solução/Implementação:** | Atualizado o relatório  2.001.004-Folha Analítica por Tomador para visualizar os dados do tomador de serviço que estão cadastrados na coligada global e corrente. E também foi refeita a lógica dos totalizadores por tomador e do total geral para computarem somente os tomadores e funcionários emitidos no relatório.  O Relatório passa a solicitar a coligada em que os dados serão usados no cabeçalho, este parâmetro se faz necessário para que os dados de coligada global não seja informado no cabeçalho. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTKD87 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
