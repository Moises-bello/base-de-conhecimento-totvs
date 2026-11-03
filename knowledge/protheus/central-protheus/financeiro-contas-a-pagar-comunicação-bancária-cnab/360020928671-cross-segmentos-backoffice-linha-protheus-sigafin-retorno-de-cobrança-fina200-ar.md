---
article_id: 360020928671
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: f8f8333ea9f44c3f2b56f15214f3517eb200e67b886e113ae44bab70e11e2783
fetched_at: '2026-06-28T22:37:56.427879+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Retorno de Cobrança
  (FINA200) - Arquivo já foi processado 1 vez . Deseja reprocessá-lo
type: support-article
updated_at: '2023-05-04T23:11:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020928671-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Retorno-de-Cobran%C3%A7a-FINA200-Arquivo-j%C3%A1-foi-processado-1-vez-Deseja-reprocess%C3%A1-lo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00min**

**Ocorrência**No módulo **Financeiro**, ao tentar reprocessar um arquivo de retorno de cobrança que já foi processado. Apresenta: Arquivo já foi processado 1 vez . Deseja reprocessá-lo?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017468072/mceclip0.png)

**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da versão 11.80  
  
**Causa**Esta mensagem é apresentado quando é interrompido por algum motivo: queda de energia  por exemplo o processamento do Retorno de Cobrança (FINA200). E quando reprocessar o mesmo arquivo que estava processando anteriormente apresentará esta mensagem informando se deseja reprocessar a partir da ultima linha lida do arquivo.

**Tabelas de rastreabilidade FI0 e FI1.**

FI0 - Cabeçalho do LOG de processamento

FI1 - Detalhe do LOG de Processamento.

Na tabela FI0, existe o campo: FI0\_LASTLN, onde informa qual foi a última linha processada do arquivo de retorno. Quando este campo está preenchido com a quantidade total de linhas referente ao "detalhe" no arquivo de retorno, o sistema entende que foi processado todas as linhas do arquivo, então não teria o que reprocessar. A rotina somente reprocessa a partir do ponto que foi interrompido, por exemplo, caso o arquivo tenha 10 registros e somente foi processado 06 devido a uma queda de energia, ao selecionar reprocessar, será processado as 4 linhas restantes.

E se o título for baixado então o sistema atualiza a FI1.  
  
**Solução**Quando apresentar a mensagem, acione a opção: "Sim" para que o sistema reprocesse o arquivo a partir da ultima linha lida.

**Saiba Mais**  
**Remessa CNAB Contas a Receber:**

**Retorno CNAB Contas a Receber:**
