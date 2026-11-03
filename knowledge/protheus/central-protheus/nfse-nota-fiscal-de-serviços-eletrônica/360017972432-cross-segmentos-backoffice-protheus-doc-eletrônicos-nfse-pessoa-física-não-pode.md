---
article_id: 360017972432
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 1064f91cf57387464b5fea65844d082fc105fce65c1c1048ff825a961c3d1b8f
fetched_at: '2026-06-28T22:39:56.204981+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Pessoa física
  não pode ser responsável tributário - São Paulo
type: support-article
updated_at: '2025-07-18T14:41:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017972432-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Pessoa-f%C3%ADsica-n%C3%A3o-pode-ser-respons%C3%A1vel-tribut%C3%A1rio-S%C3%A3o-Paulo
---

**Ocorrência**No módulo **Faturamento**, ao realizar a transmissão da nota fiscal de serviço para a Prefeitura de São paulo, onde o tomador for de fora do município de São Paulo, é apresentada a seguinte mensagem: "**Pessoa física não pode ser responsável tributário**".  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Apenas tomadores inscritos na Prefeitura de São Paulo podem recolher o ISS dentro do município.  
  
**Solução**  
Para solucionar essa ocorrência há duas alternativas, na qual o Fiscal de sua empresa deverá avaliar qual a mais adequada para a situação, sendo elas:  
  
Alterar o **F4\_ISSST** para 2 na **TES** - desta maneira o imposto será retido fora do município, que é no município do tomador no caso.

Ou

Alterar o **C5\_RECISS** e **A1\_RECISS** para 2 - desta maneira o prestador que será o responsável tributário pelo imposto.

Uma observação importante é que quando o tomador é o responsável tributário, deve ser informado o CNPJ e Inscrição Municipal do mesmo.
