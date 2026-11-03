---
article_id: 360057638214
category: BI - Business- Intelligence - Workflow
content_hash: cf5abb5506a3f2c3b53826cb433e150c6b0921b851800c4a60d033f048f48a15
fetched_at: '2026-06-28T22:37:03.067208+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Tabela SXM em ambiente
  com dicionário no banco
type: support-article
updated_at: '2022-02-15T19:03:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057638214-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Tabela-SXM-em-ambiente-com-dicion%C3%A1rio-no-banco
---

**Ocorrência**

```
Ctree error - Open - It was not possible to Check Internal Struct of File: d:\totvs\microsiga\protheus_data\system\sxm010.dtc on TBITABLE:LOPEN(TBITABLE.PRW) 02/06/2017 09:46:05 line : 153
```

**Ambiente**Protheus – BI – A partir da versão 12  
  
**Causa**Esse incidente ocorre, pois após a virada de versão para as releases mais atuais, alguns clientes optaram por desligar o **CTREE**, gerando assim problemas com Workflow, ao utilizar a configuração de Timeout.  
  
**Solução**

Foi realizada a importação da tabela **SXM** para o banco de dados, eliminando assim o uso do arquivo**CTREE****.**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Após aplicar o pacote **(DSERBA1-6685)**;  
2. Pare o **DbAccess** e o **AppServer**;  
3. Caso não tenha, realize a configuração do job do **timeout(**SchedulerWF**)** no .**ini**(appserver);4**.** Inicie novamente o **DbAccess** e **AppServer.** **Importante:**

Para que os dados sejam importados do arquivo em disco(**CTREE**) para o banco, é necessário verificar se as **Dlls** do **CTREE** existem na pasta do **AppServer**.  
É possível que a tabela seja criada em branco, ou seja, sem os dados do arquivo antigo, para isso basta remover o arquivo (ex.:**SXM010**) da pasta **System**.  

**Observação:**Após a importação da tabela para o banco, o arquivo em disco será **deletado** automaticamente.
