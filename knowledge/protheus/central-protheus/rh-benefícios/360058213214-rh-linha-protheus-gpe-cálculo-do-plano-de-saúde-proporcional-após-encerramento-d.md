---
article_id: 360058213214
category: RH - Benefícios
content_hash: 79be64a730a7ff866a920a96078d2b7df0efda4414cfddb5f95b8b034098cd28
fetched_at: '2026-06-28T22:44:03.597778+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo do plano de saúde proporcional após encerramento
  do plano
type: support-article
updated_at: '2025-09-29T13:10:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058213214-RH-Linha-Protheus-GPE-C%C3%A1lculo-do-plano-de-sa%C3%BAde-proporcional-ap%C3%B3s-encerramento-do-plano
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32985713175447) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como o sistema proporcionaliza o calculo do plano de saúde após o encerramento do plano?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Na rotina de **Planos Ativos**, foram criados os campos abaixo relacionados ao cálculo proporcional no encerramento do plano.   
Para isso, é necessário cadastrar as verbas referente a diferença [conforme esta documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049761054-RH-Linha-Protheus-GPE-Cadastro-de-Verba-com-ID-base-parte-empresa-diferen%C3%A7a-para-plano-de-sa%C3%BAde-e-odontol%C3%B3gico?source=search)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32985690140823)

**Exemplo:**Titular e dependente terão os seus planos encerrados em 15/06/2025.   
Para o cálculo proporcional ao encerramento, é necessário preencher os campos referente ao **Período Final, Data Fim e Verba de Diferença.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32985713177751)

Desta forma, o cálculo será proporcionalizado de acordo com a **Data Fim** do plano  
Conferência do cálculo de acordo com o plano do funcionário

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32985713177879)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32985690142871)

**Em Vermelho - Verbas 410 e 453:** Desconto do plano para titular e dependente, não houve alterações.   
  
**Em Azul - Verbas 549 e 550:** Base parte empresa referente ao valor do plano, não houve alterações.  
 **Em Verde - Verbas 484 e 485:** Verbas de reembolso/diferença dos dias que não foram utilizados o plano.  
-Verba 484 - Diferença titular (valor desconto titular / dias do mês \* dias que não utilizou o plano)  
50,00 / 30 \* 15 = 25,00  
-Verba 485 - Diferença dependente (valor desconto dependente / dias do mês \* dias que não utilizou o plano)  
50,00 / 30 \* 15 = 25,00  
  
**Em Laranja - Verbas 486 e 488:** Verbas parte empresa referente a diferença dos dias que não foram utilizados o plano.   
-Verba 486 (id 1426) - Base diferença titular (valor parte empresa titular / dias do mês \* dias que não utilizou o plano)  
50 / 30 \* 15 = 25,00  
-Verba 488 (id 1427) - Base diferença dependente (valor parte empresa dependente/ dias do mês \* dias que não utilizou o plano)  
50 / 30 \* 15 = 25,00

**Saiba Mais**[RH - Linha Protheus - GPE - Histórico de planos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051263014-RH-Linha-Protheus-GPE-Hist%C3%B3rico-de-planos-ativos?source=search)  
[RH - Linha Protheus - GPE - Cancelamento do Plano de Saúde/Odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050086373-RH-Linha-Protheus-GPE-Cancelamento-do-Plano-de-Sa%C3%BAde-Odontol%C3%B3gico?source=search)  
[RH - Linha Protheus - GPE - Como excluir/cancelar o cálculo do plano de saúde/odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054180934-RH-Linha-Protheus-GPE-Como-excluir-cancelar-o-c%C3%A1lculo-do-plano-de-sa%C3%BAde-odontol%C3%B3gico?source=search)
