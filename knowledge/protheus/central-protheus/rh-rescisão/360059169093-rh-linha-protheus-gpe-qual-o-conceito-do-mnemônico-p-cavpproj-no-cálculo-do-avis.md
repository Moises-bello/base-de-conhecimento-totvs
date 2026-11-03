---
article_id: 360059169093
category: RH - Rescisão
content_hash: c918a59d6436286d65d578aef0e7338dd6ba0627cd973cb08a3041c0c54979ba
fetched_at: '2026-06-28T22:43:50.849966+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Qual o conceito do mnemônico P_CAVPPROJ no cálculo
  do Aviso Prévio na Rescisão
type: support-article
updated_at: '2025-06-12T12:39:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059169093-RH-Linha-Protheus-GPE-Qual-o-conceito-do-mnem%C3%B4nico-P-CAVPPROJ-no-c%C3%A1lculo-do-Aviso-Pr%C3%A9vio-na-Rescis%C3%A3o
---

**Dúvida**Qual o conceito do mnemônico P\_CAVPPROJ no cálculo do aviso prévio na rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**O mnemônico P\_CAVPPROJ determina se os dias de aviso prévio deverão ser considerados para o cálculo do tempo de casa (anos trabalhados), e verifica se assim tem direito a mais um ano de casa, para calcular a projeção do Aviso Prévio, conforme exemplos abaixo:  
  
Admissão: 15/01/2015  
Demissão: 03/01/2016  
Completa 1 ano de casa: 15/01/2016  
  
1. Mnemônico **P\_CAVPPROJ** com **“S”**:  
Nesse caso o sistema vai considerar a data de demissão + os 30 dias de aviso prévio (03/01/2016 + 30 = 01/02/2016) para verificar se completa o ano trabalhado (considerando o mnemônico **P\_ANOAVPRO=1**) e gerar no cálculo os 3 dias de projeção do aviso prévio:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097152894/mceclip0.png)  
![](https://tdn.totvs.com/download/attachments/271168843/image2017-1-20%208%3A25%3A40.png?version=1&modificationDate=1484908329000&api=v2)  
  
  
2. Mnemônico **P\_CAVPPROJ** com **“N”**:  
Nesse exemplo o sistema não considera os dias de aviso prévio para somar a data de desligamento e verificar se completa mais um ano de casa, será considerada apenas a data de demissão para calcular o aviso prévio:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099463973/mceclip1.png)  
![](https://tdn.totvs.com/download/attachments/271168843/image2017-1-20%208%3A28%3A6.png?version=1&modificationDate=1484908329000&api=v2)

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo [MP - GPE - Para que serve o Mnemônico NANOAVIPRO / P\_ANOAVIPRO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014595351-MP-GPE-Para-que-serve-o-Mnem%C3%B4nico-NANOAVIPRO-P-ANOAVIPRO-)
