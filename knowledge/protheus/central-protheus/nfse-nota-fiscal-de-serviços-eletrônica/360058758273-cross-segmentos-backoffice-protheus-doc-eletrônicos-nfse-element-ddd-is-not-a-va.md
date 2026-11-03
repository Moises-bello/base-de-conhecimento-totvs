---
article_id: 360058758273
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d7bb155635d9fd40c20b9829ea18ef1481d66946f7d7b6c3b309c7f617b71392
fetched_at: '2026-06-28T22:39:56.252517+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - ''Element
  ''ddd'': ''***'' is not a valid value of the atomic type ''{tss_nfse_tipos_v2.00}
  tsddd.'''
type: support-article
updated_at: '2025-06-02T12:34:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058758273-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Element-ddd-is-not-a-valid-value-of-the-atomic-type-tss-nfse-tipos-v2-00-tsddd
---

**Ocorrência**Ao realizar a transmissão de um RPS ocorre o erro de schema: '**Element 'ddd': '\*\*\*' is not a valid value of the atomic type '{tss\_nfse\_tipos\_v2.00} tsddd.'**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096541554/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Esse erro ocorre quando estoura o tamanho máximo recebido e permitido pela tag <ddd>, podendo ser os dados do cliente ou do prestador.  
Geralmente quando informado um DDD igual ou maior que 3 dígitos no Cadastro do Cliente (A1\_DDD ou o formato incorreto no campo M0\_TEL no Cadastro da Filial).  
  
**Solução**Para correção deverá **revisar os cadastros do cliente e/ou da filial** e deixa-los dentro do padrão, exemplos abaixo:  
  
Cadastro do Cliente:  
A1\_DDD = 11  
A1\_TEL = 912345678  
*Obs.: Informar apenas um único TEL dentro do campo A1\_TEL e não informar o DDD novamente dentro do campo A1\_TEL, caso contrário poderá ultrapassar o limite máximo permitido do campo.*  
  
Cadastro da Filial:  
M0\_TEL = Será o DDD + TEL, exemplo: 11 912345678  
  
  
  
**Artigo Sugerido (com relação após preenchimento do DDD):**- [MP - NFSE - type mismatch on compare on PREST(NFSEXMLENV.PRW) DD/MM/2021 HH:MM:SS line : XXXX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006330161-MP-NFSE-type-mismatch-on-compare-on-PREST-NFSEXMLENV-PRW-DD-MM-2021-HH-MM-SS-line-XXXX?source=search)
