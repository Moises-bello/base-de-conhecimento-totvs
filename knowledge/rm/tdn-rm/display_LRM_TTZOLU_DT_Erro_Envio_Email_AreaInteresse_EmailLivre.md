---
content_hash: 997596314813f875accfeb8ec9484231f7743f16493097166e9da8185de3e35e
fetched_at: '2026-06-29T00:06:22.591493+00:00'
page_id: '223923191'
product: rm
source: tdn-rm
title: TTZOLU_DT_Erro_Envio_Email_AreaInteresse_EmailLivre
type: documentation
url: https://tdn.totvs.com/display/LRM/TTZOLU_DT_Erro_Envio_Email_AreaInteresse_EmailLivre
version: 122
---

# ENVIAR E-MAILS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Envio de e-mails* |
| **Situação/Requisito:** | *Ao tentar enviar e-mails do tipo 'Áreas de interesse do usuário' e 'E-mail livre' o sistema está retornando um erro e não permite o envio.* |
| **Solução/Implementação:** | *Foi identificado que para o primeiro tipo de mensagem o ocorre o erro pois a mensagem não existia a mensagem, foi feito o ajuste para alertar o usuário que a mensagem não existe. Para o segundo tipo de mensagem o erro era causado pelo componente de edição da mensagem que não estava sendo criado corretamente, após o ajuste o mesmo passou a ser criado corretamente e o erro não ocorreu mais.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
