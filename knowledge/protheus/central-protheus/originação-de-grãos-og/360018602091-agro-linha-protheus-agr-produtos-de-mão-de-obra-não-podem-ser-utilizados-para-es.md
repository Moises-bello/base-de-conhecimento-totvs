---
article_id: 360018602091
category: Originação de Grãos (OG)
content_hash: 5434405e1de85d5e030187f1bedf566578c9e60589aa0b7ef5ea435d777f0106
fetched_at: '2026-06-28T22:45:44.728934+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Produtos de mão-de-obra não podem ser utilizados
  para esta operação
type: support-article
updated_at: '2024-01-16T18:11:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018602091-Agro-Linha-Protheus-AGR-Produtos-de-m%C3%A3o-de-obra-n%C3%A3o-podem-ser-utilizados-para-esta-opera%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20619363102999)*** Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Nas rotinas de **OGA250** - **Romaneio com Pesagem**e **OGA245** - **Ordem de Trânsito** ao gerar a Nota Fiscal é exibida a mensagem: **AJUDA:NAOMVMOD Produtos de Mão-de-Obra não podem ser utilizados para esta operação**.  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Esse incidente ocorre quando é incluído um **Documento de Entrada** vinculando um produto mão-de-obra. Os produtos **MOD** são identificados quando o **código** é **iniciado pela sigla MOD+CC - Centro de Custo,** ou se os campos **B1\_CCCUSTO e/ou B1\_GCCUSTO** estiverem preenchidos.  
A rotina não aceita esse tipo de produto devido ao seu custo ser obtido somente por meio do rateio dos movimentos vinculados a **Ordem de Produção** **-** **SD3**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Acesse o **cadastro do Produto** e verifique se ele é **mão-de-obra**. Caso seja, não será possível utilizá-lo para a geração de **Nota Fiscal**;

**2.** Verifique se o código do produto é formado pela sigla **MOD + Centro de Custo**, pois isso identifica um produto como Mão-de-Obra;

**3.** Verifique se os campos **B1\_CCCUSTO e B1\_GCCUSTO** estão preenchidos, pois o preenchimento destes campos faz com que o produto seja considerado mão-de-obra. Caso precise que a informação de centro de custo esteja no cadastro de produto, informar na primeira aba campo **B1\_CC-centro de custo** e campo e **B1\_CONTA-conta contábil**.
