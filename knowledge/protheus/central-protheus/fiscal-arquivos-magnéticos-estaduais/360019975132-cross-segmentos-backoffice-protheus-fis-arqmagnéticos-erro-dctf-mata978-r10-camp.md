---
article_id: 360019975132
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 4fbf50f744feb98b7aadb8888ba95a79e69dd0e5f27dae6f2b154a7c74a1e8b7
fetched_at: '2026-06-28T22:42:10.867256+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Erro DCTF (MATA978)
  R10 - Campo 06, Grupo de Tributo
type: support-article
updated_at: '2022-08-17T20:22:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019975132-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Erro-DCTF-MATA978-R10-Campo-06-Grupo-de-Tributo
---

**Ocorrência**Erro de importação do Tipo do Registro **R10** da **DCTF** (**MATA978**), **Campo 06 Grupo de Tributo**, com a descrição: Valor deve estar compreendido entre "01" e "13".  
   
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**Esse erro de validação ocorre, pois não foi criado um **Cadastro de Natureza** para cada imposto. É da Natureza financeira que a informação é levada para o arquivo, por isso, ocorre essa divergência. Caso haja cadastro de **IRRF** e **PCC** na mesma natureza, pode gerar a linha do **R10** com apenas um código do **IRRF** por exemplo, causando o erro de validação.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Cadastre uma Natureza por código de imposto. Logo, o **Campo 06** será informado no arquivo gerado, conforme os códigos dos impostos 01 ao 13.

![blobid0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015949792/blobid0.png)
