---
article_id: 360052523474
category: Comércio Exterior - Easy Export Control - Siscomex
content_hash: 506d2e5434ba0a7d060523db4bd310518de754e5f38b2f07de13e6f7ade1ccd7
fetched_at: '2026-06-28T22:37:00.560091+00:00'
product: protheus
section_id: 1500001538121
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Retorno DUE:
  Unidade de Embarque informada não possui coordenadas geográficas cadastradas'
type: support-article
updated_at: '2022-06-14T18:59:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052523474-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Retorno-DUE-Unidade-de-Embarque-informada-n%C3%A3o-possui-coordenadas-geogr%C3%A1ficas-cadastradas
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:03:00 min  
  
Dúvida**Integração Due retornou a mensagem: Unidade de Embarque informada não possui coordenadas geográficas cadastradas, como resolver?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Export Control* – A partir da versão 12.1.17   
  
**Solução**Na aba Siscomex no embarque de exportação, quando o campo Tipo Despach (EEC\_EMFRRC) estiver selecionado "19=Fora de Recinto Alfandegado-Domiciliar", é necessário informar o  O Endereço do Local de Despacho,  a Latitude e Longitude do local de despacho e o Responsável pelo despacho.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085467394/mceclip0.png)  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085371994/mceclip0.png)

Esses novos campos foram criados para atender as especificações da DU-E, e estarão disponíveis no dicionário diferencial de **Janeiro/2019** . Caso seja necessário o uso é possível cria-los pelo configurador (SIGACFG) conforme especificações dos campos : [DT\_Pr. Carga,Obs. Pr.Car e LPCO informações adicionais nos itens do processo não é permitido incluir as informações na tela de itens.](https://tdn.totvs.com/pages/releaseview.action?pageId=421366945)  
  
**Saiba mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pacote Acumulado Comex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793)
