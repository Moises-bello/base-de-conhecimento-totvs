---
article_id: 4406758944791
category: RH - Leitura e Apontamento
content_hash: 9966990a12f234c02979995b96766f395879cb392027d832834f70cfc7c7d42d
fetched_at: '2026-06-28T22:44:45.899560+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Apontamento de Adicional Noturno quando existe
  Afastamento
type: support-article
updated_at: '2025-08-18T12:18:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406758944791-RH-Linha-Protheus-PON-Apontamento-de-Adicional-Noturno-quando-existe-Afastamento
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34258193373335) Tempo aproximado para leitura: 00:01:30 min******Dúvida**O sistema não está lançando o adicional de horas noturnas quando o funcionário possui um atestado, mas trabalhou no dia. Apontamento de Adicional Noturno quando existe Afastamento.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**

Foi **criado** um novo **parâmetro**, **MV\_APOHRAF**, para **flexibilizar os lançamentos de Horas Normais Trabalhadas** para o funcionário, quando o mesmo trabalhou o que deveria no dia e possuí um **atestado médico**.  
  
Quando o **MV\_APOHRAF** estiver com **.T.**, o sistema **irá lançar as horas normais e o adicional noturno** se houver. Em casos onde o funcionário trabalhou apenas meio período e foi ao médico, não será lançado qualquer evento, como por exemplo faltas, saída antecipada, hora extra e etc.  
  
Quando o **MV\_APOHRAF** estiver com **.F.**, o sistema **não irá lançar os eventos, mesmo que o funcionário tenha realizado sua jornada completa em dias em que o funcionário possui atestado médico**.  
  
**Atenção**A funcionalidade descrita estará liberada no pacote de expedição do RH e, além de **aplicar o patch**, será necessário **executar o UPDDISTR** com o **dicionário diferencial** para a criação da tabela e grupos de perguntas.

**Informações técnicas MV\_APOHRAF:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| X6\_VAR | X6\_TIPO | X6\_DESCRIC | X6\_DESC1 | X6\_DESC2 |
| MV\_APOHRAF | L (Lógico) | Define se ira apontar as horas normais trabalhadas | em dias que o funcionário possui atestado medico. | .T. = Aponta; .F. = Não aponta |

  
**Saiba Mais**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
