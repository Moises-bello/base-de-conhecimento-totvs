---
content_hash: 302ac011a6c75af238e086bbc48fce3f7e807ed383eb0223b45f490e29cf3785
fetched_at: '2026-06-29T00:08:31.140573+00:00'
page_id: '273293160'
product: rm
source: tdn-rm
title: 671416_DT_Erro_Regeracao_Lancamentos_Ajuste_Matricula_OnLine
type: documentation
url: https://tdn.totvs.com/display/LRM/671416_DT_Erro_Regeracao_Lancamentos_Ajuste_Matricula_OnLine
version: 108
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Geração de lançamentos financeiros* |
| **Situação/Requisito:** | *Ao alterar a matrícula de um aluno pelo portal, quando a configuração de matrícula no portal está parametrizada para gerar lançamentos financeiros, o sistema tenta gerar os lançamentos para as parcelas parametrizadas, porém caso alguma parcela já tenha tido o seu lançamento gerado e baixado, o sistema acusa um erro, pois não é possível regrar lançamentos baixados e impossibilita a alteração da matrícula.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de geração de lançamentos, permitindo ao sistema, concluir a alteração na matrícula, através do portal, nos casos onde as alterações realizadas tentar gerar lançamentos para as parcelas que já tenham seus lançamentos gerados e baixados.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.17* |
| **Versão Corrigida:** | *12.1.17* |
| **Versão Expedida:** | *12.1.17* |

divs
