---
content_hash: 122acbb0f0481f681c83bde904feeda3705725997d5f050ad37a782f5d9a13bc
fetched_at: '2026-06-29T00:08:23.187185+00:00'
page_id: '269549956'
product: rm
source: tdn-rm
title: MEDU-1058_DT_Utilitario_Envio_Email_Concatenando_Mensagem
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-1058_DT_Utilitario_Envio_Email_Concatenando_Mensagem
version: 113
---

# ENVIO DE E-MAILS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Bibliotecária* |
| **Função:** | *Envio de e-mails* |
| **Situação/Requisito:** | *Foi identificado no utilitário de envio de e-mails, quando utilizado os tipos de e-mail "Áreas de interesse do usuário" e "Texto livre", ao acessar a tela de edição da mensagem e retornar a tela de seleção do tipo de mensagem, o sistema vai concatenando a mensagem toda vez que a tela de edição é acessada novamente para o mesmo tipo de mensagem.* |
| **Solução/Implementação:** | *Foi identificado uma inconsistência no método que exibe a mensagem, sendo assim, este foi alterado para que toda vez que a mensagem for carregada o campo da mensagem seja limpo antes, evitando assim a concatenação, porém, ao retornar da tela de edição da mensagem para a seleção do tipo de mensagem será exibido um alerta informando que o retorno irá apagar qualquer alteração que tenha sido feita na mensagem.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
