---
article_id: 360018337811
category: FATURAMENTO - RELATÓRIOS
content_hash: 42cb18d2db4edbc4972107f29653cd1c00bbc9e33c8e0ce75ecc11554a261410
fetched_at: '2026-06-28T22:38:22.874980+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Dedução de PIS
  e COFINS no relatório MATR590 através do parâmetro MV_PAR015
type: support-article
updated_at: '2023-02-03T18:12:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018337811-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Dedu%C3%A7%C3%A3o-de-PIS-e-COFINS-no-relat%C3%B3rio-MATR590-atrav%C3%A9s-do-par%C3%A2metro-MV-PAR015
---

**Dúvida**

Dedução de PIS e COFINS no relatório MATR590 através do parâmetro MV\_PAR015.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Em algumas ocasiões os valores do Pis e Cofins não são listados no relatório MATR590, mesmo o parâmetro MV\_PAR015 estando configurado para deduzir o PIS/COFINS, isso ocorre, por que a  pergunta 15 - "Deduz PIS, COFINS e ICMS?" do relatório **MATR590** - "Faturamento por Cliente" apresenta como comportamento padrão e esperado deduzir os tributos que foram somados ao total do documento, ou seja, cobrados por fora, sendo que o pergunte foi criado para exclusão dos valores de PIS e COFINS ST.  
  
O PIS e COFINS Apuração, tributo incidente sobre a receita **não será deduzido** ao do valor apresentado quando a configuração do documento fiscal somar este valor ao total do documento.

Para que o  relatório "Faturamento por cliente (MATR590)" respeite o conteúdo do parâmetro MV\_PAR15 e deduza o imposto de pis/cofins do campo vl. s/ imposto é necessário alimentar os campos **SF4->F4\_AGRPIS e SF4->F4\_AGRCOF**  com conteúdo sim e campo **SF4->F4\_PSCFST** em branco ou como não.

Se a necessidade for que o relatório apresente o valor líquido da operação, para este caso, somente com a evolução de produto por sugestão de melhoria, que pode ser efetuada diretamente através da central colaborativa do portal do cliente, opção melhorias: **<https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br>**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060099654/mceclip0.png)
