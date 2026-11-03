---
article_id: 4413857414039
category: ADVPL - Classe e Função
content_hash: 53934b42c2ffa10055d3e5a91ddedda7c9c803260f8859ac3284c2ca54f2990b
fetched_at: '2026-06-28T22:40:18.341269+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro na aplicação
  de pacotes Release 12.1.33
type: support-article
updated_at: '2021-11-22T19:36:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413857414039-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-na-aplica%C3%A7%C3%A3o-de-pacotes-Release-12-1-33
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**

Ao realizar a tentativa de aplicação de um pacote no Release **12.1.33**, o sistema apresenta mensagens “**Patch Validate could not be executed**” no **VS Code** e não conclui a aplicação:

![Aplica__o_de_Pacotes.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413843972503/Aplica__o_de_Pacotes.jpg)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - a partir do release 12.1.33.  
  
**Causa**

Esta mensagem pode indicar que o VS Code não conseguiu acesso exclusivo ao Repositório para realizar a aplicação do pacote. Isso pode ocorrer quando:

1. O AppServer.ini possui Jobs configurados e eles estão em execução impedindo o acesso exclusivo;

2. Caso possua a **porta Multiprotocolo** ativada (**<https://tdn.totvs.com/x/UVlcIw>)** em seu **AppServer.ini**  
  
**Solução**É necessário desativar os **Jobs/Porta Multiprotocolo** no AppServer.ini para executar a aplicação do pacote, para isso basta comentar a linha da forma demonstrada abaixo, mas atenção, este procedimento deve ser realizado por sua área de TI ou analista especialista:

![Captura_de_tela_2021-11-22_152623.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413857221143/Captura_de_tela_2021-11-22_152623.jpg)
