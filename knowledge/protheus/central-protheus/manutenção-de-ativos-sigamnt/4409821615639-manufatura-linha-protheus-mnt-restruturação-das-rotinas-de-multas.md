---
article_id: 4409821615639
category: Manutenção de Ativos (SIGAMNT)
content_hash: 0fa621052d125bf52a934c21340d7090c11b52beea243e5a751ab1490fa8abb1
fetched_at: '2026-06-28T22:42:34.398688+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Restruturação das rotinas de Multas
type: support-article
updated_at: '2021-10-04T13:06:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409821615639-Manufatura-Linha-Protheus-MNT-Restrutura%C3%A7%C3%A3o-das-rotinas-de-Multas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:30 min****Dúvida**As rotinas da *suite* de **Multas** no módulo **Manutenção de Ativos** foram convertidas para o padrão **MVC - Model View****Controller**?  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Sim. Visando a melhoria na utilização dos processos de **Multas** do módulo **Manutenção de Ativos** com **Gestão de Frotas** as rotinas abaixo foram convertidas para o padrão **MVC** de desenvolvimento:

* **MNTA765 - Multa**
* **MNTA766 - Notificação**
* **MNTA845 - Inconsistências**

As rotinas disponíveis neste padrão de desenvolvimento estão aptas a receber outras integrações via **execauto** por exemplo. Devido a conversão, algumas alterações de dicionário foram necessárias para a implementação correta das alterações na release **12.1.23.**Desta forma, é necessário realizar a aplicação do pacote acumulado de manutenção da release **12.1.23**, disponível [neste link](https://suporte.totvs.com/portal/p/10098/download?e=742966).  
Para a release de versão futura, **12.1.25**, as alterações serão nativas em dicionário. Para a release **12.1.17** não é necessário realizar a aplicação de pacotes de atualização de dicionário.  
  
**Saiba mais**  
Devido a reestruturação para o padrão de desenvolvimento **MVC** houve também a necessidade de atualização dos **Pontos de entrada** utilizados pelas rotinas descritas neste documento. Para explicação completa das alterações e indicações de alterações caso necessário, recomendamos a consulta do artigo [Manufatura - Linha Protheus - MNT - Pontos de entrada rotinas de Multas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409832568599).
