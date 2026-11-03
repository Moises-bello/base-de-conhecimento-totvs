---
article_id: 360033380894
category: Escrita Fiscal - Impostos - ISS
content_hash: c81ba2ed50eaf277f1396e1412b775c54eb0e8671f1c9c95e83f4dd2f6b4b4c5
fetched_at: '2026-06-28T22:39:35.304683+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: MP - FIS - Valores de ISS Gravados nos Campos de ICMS
type: support-article
updated_at: '2021-04-28T21:17:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033380894-MP-FIS-Valores-de-ISS-Gravados-nos-Campos-de-ICMS
---

**Dúvida**Nota de serviço escriturada com retenção de ISS no documento de entrada, quando consultado na aba livros fiscais, aparece a base, alíquota e valor de ISS nos campos de ICMS.  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
O valor de ISS no documento de entrada é demonstrado nos campos de Base e Valor de ICMS por motivo de não existir campos específicos para ISS.  
  
Na linha do produto na nota fiscal de entrada ou saída o ISS esta informado corretamente na coluna de ISS.  
  
Se pesquisar o livro modelo 51 "saída" ou 56 "entrada" ira estar constando corretamente.  
  
Nas tabelas SF3 -Livros Fiscais e SFT - Itens do Documento, o ISS não possui campos próprios, os valores de base de ISS e valor do ISS é gravado nos campos do ICMS conforme abaixo:

FT\_BASEICM  
FT\_VALICM

O que irá identificar que a nota é de serviços é o campo F3\_TIPO = S.
