---
article_id: 39804145247639
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b290d88fe5068202ab5b772dd5899d1fae44f3cfb9051e0a124cad92f6ce61b6
fetched_at: '2026-06-28T22:38:57.012773+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA261 - "variable
  does not exist B1_EC05CR on A261GRAVA(MATA261.PRX)"
type: support-article
updated_at: '2026-04-16T19:35:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39804145247639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-variable-does-not-exist-B1-EC05CR-on-A261GRAVA-MATA261-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39804145218839) Tempo aproximado para leitura: **00:01:48 min**  
  
**Ocorrência**  
Ao concluir a Transferência Multipla (MATA261), ocorre o error.log: *"variable does not exist B1\_EC05CR on A261GRAVA(MATA261.PRX)"*  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
O erro variable does not exist B1\_EC05CR indica que o sistema tentou acessar o campo B1\_EC05CR (referente a campos de e-commerce/integração no Cadastro de Produtos) na tabela SB1, mas este campo não foi localizado no dicionário de dados da empresa ou não está disponível na memória durante a execução da função A261GRAVA.  
  
**Solução**  
Para solucionar o incidente é necessário realizar os seguintes passos:

Valide se o campo B1\_EC05CR está válido no dicionario e no banco. Segue abaixo detalhes de como configurar o campo em questão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39804174337687)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39804145221911)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39804145223063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39804174344471)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39804145225623)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39804145226775)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39804174349719)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39804174354327)

Após o campo estar devidamente configurado no Dicionário de Dados, basta tentar efetuar novamente a transferência para que consiga completá-la com sucesso.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
