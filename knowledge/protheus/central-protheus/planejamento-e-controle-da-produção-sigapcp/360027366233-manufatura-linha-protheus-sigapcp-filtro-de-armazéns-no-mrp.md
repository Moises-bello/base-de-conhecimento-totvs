---
article_id: 360027366233
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4a9bc6070408c448d67020a584ec870983e12e9dc2576b98885cae38a21614ab
fetched_at: '2026-06-28T22:42:43.223596+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Filtro de armazéns no MRP
type: support-article
updated_at: '2024-05-13T13:16:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027366233-Manufatura-Linha-Protheus-SIGAPCP-Filtro-de-armaz%C3%A9ns-no-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:05 min**  
**Dúvida**É possível filtrar os armazéns que serão considerados no **MRP - Manufacturing Resources Planning**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Sim, é possível filtrar os armazéns que serão considerados no **MRP**. Para isso temos as alternativas abaixo:

* Na lista de parâmetros do **MRP** informar o range de armazéns a serem considerados nos parâmetros **Armazém De** e **Armazém Ate;**
* Ative o parâmetro **MV\_MRPFILA - Filtra Armazéns**, dessa forma será apresentado ao usuário uma tela para a seleção dos armazéns no momento da execução do **MRP**;
* Determine os armazéns que serão considerados através do **AGRA045 - Locais de estoque**, através do preenchimento do campo **NNR\_MRP - Entra MRP** com o conteúdo igual a **1**;
* Determine os armazéns através do ponto de entrada **A710FILALM - Filtra Armazéns**.
