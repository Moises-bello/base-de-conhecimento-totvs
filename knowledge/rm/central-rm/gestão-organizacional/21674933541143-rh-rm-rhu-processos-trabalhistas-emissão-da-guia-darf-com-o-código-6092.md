---
article_id: 21674933541143
category: Gestão organizacional
content_hash: 3a9ba22ade83b52bc0a5489f606b58bdcfd5878fb12e4622c7303a53dd04da9e
fetched_at: '2026-06-28T22:47:22.268213+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Processos Trabalhistas: Emissão da Guia DARF com o código
  6092'
type: support-article
updated_at: '2025-12-16T17:12:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21674933541143-RH-RM-RHU-Processos-Trabalhistas-Emiss%C3%A3o-da-Guia-DARF-com-o-c%C3%B3digo-6092
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21674933526039) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como deve ser feito a emissão do DARF para o DCTFWeb no código 6092 para envio dos Tributos (S-2501)?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263, 12.1.2205.211, 12.1.2209.155 e superiores.**  
  
**Solução**

Em casos onde houve Recolhimento dos tributos feito pela justiça do trabalho, deve ser enviado o evento S-2500, mas não deve ser enviado o evento S-2501, pois não há DCTFWeb.

Quando o recolhimento dos tributos é efetuado pela Justiça do Trabalho ela utiliza um DARF comum com código 6092 de uso exclusivo da Justiça do Trabalho. Cabe à Justiça a decisão de realizar o recolhimento dos tributos pelo contribuinte ou se o recolhimento deve ser feito diretamente pelo próprio contribuinte.

Sendo assim, o código DARF 6092 é feito pela justiça, pois o pagamento é feito direto. Se for esse o caso não é preciso enviar o evento S-2501, somente o S-2500 para alimentação no CNIS (INSS).

Caso tenha dúvidas quanto a geração da Guia DARF neste código ou outras dúvidas relacionadas a este processo, orientamos que valide juntamente com o suporte do eSocial do Governo.

[RH - RM - FOP - eSocial - Contato com o Governo para dúvidas sobre os eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432)

**Saiba mais**

Para maiores informações sobre os cadastros, acesse os links abaixo:

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)

- [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
