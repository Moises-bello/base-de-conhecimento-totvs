---
article_id: 360017423492
category: Materiais - Compras (SIGACOM)
content_hash: 0eb99ecae2787a70cd7ffd821cdace3cb2935f4e3262ddb2cc6490dc94c5b50e
fetched_at: '2026-06-28T22:41:09.052771+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não permite Personalizar
  os relatórios de Itens das Notas Fiscais ( MATR090 ) e Relação das Notas Fiscais
  ( MATR080 )
type: support-article
updated_at: '2025-03-10T12:50:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017423492-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-permite-Personalizar-os-relat%C3%B3rios-de-Itens-das-Notas-Fiscais-MATR090-e-Rela%C3%A7%C3%A3o-das-Notas-Fiscais-MATR080
---

**Dúvida**

Ao tentar personalizar os relatórios de Itens das Notas Fiscais (MATR090) e Relação das Notas Fiscais (MATR080), o sistema não permite, apresentando os campos em cinza, sem possibilidade de ajuste.

MATR090

![1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360012954551/1.JPG)

**Ambiente**Protheus – Compras – A partir da versão 12  
  
  
**Solução**

Estes relatórios, por conceito do sistema, não podem de fato serem personalizados, pois além de serem sumarizado (utiliza variáveis para impressão), também utilizam QUERY com UNION (para melhoria de performance).

Ocorre também que novos campos não podem ser incluídos na personalização do relatório pois podem afetar o resultado e por meio disso foi bloqueado para que não seja gerado com informações equivocadas.

Caso haja necessidade, poderá baixar o fonte dos relatórios do Portal do Cliente, pois encontra-se disponível para download para livre personalização. Abaixo link de artigo com instruções.

***Saiba Mais :***

[MP - SIGACOM - Fontes de Relatórios de Compras para personalização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022534771-MP-SIGACOM-Fontes-de-Relat%C3%B3rios-para-personaliza%C3%A7%C3%A3o-Compras)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
