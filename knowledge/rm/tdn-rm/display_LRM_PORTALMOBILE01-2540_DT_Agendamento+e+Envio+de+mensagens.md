---
content_hash: aab24b98570b549e05a3c97ea36c13565fae3acf306e46d0593e6ce9e9b8045b
fetched_at: '2026-06-29T00:08:47.120005+00:00'
page_id: '318608434'
product: rm
source: tdn-rm
title: PORTALMOBILE01-2540_DT_Agendamento e Envio de mensagens
type: documentation
url: https://tdn.totvs.com/display/LRM/PORTALMOBILE01-2540_DT_Agendamento+e+Envio+de+mensagens
version: 98
---

# Agendamento/envio de mensagens

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Atividades acadêmicas| Central de Comunicação | Agendamento/envio de mensagens |
| **Situação/Requisito:** | A funcionalidade de enviar mensagens por consulta SQL não estava aderente com o processo, e com isso o usuário não conseguia criar/utilizar uma consulta SQL para enviar notificação aos usuários corretamente. |
| **Solução/Implementação:** | Foi realizado uma implementação na funcionalidade "Agendamento/envio de mensagens" em relação a utilização de consulta SQL. O processo foi alterado/otimizado para facilitar a utilização de consulta SQL pelos usuários do sistema. No primeiro passo do processo, o usuário poderá marcar que irá utilizar consulta SQL e selecionar ou não uma mensagem pré-configurada com o objetivo "Enviar mensagens eventuais para via e-mail, Fluig ou eduCONNECT". Caso seja marcado a opção consulta SQL, não será permitido informar o público-alvo, pois este será recuperado pelos dados da consulta SQL do cliente. Para facilitar a utilização dos dados retornados da consulta SQL no texto da mensagem, será possível inserir no texto o nome da coluna da consulta SQL entre colchetes.  Exemplo de uma consulta SQL:  SELECT **'Valor da coluna1'** **COLUNA1**, **'Valor da coluna 2'** **COLUNA2** FROM MINHATABELA  Caso o usuário deseje inserir o valor de alguma coluna no texto, basta escrever o nome da coluna entre colchetes no texto, por exemplo:  "Olá, o valor da primeira coluna é **[COLUNA1]** e da segunda coluna é **[COLUNA2]**"  O sistema irá trocar o nome da coluna pelo valor da coluna, por exemplo:  "Olá, o valor da primeira coluna é **Valor da coluna1** e da segunda coluna é **Valor da coluna 2**"  Permitindo ao usuário customizar o envio de mensagens com o uso de consulta SQL conforme sua necessidade. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
