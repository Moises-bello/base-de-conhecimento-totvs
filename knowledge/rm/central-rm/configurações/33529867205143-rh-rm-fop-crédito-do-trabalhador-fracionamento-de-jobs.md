---
article_id: 33529867205143
category: Configurações
content_hash: e7a494d4a84b3aacb7e057146bc088efa74e3199969a58996e0b376d5b450924
fetched_at: '2026-06-28T22:46:49.443408+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - Fracionamento de Jobs
type: support-article
updated_at: '2025-07-17T12:00:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33529867205143-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Fracionamento-de-Jobs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33529873257751) Tempo aproximado para leitura: **00:02:08 min**  
  
**Dúvida**  
  
Durante o processo de importação de créditos para os trabalhadores no RM - Folha de Pagamento, existe o parâmetro **“Qtde de Job’s”**, localizado em ***Configurações | Parametrizador | Folha Normal | Crédito Trabalhador***.

O que significa esse campo? Qual a diferença entre informar 0, 1 ou valores maiores? Como funciona o fracionamento de jobs nesse contexto?  
  
**Ambiente**  
  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.294

12.1.2410.267

12.1.2502.170

12.1.2506.114  
  
**Solução**  
  
O campo “Qtde de Job’s”, disponível no processo de crédito do trabalhador, define quantas divisões (jobs) serão criadas para processar os lançamentos de forma fracionada.

🔹 O que é “job”?

Um job é uma unidade de execução de um processo automático dentro do RM. Ao fracionar em jobs, o sistema divide o total de colaboradores em partes menores para processar em blocos, melhorando o desempenho e reduzindo risco de falhas em grandes volumes de dados.

🔹 Funcionamento do parâmetro:   
  
Esse parâmetro controla em quantas partes o processo de crédito será dividido.

Se **0 ou 1** - O processo é executado inteiro em uma única vez (sem fracionamento).

Se **maior que 1** - O RM divide o processamento em vários jobs, de acordo com o número informado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33529867194775)

Exemplo:

1. Você tem 1.000 colaboradores para processar crédito.
2. Informa Qtde de Job’s = 5.
3. O sistema divide o processamento em 5 blocos de aproximadamente 200 funcionários cada, processando-os separadamente.

**SAIBA MAIS:**

[Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/releaseview.action?pageId=925361639)

[Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719677&draft=true)
