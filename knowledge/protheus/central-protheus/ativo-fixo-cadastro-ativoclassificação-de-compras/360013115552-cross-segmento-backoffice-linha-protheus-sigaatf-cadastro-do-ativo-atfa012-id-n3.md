---
article_id: 360013115552
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 8b2027dc4d4e217114371d7e22522ad08598bd4102f10b2e16ef097291891630
fetched_at: '2026-06-28T22:41:48.403259+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - CADASTRO DO ATIVO -
  ATFA012 (Id N3_TXDEPR  inválido on FWFORMGRIDMODEL)
type: support-article
updated_at: '2023-11-30T16:39:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013115552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-CADASTRO-DO-ATIVO-ATFA012-Id-N3-TXDEPR-inv%C3%A1lido-on-FWFORMGRIDMODEL
---

**Ocorrência**

Na alteração ou inclusão do ativo retorna errorlog

THREAD ERROR ([3848], selma.alves, 23-CONTAB) 06/08/2018 13:06:51  
erro no parâmetroFWFormGridModel: Id N3\_TXDEPR inválido on FWFORMGRIDMODEL:GETVALUE(FWFORMGRIDMODEL.PRX)

**Ambiente**

PROTHEUS  – Ativo fixo  – A partir da versão 12  
  
**Causa**

Parametro MV\_ATFMOED esta configurado e forma incorreta

**Solução**[Exemplo:

O parametro MV\_ATFMOED (moeda a ser considerada para calculo do ativo Fixo , utilizando a moeda 1 (real) ou moedas cadastradas no sistema

A moeda informada deve ter apenas um caracter, informando mais de um apresenta esta ocorrência.
