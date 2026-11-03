---
article_id: 21211175839511
category: SIGAEST - PROCESSAMENTOS
content_hash: 0be1f963ce6f9694f3bff44a800c6b1927368ce2614c7468c70a4a275ec30f98
fetched_at: '2026-06-28T22:39:04.993610+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - TOP Error -19 - Invalid
  parameter type (Erro na chamada de processo) '
type: support-article
updated_at: '2025-03-12T12:25:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21211175839511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-TOP-Error-19-Invalid-parameter-type-Erro-na-chamada-de-processo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21211175819415) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao executar rotinas de processamentos do estoque que utilizam procedures é gerado o erro na chamada de processo **"TOP Error -19 - Invalid parameter type",** como corrigir?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21211145105431)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Causa**Esse incidente ocorre pois possui algum parametro em sua SX6 que não está com o tipo da variável correto ou o conteúdo, sendo necessário reavaliar se foi feito alguma alteração que impactasse e ajustar para o dicionário correto.

**Solução**

1. Avaliar se não houve nenhuma alteração do tipo da variável dos parametros e conteúdo da sua SX6 relacionado a rotina em questão;

2. Fazer um teste sem as procedures relacionadas ao estoque para que o sistema gere o error.log e informe qual parametro que esteja gerando erro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21212043541527)

**Observação**: No exemplo acima o erro: "**type mismatch on compare on LOCALIZA**" se dá por conta do **tipo** do parâmetro **MV\_LOCALIZ** estar diferente do que se espera.

Ao gerar o error.log, verifique qual é o parâmetro que está com inconsistência e reavalie.

3. Avaliar o tipo de compartilhamento do parametro e verificar se está exclusivo ou compartilhado.

**Exemplo:** Tem 5 filiais no grupo de empresa, e o parametro MV\_RASTRO está exclusivo **apenas para uma filial,** vai gerar o **erro acima pois precisa ter esse parametro em todas as filiais.**

4. Caso persista, por gentileza abrir um ticket ao time de Suporte para que possa enviar o error.log sem a procedure instalada gerado para que possamos apontar qual é o parâmetro que está com o tipo incorreto e efetuar o ajuste.

**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro na chamada do processo em rotinas de Processamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000275147-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-na-chamada-do-processo-em-rotinas-de-Processamento)
