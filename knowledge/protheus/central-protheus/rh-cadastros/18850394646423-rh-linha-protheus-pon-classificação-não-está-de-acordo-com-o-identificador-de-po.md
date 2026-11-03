---
article_id: 18850394646423
category: RH - Cadastros
content_hash: 3a4ba4d1d581889c38a148275be802afd45efffc2986a4545c852fe1879ad644
fetched_at: '2026-06-28T22:44:52.766564+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Classificação não está de acordo com o Identificador
  de Ponto selecionado
type: support-article
updated_at: '2025-12-29T13:25:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18850394646423-RH-Linha-Protheus-PON-Classifica%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-de-acordo-com-o-Identificador-de-Ponto-selecionado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18850438865559) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
No módulo Ponto Eletrônico, ao tentar realizar o cadastro de um Evento é apresentado o ***help*** "Aviso de Inconsistência! Classificação não está de acordo com o Identificador de Ponto selecionado."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18851161686423)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
Esse incidente pode ocorrer quando um Evento é classificado de uma forma que não é compatível com o ID selecionado.  
  
**Solução**  
Para solucionar essa ocorrência, acessar a rotina **Atualizações > Cadastro do Ponto > Eventos**, deve ser ajustada a classificação do Evento de acordo com o ID selecionado.  
  
No exemplo abaixo, veja que foi selecionado o **ID 028A** - Adicional Noturno sobre Horas Extras Autorizada, neste caso, a **Classificação** deve ser **ZZ - Outros**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18862256061463)

Se for cadastrado um Evento de Hora Extra, para manter a classificação com a opção **"1 - Hora Extra",** não deve ser informado ID de Ponto, pois como não existe uma limitação na criação de Eventos de Hora Extra, ou seja, podem ser criados quantos eventos forem necessários, não existem IDs específicos para tratamento destes Eventos.  
  
**Importante:** Essa ocorrência pode ser apresentada para qualquer Evento que for classificado de forma incorreta. Por exemplo, se tentarmos classificar como Hora Extra um evento que esteja vinculado ao ID 010A - Falta Autorizada.  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
