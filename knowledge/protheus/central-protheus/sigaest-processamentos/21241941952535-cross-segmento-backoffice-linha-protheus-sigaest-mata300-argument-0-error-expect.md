---
article_id: 21241941952535
category: SIGAEST - PROCESSAMENTOS
content_hash: ceaec6fe6e4d3c8b5b04d4aa096e33480cdc92998ba354c7b18bf910912afad8
fetched_at: '2026-06-28T22:39:04.957542+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA300 - argument
  #0 error, expected D->L, function dtos on MA300PROCESS(MATA300.PRX)'
type: support-article
updated_at: '2024-02-09T14:50:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21241941952535-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-argument-0-error-expected-D-L-function-dtos-on-MA300PROCESS-MATA300-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21241925498391) Tempo aproximado para leitura: **00:03:12 min****Ocorrência**Ao executar o processamento Refaz Saldos (MATA300) é exibido o error.log: "*argument [#0](https://totvssuporte.zendesk.com/agent/tickets/0) error, expected D->L, function dtos on MA300PROCESS(MATA300.PRX)*"  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Este erro ocorre quando a linha do fonte está fazendo validação em parâmetros e comparando com o parâmetro no dicionário de dados do ambiente. Se o tipo do parâmetro esperado no fonte for diferente do tipo que estiver no dicionário de dados, é exibido o error.log em questão.  
  
**Solução**Para validar internamente este erro, siga os passos abaixo:  
   
1° Passo - validação do tipo dos parâmetros:   
   
Outros 4 parâmetros mais comuns que podem estar com tipagem incorreta a validar no SX6 são: 

MV\_D2DTDIG -> Tipo padrão dele é **Lógico (L)**

MV\_A280GRV -> Tipo padrão dele é **Lógico (L)**

MV\_ULMES -> Tipo padrão **Data (D)**

MV\_LOCALIZ -> Tipo padrão **Caractere (C)**  
   
É importante avaliar e eventualmente ajustar caso estejam no ambiente com tipagem diferente do padrão.  
   
2° Passo - Estando todos adequados, ou se houve a necessidade de ajustar, **desinstale e instale os procedures 14 ao 22**. Isso é importante para o Procedure recriar inclusive com as configurações de tipagens dos parâmetros conforme o dicionário de Dados.   
   
3° Passo - Após isso, basta executar o processamento novamente.  
 

É esperado que com essas ações, o problema seja resolvido.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)
