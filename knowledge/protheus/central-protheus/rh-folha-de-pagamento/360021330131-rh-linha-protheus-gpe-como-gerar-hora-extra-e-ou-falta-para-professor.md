---
article_id: 360021330131
category: RH - Folha de Pagamento
content_hash: 575f4c8d93ec6431723fa431acadc5e8d4a23f7fadf7f06dabaa9cf4706e2a34
fetched_at: '2026-06-28T22:44:13.533517+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar hora extra e/ ou falta para professor
type: support-article
updated_at: '2024-09-10T21:01:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021330131-RH-Linha-Protheus-GPE-Como-gerar-hora-extra-e-ou-falta-para-professor
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26282238177047)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como gerar hora extra e/ ou falta para professor?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. Configuração do parâmetro MV\_NCPROF:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017887331)

2. Configuração do sindicato/ aba professores:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017887431)

3. Inclusão de tarefas na tabela S070:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017887491)  
  
4. Vinculo da verba informada na coluna Cod. Verba ao Cod. Tarefa:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018003752)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017887591)  
**Observação**: A verbas de Hora extra e Falta informadas dentro da tabela S070 não precisam ser vinculadas a uma tarefa.  
  
5. Categoria do funcionário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018004712)

6. Lançamento da tarefa, hora extra e falta:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018004092)

**Horas Extras**: Utilizado somente para inclusão de lançamentos de tarefas exclusivos para pagamento de tarefas extras. Para utilização, deve ser incluído um novo lançamento de tarefa, nos quais os campos Aulas Semana (RO\_QTDSEM) e Qtd. Tarefa (RO\_QUANT) precisam estar zerados, e as datas de início e fim desse lançamento de tarefa necessitam estar dentro da competência de cálculo desejada (as datas de início e fim devem obrigatoriamente estar preenchidas dentro da mesma competência).

No cálculo da folha, o resultado dessa tarefa extra será a geração de um lançamento mensal com o código do campo Cód. H.E. especificado na tabela S070 – Tarefas, e seu valor correspondente à multiplicação da quantidade de Horas Extras (RO\_HRSEXT) pelo Val. Unitário (RO\_VALOR) do lançamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017887911)

**Horas Faltas**: Utilizado somente para inclusão de lançamentos de tarefas exclusivos para desconto de tarefas. Para utilização, deve ser incluído um novo lançamento de tarefa, nos quais os campos Aulas Semana (RO\_QTDSEM) e Qtd. Tarefa (RO\_QUANT) precisam estar zerados, e as datas de início e fim desse lançamento de tarefa necessitam estar dentro da competência de cálculo desejada (as datas de início e fim devem obrigatoriamente estar preenchidas dentro da mesma competência).

No cálculo da folha, o resultado dessa tarefa de desconto será a geração de um lançamento mensal com o código do campo Cód. Faltas especificado na tabela S070 – Tarefas, e seu valor correspondente à multiplicação da quantidade de Horas Faltas (RO\_HRSFAL) pelo Val. Unitário (RO\_VALOR) do lançamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017888091)  
  
7. Cálculo da folha de pagamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018004412)

O cálculo das horas extras e faltas são baseados no valor unitário da tarefa, lembrando que, no caso de horas extras o resultado do valor unitário x quantidade de horas extras será valorizado de acordo com o percentual de pagamento definido na verba de Hora Extra.

**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
