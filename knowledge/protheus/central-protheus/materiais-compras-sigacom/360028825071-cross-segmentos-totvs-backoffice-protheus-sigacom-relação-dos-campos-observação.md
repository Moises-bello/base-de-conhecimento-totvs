---
article_id: 360028825071
category: Materiais - Compras (SIGACOM)
content_hash: 70cb3c5f61a424ecef3962d6fec0bf05736127eb47d085545680abcba031a9a3
fetched_at: '2026-06-28T22:41:24.373972+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Relação dos campos
  Observação ( C7_OBS e C7_OBSM ) no relatório MATR110
type: support-article
updated_at: '2022-01-11T19:46:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028825071-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rela%C3%A7%C3%A3o-dos-campos-Observa%C3%A7%C3%A3o-C7-OBS-e-C7-OBSM-no-relat%C3%B3rio-MATR110
---

**Dúvida**

Relação dos campos Observação ( C7\_OBS e C7\_OBSM ) no relatório MATR110  
  
**Ambiente**

Protheus – SIGACOM – A partir da versão 12  
  
**Solução**

Referente a utilização desses campos ( C7\_OBS e C7\_OBSM ), é necessário que esteja com a a rotina MATR110 atualizada com fonte padrão.

O campo observações do MATR110 será preenchido com as informações do campo C7\_OBSM. Foi criado este campo do tipo "Memo" para permitir o preenchimento do maior número de caracteres (o limite passou de 30 para 50 caracteres).

Para utilizá-lo, é necessário marcar a opção "Browse" no SIGACFG. Recomendamos também que desabilite a visualização campo C7\_OBS para evitar que os usuários preencham as informações neste campo e ocorram conflitos de informações durante a impressão do registro.

É indicado utilizar apenas um dos campos, ou seja C7\_OBS ou C7\_OBSM.

Caso possua conteúdo em um dos campos antes de executar o ajuste de usado e browse no configurador, consulte a informação na tabela para não apresentar divergência na impressão do relatório.

***Saiba Mais :***

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
