---
article_id: 35336380300951
category: Materiais - Compras (SIGACOM)
content_hash: 5eb864b09f0094788f118aa9fedebe547778c8e1744e6622176654bbd9f39021
fetched_at: '2026-06-28T22:41:18.764514+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Habilitar o campo F1_CHVNFE
  para a espécie NFCOM no documento de entrada
type: support-article
updated_at: '2025-10-01T18:20:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35336380300951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Habilitar-o-campo-F1-CHVNFE-para-a-esp%C3%A9cie-NFCOM-no-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35336380265495) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Dúvida**  
**Como habilitar o campo de chave NFE no documento de entrada para a espécie NFCOM ?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Todas as versões  
  
**Solução**  
Por padrão o campo de chave NFE no documento de entrada ( F1\_CHVNFE ) só é habilitado quando as espécies da nota forem SPED e CTE.

Para que o campo seja também habilitado para a nova espécie NFCOM é necessário observar os parâmetros abaixo, no configurador do sistema.

Caminho : CFG -> Ambiente -> Cadastros -> Parâmetros

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35336380268823)

**MV\_DCHVNFE: Informa se deverá digitar a chave da Nfe/Cte caso a espécie seja SPED/CTE e Form.Próprio=NÃO**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35336397318551)

**MV\_CHVESPE: Validar outras espécies que não sejam SPED/CTE.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35336397319447)

Ao acessar a rotina de documento de entrada, ao preencher a espécie NFCOM, o campo chave NFE na aba Informações da Danfe,  será habilitado, para que a chave possa ser preenchida.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35336380276759)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
