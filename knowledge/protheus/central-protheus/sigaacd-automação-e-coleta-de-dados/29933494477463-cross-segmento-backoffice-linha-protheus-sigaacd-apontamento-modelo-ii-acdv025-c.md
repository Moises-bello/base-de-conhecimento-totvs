---
article_id: 29933494477463
category: SIGAACD - Automação e Coleta de Dados
content_hash: 0d05b30bfa8d0b848dc0c9ec08a9a9b3f08709490e8645d5f79d6528d15c81e2
fetched_at: '2026-06-28T22:39:11.383436+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Apontamento Modelo
  II (ACDV025) considera tempo da pausa durante a transação?
type: support-article
updated_at: '2025-03-12T12:45:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29933494477463-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Apontamento-Modelo-II-ACDV025-considera-tempo-da-pausa-durante-a-transa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29933483175319) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Na rotina de Apontamento Modelo II (ACDV025), é considerado o tempo de Pausa?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

Os apontamentos de produção na rotina **ACDV025** seguem o mesmo modelo das rotinas do **SIGAPCP**.

Quando falamos em Horas Improdutivas (**MATA682**) podemos ter dois comportamentos, a depender do motivo de parada informada (cadastrado no **SFCA004**).

Se for informada uma parada e nessa parada um motivo de parada que não está com o campo Gera MOD preenchido, a mesma será somente informativa, porém informando uma parada, com um motivo de parada com o campo **Gera Mod** (rotina **SFCA004**) preenchido, será requisitada a **MOD** vinculada ao recurso informado.

**Exemplos**:

Supondo que temos três apontamentos:

* OP 00000101001 Recurso 001 Tempo: 01h:30min
* OP 00000201001 Recurso 001 Tempo: 01h:00min
* OP 00000301001 Recurso 001 Tempo: 00h:30min

No total, esses três apontamentos consumiram 03h:00min da **MOD** relacionada ao recurso 001, então no recalculo de custo médio, o custo atrelado a essa **MOD** será rateado entre essas três OPs, considerando que uma consumiu 01h:30min, outra 01h:00min e outra 00h:30min.

Na SD3 teremos:

* OP 00000101001 Produto MOD0005 Tempo: 01h:30min
* OP 00000201001 Produto MOD0005 Tempo: 01h:00min
* OP 00000301001 Produto MOD0005 Tempo: 00h:30min

Se realizarmos um apontamento de parada relacionando uma parada que tem o campo **Gera MOD** não preenchido, nada é alterado na SD3, só é feito um registro na **SH6** documentando a parada.

Já se realizarmos um apontamento de parada e informarmos um tipo de parada com o campo **Gera MOD** marcado, supondo que essa parada foi de 00h:15min, teremos na **SD3**:

* OP 00000101001 Produto MOD0005 Tempo: 01h:30min
* OP 00000201001 Produto MOD0005 Tempo: 01h:00min
* OP 00000301001 Produto MOD0005 Tempo: 00h:30min
* OP (em branco) Produto MOD0005 Tempo:    00h:25min -> Apontamento de parada (15/60=0,25)

Se o motivo de parada que eu informei tem o campo **Gera MOD** marcado, o custo referente ao tempo dessa parada não será rateado entre as OPs, já que eu tenho um registro para essa parada na **SD3**.

Observação:

Independente da configuração do Tipo de Parada o campo **H6\_TEMPO** não abate o tempo de pausa, pois no conceito do **SIGAPCP** esse tempo sempre será o total de produção, diferente do módulo [“Chão de Fábrica” (SIGASFC)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005696234-Ch%C3%A3o-de-F%C3%A1brica-SIGASFC)

Essa pausa será utilizada unicamente para cálculo do custo das MOD, caso necessite retirar horas/minutos da produção, é necessário inserir manualmente a informação, exceto se for uma parada prevista na rotina de Calendário (**MATA780**)

**Exemplo:**

Início da produção às 09h:00min, até as 15h:00min, porém no calendário (**MATA780**) temos um intervalo para almoço de 01h:00min, esse tempo de almoço, que está cadastrado no calendário será descontado pelo sistema, ou seja, fará uma requisição da MOD de 05h:00min.

Caso, além do almoço, houve falta de luz (**exemplo**) por 00h:30min, seria necessário apontar a produção sem esses 00h:30min:

* Início da Produção 09h00min até 10h:30min e das 11h:00min até 15h00min

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como calcular o campo "Tempo Real" (H6\_TEMPO) no ACD corretamente?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28384567455895-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-calcular-o-campo-Tempo-Real-H6-TEMPO-no-ACD-corretamente)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV023 e ACDV025 - Pontos de Entrada disponíveis nas rotinas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14155774651799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV023-e-ACDV025-Pontos-de-Entrada-dispon%C3%ADveis-nas-rotinas)
