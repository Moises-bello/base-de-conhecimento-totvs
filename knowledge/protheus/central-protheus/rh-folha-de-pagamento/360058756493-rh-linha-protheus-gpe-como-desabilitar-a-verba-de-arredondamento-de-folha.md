---
article_id: 360058756493
category: RH - Folha de Pagamento
content_hash: cca04d83008362bc4acf04e645dfc7e876ae0119488bd37f57de564eaa318990
fetched_at: '2026-06-28T22:44:13.363667+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como desabilitar a verba de arredondamento de Folha
type: support-article
updated_at: '2025-03-27T20:13:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058756493-RH-Linha-Protheus-GPE-Como-desabilitar-a-verba-de-arredondamento-de-Folha
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18886585596823) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como desabilitar as verbas de arredondamento de Folha?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Necessário deixar todos os parâmetros descritos abaixo zerados, pois o sistema entende que se não deve ter arredondamento na Folha de pagamento, Férias, 13º e Adiantamento.

Para configurar o parâmetro acesse o **Configurador SIGACFG** em **Ambiente > Cadastros > Parâmetros (CFGX017)** e pesquise pelos parâmetros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30979043446167)  
  
Configure com 0 os parâmetros, dessa forma o sistema não irá mais calcular o arredondamento na Folha de pagamento, Férias, 13º e Adiantamento.

Valide também se os mnemônicos descritos abaixo também estão zerados. Em **Atualizações > Definições de Cálculo > Mnemônicos (GPEA300)** pesquise pelos mnemônicos e configure com 0. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30979043450647)

**Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
