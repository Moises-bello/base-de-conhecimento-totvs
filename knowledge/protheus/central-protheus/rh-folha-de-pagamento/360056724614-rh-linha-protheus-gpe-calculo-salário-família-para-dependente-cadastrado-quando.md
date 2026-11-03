---
article_id: 360056724614
category: RH - Folha de Pagamento
content_hash: f5314fe52c57bd908086cd01696024ad0873e36794bae6416e5caf0460cf9268
fetched_at: '2026-06-28T22:44:12.142192+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo salário família para dependente cadastrado
  quando não há limite de idade
type: support-article
updated_at: '2025-08-12T13:31:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056724614-RH-Linha-Protheus-GPE-Calculo-sal%C3%A1rio-fam%C3%ADlia-para-dependente-cadastrado-quando-n%C3%A3o-h%C3%A1-limite-de-idade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26354283229079) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Como o sistema valida o calculo salário família quando o dependente cadastrado não há limite de idade?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para dependentes que não há limite de idade para considerar o pagamento do salário família é necessário a configuração no cadastro de dependentes: **Atualizações > Funcionários > Dependentes (GPEA020),** no campo **Tipo Dep. IR** selecionar a opção **1. s/Lim. Idade:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098583193)

Realizar o calculo da folha, gera o valor para o pagamento do salário família para o dependente:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098583233)

**Obs.:** A tabela S003 na rotina manutenção de tabelas em **Atualizações > Definições de Cálculos > Manutenção de tabelas (GPEA320)** deve constar o cadastro para a validação no momento do cálculo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098583493)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
