---
article_id: 360013084192
category: RH - Fechamentos
content_hash: e81af8dec81bd7a35e8f90de6cf4eebc233769554917637d2558c6cb53ce7e7c
fetched_at: '2026-06-28T22:44:48.918041+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Migração de dados no Fechamento Mensal do Ponto
type: support-article
updated_at: '2026-03-17T18:29:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013084192-RH-Linha-Protheus-PON-Migra%C3%A7%C3%A3o-de-dados-no-Fechamento-Mensal-do-Ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38351364784151) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Após o **fechamento mensal** do ponto, para **quais tabelas** as informações do período são **migradas**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
No **Fechamento Mensal do Ponto**, as informações das tabelas do período aberto **são migradas** para as suas respectivas tabelas de **Acumulados**, procedimento este que visa **manter a segurança** das informações, além de **histórico dos dados.**  
  
Segue abaixo relação das **tabelas de período aberto** e sua respectiva **tabela de acumulado (pós fechamento)**:

|  |  |
| --- | --- |
| **Tabelas Período Aberto** | **Tabelas Pós Fechamento** |
| **SP5** - Movimentação de Refeitório | **SPN -** Histórico Movimento Refeitório |
| **SP8** - Movimentação das Marcações | **SPG** - Histórico de Marcações |
| **SPB** - Resultados | **SPL** - Histórico de Resultados |
| **SPC** - Apontamentos | **SPH -** Histórico de Apontamentos |
| **RFE -** Pré-Leitura | **RFH** - Acumulado de Pré-Leitura |
| **RFF -** Pré-ACJEF/AEJ | **RFG** - Acumulado de Pré-ACJEF/AEJ |

**Saiba mais:**  
[RH - Linha Protheus - PON - Como efetuar o Fechamento Mensal do Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004103232-RH-Linha-Protheus-PON-Como-efetuar-o-Fechamento-Mensal-do-Ponto)  
[RH - Linha Protheus - PON - Como utilizar os parâmetros de Leitura e a tabela SPO, responsável pelo fechamento mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045460153-RH-Linha-Protheus-PON-Como-utilizar-os-par%C3%A2metros-de-Leitura-e-a-tabela-SPO-respons%C3%A1vel-pelo-fechamento-mensal)  
[MP - PON - O que verificar quando na execução do Fechamento Mensal, apresentar log de marcações ímpares](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012927531-MP-PON-O-que-verificar-quando-na-execu%C3%A7%C3%A3o-do-Fechamento-Mensal-apresentar-log-de-marca%C3%A7%C3%B5es-%C3%ADmpares?source=search)  
[MP - PON - Após o fechamento mensal, o sistema não alterou o período de apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012922731-MP-PON-Ap%C3%B3s-o-fechamento-mensal-o-sistema-n%C3%A3o-alterou-o-per%C3%ADodo-de-apontamento?source=search)
