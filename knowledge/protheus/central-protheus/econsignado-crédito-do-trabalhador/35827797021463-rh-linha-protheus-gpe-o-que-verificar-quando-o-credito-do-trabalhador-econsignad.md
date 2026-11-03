---
article_id: 35827797021463
category: eConsignado (Crédito do Trabalhador)
content_hash: 89998b411a1cf02ba060b343c352fe9ad2e7ab1c788f41e839beead9654938e3
fetched_at: '2026-06-28T22:43:07.342257+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando o Credito do Trabalhador
  eConsignado for descontado no período indevido.
type: support-article
updated_at: '2026-02-09T18:18:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35827797021463-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-Credito-do-Trabalhador-eConsignado-for-descontado-no-per%C3%ADodo-indevido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35827797016855) Tempo aproximado para leitura: **00:00:30 min**  
  
**Dúvida**  
O que verificar quando o Credito do Trabalhador eConsignado for descontado no período indevido?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Quando ocorrer o calculo do Credito do Trabalhador eConsignado no período incorreto, devemos verificar na rotina **Valores Futuros** em **Atualizações > Lançamentos > Valores Futuros (GPEA110)** o preenchimento do campo **Data Próximo Vencimento,** pois não é validado para o calculo de folha de pagamento o campo Per. Inicio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35830845803671)  
  
O campo Data Próximo Vencimento será preenchido sempre com o 1º dia do mês de lançamento, independente se o lançamento for realizado manualmente na rotina de valores futuros, ou se for importado pela rotina Credito do Trabalhador (GPEM944).

Para que o desconto do eConsignado seja descontado na data correta conforme o campo **Per. Inicio**, o campo **Data Próximo Vencimento** deve ser preenchido com data posterior ao campo **Data de Pagamento da folha** no cadastro de período na rotina **Períodos (GPEA400)**. Esse ajuste é realizado **manualmente** pelo usuário diretamente na rotina Valores Futuros em **Atualizações > Lançamentos > Valores Futuros (GPEA110)**.

**Importante**

Caso o campo **saldo** apresente valor **negativo** e consequentemente com a situação igual a **3-Pago,** será necessário **atualizar o Sistema** conforme links abaixo e aplicar a **Expedição Contínua do RH** (selecione o link relacionado a versão so seu Protheus apenas).  
  
12.1.2210:<https://r.totvs.io/p/1222663> **SOMENTE PARA CLIENTES COM GARANTIA ESTENDIDA**;   
12.1.2310:<https://r.totvs.io/p/1222661> **SOMENTE PARA CLIENTES COM GARANTIA ESTENDIDA**;   
12.1.2410:<https://r.totvs.io/p/1222662> ;   
12.1.2510:<https://r.totvs.io/p/1222664> ;  
  
**Expedição Contínua do RH:** <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO_CONTINUA>

O conteúdo dos campos **Vr. Principal** (RK\_VALORTO) e **Saldo**(RK\_VLSALDO) serão corrigidos no momento que ocorrer **uma nova importação dos empréstimos**.

**Saiba mais:**

[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)

[eConsignado - Credito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)
