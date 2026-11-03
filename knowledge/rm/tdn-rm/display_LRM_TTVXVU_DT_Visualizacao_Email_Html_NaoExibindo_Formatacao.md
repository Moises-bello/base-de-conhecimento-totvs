---
content_hash: e06373ec4ad2668ef4a54a4d2ede3e830c0cb419378a3dcf665330b21c92aa95
fetched_at: '2026-06-29T00:06:22.257056+00:00'
page_id: '223911412'
product: rm
source: tdn-rm
title: TTVXVU_DT_Visualizacao_Email_Html_NaoExibindo_Formatacao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVXVU_DT_Visualizacao_Email_Html_NaoExibindo_Formatacao
version: 126
---

# ENVIO DE E-MAILS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Envio de e-mails* |
| **Situação/Requisito:** | *Ao utilizar o utilitário de envio de e-mails, quando é utilizado uma mensagem no formato html a simulação retorna a mensagem com as tags htmls, não carregando o texto formatado com o estilo corretamente.* |
| **Solução/Implementação:** | *Foi identificado que antes da nova central de notificação não era permitido o uso de html e da forma como funcionava, a simulação atendia corretamente ao padrão de envio, após a implementação da nova central de notificação, a utilização de mensagens html não era carregada na tela. Foi realizado um ajuste no processo para que se a mensagem da simulação é html, o sistema gere um arquivo html para exportação e visualização em qualquer navegador que suporte html. Assim a visualização com a devida formatação pode ser feita corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
