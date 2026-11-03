---
article_id: 4412360614167
category: RH - Soluções para error.log
content_hash: ebcf9923ce783e2c3af03826edef47dd995dc9574e815703c63353e487b72ea9
fetched_at: '2026-06-28T22:44:09.058445+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - É possível realizar limpeza de dados em tabelas
  com dados antigos
type: support-article
updated_at: '2025-09-11T20:08:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412360614167-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-realizar-limpeza-de-dados-em-tabelas-com-dados-antigos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34878396183063) Tempo aproximado para leitura: **00:05:00 min****Dúvida**É possível realizar limpeza de dados em tabelas com dados antigos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quanto às tabelas do **RH** (neste caso, sendo os Módulos de **Ponto Eletrônico** e **Gestão de Pessoal**), elas trabalham em sua grande maioria, com registros de Períodos. Nem todas as tabelas possuem um campo de "Período", propriamente dito, mas podem possuir campos de Data de Pagamento, Data de Apontamento, entre outros, que indicam, de quando este registro em particular é relativo, por exemplo, uma Marcação de Período Fechado (SPG) do período de apontamento de 01/01/2005 à 31/01/2005, terá o campo "PG\_DATA", preenchido com uma data antiga, dentro do Período de Apontamento da época.  
  
Esse trabalho de período, faz com que existam então tabelas de Períodos Abertos e tabelas de Períodos Fechados.   
   **-> Tabelas que compõe o Período Aberto**, são tabelas que permitem os ajustes, os pagamentos, os lançamentos, de um período que ainda está em movimentação;  
   **-> Tabelas que compõe o Período Fechado**, são tabelas que são preenchidas com os dados das tabelas de Período Aberto, após realizar o fechamento do Período, ou seja, mantém todo o histórico do que foi movimentado, pago, lançado ou calculado no Período.  
  
Para o RH, as tabelas de **Período Fechado (Histórico)**, são utilizados apenas em rotinas/situações pontuais, como por exemplo, ao gerar um Recibo de Pagamento de um Roteiro de uma data específica, um relatório de Espelho de Ponto de um período específico, sempre controlado pelos Parâmetros utilizados para a geração destas rotinas.  
  
Posto isto, é seguro afirmar que, mantendo nas tabelas, um histórico de até 3 anos (no caso do GPE, para cálculos de Dissídio e manter as Médias corretamente), não acarretará em nenhum problema na utilização das rotinas, para a Movimentação dos Períodos Abertos.  
  
Algumas das tabelas que podem possuir muitos registros são:  
  **-** **Módulo de Gestão de Pessoal**:  
      **->** **SRD**: Histórico de Pagamentos da Folha;  
      **->** **SRG**: Cabeçalho de Cálculo de Rescisão;  
      **-> SRH**: Cabeçalho de Cálculo de Férias;   
      **->** **SRR**: Itens dos Cálculos de Férias e Rescisão;  
      **->** **SRT**: Provisão  
      **->** **SRE**: Histórico de Transferências;  
    **-> SRF**: Programação de Férias/Controle de Dias de Direto  
  
  **-** **Módulo de Ponto Eletrônico**:  
      **->** **SPN**: Movimentação de Refeitório;  
      **-> SPG**: Movimentação de Marcações;  
    **->** **SPL**: Resultados  
      **->** **SPH**: Apontamentos  
    **->** **RFH**: Pré-Leitura  
    **->** **RFG**: Pré-ACJEF  
  
**Obs.:** Sempre mantenha o backup destas tabelas de forma prática ou em ambiente apartado, pois elas podem ser necessárias vez ou outra para a extração de algum relatório pontual ou possível Fiscalização, onde estes dados históricos serão requeridos.

**Saiba Mais:**[RH - Soluções Error Log](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115003853987-RH-Solu%C3%A7%C3%B5es-para-error-log)   
Pacote de expedição contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>
