---
article_id: 29538008859287
category: Gestão de Transportes (TMS)
content_hash: b5653b1705b8bdacace28780209914e48991757943d3134e8f646058307c8ceb
fetched_at: '2026-06-28T22:45:33.410272+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - TMSA20057 - Não é possível estornar o documento.
  Aguardando retorno da SEFAZ
type: support-article
updated_at: '2025-01-30T13:29:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29538008859287-Log%C3%ADstica-Linha-Protheus-TMS-TMSA20057-N%C3%A3o-%C3%A9-poss%C3%ADvel-estornar-o-documento-Aguardando-retorno-da-SEFAZ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29538008841495) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como tratar o *help* **TMSA20057 - Não é possível estornar o documento. Aguardando retorno da SEFAZ** ao estornar o calculo de documentos no **Protheus TMS** ?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O *help* **TMSA20057 - Não é possível estornar o documento. Aguardando retorno da SEFAZ**ocorre quando o documento foi transmitido para a **SEFAZ - Secretaria da Fazenda**, mas ainda não obteve retorno, ficando com a situação **Aguardando retorno SEFAZ**, indicada pelo campo **DT6\_SITCTE = 1.** Esta situação também pode ocorrer quando a transmissão obtém os retornos **678 - Consumo Indevido** ou **999 - Erro não catalogado**.  
  
Nestes cenários, a primeira coisa a se fazer é validar se a comunicação com a **SEFAZ** está normal. O retorno de autorização ou rejeição da **SEFAZ** é necessário para permitir o estorno do cálculo.   
  
Se o documento não chegou a ser autorizado na **SEFAZ** e o Sistema continua exibindo o **TMSA20057**, uma solução é desativar temporariamente o parâmetro **MV\_CTECAN**. Isso impedirá a exibição do help e permitirá o estorno do cálculo normalmente.   
  
Para que a solução acima funcione, o fonte **TMSA200.prw** deve estar atualizado para **27/01/2025** ou superior, disponível em **Saiba mais**ou então, ajustar o campo **DT6\_SITCTE = 0**para que o Sistema permita o estorno do cálculo do documento.  
  
**Saiba mais**Atualização da rotina **TMSA200** de **27/01/2025** para **12.1.2210 - Garantia Estendida**: [PACOTE\_DE\_CORRECAO\_22386048\_DLOGTMS02-27780\_12.1.2210.ZIP](https://r.totvs.io/p/1183076)   
Atualização da rotina **TMSA200** de **27/01/2025** para **12.1.2310** -  [PACOTE\_DE\_CORRECAO\_22386048\_DLOGTMS02-27780\_12.1.2310.ZIP](https://r.totvs.io/p/1183074)   
Atualização da rotina **TMSA200** de **27/01/2025** para **12.1.2410** - [PACOTE\_DE\_CORRECAO\_22386048\_DLOGTMS02-27780\_12.1.2410.ZIP](https://r.totvs.io/p/1183077)
