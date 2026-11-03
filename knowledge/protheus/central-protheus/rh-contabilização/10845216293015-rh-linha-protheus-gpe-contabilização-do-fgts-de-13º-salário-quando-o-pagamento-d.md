---
article_id: 10845216293015
category: RH - Contabilização
content_hash: 5491761e9ecb9aa31496ee1728699aa92a15e14ced41396f607f30d6981d4e10
fetched_at: '2026-06-28T22:43:45.948255+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização do FGTS de 13º Salário quando o
  Pagamento do 13º e Rescisão ocorrem no mesmo mês
type: support-article
updated_at: '2025-07-23T20:14:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10845216293015-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-do-FGTS-de-13%C2%BA-Sal%C3%A1rio-quando-o-Pagamento-do-13%C2%BA-e-Rescis%C3%A3o-ocorrem-no-mesmo-m%C3%AAs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15279014270615) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao Realizar a contabilização da Folha e 13º Salário (Roteiro 131 ou 132), quando o funcionário é desligado no mesmo mês de Pagamento do 13º Salário, o sistema contabiliza duas vezes a verba de FGTS sobre o 13º Salário.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões.  
  
**Causa**Ao calcular a rescisão no mesmo mês de pagamento da 1ª ou 2ª parcela do 13º salário, o sistema mantém a verba de FGTS 13º Salário nos Roteiros 131 ou 132 (Identificador de Cálculo 0109) e apresenta nos cálculos de rescisão uma nova verba com o valor de FGTS de 13º Salário (Identificador de Cálculo 0214).  
Ao realizar a contabilização da Folha de Pagamento e do 13º Salário, o sistema contabilizará as duas verbas, causando duplicidade no valor de FGTS.  
  
**Solução:**

Será necessário configurar no Lançamento Padrão da verba de Identificador de Cálculo 0109, uma regra que valide a situação do funcionário no momento da contabilização (EX: posicionando na SRA e verificando o campo RA\_SITFOLH ==D) , de modo que no cenário apresentado seja desconsiderada no momento da contabilização.

**Observação:** Caso necessite de apoio para configurar o Lançamento Padrão, sugerimos que acione nosso time de HUB para análise e orçamento, uma vez que este atendimento é realizado somente via consultoria.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)

[Página Centralizadora da Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)

[RH - Linha Protheus - GPE - Sistema não realiza contabilização do Décimo Terceiro Salário no mês de dezembro, roteiros 131 - 1ª parcela do 13º e 132 - 2ª parcela de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013810772-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-realiza-contabiliza%C3%A7%C3%A3o-do-D%C3%A9cimo-Terceiro-Sal%C3%A1rio-no-m%C3%AAs-de-dezembro-roteiros-131-1%C2%AA-parcela-do-13%C2%BA-e-132-2%C2%AA-parcela-de-13%C2%BA?source=search)
