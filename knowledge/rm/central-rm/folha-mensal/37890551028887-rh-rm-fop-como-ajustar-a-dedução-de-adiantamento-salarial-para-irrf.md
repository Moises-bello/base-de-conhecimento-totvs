---
article_id: 37890551028887
category: Folha Mensal
content_hash: 52f0e61e19a757c848214d5a0fb69f2a89482b8bb4457885c772572acb3a2121
fetched_at: '2026-06-28T22:46:57.985468+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Como ajustar a dedução de adiantamento salarial para IRRF
type: support-article
updated_at: '2026-01-23T19:21:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37890551028887-RH-RM-FOP-Como-ajustar-a-dedu%C3%A7%C3%A3o-de-adiantamento-salarial-para-IRRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37890587792919) Tempo aproximado para leitura: 00:00:43 min  
  
**Ocorrência**  
No módulo Folha de Pagamento, o sistema não estava deduzindo corretamente o adiantamento salarial na base dos rendimentos tributáveis para o IRRF conforme a nova regra da LEI 15.270.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:  
  
12.1.2502.251  
12.1.2506.209  
12.1.2510.137 e superiores  
  
**Causa**  
Esse incidente ocorre, pois o evento de adiantamento salarial **Código de calculo 19** estava marcado como **"Dedutível IRRF"**, quando deveria estar com a incidência **"Estorna IRRF"**, o que impacta na base de cálculo do imposto.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o módulo de Eventos de Folha de Pagamento;  
  
2. Localize o evento referente ao adiantamento salarial **Código de calculo 19**;  
  
3. Verifique a configuração de incidência do evento;  
  
4. Altere a incidência de **"Dedutível IRRF"** para **"Estorna IRRF"**;  
  
5. Salve as alterações e recalcule a folha para verificar se o cálculo ficou correto.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37890550997271)  
  
**Lembrete**

> **A marcação do campo Valor Dedutível ou Estorna IRRF é de responsabilidade do usuário, sendo que o valor dedutível refere-se ao que é dedução legal e o valor que estorna é o valor que abate na base do imposto de renda, por exemplo falta.**

Para maiores informações:[**Código de Cálculo 19 - Adiantamento**](https://tdn.totvs.com/pages/releaseview.action?pageId=452719767)

**Saiba mais**

* [RM - FOP - Novo Cálculo IRRF - LEI 15.270](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37093881771159-RH-RM-FOP-Novo-C%C3%A1lculo-IRRF-LEI-15-270)
