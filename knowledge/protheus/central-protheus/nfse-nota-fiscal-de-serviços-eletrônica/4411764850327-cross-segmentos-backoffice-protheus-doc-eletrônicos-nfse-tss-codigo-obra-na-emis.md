---
article_id: 4411764850327
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 67d430ba07df37e3dd06feb573859f66dfcbbf065dab4eae4e1c2250567da56a
fetched_at: '2026-06-28T22:39:58.558396+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: Codigo
  Obra na emissão de NFTS'
type: support-article
updated_at: '2021-12-28T11:46:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411764850327-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-Codigo-Obra-na-emiss%C3%A3o-de-NFTS
---

**Dúvida**Como gerar no arquivo txt de Tomador o código de obra.  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**1 - Criar dois campos na tabela SD1, um para Cod.Obra e outro para Art.Obra, com o tipo Caracter.  
Colocar o nome dos campos no parâmetro MV\_NFSOBRA.  
  
Exemplo:  
MV\_NFSOBRA = {"D1\_XOBRA","D1\_ARTOBRA"} 

Deve fornecer o conteúdo nos dois campos, caso contrário não gera informação no arquivo txt.
