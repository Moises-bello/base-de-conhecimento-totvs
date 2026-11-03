---
article_id: 360034773233
category: eSocial - Cadastros
content_hash: 12c3ae46900e304ae9c0755e932a715c4b505ff75a75a2b02a4cb19471567ed7
fetched_at: '2026-06-28T22:47:14.560225+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Quantidade de gatilhos gerados no S-2230
type: support-article
updated_at: '2025-01-28T15:06:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034773233-RH-RM-FOP-eSocial-Quantidade-de-gatilhos-gerados-no-S-2230
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25069607167639) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**A data inicio e a data término de um afastamento são informadas em um único XML S-2230?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**Existem algumas regras para geração dos gatilhos do S-2230:

1. Caso o afastamento seja inferior a 15 dias, e se no parametrizador não constar marcado a opção **[Não gerar gatilho para afastamentos (P e O) com duração inferior ao definido no MOS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23727530902679-RH-RM-FOP-eSocial-S-2230-N%C3%A3o-gerar-gatilho-para-afastamentos-P-e-O-com-dura%C3%A7%C3%A3o-inferior-ao-definido-no-MOS?source=search)** será gerado um único XML com data início e término;
2. Caso o afastamento afastamento seja por férias (tipo 15), a data início e a data término sempre serão gerados em um único XML.
3. Caso o afastamento seja superior a 15 dias e diferente de férias (tipo 15), será gerado um gatilho para o início e um gatilho para o término do afastamento.

**Saiba mais**Para mais informações acesse:

* [S-2230 - Afastamento Temporário](http://tdn.totvs.com/pages/releaseview.action?pageId=364908488)
