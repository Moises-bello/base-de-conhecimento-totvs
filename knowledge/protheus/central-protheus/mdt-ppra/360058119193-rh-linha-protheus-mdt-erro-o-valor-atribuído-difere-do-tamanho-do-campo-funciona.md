---
article_id: 360058119193
category: MDT - PPRA
content_hash: 6ebcff870b00a131dd4ff33711c7fbac306cc077d3a3e8a8e07f9e8eec974d69
fetched_at: '2026-06-28T22:44:27.209107+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus -  MDT - Erro "O valor atribuído difere do tamanho do campo
  (Funcionario)" quando informado a matricula na rotina Tarefas x Funcionário (MDTA090)
type: support-article
updated_at: '2025-08-14T18:46:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058119193-RH-Linha-Protheus-MDT-Erro-O-valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Funcionario-quando-informado-a-matricula-na-rotina-Tarefas-x-Funcion%C3%A1rio-MDTA090
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19641721562647)**Tempo aproximado para leitura **00:02:00 min****Ocorrência**Erro "O valor atribuído difere do tamanho do campo (Funcionário)" quando informado a matricula na rotina Tarefas x Funcionário (MDTA090) no modulo medicina e segurança do trabalho (SIGAMDT).  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097796593)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho  - Todas as versões  
  
**Causa**Esse erro ocorre quando o tamanho do campo **Funcionário** (TN6\_NOME) está diferente do tamanho do campo **Nome** (RA\_NOME).  
  
**Solução**  
Por padrão o campo **Nome** (RA\_NOME) tem tamanho 30, então o campo **Funcionário** (TN6\_NOME) também deve ter esse mesmo tamanho.  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesso o modulo Configurador (SIGACFG) no caminho: Base de Dados > Base de Dados, busque pela tabelas SRA e TN6 e verifique o tamanho do campo **Nome** (RA\_NOME) e **Funcionário** (TN6\_NOME) .  
  
Note que no meu exemplo o campo **Funcionário** (TN6\_NOME) está com tamanho **29**, sendo que o padrão do **Nome** (RA\_NOME) é **30**.  
  
![tn6_funcionario.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360095496334)  
  
![ra_nome.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360095496354)  
  
2. Para ajustar esse erro é necessário deixar o campo **Funcionário** (TN6\_NOME) com tamanho **30:**

![alteracao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360095496614)  
  
**Observação**

* Em caso de dúvidas em como fazer a alteração do tamanho de campos entre em contato com o suporte do **Framework**;
* Recomendamos que efetue o backup da base antes de qualquer modificação.

**Saiba Mais**[Artigos PPRA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945454-MDT-PPRA)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
