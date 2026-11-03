---
article_id: 13661762762263
category: Financeiro - Contas a Receber
content_hash: dc7093aea7d7f2f4617139bec6698c606dae35feebd08472cf960468010f53f4
fetched_at: '2026-06-28T22:38:13.967548+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA060 - RECNO Não
  existem registros no arquivo em pauta
type: support-article
updated_at: '2023-12-12T19:02:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13661762762263-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA060-RECNO-N%C3%A3o-existem-registros-no-arquivo-em-pauta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19785680406167) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**

Ao tentar colocar um registro em borderô pela rotina FINA060, apresenta o mensagem de HELP: **RECNO Não existem registros no arquivo em pauta**

**![RECNO.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/13661396301207)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**

Verificar a situação de carteira em que o registro se encontra.

**Exemplo:** Caso o registro esteja na situação 0, acesse a rotina "**FINA022 - Situação de Cobrança**" e encontre a situação, e caso o campo esteja com o conteúdo "**Situação PDD = SIM" (FRV\_SITPDD = 1**), irá apresentar a mensagem RECNO, pois essa situação está configurada para "**Provisão de devedores Duvidosos**"

**Solução 01**

Alterar o campo "**Situação PDD = Não**" (**Provisão de devedores Duvidosos**) da situação de carteira que esse título se encontra.

**Solução 02**

Habilitar NORUN e avaliar utilização de pontos de entrada que podem impactar no processo.

Ex: Geração de borderô poderá ser impedida se houver a obrigatoriedade de um campo ex: E1\_PORTADO, estar preenchido com o código do banco.

**Saiba Mais:**   
[Situação de Cobrança (FINA022 - SIGAFIN)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=415715057)
