---
article_id: 360045641833
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 4f639dad91b536eb17cb1f752338d95bdc970e25e9b6c6ea678c3f239f95e282
fetched_at: '2026-06-28T22:39:56.263247+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - 00270: O
  somatório das parcelas informadas não equivale ao valor total da NFSe (IPM)'
type: support-article
updated_at: '2025-07-14T21:45:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045641833-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-00270-O-somat%C3%B3rio-das-parcelas-informadas-n%C3%A3o-equivale-ao-valor-total-da-NFSe-IPM
---

**Ocorrência**Ao realizar a transmissão de uma RPS onde há destaque de PCC (PIS, COFINS e CSLL) é apresentado a seguinte rejeição: '***00270 – O somatório das parcelas informadas não equivale ao valor total da NFSe'.***  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição ocorre pelo fato de que a tag <valor> dentro da estrutura de <parcela> precisará ter as retenções (PIS, COFINS e CSLL) abatidas no valor total da nota de acordo com a prefeitura.[(Print - Resposta da Prefeitura)](https://prnt.sc/rmoand). Exemplo abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062452234)  
  
**Solução**Hoje o rdmake NFSEXMLENV utiliza um função financeira (SomaAbat) a qual já faz essa tratativa.   
Porém vale lembrar que é somente feita quando a **retenção do PIS, COFINS e CSLL são feitos na emissão**.  
Para isso o parâmetro deve estar da seguinte maneira:  
  
**MV\_DUPLLIQ = .T.** (Considerar a função SomaAbat).  
  
**Importante:** Necessário rdmake NFSEXMLENV igual ou superior a 01/11/2019.  
  
Detalhes abaixo dos parâmetros:  
- [MP - NFSE - Destaque do PIS, COFINS e CSLL no XML da NFSe, retenção na Emissão.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027642412-MP-NFSE-Destaque-do-PIS-COFINS-e-CSLL-no-XML-da-NFSe-reten%C3%A7%C3%A3o-na-Emiss%C3%A3o-)
