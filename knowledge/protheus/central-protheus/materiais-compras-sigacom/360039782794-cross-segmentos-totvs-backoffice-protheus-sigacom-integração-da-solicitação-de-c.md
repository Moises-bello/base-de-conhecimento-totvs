---
article_id: 360039782794
category: Materiais - Compras (SIGACOM)
content_hash: 764f8b5a174528828520beb7f0c7fa963767cf89a30a983149c990431548550e
fetched_at: '2026-06-28T22:41:19.999899+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Integração da Solicitação
  de Compras(MATA110) x Itens para Importação(MATA112) '
type: support-article
updated_at: '2023-08-01T20:59:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039782794-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Integra%C3%A7%C3%A3o-da-Solicita%C3%A7%C3%A3o-de-Compras-MATA110-x-Itens-para-Importa%C3%A7%C3%A3o-MATA112
---

**Dúvida**

Integração da Solicitação de Compras (MATA110) x Itens para Importação (MATA112)?  
  
**Ambiente**

Microsiga Protheus – Compras – A partir da versão 12  
  
**Solução**

Segue exemplo com o passo a passo para essa situação:

1. Habilite o parâmetro **MV\_EASY =** S

2. Na inclusão da Solicitação de Compras preencha os campos Unid. Requis**(C1\_UNIDREQ)**e Cod.Comprador**(C1\_CODCOMP)**e o campo Produto Imp.**(C1\_IMPORT)** = **Sim**conforme exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052847414)

A legenda da solicitação ficará com a cor rosa

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053743273)

3. Acesse a rotina Itens para Importação**(MATA112),**preencha os parâmetros conforme os dados do cadastro da Solicitação de Compras.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052857354)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053751313)

4. Observe que o item da Solicitação de Compras foi carregado com sucesso na rotina de Itens para seleção e importação**(MATA112).**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053744393)

5. Marque o item e selecione o Gerar  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090764314)

6. Ao gerar a SC ficará com a legenda vermelha:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092895953)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
