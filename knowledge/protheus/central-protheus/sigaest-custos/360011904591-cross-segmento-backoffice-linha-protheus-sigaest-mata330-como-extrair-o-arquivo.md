---
article_id: 360011904591
category: SIGAEST - CUSTOS
content_hash: 6c27547747fd3481bd6c8ca51082016a8dbac14b2725893b3916ffb4ec22aef6
fetched_at: '2026-06-28T22:39:00.391393+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como extrair
  o arquivo TRB após executar o custo medio?
type: support-article
updated_at: '2026-04-13T16:09:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011904591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-extrair-o-arquivo-TRB-ap%C3%B3s-executar-o-custo-medio
---

O artigo explica como extrair o arquivo TRB ao executar o Recálculo do Custo Médio (MATA330) no Protheus 12.1.27. A tabela temporária TRBXXSP é gerada no banco de dados do cliente após o processamento, devendo ser coletada via APSDU e filtrada por código de filial e produto. O arquivo deve ser salvo em .dtc, SQLITE ou SQLSERVER para análise e validação da ordenação dos movimentos conforme o Kardex.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18856103679639)** Tempo aproximado para leitura: **00:02:40 min**

**Dúvida**  
Como extrair arquivo de trabalho TRB ao executar o Recálculo do Custo Médio (MATA330)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.27.

**Solução**

A TRB é de grande importância para analisarmos os erros gerados durante o processamento do Recálculo do Custo Médio em situações específicas.

Para usuários que possuem a rotina Recálculo do Custo Médio (MATA330) com data igual ou superior à 18/12/2019, a geração das tabelas temporárias passou a ser no banco de dados do cliente, **ela é gravada após processamento de custo médio para o periodo em apuração.**

Desta forma a coleta da tabela deve ser feita via APSDU procurando pela tabela TRBXXSP onde XX é o grupo de empresa do cliente.

**How To | MP - SIGAEST - Como gerar e gravar o arquivo TRB #TOTVS\_Backoffice\_Linha\_Protheus**

**Tabela correta:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18855911794967)

Importante filtrar o **Codigo da filial + Produto**, para extrair somente o especifico, e deve ser salvo em formato **.dtc ou para as versões mais recentes em SQLITE ou SQLSERVER**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18855911807127)

Dessa forma, podemos appendar a tabela e aplicar o indice dentro da tabela, e avaliar se a ordenação, esta de acordo com sua apropriação é correta ou não, e os movimentos devem ser espelhados da mesma forma no KARDEX.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é feita a ordenação dos movimentos após recálculo do custo médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17221653862551)

**Indice:** DTOS(TRB\_DTBASE)+TRB\_SEQPRO+TRB\_ORDEM+TRB\_NIVEL+TRB\_NIVSD3+TRB\_CHAVE+TRB\_SEQ

Esse indice nao funciona para arquivos SQLITE ou SQLSERVER, sendo necessario avaliar com o seu analista DBA, como efetuar a validação do indice de acordo com sua base de dados.

**Tabela com indice aplicado:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18855918176151)

Espelho do Kardex, esta correto conforme indice a mesma ordem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18855911819287)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-MP-SIGAEST-An%C3%A1lise-de-Custos-MATR900-Kardex-por-Per%C3%ADodo)
