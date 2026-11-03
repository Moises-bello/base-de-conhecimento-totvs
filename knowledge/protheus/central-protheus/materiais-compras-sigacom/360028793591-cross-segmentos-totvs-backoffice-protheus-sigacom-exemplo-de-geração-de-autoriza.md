---
article_id: 360028793591
category: Materiais - Compras (SIGACOM)
content_hash: ac652b17ce358e3893f0264a1c865bc3097c09e756d781bb7ea290d939d1d321
fetched_at: '2026-06-28T22:41:17.714210+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de geração
  de Autorização de Entrega Prevista a partir da rotina MRP
type: support-article
updated_at: '2025-01-02T13:08:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028793591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-gera%C3%A7%C3%A3o-de-Autoriza%C3%A7%C3%A3o-de-Entrega-Prevista-a-partir-da-rotina-MRP
---

**Dúvida**

Exemplo de geração de Autorização de Entrega Prevista a partir da rotina MRP  
  
  
**Ambiente**

Protheus – Gestão de Compras– A partir da versão 12

**Solução**

**1- MATA010 (Produto)**

Cadastrar o produto com:

* Contrato = Ambos
* Ponto de pedido
* Forn. Padrão
* Loja padrão.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029343551)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029342852)

**2- MATA125 (Contrato de Parceria)**

Cadastrar o contrato de parceria para o produto que possui o Forn. Padrão e Loja padrão.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029343352)

   
**3- MATA712 (MRP)**

Executar o MRP. Parametrizar para considerar o ponto de pedido, apagar OPs/SCs previstas e Tipo de OPs/SCs para geração como Prevista. Gerar as OPs/SCs.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029345332)

***Obs:***

Para dúvidas sobre os parâmetros e a rotina do MRP, orientamos a verificaçao junto a Equipe do Suporte à Manufatura do módulo SIGAPCP (Planejamento e Controle da Produção)

**4- MATA653 (AEs)**

Para o produto que possui o contrato de parceria, deve ser gerado uma autorização de entrega.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029345812)

Lembrando que trata-se de um exemplo de configuração e devem ser considerado as datas nos perguntes.

***Saiba Mais :***

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
