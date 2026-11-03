---
article_id: 36279490124567
category: eConsignado (Crédito do Trabalhador)
content_hash: 8f2ebf3ef310e4ffe5d5fcd78887709b2f31012f152898cba0973879dd75d9ce
fetched_at: '2026-06-28T22:43:07.239485+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Como quitar um débito de empréstimo consignado
type: support-article
updated_at: '2025-11-12T18:04:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36279490124567-RH-Linha-Protheus-GPE-Como-quitar-um-d%C3%A9bito-de-empr%C3%A9stimo-consignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36279490113687) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como quitar um débito de empréstimo consignado?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal -  A partir da Versão 12.1.17

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Localize o cadastro do funcionário que possui o empréstimo consignado;
2. Suspenda o parcelamento atual do empréstimo através da rotina Conta Corrente Valores Futuros

   [Rotina Conta Corrente Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006568592-RH-Linha-Protheus-GPE-Como-controlar-as-movimenta%C3%A7%C3%B5es-de-Lan%C3%A7amentos-Valores-Futuros)
3. Ou ao realizar o fechamento do período, o sistema automaticamente classificará a situação como suspensa. Consequentemente, ao importar o mês subsequente, o funcionário não será incluído no arquivo enviado pelo banco, resultando na interrupção do desconto do empréstimo.

**Importante**  
**Caso o arquivo disponibilizado no Emprega Brasil do mês subsequente ainda apresente valores pendentes, o funcionário deverá contatar a Instituição Financeira para a devida regularização.**  
**No Sistema ajuste o lançamento para Suspenso na rotina de Conta Corrente Valores Futuros.**

**Saiba Mais:**

[RH - Linha Protheus - GPE - Econsignado - Informações e atualizações sobre Credito Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-Econsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-Trabalhador-MP1-292-2025)

[RH - Linha Protheus - GPE - Verba de desconto do econsignado não é apresentado na folha de pagamento - Econsignado MP(1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32741678546199-RH-Linha-Protheus-GPE-Verba-de-desconto-do-econsignado-n%C3%A3o-%C3%A9-apresentado-na-folha-de-pagamento-Econsignado-MP-1-292-2025)
