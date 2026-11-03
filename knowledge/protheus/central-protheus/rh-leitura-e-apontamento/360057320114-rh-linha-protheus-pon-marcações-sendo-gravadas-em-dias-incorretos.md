---
article_id: 360057320114
category: RH - Leitura e Apontamento
content_hash: f84ab9b54788436118f7dd3da3c82f8ba8ccb842c3a6663000949d1707d23081
fetched_at: '2026-06-28T22:44:45.977760+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Marcações sendo gravadas em dias incorretos
type: support-article
updated_at: '2026-04-27T12:29:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057320114-RH-Linha-Protheus-PON-Marca%C3%A7%C3%B5es-sendo-gravadas-em-dias-incorretos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32529674864023) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como corrigir quando, ao fazer Leitura/Apontamento, as marcações são gravadas em dias incorretos (dia seguinte ou dia anterior)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Este incidente ocorre por alguns fatores principais e deve ser validado em seu ambiente, que são:  
  
**1.** [**Tabela de Horário Padrão**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293)**:** é necessário preencher horários para todos os dias, inclusive os dias Não Trabalhados, DSR e Compensado.  
  
**2.** [**Limite Inferior e Superior**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002754861) **de todos os dias:** na Tabela de Horário Padrão, os limites se tratam de coberturas de horários além do cadastrado na tabela, ou seja, para uma entrada prevista às 08h da Segunda-Feira que tem 05h de Limite Inferior, significa que marcações feitas a partir das 03h pertencem a este dia. Para uma saída prevista às 18h que tem 05h de Limite Superior, significa que marcações feitas até às 23h pertencem a este dia.  
É possível aumentar estes limites, porém, é importante garantir que o limite de um dia não sobreponha o do dia anterior/seguinte.  
É recomendado também que a soma dos limites Inferior, Superior e carga horária diária não ultrapassem o valor de **23h59** no total.  
  
Exemplo de uma Tabela de Horário Padrão com os limites Inferior e Superior no limite máximo de 23h59 totais e não sobrepondo o dia anterior/seguinte:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410340006039)  
  
  
**3.** É necessário termos [Troca de Turno](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671) com o primeiro dia do período para todos os funcionários. Estes registros são criados quando incluímos a troca manualmente, ou quando o Fechamento Mensal do período é executado, por esse motivo, é de extrema importância a execução mensal do fechamento do ponto.  
  
Lembrando que se for necessário qualquer ajuste cadastral depois de já ter feito a leitura das marcações, deverá ser executado um reapontamento através da rotina de Leitura/Apontamento, pois esta rotina é capaz de ajustar a ordem/classificação das marcações.  
  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Funcionalidades dos campos de Limite inferior e Limite superior na Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002754861-RH-Linha-Protheus-PON-Funcionalidades-dos-campos-de-Limite-inferior-e-Limite-superior-na-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o)  
[RH - Linha Protheus - PON - Como funciona a Troca de Turno dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-RH-Linha-Protheus-PON-Como-funciona-a-Troca-de-Turno-dos-funcion%C3%A1rios)
