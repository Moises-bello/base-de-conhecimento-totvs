---
article_id: 360024185511
category: Faturamento - Cadastros
content_hash: 57c8dad516b5f692d6a98f73f697443d495961be657639ebeeeaf9bcae1c5715
fetched_at: '2026-06-28T22:38:35.565918+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos- TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) -
  Código do Município não Aparece no Cadastro
type: support-article
updated_at: '2021-05-14T13:38:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024185511-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-C%C3%B3digo-do-Munic%C3%ADpio-n%C3%A3o-Aparece-no-Cadastro
---

**Dúvida**

O código de município não aparece no cadastro de clientes/transportadora, porem esta cadastrado no sistema, o que fazer?

**Ambiente**

Cross Segmentos- TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT)– A partir da release 11.80.  
  
**Solução**

Para mostrar os municípios cadastrados no sistema é necessário preencher o campo estado no cadastro que esta realizando, o sistema tem uma função ***Funçäo:ExistCpo("CC2",M->A4\_EST+M->A4\_COD\_MUN)*** que verifica se um código existe em um arquivo selecionado.   
Ao preenche o estado ele libera a tabela de municípios para selecionar, pois já apresenta os código de municípios filtrando de acordo com estado selecionado.
