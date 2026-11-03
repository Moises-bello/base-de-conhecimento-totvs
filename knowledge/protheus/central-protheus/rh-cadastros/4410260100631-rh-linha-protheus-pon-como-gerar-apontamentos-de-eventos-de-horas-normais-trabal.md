---
article_id: 4410260100631
category: RH - Cadastros
content_hash: ea12685828694ecbba335437a05ff525dc0a13423c6fa0d144a2130c0d5097ba
fetched_at: '2026-06-28T22:44:52.881951+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como gerar Apontamentos de eventos de Horas Normais
  trabalhadas ou não trabalhadas dentro da jornada prevista do Funcionário
type: support-article
updated_at: '2026-02-03T16:49:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410260100631-RH-Linha-Protheus-PON-Como-gerar-Apontamentos-de-eventos-de-Horas-Normais-trabalhadas-ou-n%C3%A3o-trabalhadas-dentro-da-jornada-prevista-do-Funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35380240340759) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como gerar Apontamentos de eventos de Horas Normais trabalhadas ou Não Trabalhadas dentro da jornada prevista do Funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
No **Ponto Eletrônico**, temos alguns eventos que são **destinados para apuração na Regra de Apontamento para Funcionários Horistas**, onde os mesmos, como o próprio nome diz, receberão de acordo com quantas horas, diariamente, trabalharem.  
  
Para que sejam gerados os eventos de horas normais/trabalhadas conforme a prevista na tabela de horário do funcionário, deverá seguir com os procedimentos abaixo:  
  
Exemplo de configuração na **Regra de Apontamento** para **Horistas**:  
Acesse em **Atualizações > Cadastro do Ponto > Regra de Apontamento**, crie ou altere a Regra de Apontamento:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410259313175)  
  
Os **Identificadores de Ponto dos Eventos relacionados as Horas Normais trabalhadas ou não trabalhadas** são:

|  |  |
| --- | --- |
| 001A | Horas Normais |
| 002A | Horas de DSR |
| 005A | Horas Normais Não Realizadas |
| 006A | Horas Noturnas Não Realizadas |
| 026A | Horas Normais Noturnas |
| 030A | Horas Trabalhadas Intervalo |
| 031A | Intervalo Normal Noturno |

Os **eventos** que **serão pagos** em **Folha de Pagamento**, precisam possuir a **verba** vinculada.  
Acesse em **Atualizações >  Cadastro do Ponto > Eventos**, crie o evento e **amarre-o ao Identificador do Ponto** respectivo e vincule o **Cod p/Folha(verba)** nele:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410259850647)  
  
Cadastrar ou já ter uma Verba cadastrada de Salário Horista - id de cálculo 0032. Veja mais sobre o cadastro de verba: [RH - Linha Protheus - GPE - Como cadastrar verbas no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411677253783-RH-Linha-Protheus-GPE-Como-cadastrar-verbas-no-Protheus?source=search)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410259893655)  
Verba de DSR horista (provento) - id de cálculo 0033  
  
Caso o cliente possua funcionários **mensalistas** e queira utilizar os **eventos** citados apenas como **Eventos Base**, ou seja, para **demonstração** nas **rotinas de manutenção**, **é possível**, porém, deve se **atentar** a não deixar **verba vinculada** e não deixar parametrizado para computar estas horas no **Banco de Horas**, conforme exemplo abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410277239319)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410277248279)  
  
**Lembrando que** se na **mesma filial** existem funcionários **Horistas e Mensalistas**, os **eventos** serão **SEMPRE** utilizados pelos **horistas**, **não sendo possível usar para os Mensalistas**. O processo de uso dos **eventos** como **Base**, funcionam **apenas** para clientes que **não possuem Horistas na empresa**.  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como utilizar o cadastro de evento do ponto eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407450836887-RH-Linha-Protheus-PON-Como-utilizar-o-cadastro-de-evento-do-ponto-eletr%C3%B4nico?source=search)  
[RH - Linha Protheus - PON - Principais apontamentos, forma de apuração e identificadores de cálculo do módulo ponto eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015532691-RH-Linha-Protheus-PON-Principais-apontamentos-forma-de-apura%C3%A7%C3%A3o-e-identificadores-de-c%C3%A1lculo-do-m%C3%B3dulo-ponto-eletr%C3%B4nico?source=search)
