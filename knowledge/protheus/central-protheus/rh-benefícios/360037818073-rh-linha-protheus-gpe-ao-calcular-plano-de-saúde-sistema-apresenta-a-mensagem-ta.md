---
article_id: 360037818073
category: RH - Benefícios
content_hash: 9665de5e531bdc950d17a750ff7383fbf95efc5bcc90dc620c3ad42c6afd3c1c
fetched_at: '2026-06-28T22:44:03.455159+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao calcular plano de saúde sistema apresenta a
  mensagem: Tabela Não cadastrada ou Valores fora da Faixa'
type: support-article
updated_at: '2025-09-15T18:36:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037818073-RH-Linha-Protheus-GPE-Ao-calcular-plano-de-sa%C3%BAde-sistema-apresenta-a-mensagem-Tabela-N%C3%A3o-cadastrada-ou-Valores-fora-da-Faixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34955306592279) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao calcular plano de saúde sistema apresenta mensagem no LOG abaixo:

Ex: Competência calculo plano 04/2019

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048896234)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Verificar como está o castrado da tabela S009 - Planos por Faixa Etária **(Atualizações/ Definições de Calculo/ Manutenção de Tabelas):**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049793973)

Verificar o plano que está cadastrado para o funcionário na rotina de Planos Ativos **(Atualizações/ Benefícios/ Planos de Saúde/ Planos de Saúde Ativos):**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049794313)

Nesse caso a data de nascimento do colaborador é 15/03/1985 - Código 43 é referente a faixa 33 anos.

Na competência 03/2019 o calculo do plano foi feito corretamente, e no mês 04, mês em que o colaborador mudaria de faixa etária, o erro é apresentado.

Sendo assim, entendemos que o problema está no cadastro da Tabela S009, pois se o campo Código estiver um para cada idade, o colaborador estará amarrado a apenas uma faixa etária do plano, o que é errado, e o erro será apresentado quando o funcionário fizer aniversário e mudar de faixa etária.

Logo, o correto é o campo Código ser o mesmo para todo plano exemplo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048903114)

Após ajustar a tabela S009 deve ser ajustado também os planos ativos dos colaborador, assim o sistema fará a validação Código do plano ativo, idade e competência para calcular corretamente o plano de saúde por faixa etária.

**Saiba Mais**[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11223604924695-RH-Linha-Protheus-GPE-Quais-as-documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-plano-de-sa%C3%BAde?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar e calcular assistência médica por faixa etária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018353371-RH-Linha-Protheus-GPE-Como-cadastrar-e-calcular-assist%C3%AAncia-m%C3%A9dica-por-faixa-et%C3%A1ria?source=search)  
[RH - Linha Protheus - GPE - Transferência em Lote do Plano de Saúde/Odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042994494--RH-Linha-Protheus-GPE-Transfer%C3%AAncia-em-Lote-do-Plano-de-Sa%C3%BAde-Odontol%C3%B3gico?source=search)  
[RH - Linha Protheus - GPE - Como funciona a rotina de Planos Saúde Ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056072793-RH-Linha-Protheus-GPE-Como-funciona-a-rotina-de-Planos-Sa%C3%BAde-Ativos?source=search)
