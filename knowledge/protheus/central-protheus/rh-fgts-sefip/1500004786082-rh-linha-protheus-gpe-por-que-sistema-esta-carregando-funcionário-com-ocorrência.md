---
article_id: 1500004786082
category: RH - FGTS / SEFIP
content_hash: 7ab25c4edcdd4e81a47ed9b044113ea9ddeeebb55f5a3c0de8f68b9849959afa
fetched_at: '2026-06-28T22:43:41.312668+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Por que Sistema esta carregando funcionário com
  ocorrência de múltiplo vínculo na Sefip para funcionário com afastamento
type: support-article
updated_at: '2025-09-05T12:09:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004786082-RH-Linha-Protheus-GPE-Por-que-Sistema-esta-carregando-funcion%C3%A1rio-com-ocorr%C3%AAncia-de-m%C3%BAltiplo-v%C3%ADnculo-na-Sefip-para-funcion%C3%A1rio-com-afastamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34708447215511) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Por que o Sistema esta carregando ocorrência de múltiplo vínculo na Sefip para funcionário com afastamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O Sistema esta carregando ocorrência de múltiplo vínculo para funcionário com afastamento pois houve alteração no *layout* da Sefip, e no novo *layout* deve ser gerada essa informação para os afastamentos,  conforme abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006235242)  
Sem essa informação não é possível informar o Valor Descontado Segurado (INSS parte Funcionário), pois ao simular a Sefip é apresentado o erro abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014168282)

**Saiba mais**  
[10774600 DRHPAG-43148 DT Adequação à versão 8.4 de 12/2020 da SEFIP - Auxilio doença/acidente e Licença Maternidade](https://tdn.totvs.com/pages/viewpage.action?pageId=592285248)
