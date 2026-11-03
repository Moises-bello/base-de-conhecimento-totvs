---
content_hash: c0c08452219ec0b9ce068868d50ff8631ab4d48b600e505eefd72c573efdf1f5
fetched_at: '2026-06-29T00:08:35.988141+00:00'
page_id: '283400776'
product: rm
source: tdn-rm
title: EDUCACIONAL01-1126 - DT - Mensagem de Aviso na Inclusão de Bolsas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=283400776
version: 103
---

# MENSAGEM DE AVISO NA INCLUSÃO DE BOLSAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | T*****otvs Educacional***** |
| **Função:** | Inclusão de Bolsas |
| **Situação/Requisito:** | Na inclusão de bolsa pelo Assistente | Inclusão de bolsa (Menu Financeiro/Contábil) o sistema deveria colocar esta observação no LOG do processo, dizendo que os lançamentos devem ser regerados para considerar as bolsas incluídas (estudar a melhor forma de apresentar esta informação).     Neste exemplo, o símbolo apresentado é de advertência mas está em vermelho e fala que ocorreu um erro no processo. Ajustar o símbolo e o texto. (para este exemplo o sistema incluiu a bolsa em um dos contratos do aluno e no outro não, pois o contrato está cancelado. No contrato onde o sistema conseguiu incluir a bolsa todas as parcelas já estavam geradas, porem nenhuma informação a este respeito foi informada no LOG). |
| **Solução/Implementação:** | O log de inclusão de bolsa foi alterado para alertar para a necessidade de regerar as parcelas para que as alterações tenham efeito. Também foi modificado o tipo de mensagem para aviso e não mais erro, quando há algum problema na geração da bolsa. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
