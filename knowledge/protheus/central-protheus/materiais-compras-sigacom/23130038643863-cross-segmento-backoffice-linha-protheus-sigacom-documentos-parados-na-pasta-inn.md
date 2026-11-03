---
article_id: 23130038643863
category: Materiais - Compras (SIGACOM)
content_hash: 705d82fd080c0adc2185baf99d6785a79bbd9ffc437f6a86b49d203ce84f1365
fetched_at: '2026-06-28T22:41:10.584937+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Documentos parados
  na pasta INN.
type: support-article
updated_at: '2024-04-29T15:02:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23130038643863-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Documentos-parados-na-pasta-INN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23130076623767) Tempo aproximado para leitura: **00h02 min****Ocorrência**Documentos parados na pasta INN.  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12

**Causa**A Nomenclatura do arquivo XML está maior do que o tamanho do campo **CKO\_ARQXML.**

**Solução**

O campo **CKO\_ARQXML**, que armazena o nome do arquivo XML na tabela **CKOCOL**, está limitado a 60 caracteres por padrão. No entanto, o nome do arquivo XML está ocupando mais de 60 caracteres, o que está causando a perda de parte do nome do arquivo e impedindo sua importação correta.

Para resolver esse problema, será necessário aumentar o tamanho do campo **CKO\_ARQXML** para **70 caracteres.** Isso permitirá que o nome completo do arquivo XML seja armazenado sem perdas. Esse aumento pode ser feito diretamente no módulo de configurador, uma vez que o campo é do tipo caracter e não terá impacto significativo.

Após aumentar o tamanho do campo para 70 caracteres, verifique se o problema foi resolvido e se os arquivos XML estão sendo importados corretamente para o sistema.

***Saiba Mais :***

* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
