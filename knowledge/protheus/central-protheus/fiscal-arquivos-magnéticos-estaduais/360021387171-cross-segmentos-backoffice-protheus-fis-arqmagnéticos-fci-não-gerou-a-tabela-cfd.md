---
article_id: 360021387171
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: ececed229a985d0313316bb2189df43bf1b5aabba3c06b6f7406080f7156a2f8
fetched_at: '2026-06-28T22:42:10.896688+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - FCI não gerou
  a tabela CFD quando o parâmetro MV_FCICALC = 3
type: support-article
updated_at: '2022-08-17T20:31:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021387171-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-FCI-n%C3%A3o-gerou-a-tabela-CFD-quando-o-par%C3%A2metro-MV-FCICALC-3
---

**Ocorrência**FCI não gerou a tabela CFD quando o parâmetro **MV\_FCICALC = 3**.  
  
**Ambiente**Microsiga Protheus – Livros Fiscal – A partir da versão 11.80.  
  
**Causa**Quando a tabela **SA8** é preenchida, porém a tabela **CFD** não é alimentada, é necessário conferir se os campos e parâmetros informados abaixo estão com a configuração correta.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Se possuir nota de Venda (SD2) dentro do período apurado ou anteriormente, verifique:

**MV\_FCIALIQ** - deve conter as alíquotas utilizadas no **D2\_PICM**;  
**MV\_FCICL** - deve conter os **CST** utilizados no **D2\_CLASFIS**;  
**MV\_FCIMOD** - deve conter o Modelo da nota que consta no **MV\_ESPECIE**;  
**MV\_FCIVI** - deve conter os **CFOP's** de Venda dentro do estado, de acordo com o **D2\_CF**;  
**MV\_FCIVE** - deve conter os **CFOP's** de Venda interestadual, de acordo com o **D2\_CF**.

2. Caso não tenha vendas, o sistema verifica a configuração para produtos novos:

* Necessário preencher **B1\_PRV1** ou **B5\_FCIPRV** ou **BZ\_FCIPRV**
* Informar corretamente no **MV\_FCIPRV** (campo que o sistema irá buscar o preço de venda).
* Informar a **UF** no **MV\_FCINWPR**.
