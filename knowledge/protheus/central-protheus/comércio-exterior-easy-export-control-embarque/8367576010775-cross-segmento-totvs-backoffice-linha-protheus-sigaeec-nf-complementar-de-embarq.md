---
article_id: 8367576010775
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: f24628101723f9fc8063cedc109abde9a7eded8252091215b193214a94de5bc8
fetched_at: '2026-06-28T22:36:56.583252+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - NF Complementar
  de Embarque não respeita a TES Inteligente informada no processo
type: support-article
updated_at: '2024-05-08T11:45:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8367576010775-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-NF-Complementar-de-Embarque-n%C3%A3o-respeita-a-TES-Inteligente-informada-no-processo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **05:00 min** **Dúvida**Ao tentar gerar uma **NF Complementar de Embarque** dentro da**rotina de Complementos do SIGAEEC** o sistema não respeita a **TES Inteligente cadastrada no Processo**, gerando o seguinte erro:  
   
![](https://totvssuporte.zendesk.com/attachments/token/bHawzAmgSdRz88bYtph71XP02/?name=image.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Inicialmente, informamos que o ocorrido foi corrigido através da **ISSUE DTRADE-7751**.   
No entanto, caso o ambiente possua o **RdMake Padrão "EECFATCP\_RDM" compilado no repositório**, o erro volta a ser apresentado.  
Desta forma, o Time de Produtos informa que o rdmake "***EECFATCP\_RDM**"* foi substituído pelo programa padrão "***EECFATCC**"* ["https://tdn.totvs.com/pages/viewpage.action?pageId=559284382"](https://tdn.totvs.com/pages/viewpage.action?pageId=559284382) não sendo necessário compilá-lo para se ter a solução referente à **TES Inteligente**. Neste caso, basta o cliente aplicar o patch referente a **ISSUE DTRADE-7751.**Conforme documentado em "<https://tdn.totvs.com/pages/viewpage.action?pageId=526987588>", os rdmakes liberado na Expedição Contínua como modelo de customização, servem apenas como ponto de partida para os clientes que optarem por não seguir com o programa padrão e sim, com um modelo customizado, sendo de responsabilidade do cliente a sua evolução, caso opte por compilá-lo e tê-lo no repositório em substituição ao Produto Padrão.
