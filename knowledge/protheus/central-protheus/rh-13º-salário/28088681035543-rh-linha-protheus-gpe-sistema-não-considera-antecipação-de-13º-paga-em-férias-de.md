---
article_id: 28088681035543
category: RH - 13º salário
content_hash: 5f670d807544a2f4c2e6c0e4de85aa05a82cbb33b34e4eb60f5d57f464e6e548
fetched_at: '2026-06-28T22:44:01.645494+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não considera antecipação de 13º paga em
  férias dentro do mesmo mês e calcula valor de pagamento novamente
type: support-article
updated_at: '2025-08-15T19:16:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28088681035543-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-considera-antecipa%C3%A7%C3%A3o-de-13%C2%BA-paga-em-f%C3%A9rias-dentro-do-mesmo-m%C3%AAs-e-calcula-valor-de-pagamento-novamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28088693343383) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao calcular a Primeira Parcela de 13º Salário, o Sistema não considera antecipação paga em férias dentro do mesmo mês e calcula valor de pagamento novamente  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Para calcular o 13º salário, o Sistema valida as tabelas **SRD** - **acumulados** (períodos fechados), **RGB** - **parâmetros** (tabela de transição, ou seja, verbas de outros roteiros integrados, verbas lançadas/ informadas manualmente pelo usuário ou que foram geradas pelo fechamento) e **SRC** - **Movimento atual** (valores da folha que está sendo calculada ainda em aberto) se existem dados do id **0022 - 1ª Parcela de 13º Salário.**

Como as férias **não** tinham sido **integradas** na folha, o sistema **não** tem referência que o valor já foi pago nas férias, e calcula novamente.  
  
**Solução**Para que o Sistema entenda a antecipação do 13º nas férias, é necessário seguir os seguintes passos:  
  
1. Faça o cancelamento do cálculo do 13º pela rotina de Cancelamento no menu **Miscelânea > Cálculos > Cancelamento de Cálculos**.  
  
2. Após o cancelamento, realize a integração do roteiro FER pelo menu **Miscelânea > Cálculos > Integrações.**  
3. **Recalcule** o roteiro **131** - 1ª parcela de 13º Salário.  
  
Desta forma, o valor pago em férias anteriormente será considerado e não deve ser gerado provento para este funcionário.

**Saiba Mais**

[Artigos RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio?page=1#articles)

[RH - Linha Protheus - GPE - 13º Parcela Única](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057320354-RH-Linha-Protheus-GPE-13%C2%BA-Parcela-%C3%9Anica)

[RH - Linha Protheus - GPE - Como antecipar o 13º nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006362581-RH-Linha-Protheus-GPE-Como-antecipar-o-13%C2%BA-nas-f%C3%A9rias)
