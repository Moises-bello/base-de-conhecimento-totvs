---
article_id: 360021511511
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: fc35cf1c2deee1c1c075b64f0f0fb3cf05f2c6bb9887d78e040b1d466acbdc72
fetched_at: '2026-06-28T22:38:32.800906+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Integração
  GFE: Valor Bruto ou Valor Liquido'
type: support-article
updated_at: '2025-07-14T17:56:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021511511-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Integra%C3%A7%C3%A3o-GFE-Valor-Bruto-ou-Valor-Liquido
---

**Dúvida**O valor da nota que está sendo enviado para o GFE não é o valor total da nota.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- A partir da versão 11.80  
  
**Solução**Hoje no GFE o campo de total da nota é conforme consta no parâmetro abaixo.  
Quando MV\_GFEVLIT = 2  o valor é o  SD2->D2\_TOTAL  
Quando MV\_GFEVLIT = 1  o valor é o  SD2->D2\_VALBRUT

***Obs.***: O parâmetro não tem efeito na Simulação de Frete no Pedido de Vendas.

Essa solicitação se trata de uma melhoria e para inclusão acesse o  [**Portal do Cliente**](http://suporte.totvs.com/). Um espaço que você poderá sugerir as  melhorias, acompanhar a evolução das solicitações já realizadas, comentar, seguir, votar em sugestões feitas por outros clientes e muito mais!  
  
Esse espaço é a nossa [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics).  
Para conhecer mais sobre as suas **funcionalidades**clique **[AQUI](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13)**e assista o nosso vídeo ou acesse nosso artigo **[Central Colaborativa - Funcionalidades Disponíveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Funcionalidades-Dispon%C3%ADveis-na-Central-Colaborativa-TOTVS)​**.

**([DSERFAT-10517)](https://jiraproducao.totvs.com.br/browse/DSERFAT-10517)**

Para mais detalhes da Integração, conheça nossa FAQ Faturamento X GFE no Link abaixo:

**[FAT0244 - Ocorrências da Integração Protheus Faturamento (SIGAFAT) X Protheus Gestão de Frete Embarcador (SIGAGFE)](https://tdn.totvs.com/x/RbMbF)**
