---
article_id: 36690582862999
category: eConsignado (Crédito do Trabalhador)
content_hash: 23a24c741e690b4908a5c5b5c07ee61df5afdbfea0a9b6274f7ab61677d5eb4b
fetched_at: '2026-06-28T22:43:07.380172+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Qual é a ordem que o Sistema utiliza para realizar
  o desconto do eConsignado quando há mais de um contrato e o funcionário não possui
  margem para realizar o desconto de todos os empréstimos
type: support-article
updated_at: '2025-12-01T17:39:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36690582862999-RH-Linha-Protheus-GPE-Qual-%C3%A9-a-ordem-que-o-Sistema-utiliza-para-realizar-o-desconto-do-eConsignado-quando-h%C3%A1-mais-de-um-contrato-e-o-funcion%C3%A1rio-n%C3%A3o-possui-margem-para-realizar-o-desconto-de-todos-os-empr%C3%A9stimos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36690582855959) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Quando os funcionários possuem **mais de 1 empréstimo** consignado e **não há margem** disponível para realizar o desconto de todos os empréstimos, qual é a **ordem** que o sistema utiliza para realizar o **desconto**?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2310

**Solução**  
Os valores dos empréstimos consignados são ordenados de acordo com diferentes critérios.

Para empréstimos **importados**, a ordenação é realizada com base na **data de início do empréstimo** (RUO\_DTINIC).   
Já os valores **lançados manualmente** são organizados pela **data de movimentação** e **número do documento** (RK\_DTMOVI e RK\_DOCUMEN).

**Saiba Mais**  
[RH - Linha Protheus - GPE - Smartview - Relatório de Saldo Devedor econsignado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32755384304535-RH-Linha-Protheus-GPE-Smartview-Relat%C3%B3rio-de-Saldo-Devedor-econsignado)   
[RH - Linha Protheus - GPE - Smartview - Recibo de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33399984340375-RH-Linha-Protheus-GPE-Smartview-Recibo-de-Pagamento)  
Manual [Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=944703898)
