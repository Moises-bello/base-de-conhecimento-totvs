---
article_id: 8836693849111
category: RH - Arquivos Magnéticos
content_hash: 1735f492438d224a6af79c702178242001b3f42f92af6070e04dda952ed6fb04
fetched_at: '2026-06-28T22:44:55.254049+00:00'
product: protheus
section_id: 32302371669783
source: central-protheus
title: RH - Linha Protheus - PON - ACJEF Evento de Hora Extra não encontrado para
  a filial
type: support-article
updated_at: '2025-09-16T12:14:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8836693849111-RH-Linha-Protheus-PON-ACJEF-Evento-de-Hora-Extra-n%C3%A3o-encontrado-para-a-filial
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34971345067543) Tempo aproximado para leitura: 00:01:00 min******Dúvida**RH - Linha Protheus - PON - ACJEF Evento de Hora Extra não encontrado para a filial  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Este log é apresentado, quando temos um evento de Hora Extra calculado nas tabelas referente ao ACJEF, são elas: RFF - período aberto de Ponto e RFG - períodos fechados de Ponto e, este evento encontrado e, classificado como Hora Extra, hoje não encontra-se cadastrado como uma Hora Extra autorizada na rotina de Tipos de Horas Extras - tabela SP4.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8836634724375)  
  
O ACJEF gera os eventos de Hora Extra, conforme estão gravados nas tabelas RFF e RFG, períodos abertos e fechados, respectivamente, com isso, ao gerar o ACJEF e tivermos Horas Extras a serem impressas, o Sistema irá validar o código gravado na tabela RFF ou RFG com o evento que está hoje, cadastrado na tabela SP4.  
  
Nesse caso, não orientamos a alteração dos códigos de eventos na rotina Tipos de Horas Extras, tabela SP4, pois se um dia o evento de Hora Extra normal foi apontado e calculado no código 100, por exemplo e, hoje na tabela SP4 foi alterado o evento autorizado de Hora Extra normal para 101, o ACJEF irá realizar uma comparação e, por estar divergente, o arquivo magnético não irá ser impresso.  
  
A solução seria, retornar o cadastro dos Tipos de Horas Extras, aos eventos que eram anteriormente, para geração do ACJEF, por isso, é importante ressaltar que, não orientamos, alterar os códigos de eventos autorizados na rotina Tipos de Horas Extras, se houver necessidade de mudança de contabilização de hora extra, alterar o cadastro do evento em si, preservando sempre o código dele na SP4, para não termos divergência com a RFF ou RFG.  
  
  
**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
