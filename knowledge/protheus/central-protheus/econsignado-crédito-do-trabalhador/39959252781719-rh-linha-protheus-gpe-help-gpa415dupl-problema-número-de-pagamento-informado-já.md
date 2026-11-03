---
article_id: 39959252781719
category: eConsignado (Crédito do Trabalhador)
content_hash: c013f17cd4590fe2778d3b971fd4988d0b4acd019d46b8b7b1ecf8e2defb6ed6
fetched_at: '2026-06-28T22:43:07.295105+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: 'RH - Linha Protheus - GPE - Help: GPA415DUPL Problema: Número de pagamento
  informado já existe'
type: support-article
updated_at: '2026-04-23T19:51:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39959252781719-RH-Linha-Protheus-GPE-Help-GPA415DUPL-Problema-N%C3%BAmero-de-pagamento-informado-j%C3%A1-existe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39959252754967) Tempo aproximado para leitura: **00:01:45 min**  
  
**Ocorrência**  
Ao tentar efetuar a edição de contratos de **eConsignado** na rotina de C**onta Corrente Valores Futuros** (GPEA415), o sistema apresenta a mensagem de erro informando que o **número de pagamento já existe**, impedindo a manutenção do registro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39959252755991)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Causa**  
A inconsistência ocorre devido ao registro incorreto da **ordem** de **pagamentos** no ***grid*** **inferior** da rotina, gravados na tabela **RCK** devido a atualizações pendentes no ambiente no momento do fechamento do período da folha.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39959190678423)  
  
**Solução**  
Para correção do cenário e prevenção de novas ocorrências, deve-se realizar o ajuste dos dados e a atualização do ambiente.  
  
**Passos**

1. Realizar o ajuste manual da ordem de pagamentos diretamente na tabela **RCK** via **banco de dados**, garantindo que a sequência numérica esteja **correta** e **sem duplicidades** para o colaborador afetado;
2. Efetuar a **atualização** do ambiente com o pacote **acumulado** do RH ou patch de correção específico para a rotina GPEA415, visando evitar que o problema ocorra nos próximos fechamentos de folha.

   12.1.2410: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1170810>

   12.1.2510: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1221795>

**Saiba Mais**

[RH - Linha Protheus - GPE - Como controlar as movimentações de Lançamentos Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006568592-RH-Linha-Protheus-GPE-Como-controlar-as-movimenta%C3%A7%C3%B5es-de-Lan%C3%A7amentos-Valores-Futuros)

[RH - Linha Protheus - GPE - Informada verba incorreta nos Lançamentos Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059007914-RH-Linha-Protheus-GPE-Informada-verba-incorreta-nos-Lan%C3%A7amentos-Futuros)

[RH - Linha Protheus - GPE - Situação do eConsignado na rotina de Valores Futuros é alterada para 3-Pago](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36725759783959-RH-Linha-Protheus-GPE-Situa%C3%A7%C3%A3o-do-eConsignado-na-rotina-de-Valores-Futuros-%C3%A9-alterada-para-3-Pago-e-no-campo-Saldo-apresenta-valor-negativo-ap%C3%B3s-o-fechamento-do-per%C3%ADodo-da-folha)
