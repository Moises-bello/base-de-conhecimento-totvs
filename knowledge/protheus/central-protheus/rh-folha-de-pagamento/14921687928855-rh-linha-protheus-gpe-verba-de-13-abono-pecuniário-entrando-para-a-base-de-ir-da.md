---
article_id: 14921687928855
category: RH - Folha de Pagamento
content_hash: 8b5744262d0b58275f9897983f0ab4b59da1f075975838c2c342fd9495736902
fetched_at: '2026-06-28T22:44:16.405714+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Verba de 1/3 abono pecuniário entrando para a base
  de IR da folha
type: support-article
updated_at: '2025-10-06T13:31:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14921687928855-RH-Linha-Protheus-GPE-Verba-de-1-3-abono-pecuni%C3%A1rio-entrando-para-a-base-de-IR-da-folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26187092383383) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Verba de 1/3 abono pecuniário entrando para a base de IR da folha de pagamento ID 0015.  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.27.  
  
**Causa**Verba com incidência errada.  
  
**Solução**A verba de ID 1890 deve ficar com **SIM** no campo **Ref a Fer** e **IR**, assim como a verba de 1/3 abono pecuniário também deve ficar com **SIM** no campo **Ref a Fer**, desta forma, o IR da verba será considerado na base de IR Férias corretamente.  
  
Para ajuste, entre na rotina de **Verbas** pelo caminho **>Atualizações >Definições de cálculo >Verbas**, e na aba Incidências deixe os campo conforme abaixo, assim o cálculo da folha ficará correto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14921627555223)

**Saber Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como criar uma verba com o ID 1890](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8179699532951-RH-Linha-Protheus-GPE-Como-criar-uma-verba-com-o-ID-1890?source=search)

[RH - Linha Protheus - GPE - Separação ID 1449 - Abono Pago mês anterior](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8134979381399-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-ID-1449-Abono-Pago-m%C3%AAs-anterior?source=search)
