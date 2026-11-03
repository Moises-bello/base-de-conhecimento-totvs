---
article_id: 360037335714
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: a24661052f1ca9f4b90d587b2fd473aca5025b350330793f09256b628c969388
fetched_at: '2026-06-28T22:41:48.360328+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - N3_CUSTBEM
  - Codigo reduzido
type: support-article
updated_at: '2021-10-15T17:17:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037335714-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-N3-CUSTBEM-Codigo-reduzido
---

**Dúvida**

Ao realizar o cadastro de um Ativo Fixo ATFA012 e preencher o campo N3\_CUSTBEM com código do centro de custo reduzido o mesmo não está retornando o código do centro de custo cadastrado conforme o campo CTT\_CUSTO?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.1.17

**Solução**

Para utilizar o Código Reduzido de uma entidade configure o parâmetro MV\_REDUZID. Ao configurar este parâmetro com “S”, o sistema passará a considerar que a digitação de qualquer entidade contábil será feita pelo seu código reduzido. Se o parâmetro for mantido com “N”, a digitação de qualquer código reduzido deverá ser precedido de “\*”.  Ao digitar o código reduzido, o sistema o converte automaticamente para a entidade original.  
  
Se o código reduzido de sua empresa for menor que o sugerido pelo sistema, altere no Configurador o tamanho deste campo (CTT\_RES) antes de iniciar o cadastramento dos Centros de Custo.  
  
Obs: Todo e qualquer lançamento será gravado com os códigos das entidades originais.
