---
article_id: 4409601077015
category: Manutenção de Ativos (SIGAMNT)
content_hash: 9f502889c74200ab4a21ec020bf010adb10436674afde7d72aaf34f485b554e9
fetched_at: '2026-06-28T22:42:33.140632+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Documento de entrada com CTe não gera insumos
type: support-article
updated_at: '2021-09-29T20:02:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409601077015-Manufatura-Linha-Protheus-MNT-Documento-de-entrada-com-CTe-n%C3%A3o-gera-insumos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:15 min** **Dúvida**Ao informar um documento de entrada com **CT-e** não está gerando insumo para uma **O.S. - Ordem de Serviço**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Ao informar um documento de entrada com os seguintes tipos: **Conhecimento de Transporte Eletrônico - CT-e**, **Conhecimento de Transporte Multimodal - CT-m**, **Conhecimento de Transporte Rodoviária - CT-r**, **Conhecimento de Transporte Ferroviário - CT-f** e **Conhecimento de Transporte Aquaviário - CT-a** e vincular a uma **O.S**, esta **O.S** não está recebendo um insumo realizado. Isso ocorre pois conhecimentos de transporte não devem gerar custos ou movimentações de estoque, levando em consideração que um documento de frete é utilizado para registrar a contratação do serviço de transporte, sendo o documento e seu valor referentes a prestação de um serviço. Desta mesma forma uma **O.S** não pode ser finalizada com insumos realizados sem uma quantidade.   
  
**Saiba mais**  
Para realizar a finalização de um **O.S** sem insumos pode ser utilizado o **PE - Ponto de Entrada** [DT PE NGSEMINS - Finalização de OS sem insumos.](https://tdn.totvs.com/display/public/PROT/DT+PE+NGSEMINS+-+Finalizacao+de+OS+sem+insumos)
