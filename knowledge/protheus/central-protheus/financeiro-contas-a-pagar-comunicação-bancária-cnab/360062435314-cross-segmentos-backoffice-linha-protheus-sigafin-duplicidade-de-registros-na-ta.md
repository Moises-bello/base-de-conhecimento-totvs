---
article_id: 360062435314
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 4686ebebd5f823cafafc23bc8e9f46cc25cc5a7787cf7069f6bdb8d90e98f943
fetched_at: '2026-06-28T22:37:55.387888+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Duplicidade de registros
  na tabela FIG
type: support-article
updated_at: '2025-02-05T19:33:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062435314-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Duplicidade-de-registros-na-tabela-FIG
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00min**

**Dúvida**Quando é importado o mesmo arquivo de varredura do DDA o sistema grava registros já importados na tabela FIG.  
  
**Ambiente**Microsiga Protheus - Financeiro - A partir versão 11.80  
  
**Solução**Por conceito a rotina identifica que o arquivo já foi processado e exibe o **Help: CHK200FILE**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103330874/mceclip0.png)  
Com esse conceito, o controle do processamento do arquivo é gravado na tabela com o nome **TB+Empresa+Filial+.VRF** na pasta system do Protheus  
Quanto aos dados do arquivo importado que são gravados na tabela **FIG** não possui **chave de validação única**, uma vez que os registros retornados do banco podem não ter uma chave cadastrada no Protheus.
