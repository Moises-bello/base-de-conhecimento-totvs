---
article_id: 11484220498455
category: Espelho
content_hash: 7a9e2a7af6f2fda499d587ed549211e2f8718686a55899c0acdd698305352333
fetched_at: '2026-06-28T22:46:31.276452+00:00'
product: rm
section_id: 6045459696023
source: central-rm
title: RH - RM - PTO - Alteração manual da natureza da batida não ser desfeito
type: support-article
updated_at: '2026-06-24T12:55:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11484220498455-RH-RM-PTO-Altera%C3%A7%C3%A3o-manual-da-natureza-da-batida-n%C3%A3o-ser-desfeito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16034150738199) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Após ajustar a natureza da(s) batida(s) de forma manual, ao realizar uma nova importação de batida a alteração é desfeita, o que fazer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto- 12.1.17 e superiores  
  
**Solução**Para que não ocorra a desfigurações das batidas já corrigidas, siga os passos abaixo:

1. Acesse o menu Configurações | Parametrizador ao abrir o assistente clique em avançar e selecione o processo **08.01- Iniciais** e avance.
2. Vai ser aberto um novo assistente e avance até a **Etapa 2 - Importação** e marque q flag do parâmetro "**Considera a alteração de natureza da batida no processo de acerto de batidas".**  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11484620751895)  
     
   Utilizando este parâmetro, caso seja feito a inclusão de batidas, inclusão de batidas pela edição ou a alteração de natureza das batidas no espelho (RM.exe ou Portal), esta natureza não será alterada nos processos de importação de batidas, lançamento de horário planejado e recálculo.

**Observação**

No lançamento de Horário Planejado, se existir batida inserida para o dia com a natureza alterada,             todas as batidas do horário planejado serão lançadas respeitando a batida já inserida. Na existência           de batidas sem par no espelho, ao realizar o recálculo, poderá ser calculado extras ou faltas.  
  
**Saiba Mais**Mais detalhes sobre o parâmetro e as demais parametrizações disponíveis: [Parâmetros da Importação](https://tdn.totvs.com/pages/viewpage.action?pageId=452719611)  
[Batidas desposicionadas (natureza errada) no processo de importação de batidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042820233)
