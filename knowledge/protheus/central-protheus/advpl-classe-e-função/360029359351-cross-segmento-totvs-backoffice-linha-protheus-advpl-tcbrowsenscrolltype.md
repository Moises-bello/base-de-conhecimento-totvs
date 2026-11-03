---
article_id: 360029359351
category: ADVPL - Classe e Função
content_hash: 4b09decfff5cd34cea7c194a8d29f2e282011b5e47dd090e04719cc254001852
fetched_at: '2026-06-28T22:40:18.069885+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TCBrowse:nScrollType
type: support-article
updated_at: '2022-06-13T21:37:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029359351-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TCBrowse-nScrollType
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao utilizar a propriedade "nScrollType" da Classe TCBrowse, podemos configurar a barra de rolagem padrão ou VCR, no entanto, ao configurar tanto com "0" quanto com "1", só retorna VCR não acata padrão  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Solução**Para utilizar essa propriedade *nScrollType*, os componentes devem utilizar *array* como tipo de dados. Não é possível alterar o tipo da barra de rolagem caso esteja sendo utilizado um **Alias**, por exemplo, a tabela de clientes SA1.   
  
**Saiba mais**  
**[Implementação - Definição do tipo da barra de rolagem na grade grid](http://tdn.totvs.com/pages/viewpage.action?pageId=6065161)**
