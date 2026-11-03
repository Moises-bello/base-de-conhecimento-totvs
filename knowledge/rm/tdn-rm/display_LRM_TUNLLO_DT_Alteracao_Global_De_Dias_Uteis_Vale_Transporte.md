---
content_hash: 8933a9415df0f73f1b4ec9e781577c5bff446b442cd5982b9d6c62f8d6b889a8
fetched_at: '2026-06-29T00:08:04.077015+00:00'
page_id: '235335308'
product: rm
source: tdn-rm
title: TUNLLO_DT_Alteracao_Global_De_Dias_Uteis_Vale_Transporte
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNLLO_DT_Alteracao_Global_De_Dias_Uteis_Vale_Transporte
version: 114
---

# ALTERAÇÃO DE DIAS ÚTEIS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Alteração de Dias Úteis |
| **Situação/Requisito:** | Ao executar uma alteração de dias úteis, informando mais de uma linha para a relação DE/PARA, de forma crescente e com interseção, o sistema não lança corretamente, fixando a última relação DE/PARA.  Ex: Alteração para funcionário X, que contém como dias úteis o valor 15.    Relação de para em parâmetros do processo:   | DE | PARA | | --- | --- | | 15 | 20 | | 20 | 22 | | 22 | 25 |   Conforme ordem, o sistema realiza a alteração primeiramente de 15 dias úteis para 20 dias úteis. Posteriormente, ele não ignora o funcionário X para a próxima troca, de 20 dias úteis para 22 dias úteis, realizando-a novamente, ou seja, o funcionário X, passa a adotar 22 dias úteis. Em sequência, ele realiza novamente alterando de 22 dias úteis para 25 dias úteis, quando na verdade deveria ser 20 dias úteis. |
| **Solução/Implementação:** | Foi realizado uma implementação, onde é verificado que caso o valor do dias úteis já tiver sido alterado para o funcionário, o mesmo não será reconsiderado para a próxima linha da relação DE/PARA. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUNLLO; TUQHW3 |
| **Requisito (ISSUE):** |  |

divs
