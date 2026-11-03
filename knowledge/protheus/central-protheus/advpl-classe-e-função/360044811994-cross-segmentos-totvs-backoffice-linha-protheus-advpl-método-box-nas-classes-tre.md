---
article_id: 360044811994
category: ADVPL - Classe e Função
content_hash: 091d79037309d15dc597dcaba64ae4ece469891b2ec15e0045f846ad8e8c9902
fetched_at: '2026-06-28T22:40:20.509911+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Método BOX nas
  classes TREPORT e FWMSPRINTER
type: support-article
updated_at: '2022-01-11T19:13:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044811994-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-M%C3%A9todo-BOX-nas-classes-TREPORT-e-FWMSPRINTER
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao utilizar o método *SAY* e depois o método *BOX* da classe *Treport* ou na classe *FWMSprinter*, o método BOX sobrepõe o texto utilizado no método *SAY* após gerar o PDF

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Tanto na classe *Treport* como na classe ***FwMSPrinter*** se trata de um comportamento na impressão *PDF* ou *PDF* por e-mail que possuem componentes com comportamentos diferentes.  
É necessário definir componente *BOX* primeiro e para que fique por trás dos outros componentes.
