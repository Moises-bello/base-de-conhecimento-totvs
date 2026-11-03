---
article_id: 9531944838295
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 59ae800a6c141fa183f02754f5c50c5f44ea95bdad071bdc58e0988d83b2d697
fetched_at: '2026-06-28T22:37:55.150734+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus -  SIGAFIN - FINA205/FINA435 - Ao
  rodar o retorno do CNAB via Job (Schedule) não executa as baixas dos títulos
type: support-article
updated_at: '2022-10-13T20:34:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9531944838295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA205-FINA435-Ao-rodar-o-retorno-do-CNAB-via-Job-Schedule-n%C3%A3o-executa-as-baixas-dos-t%C3%ADtulos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Ao rodar o retorno do CNAB via Job (Schedule) o mesmo não executa as baixas dos títulos  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA205 - A partir da versão 12.1.33  
  
**Solução**Esse incidente ocorre pois nos **Parâmetros de banco** rotina (**FINA130**) existe os campos **EE\_INCREC** para informar o diretório de processamento do arquivo, com inconsistência no **Contas a Receber** e no campo **EE\_INCPAG** para **Contas a Pagar** e o mesmo estão em branco.

**Exemplo:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9531640549527)

Para solucionar deve-se, criar uma pasta na Root path(Protheus\_Data) e informar o caminho nos **Parâmetros de banco** utilizado.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9531718173207)

Ao realizar o procedimento, quando rodar o JOB novamente os títulos deverão ser baixados normalmente.

**Saiba mais:**

**Campos EE\_INCPAG** e  **EE\_INCREC**: [Não move o arquivo para diretório de inconsistência](https://tdn.totvs.com/pages/releaseview.action?pageId=704911354)

[Configuração do Retorno de CNAB Automático (FINA205/FINA435)](https://tdn.totvs.com/pages/releaseview.action?pageId=471926159)
