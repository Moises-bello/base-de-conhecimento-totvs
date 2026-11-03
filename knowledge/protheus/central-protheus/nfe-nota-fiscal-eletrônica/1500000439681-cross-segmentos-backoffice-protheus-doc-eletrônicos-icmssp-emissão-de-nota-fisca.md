---
article_id: 1500000439681
category: NFe - Nota Fiscal Eletrônica
content_hash: 23d523a5ead62e0c68eba88967c4a0ab408c5ccf00d15cfdaf81111030d067e9
fetched_at: '2026-06-28T22:40:00.333630+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  ICMS/SP - Emissão
  de Nota Fiscal com a Expressão - "Relativa à Liquidação no Mercado de Curto Prazo"
  ou “Relativa à apuração e Liquidação do Mecanismo de Compensação de Sobras e Déficits
  - MCSD;'
type: support-article
updated_at: '2021-10-11T14:29:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000439681--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-ICMS-SP-Emiss%C3%A3o-de-Nota-Fiscal-com-a-Express%C3%A3o-Relativa-%C3%A0-Liquida%C3%A7%C3%A3o-no-Mercado-de-Curto-Prazo-ou-Relativa-%C3%A0-apura%C3%A7%C3%A3o-e-Liquida%C3%A7%C3%A3o-do-Mecanismo-de-Compensa%C3%A7%C3%A3o-de-Sobras-e-D%C3%A9ficits-MCSD
---

**Dúvida**Como configurar no Protheus ICMS/SP - Emissão de Nota Fiscal com a Expressão - "Relativa à Liquidação no Mercado de Curto Prazo" ou “Relativa à apuração e Liquidação do Mecanismo de Compensação de Sobras e Déficits - MCSD ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

*1 - no quadro “Destinatário/Remetente”, no campo **"Relativa à Liquidação no Mercado de Curto Prazo" ou “Relativa à apuração e Liquidação do Mecanismo de Compensação de Sobras e Déficits - MCSD;***

* Preencher no cadastro de cliente os campos **Nome A1\_NOME e N Fantasia A1\_NREDUZ**

![cliente.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100286293/cliente.png)

* **Observação:**

Caso seja cadastro de fornecedor, preencher os campos **Razão Social A2\_NOME e N Fantasia A2\_NREDUZ**

![forne.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100290233/forne.png)

*2 - no campo **“Informações Complementares”**, os dados da liquidação na CCEE, incluindo o valor total da liquidação financeira e o valor efetivamente liquidado, no quadro*

* Utilizar os campos padrões do sistema para gerar a **mensagem em informações complementares, conforme os links abaixo:**

[MP-NFE- Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)

[MP-NFE- Gerar mensagem em informações complementares do Danfe utilizando fórmula ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)

***Caso não possa realizar os processos acima,** para que o XML e o Danfe atenda sua necessidade há **duas opções de processos** a ser seguido:  
  
1-Primeira opção pode ser customizado o **NFESEFAZ .**  
  
[MP - NFE - Documentos Eletrônicos NFe / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493-MP-NFE-Documentos-Eletr%C3%B4nicos-NFe-NFSe-MDFe-MDe-?source=search)  
  
**Rdmake disponível no link acima.**  
  
2- Segunda opção pode ser aberto melhoria na Central Colaborativa:  
  
[***Central Colaborativa TOTVS.***](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
**Para saber como criar uma sugestão de melhoria clique [*AQUI.*](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)***

* ***Saiba mais:***

***[Parecer](https://tdn.totvs.com/pages/releaseview.action?pageId=571247115)***
