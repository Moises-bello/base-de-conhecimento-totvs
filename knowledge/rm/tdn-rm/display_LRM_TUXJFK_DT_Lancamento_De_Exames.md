---
content_hash: 0b5d34c717aac96ba564e77133c88146b7a572f2601854c1c0b63ad5f890809f
fetched_at: '2026-06-29T00:08:09.055510+00:00'
page_id: '239022223'
product: rm
source: tdn-rm
title: TUXJFK_DT_Lancamento_De_Exames
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXJFK_DT_Lancamento_De_Exames
version: 115
---

# LANÇAMENTO DE EXAMES

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Segurança e Saúde Ocupacional |
| **Função:** | Lançamento de Exames |
| **Situação/Requisito:** | Ao acessar no SSO PCMSO>Agenda de Exames, escolher um funcionário que tenha um exame agendado como PENDENTE, acessar Processo>Lançamento de Resultado de Exame, caso a Data Exame seja superior à 7 dias da data/hora do agendamento, o produto finaliza o Wizard do processo de Lançamento de Resultado de Exame com sucesso, mas mantem o exame com o status de pendente. |
| **Solução/Implementação:** | Realizada pequena melhoria no processo de lançamento de exames através da agenda de exames de forma que o cliente possa parametrizar o número de dias que o sistema irá utilizar como margem para considerar o agendamento concluído. Hoje o padrão é 7 dias e continuará desta forma até que realize a parametrização no parametrizador em SSO | Opções | Parametrizador | Exames | "Margem de dias a considerar no lançamento de resultados pela agenda de exames". |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUXJFK, TVALJW |
| **Requisito (ISSUE):** |  |

divs
