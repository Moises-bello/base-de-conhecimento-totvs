---
article_id: 12503683907479
category: RH – DIRF
content_hash: 7494d3796824e2dd7ba6225e17809829ac0e0a95bfaee49baafe263a8e9453f7
fetched_at: '2026-06-28T22:44:06.753867+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao executar Diagnóstico de base na DIRF é gerado
  log com mensagem: Valor do histórico de movimento não confere com valor do histórico
  de plano de saúde'
type: support-article
updated_at: '2025-08-06T20:49:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12503683907479-RH-Linha-Protheus-GPE-Ao-executar-Diagn%C3%B3stico-de-base-na-DIRF-%C3%A9-gerado-log-com-mensagem-Valor-do-hist%C3%B3rico-de-movimento-n%C3%A3o-confere-com-valor-do-hist%C3%B3rico-de-plano-de-sa%C3%BAde
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21025533249175) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao executar Diagnóstico de base na DIRF é gerado log com mensagem: Valor do histórico de movimento não confere com valor do histórico de plano de saúde:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12503226531223)  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Há diferenças entre os valores de plano de saúde descontados em folha e histórico de cálculo de plano.  
  
**Solução**Deverá ser feita conferência entre o Histórico de cálculo do plano de saúde e valores de plano de saúde descontados em folha, pois os valores entre as tabelas não batem ou os cadastros relacionados ao plano de saúde estão divergentes.  
  
Para validar se de fato o valores estão diferentes entre acumulado funcionário (tabela SRD) e acumulado cálculo plano de saúde (tabela RHS e RHP), siga as orientações abaixo:

1. Gere o relatório de Acumulado plano de saúde GPER014 ([RH - Linha Protheus - GPE - Como incluir a rotina Acumulados de Plano de Saúde no menu do Sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420942003351))

2. Após isso, gere a **ficha financeira** do funcionário, pelo caminho **>Relatórios >Lançamentos >Ficha Financeira**, e compare os valores descontados em folha com o relatório de acumulado plano de saúde.

Se os valores estiverem diferentes, faça o ajuste dos valores que de fato foram descontados em Informações Complementares na rotina **Manutenção arquivo**, pelo caminho **>Miscelânea >Dirf >Manutenção Arquivo**, alterando o funcionário, clicando em **>Outras Ações >Informações complementares**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12503563872023)  
  
Se os valores estiverem iguais entre os relatórios, faça a conferência conforme documentação abaixo, pois algum cadastro relacionado ao plano de saúde esta inconsistente:

[RH - Linha Protheus - GPE - Como realizar a conferência do plano de saúde, coparticipação e reembolso para a DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022836972)

**Saiba mais**  
[RH - Linha Protheus - GPE - Quando os planos de saúde são informados manualmente para o funcionário o que fazer para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021563052)
