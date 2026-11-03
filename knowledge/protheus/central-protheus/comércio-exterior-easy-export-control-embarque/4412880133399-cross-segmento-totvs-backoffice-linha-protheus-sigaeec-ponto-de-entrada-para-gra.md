---
article_id: 4412880133399
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 1c5e8d0d52a0cb751f6e6f8c20599090a0bc2d9bc7003180f71d1736ea5fc7c4
fetched_at: '2026-06-28T22:36:39.217319+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Ponto de entrada
  para gravar dados da EE9 na EE8
type: support-article
updated_at: '2021-11-11T19:16:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412880133399-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Ponto-de-entrada-para-gravar-dados-da-EE9-na-EE8
---

**Dúvida**Precisamos de um ponto de entrada para gravar alguns dados da tabela **EE9**  na tabela **EE8** quando salvamos os itens do embarque de exportação **(EECAE100)**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Utilize o ponto de entrada **PE\_GRV\_EE9** do fonte **EECAE100** que é executado no looping de gravação dos dados da tabela temporária de itens (WorkIP) para a tabela de itens do embarque de exportação (EE9) permite implementar customizações nas gravações dos registros. Estarão disponíveis os dados dos itens da tabela temporária (WorkIP) e da tabela efetiva (EE9) posicionadas no registro que em processo de gravação e as variáveis de memória da capa do embarque (EEC).  
  
**Saiba mais**[PE EECAE100 Embarque](https://tdn.totvs.com/display/public/PROT/DT+PE+EECAE100+Embarque)
