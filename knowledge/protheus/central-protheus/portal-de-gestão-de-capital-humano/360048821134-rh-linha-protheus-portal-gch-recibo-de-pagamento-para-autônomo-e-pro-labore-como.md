---
article_id: 360048821134
category: Portal de Gestão de Capital Humano
content_hash: 136e01ba6acb5db08e4b27e3c7d1a8d47bdb46e7fc2d7fde8280664e253bf0fa
fetched_at: '2026-06-28T22:43:00.139877+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Recibo de pagamento para autônomo e pro
  labore como consultar no portal
type: support-article
updated_at: '2021-04-07T13:15:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048821134-RH-Linha-Protheus-PORTAL-GCH-Recibo-de-pagamento-para-aut%C3%B4nomo-e-pro-labore-como-consultar-no-portal
---

**Dúvida**Como configurar a regra para liberar o contra cheques de Autônomos e Pro Labore no portal?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Portal Gestão Capital Humano - Todas as Versões  
  
**Solução**É necessário configurar o parâmetro **MV\_TCF013A** e apontar quais os recibos serão apresentados no portal.Para o apontamento específico de Autônomos e Pro Labores é necessário configura-lo com o conteúdo  "06" para considerar os roteiros do tipo AUT.  
  
Para realize o seguinte cadastro:  
**1.** No módulo Configurador, opção **Ambientes > Cadastros > Parâmetros** , configure o parâmetro **MV\_TCF013A**, com a opção 06 para considerar os roteiros do tipo AUT.  
  
Informações adicionais sobre o parâmetro  
Nome da Var. MV\_TCF013A  
Tipo C  
  
Descrição: Opções de consulta do demonstrativo de pagamento  
01-Adiantamento  
02-Folha  
03-1ª parcela do 13º  
04-2ª parcela do 13º  
05-PLR

Demais roteiros:  
06 - Autônomos  
07 - Valores Extras  
  
**Saiba Mais***Para saber mais consulte os links abaixo:*

*[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)*
