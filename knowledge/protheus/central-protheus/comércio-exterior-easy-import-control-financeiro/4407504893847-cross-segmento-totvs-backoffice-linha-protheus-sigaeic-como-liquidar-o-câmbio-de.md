---
article_id: 4407504893847
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 69fe820687df574de9cd08f67b248c0d7f98346b7cdbbc95ec9ee805bba73fce
fetched_at: '2026-06-28T22:39:44.348131+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Como liquidar
  o câmbio de importação com moeda internacional diferente da Invoice
type: support-article
updated_at: '2021-09-01T20:45:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407504893847-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-liquidar-o-c%C3%A2mbio-de-importa%C3%A7%C3%A3o-com-moeda-internacional-diferente-da-Invoice
---

**Dúvida**Como liquidar o câmbio de importação com moeda internacional diferente da Proforma/Comercial Invoice?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Quando possui integração com o Financeiro (**MV\_EASYFIN = .T.**) a liquidação do câmbio sempre será efetuado após a informação de um banco do exterior, portanto para baixar o câmbio com uma moeda diferente da invoice será necessário vincular a moeda diferente no cadastro de bancos através dos campos: **A6\_MOEDA** e **A6\_MOEASY**, e configurar o parâmetro **MV\_MOEDBCO**.   
  
Exemplo  
Se moeda da Invoice é dólar (US$), para liquidar o câmbio em Euro (EUR) é só informar um banco que tenha a moeda euro cadastrada. Neste caso, os campos que precisam serem informados no banco são o **A6\_MOEDA** e **A6\_MOEASY** . Lembrando que precisa de um cotação de moeda cadastrada do dia para o Dólar e  o Euro.  
  
**Saiba mais**  
[Tratamento do MV\_MOEDBCO](https://tdn.totvs.com/display/public/PROT/1590929_MTRADE-1720_DT_Tratamento+do+MV_MOEDBCO)
