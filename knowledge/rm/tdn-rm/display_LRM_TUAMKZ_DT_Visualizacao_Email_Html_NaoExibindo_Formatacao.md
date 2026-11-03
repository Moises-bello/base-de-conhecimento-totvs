---
content_hash: 43864500a73a94b55d72583f6d59a728609c9e4d8436e5262d6a43ca073ab4cb
fetched_at: '2026-06-29T00:06:25.124122+00:00'
page_id: '224132638'
product: rm
source: tdn-rm
title: TUAMKZ_DT_Visualizacao_Email_Html_NaoExibindo_Formatacao
type: documentation
url: https://tdn.totvs.com/display/LRM/TUAMKZ_DT_Visualizacao_Email_Html_NaoExibindo_Formatacao
version: 124
---

# ENVIO DE E-MAILS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Avaliação e Pesquisa* |
| **Função:** | *Envio de e-mails* |
| **Situação/Requisito:** | *Ao utilizar o utilitário de envio de e-mails para envio de resultados de provas ou informações da inscrições em provas, quando é utilizado uma mensagem no formato html a simulação retorna a mensagem com as tags htmls, não carregando o texto formatado com o estilo corretamente.* |
| **Solução/Implementação:** | *Foi identificado que antes da nova central de notificação não era permitido o uso de html e da forma como funcionava, a simulação atendia corretamente ao padrão de envio, após a implementação da nova central de notificação, a utilização de mensagens html não era carregada na tela. Foi realizado um ajuste no processo para que se a mensagem da simulação é html, o sistema gere um arquivo html para exportação e visualização em qualquer navegador que suporte html. Assim a visualização com a devida formatação pode ser feita corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
