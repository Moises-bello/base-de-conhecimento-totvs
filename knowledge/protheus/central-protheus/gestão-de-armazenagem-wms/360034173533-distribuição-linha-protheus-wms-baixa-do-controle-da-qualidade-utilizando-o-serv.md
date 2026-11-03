---
article_id: 360034173533
category: Gestão de Armazenagem (WMS)
content_hash: 3d0b21d3503fbe969b7d4c801cf940515e59684c5294d5f3e68d7538562e5b88
fetched_at: '2026-06-28T22:45:47.890087+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: 'Distribuição - Linha Protheus - WMS - Baixa do controle da qualidade utilizando
  o serviço de WMS '
type: support-article
updated_at: '2023-08-01T13:14:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034173533-Distribui%C3%A7%C3%A3o-Linha-Protheus-WMS-Baixa-do-controle-da-qualidade-utilizando-o-servi%C3%A7o-de-WMS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16431928240919)**Tempo aproximado para leitura: **00:00:48**  
**Dúvida**A baixa do controle da qualidade utilizando o serviço de **WMS** pode ser realizada via c**oletor de dados**?  
  
**Ambiente**TOTVS Distribuição - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) – A partir da versão 11.80  
  
**Solução**De forma padrão, a rotina **Baixa C.Q. - ACDV010** não integra com o **WMS - *Warehouse Management System***. No entanto, na *release* 12.1.17 foi disponibilizado o ponto de entrada **A010WMSO**, o qual permite informar o **Serviço WMS** e o **Endereço Origem WMS** na liberação do controle da qualidade, quando efetuada via **coletor de dados**.  
  
**Importante**  
O **WMS** sempre solicitará o endereço de origem para a movimentação via **MATA175 - Baixas do CQ**.  
  
**Saiba mais**  
Acione este *link* para visualização a documentação do ponto de entrada **A010WMSO**: [DT PE A010WMSO - Informar os campos Serviço e Endereço WMS na liberação CQ](https://tdn.totvs.com/pages/viewpage.action?pageId=612536828)
