---
article_id: 360045344953
category: RH - Lançamentos
content_hash: 58f68d052d1741a1e6b1a9f2a9949b487033b785a08cdac5c31c54146ecb4eba
fetched_at: '2026-06-28T22:43:31.276959+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: 'RH - Linha Protheus - GPE - HELP ATENÇÃO! Problema: data de referência não
  deve ser informada pois a verba não possui configuração para lançamento diário'
type: support-article
updated_at: '2025-04-17T19:18:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045344953-RH-Linha-Protheus-GPE-HELP-ATEN%C3%87%C3%83O-Problema-data-de-refer%C3%AAncia-n%C3%A3o-deve-ser-informada-pois-a-verba-n%C3%A3o-possui-configura%C3%A7%C3%A3o-para-lan%C3%A7amento-di%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:00 min**  
**Dúvida**

O que analisar quando é apresentada a mensagem "HELP ATENÇÃO! Problema: data de referência não deve ser informada pois a verba não possui configuração para lançamento diário" ?

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061648534/mceclip5.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.

**Solução:**Se a verba for uma verba de lançamento diário faça a seguinte verificação :   
  
1. Acesse: Atualizações  > Definições de Cálculo > Verbas (**GPEA040**), Locaize a verba em questão e clique em Alterar.  
  
2. Verifique na aba Geral, como o campo "**Lcto. Diário**" (**RV\_LCTODIA**) configurado .  
A verba tem a opção de configurar com SIM ou Não, caso a verba tenha que ser lançada com Data (Campo **Dt. Refer**. **RGB\_DTREF)**, este campodo cadastro da verba deverá ser preenchido com Sim.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061650314/mceclip6.png)

**Saiba Mais**:

[RH - Lançamentos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781734-RH-Lan%C3%A7amentos)
