---
article_id: 360025899111
category: RH - Lançamentos
content_hash: df1beaeefe973a80424b08d1739c8c42e55fcb1406e37c7fa920b59f4cc6d5d2
fetched_at: '2026-06-28T22:43:31.140092+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Ao tentar excluir uma verba integrada do ponto
  eletrônico sistema não permite e apresenta mensagem de alerta As verbas vindas do
  SIGAPON estão bloqueada para exclusão
type: support-article
updated_at: '2025-04-17T18:47:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025899111-RH-Linha-Protheus-GPE-Ao-tentar-excluir-uma-verba-integrada-do-ponto-eletr%C3%B4nico-sistema-n%C3%A3o-permite-e-apresenta-mensagem-de-alerta-As-verbas-vindas-do-SIGAPON-est%C3%A3o-bloqueada-para-exclus%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26079695686167)**Tempo aproximado para leitura:**00:02:30 min***

**Dúvida** No módulo de Gestão de Pessoal ao entrar na rotina de lançamentos por funcionário/verba o sistema apresenta mensagem de alerta ao tentar deletar uma verba integrada do ponto eletrônico.  
As verbas vindas do SIGAPON estão bloqueada para exclusão.

![Capturaraaa.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024832872)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para solução, basta acessar o módulo Configurador,  no seguinte caminho **Ambiente > Cadastro > Parâmetro** localizar o parâmetro **MV\_BLOQPON** e retirar o preenchimento do mesmo.  
  
Deixando em “branco” não bloqueia nada, ou preenchendo com as opções abaixo:                       
“1” - determina o bloqueio de manutenção na rotina de Lançamento Mensal (GPEA090);  
“2” - determina o bloqueio de manutenção na rotina de Lançamento por Verba (GPEA100);  
“3” - determina o bloqueio de manutenção na rotina de Cancelamento de Cálculo (GPEM160);  
“4” - determina o bloqueio de manutenção na rotina de Geração de Verbas (GPEM170);  
“5” - determina o bloqueio de manutenção na rotina de Cálculo de Rescisão (GPEM040).

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024841271)

**OBS: Na versão 12, tanto o Lançamento Por Funcionário, quanto o Lançamento que fica em Outras Ações na Rescisão, são a mesma rotina, logo, para habilitar a manutenção na rescisão, é necessário retirar o conteúdo 1 e 5 do parâmetro**

**Saiba Mais**  
[Artigos Gestão de Pessoal](%C2%A0https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
