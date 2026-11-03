---
article_id: 360028884931
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 3788248504e510fb237421e2d76fcd2b894ad1a8e16cf671fd6081b54095f89f
fetched_at: '2026-06-28T22:42:10.694641+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DCTF - Erro
  de validação no campo 05 do header
type: support-article
updated_at: '2022-08-17T20:13:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028884931-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DCTF-Erro-de-valida%C3%A7%C3%A3o-no-campo-05-do-header
---

**Ocorrência**Ao validar o arquivo, ocorre o erro de validação:

**Header da declaração  - Campo 05 - Campo com valor inválido**

![image2018-6-29_15-21-45.png](http://tdn.totvs.com/download/attachments/379301755/image2018-6-29_15-21-45.png?version=1&modificationDate=1530297818000&api=v2)

**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Causa**O erro ocorre pois a versão da **DCTF** foi informada de forma incorreta na *wizard* de geração do **arquivo.**  
  
**Solução**Neste campo é informado a versão do validador da **DCTF**. Como o validador não aceita pontos no arquivo, deve-se colocar a versão sem ponto.  
  
Exemplo: versão 3.4, no arquivo deve ser levado 340.  
  
No Protheus essa informação é gerada conforme a *wizard* de geração do arquivo conforme abaixo, onde deve ser informada a versão também sem o ponto:

![image2018-6-29_14-48-36.png](http://tdn.totvs.com/download/attachments/379301755/image2018-6-29_14-48-36.png?version=1&modificationDate=1530297819000&api=v2)
