---
article_id: 34778038538391
category: Meu RH - Pagamento
content_hash: 77a162df871a318ae7aa991a6a85fb75f15c5e68f7062102a4da57a0abaac0a3
fetched_at: '2026-06-28T22:47:33.849876+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: 'RH - RM - Meu RH - Erro ao abrir o envelope de pagamento: Year, Month, and
  Day parameters describe an un-representable DateTime'
type: support-article
updated_at: '2025-09-08T14:14:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34778038538391-RH-RM-Meu-RH-Erro-ao-abrir-o-envelope-de-pagamento-Year-Month-and-Day-parameters-describe-an-un-representable-DateTime
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34777993509399) Tempo aproximado para leitura: **00:02:05 min**  
  
**Ocorrência**  
Quando acessar a tela de envelope de pagamento no Meu RH, é retornada a mensagem : **Ocorreu um erro ao efetuar a leitura do registro: Year, Month, and Day parameters describe an un-representable DateTime.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Este incidente ocorre pois na Ficha Financeira do colaborador, no mesmo mês e período que está sendo acessado no Meu RH, não estão com a informação de Mês e Ano preenchidas.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse modulo Folha de Pagamento / aba Administração de Pessoal / Funcionários / Localize e selecione o Funcionário / clique no ícone da Ficha financeira:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34777993510935)

2. Selecione e Edite o período da Ficha Financeira que está sendo acessado e realize o preenchimento das informações **Ano Caixa** e **Mês Caixa**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34778038522263)

3. Acesse novamente o envelope através do Meu RH que o erro deixará de ser apresentado.
