---
article_id: 28951085715735
category: Materiais - Compras (SIGACOM)
content_hash: 6bc4230a8a785d2d392240c7b80798c681944d8b36bf2e37dbfaf883765df659
fetched_at: '2026-06-28T22:41:14.264834+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Botão "Filtra Medição"
  não aparece em notas vindas do Importador XML
type: support-article
updated_at: '2025-01-03T16:09:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28951085715735-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Bot%C3%A3o-Filtra-Medi%C3%A7%C3%A3o-n%C3%A3o-aparece-em-notas-vindas-do-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28951085667991) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quando a nota é proveniente do Importador XML não aparece o botão "Filtra Medição" na rotina Documento de entrada (MATA103).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - a partir da 12.1.33  
  
**Solução**Ao gerar o documento através do Importador Xml, o sistema gera a "pré-nota", e acessando a rotina pré-nota(MATA140), você pode selecionar o documento gerado e clicar em Alterar vai ter a opção para filtrar por medição, conforme pode ser verificado abaixo:  
   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28951039043607)  
   
   
Quando você está apenas "Classificando" o documento de entrada(MATA103), não irá apresentar a informação independente se a nota foi gerada pelo importador ou incluída manualmente via sistema.   
   
No documento de entrada(MATA103) é apresentado somente se você está incluindo um novo documento.  
   
Sendo assim, não se trata de uma falha do sistema, é o processo padrão que sempre se comportou.

Se incluir uma pré-nota sem vincular o pedido e ir no documento de entrada apenas para "classificar", o sistema irá se comportar da mesma maneira.  
   
Segue abaixo o procedimento para vinculação do pedido de compras no importador XML.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Vinculo com pedido de compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001536342-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Vinculo-com-pedido-de-compras?source=search)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
