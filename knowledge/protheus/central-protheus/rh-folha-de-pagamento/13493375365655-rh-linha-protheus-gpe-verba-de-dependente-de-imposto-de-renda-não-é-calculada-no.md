---
article_id: 13493375365655
category: RH - Folha de Pagamento
content_hash: f4de7fb2597789a2d486861a23347870d731e0bc9d19dbd88abb344662196239
fetched_at: '2026-06-28T22:44:16.408550+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Verba de dependente de imposto de renda não é calculada
  nos roteiros
type: support-article
updated_at: '2024-09-09T19:14:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13493375365655-RH-Linha-Protheus-GPE-Verba-de-dependente-de-imposto-de-renda-n%C3%A3o-%C3%A9-calculada-nos-roteiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26236166106135) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Verba de dependente de imposto de renda não é calculada nos roteiros da folha, férias, rescisão ou 13º mesmo com o cadastro de dependente válido para dependente de IR.  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Tabela S002 da rotina manutenção tabelas preenchida de forma errada.  
  
**Solução**1. Entre na rotina **Manutenção tabelas** pelo caminho **>Atualizações >Definições cálculos >Manutenção tabelas**;

2. Na **Tabela S002**, valide se as colunas Dedução Dependente e limite dependente estão preenchidas, pois se não tiver valor do dependente ou a coluna Limite dependente estiver com 00, o sistema não irá calcular as verbas de dependente de IR:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13493238414359)

**Saiba mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como cadastrar dependente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411314686231)
