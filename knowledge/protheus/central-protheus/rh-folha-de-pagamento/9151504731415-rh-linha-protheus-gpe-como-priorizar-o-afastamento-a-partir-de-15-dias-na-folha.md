---
article_id: 9151504731415
category: RH - Folha de Pagamento
content_hash: 720d57ec007e0285d66f928110686ae950b2f8981428dbe15b1e8dd3acb6814b
fetched_at: '2026-06-28T22:44:14.688226+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como priorizar o afastamento a partir de 15 dias
  na folha em meses de 31 dias
type: support-article
updated_at: '2024-09-12T11:46:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9151504731415-RH-Linha-Protheus-GPE-Como-priorizar-o-afastamento-a-partir-de-15-dias-na-folha-em-meses-de-31-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26319810085783) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como priorizar o afastamento a partir de 15 dias na folha em meses de 31 dias por conta da SEI 16120, onde o sistema considere o dia 31 como afastamento?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Para priorizar os dias de afastamento em meses de 31 dias, foi criado o mnemônico P\_LPRIAFA, onde quando habilitado, o sistema irá considerar o dia 31 como afastamento.  
  
Para habilitar, entre na rotina **Mnemônicos** pelo caminho **>Atualizações >Definições de cálculo >Mnemônicos**, pesquise pelo P\_LPRIAFA e altere o conteúdo para .T. conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9151367181207)  
  
Após salvar, ao calcular a folha, o sistema irá priorizar os dias de afastamento quando maior de 15 dias e um dos 15 primeiros dias cair no dia 31.  
  
**Saiba mais**  
[Afastamento maior de 15 dias em meses de 31 dias com dias de cálculo 30](https://tdn.totvs.com/pages/viewpage.action?pageId=627712651#exemplo-Exemplo1)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
