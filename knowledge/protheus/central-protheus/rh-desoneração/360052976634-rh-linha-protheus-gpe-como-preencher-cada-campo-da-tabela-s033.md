---
article_id: 360052976634
category: RH - Desoneração
content_hash: e09b3f2e638cb2fd5fcbb5beba4b7ac24dd28b50f1addb89176563a1e81cc316
fetched_at: '2026-06-28T22:43:42.271761+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Como preencher cada campo da Tabela S033
type: support-article
updated_at: '2025-08-06T14:16:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052976634-RH-Linha-Protheus-GPE-Como-preencher-cada-campo-da-Tabela-S033
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33986272597911) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como preencher cada campo da Tabela S033 para a desoneração da folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Abaixo segue o que se refere cada campo da **Tabela S033** para desoneração da folha de pagamento na rotina **Manutenção Tabelas,** caminho >**Atualizações** >**Definições de Cálculo** >**Manutenção Tabelas:**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088598853)

**Filial** - Indica a filial que se refere o registro do faturamento.  
**Mês/Ano -** Indica a competência que se refere o registro do faturamento.  
**Sequencia -** Campo sequencial utilizado pelo sistema.  
**Código da Atividade** - Indica o código de atividades, produtos ou serviços, de acordo com a tabela 5.1.1 do EFD - Contribuições.  
**Tipo da Receita -** Indica o tipo do faturamento: “1” - o faturamento refere-se a uma atividade beneficiada pela Lei; “2” - o faturamento refere-se a uma atividade que não é beneficiada pela Lei.  
**Valor Base para Cálculo Base de cálculo** Cálculo: (RECEITA BRUTA - Conteúdo do parâmetro MV\_RECDES).  
**Alíquota** - Alíquota do faturamento que será aplicada sobre o valor do faturamento.  
**Contribuição Devida** - Contribuição previdenciária sobre o faturamento devida. Cálculo: (VALOR x ALÍQUOTA).  
**Valor das Exclusõe**s - Valor das exclusões à base cálculo.  
**Valor das Exportação** - Valor das exportações à base cálculo.  
**Valor dos Impostos** - Valor dos impostos à base cálculo.  
**Conta Contábil -** Conta Contábil à base cálculo.

**Saiba mais:**

[RH - Desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109152-RH-Desonera%C3%A7%C3%A3o)
