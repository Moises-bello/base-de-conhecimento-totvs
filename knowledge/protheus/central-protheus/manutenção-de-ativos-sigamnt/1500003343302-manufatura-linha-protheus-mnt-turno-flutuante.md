---
article_id: 1500003343302
category: Manutenção de Ativos (SIGAMNT)
content_hash: d91ff3acf4a547cfa0d3df16f9d6fdd64def26fa26529a057431e14fb5dabf28
fetched_at: '2026-06-28T22:42:34.511161+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Turno Flutuante
type: support-article
updated_at: '2026-01-28T12:06:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003343302-Manufatura-Linha-Protheus-MNT-Turno-Flutuante
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37988276608279)*** Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Qual é o conceito e usabilidade do turno flutuante?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**  
Trata-se de uma solução para atender a necessidades de clientes que trabalham com o cadastro de **Equipe de manutenção - TP4** em regime de **Calendários** com **turnos rotativos**.  
  
Para habilitar esta solução, basta configurar o parâmetro **MV\_NGFLUT** - **Indica se a empresa trabalha com calendário flutuante** com o conteúdo **S - Sim**. Desta forma, o Sistema utilizará de forma sistêmica, calculando a disponibilidade do funcionário através da equipe o qual pertencem, passando a ignorar o calendário do mesmo  informado no campo **Turno Funcionário - T1\_TURNO** da rotina de cadastro de **Funcionários da Manutenção - MNTA020**  
Para a utilização desta solução todos os **Funcionários - ST1** devem estar relacionados a uma equipe de trabalho, na rotina **Equipe de manutenção - MNTA800**. Caso contrário, o Sistema poderá apresentar valores zerados de disponibilidade.  
  
**Exemplo**

| **Calendários - SH7** | | |
| --- | --- | --- |
| **Cídigo** | **Descrição** | **Carga Horária** |
| T-01 | Turno 12x36 (Revezamento) | 8 horas |
| T-02 | 1 - Turno - Matutino | 4 horas |
| T-03 | 2 - Turno - Vespertino | 4 horas |

| **Equipe** | **000001 - Equipe Folguista** | |
| --- | --- | --- |
| **Turnos** | **Data início** | **Data Fim** |
| T-01 | 01/01/2026 | 31/01/2026 |
| T-02 | 01/02/2026 | 28/02/2026 |
| T-03 | 01/03/2026 | 31/03/2026 |

| **Funcionários** | **Nome** | **Equipe** |
| --- | --- | --- |
| 000001 | Joao da Silva | 000001 |

Analisando o cenário acima, ao solicitar a disponibilidade do funcionário **João da Silva** para o dia **26/01/26**, teremos como resultado **8 horas**. Diferente se optado pelo dia **05/02/26**, onde o retorno será de apenas **4 horas**.  
  
Caso seja solicitado a disponibilidade para o dia **11/04/2026**, podemos perceber que não foi cadastrado um calendário para esta data, desta forma o retorno da disponibilidade será **0 - zero**.  
  
Segue o **fluxograma** da funcionalidade:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102259474)

**Saiba mais**  
Para informações complementares a respeito dos cadastrados citados nesse artigo veja:   
[Funcionários (MNTA020 - SIGAMNT)](https://tdn.totvs.com/pages/viewpage.action?pageId=506389105)  
[Equipes (MNTA800 - SIGAMNT)](https://tdn.totvs.com/pages/releaseview.action?pageId=655639753)
