---
article_id: 5976685610903
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: beb64da0383827b0b8766341e64466471a351b5ea48515e0920cfc2c1e58fbfd
fetched_at: '2026-06-28T22:42:00.834148+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Arq. Magnéticos - Sped Fiscal - 0200
  - Código do Produto concatenado com o Código da Filial
type: support-article
updated_at: '2023-05-31T18:29:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5976685610903-Cross-Segmentos-Backoffice-Protheus-Arq-Magn%C3%A9ticos-Sped-Fiscal-0200-C%C3%B3digo-do-Produto-concatenado-com-o-C%C3%B3digo-da-Filial
---

**Dúvida**  
No arquivo txt do Sped Fiscal gerado pelo Protheus o **Código do Produto** está concatenando com o **Código da Filial** no registro **0200 - Tabela de Identificação do Item**. Como ajustar para que  apresentado apenas o **Código do Produto** sem a informação do **Código da Filial?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**Para que o **Código da Filial** não seja concatenado ao **Código do Produto** é preciso avaliar o conteúdo do parâmetro **MV\_COFLSPD**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5976881738263/mceclip1.png)**

**Importante**Por padrão a filial é sempre concatenada nos registros de códigos do bloco zero, porém se houver a necessidade de que estes códigos não sejam gerados de forma concatenada com código da filial, então este parâmetro **MV\_COFLSPD** deverá ser criado manualmente e seu conteúdo deve ser **.F.**

Caso o parâmetro não exista na dicionário de dados, por padrão o código da filial será concatenado nos códigos dos registros do bloco zero.
