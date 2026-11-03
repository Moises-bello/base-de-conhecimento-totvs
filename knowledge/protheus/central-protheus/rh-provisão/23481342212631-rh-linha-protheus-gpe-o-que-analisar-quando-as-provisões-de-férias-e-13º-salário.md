---
article_id: 23481342212631
category: RH - Provisão
content_hash: 53be98c3079cfe00edff30b9f86f25250d5dc1f8ceb4233f035610df3bf334d4
fetched_at: '2026-06-28T22:43:56.925649+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - O que Analisar quando as Provisões de Férias e
  13º Salário não são Calculadas
type: support-article
updated_at: '2025-06-13T20:13:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23481342212631-RH-Linha-Protheus-GPE-O-que-Analisar-quando-as-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio-n%C3%A3o-s%C3%A3o-Calculadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23481342174999) Tempo aproximado para leitura: **00:05:00 min****Dúvida**O que analisar quando as Provisões de Férias e 13º Salário não são calculadas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Se os cálculos de Provisão estão sendo realizados, porém não está sendo gerada nenhuma verba de Provisão de Férias e 13º Salário, realize os seguintes passos:  
  
1. Acesse: Atualizações > Definição de Cálculos > Verbas (GPEA040) e confirme se todas as verbas de Provisão indicadas no artigo abaixo estão cadastradas em sua base:

[Identificadores de Cálculo de Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6071282481303-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-identificadores-de-c%C3%A1lculo-dispon%C3%ADveis-para-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA-sal%C3%A1rio)

2. Confirme se o último pacote de RH Expedição Contínua já foi aplicado:  
Para realizar o Download do pacote, clique no endereço abaixo:

12.1.33: <https://suporte.totvs.com/portal/p/10098/download#detail/1039093>

**Somente para Clientes com Gafrantia Estendida.**

12.1.2210: <https://suporte.totvs.com/portal/p/10098/download#detail/1080347>

**Somente para Clientes com Gafrantia Estendida.**

12.1.2310: <https://suporte.totvs.com/portal/p/10098/download#detail/1123885>

12.1.2410: <https://suporte.totvs.com/portal/p/10098/download?e=1170810>

Observação: Aplique-o em base de testes, e realize um Backup do RPO.  
  
3. Acesse: Atualizações > Funcionários > Controle Dias de Direito (GPEA050), e confirme se há Período Aquisitivo Ativo para os funcionários processados;  
  
4.  Confirme se há cálculo de Folha de Pagamento referente à competência em que o cálculo está sendo realizado;  
  
5. Confirme se há a verba com identificador de cálculo 0318 na Folha de Pagamento dos funcionários;  
  
6. Acesse: Atualizações > Cadastros > Centros de Custos (CTBA030), e confirme se o Centro de Custo atrelado aos funcionários está Bloqueado. O campo CC Bloq. (CTT\_BLOQ) deve estar preenchido com 2 - Não Bloqueado;  
  
7. Confirme se o cadastro dos Centros de Custos estão corretos, de acordo com o Compartilhamento da tabela CTT.  
Se por exemplo, o compartilhamento da tabela CTT for Exclusivo, o campo CTT\_FILIAL deve estar preenchido, como no exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23481342175383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23481294991383)  
  
8. Acesse o Configurador (SIGACFG) Base de Dados > Dicionário > Base de Dados (CFGX031), Localize a tabela SRT e confirme se a ordem dos campos está de acordo com o modelo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23481342178967)  
  
9. Realize novamente uma nova tentativa de Cálculo das Provisões após realizar as validações anteriores.  
  
  
  
**Saiba Mais:**  
[RH - Provisões](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
