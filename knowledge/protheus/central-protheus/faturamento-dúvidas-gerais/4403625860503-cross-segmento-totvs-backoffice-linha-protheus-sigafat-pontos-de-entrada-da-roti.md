---
article_id: 4403625860503
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 83893340a6944b0ec3707d3afa4ba9a2ec5e0becfbb75ec1dcad68361d40563f
fetched_at: '2026-06-28T22:38:32.848614+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de Entrada
  da rotina FATA300
type: support-article
updated_at: '2025-01-10T19:56:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403625860503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-Entrada-da-rotina-FATA300
---

**Dúvida**Quais são os pontos de entrada existentes na rotina Oportunidade de Venda (**FATA300**)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Solução**Abaixo a lista com os pontos de entrada existentes na rotina Oportunidade de Venda, e seus endereços de documentação no TDN:

* [**FT300D1ST** - Inclusão de novos status para o campo AD1\_STATUS](https://tdn.totvs.com/x/UeMGDg)
* [**FT30COR** - Alteração das cores de legenda do Browse de Oportunidade de Vendas](https://tdn.totvs.com/x/6wGQC)
* [**FT300FILBW** - Filtra oportunidade de venda no BROWSE de oportunidades](https://tdn.totvs.com/x/0JKNBw)
* [**CRMBRWVIEW** - Substituição das Visões Padrão do CRM](https://tdn.totvs.com/x/NT6WDg)
* [**FT300CPV** - Campos a serem exibidos nas visões da oportunidade de venda](https://tdn.totvs.com/x/Hx6TEg)
* [**FT300ORC** - Executado na janela de alteração e visualização](https://tdn.totvs.com/x/DQKQC)
* [**FT300BUT** - Adiciona botões à tela de oportunidade](https://tdn.totvs.com/x/5pKNBw)
* [**FT30LEG** - Adiciona Legenda na tela de Legendas](https://tdn.totvs.com/x/8AGQC)
* [**FT300CPO** - Campos a serem exibidos na grid dos produtos/categorias das Oportunidades de Venda](https://tdn.totvs.com/x/FCmTEg)
* [**FT300MNU** - Adiciona opções no MenuDef() da Oportunidade de Vendas](https://tdn.totvs.com/x/xgGQC)
* **[FT300TDOK - Manipula a validação de todo o formulário da oportunidade de venda](http://tdn.totvs.com/pages/releaseview.action?pageId=126718689)**
* **[FT300PV- Geração do Pedido de Venda](https://tdn.totvs.com/pages/releaseview.action?pageId=150634843)**
* **[FT300GRA (Versão 12) - Após a gravação da Oportunidade de Vendas.](https://tdn.totvs.com/pages/viewpage.action?pageId=143655394)**

**Obs.: Para pontos de entrada pelo CRMA110:** A rotina da **Oportunidade de Venda** (**FATA300**) é executada também a partir do menu do módulo **SIGACRM** através da sua chamada realizada pelo programa **CRMA110**. Porém, quando isso ocorre, o *array* disponibilizado ao ponto de entrada não conterá as opções padrões próprias do módulo **SIGACRM**. Mesmo assim, as opções que forem inseridas através deste ponto de entrada também estarão disponíveis no *browse* da rotina de **Oportunidade de Venda** pelo módulo **SIGACRM**.
