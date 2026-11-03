---
content_hash: f8291012e562d58d572e38eea3fc0a61643987d8598112e4bce8290e042cc6f9
fetched_at: '2026-06-29T00:08:16.516518+00:00'
page_id: '247923211'
product: rm
source: tdn-rm
title: ER_FRW_FRW002-33_UX#8_No_PortalRM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=247923211
version: 117
---

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Framework | **Módulo** | Globais |
| **Segmento Executor** |  | | |
| **Projeto1** | <http://jiraproducao.totvs.com.br/browse/FRW_FRW002> | **IRM1** [FRW\_FRW002-31](http://jiraproducao.totvs.com.br/browse/FRW_FRW002-31) |  |
| **Requisito1** | [FRW\_FRW002-129](http://jiraproducao.totvs.com.br/browse/FRW_FRW002-129) | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

       Criar um mecanismo para que o produto consiga disponibilizar telas feitas no frame HTML dentro do portal.

## Definição da Regra de Negócio

*As telas feitas no frame HTML que o produto deseja disponibilizar deverá ter uma action web referenciando essa tela, ou seja, requer desenvolvimentismo do produto para tal.*

*Veja abaixo os dois componentes que a lib criou para auxiliar, um UserControl  com o nome *que está em SharedServices/FrameHtml e uma action com o nome RMWActionFrameHtml que está na Lib.WebForms.**

c#RMWFrameHtml.ascxtruec#RMWActionFrameHtmltrue

       Para disponibilizar um tela feita no frame HTML basta criar uma action semelhante ao que é feito para o portal, herde da action acima(RMWActionFrameHtml), defina o atributo ActionInfo da mesma forma que faz para o portal, segue abaixo um exemplo:

c#PrtFrameHtmlActionWebtrue

     Perceba que só é necessário definir a propriedade URLServico(caminho relativo), pois no ancestral já está definido qual é o .ascx dessa action.

     Agora basta definir no menu.xml(menu client) ou no controller(menu server),  essa nova action criada, segue exemplo de criação no menu.xml:

 Após isso, basta definir a url de onde o frame html está hospedado, para isso vá em parâmetros globais conforme print abaixo, perceba na definição do caminho( [http://servidor:porta](http://servidorporta) )

## Protótipo de Tela

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
