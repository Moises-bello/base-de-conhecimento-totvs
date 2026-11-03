---
article_id: 13855595962391
category: Rescisão
content_hash: 6a87b6fab2bc98041528f3b92811776d37acefbaa2a14fb6bdc5342562f9e3e5
fetched_at: '2026-06-28T22:46:54.248782+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Erro: FKPFHSTHOR_AHORARIO violada - chave mãe não localizada
  - Transferência entre coligadas'
type: support-article
updated_at: '2024-09-16T18:28:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13855595962391-RH-RM-FOP-Erro-FKPFHSTHOR-AHORARIO-violada-chave-m%C3%A3e-n%C3%A3o-localizada-Transfer%C3%AAncia-entre-coligadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16288462968983) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**  
Erro FKPFHSTHOR\_AHORARIO violada - chave mãe não localizada ao cadastrar transferência entre coligadas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões.  
  
**Causa**O erro apresentado é causado devido a incompatibilidade de registros na tabela de horário.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Para que efetue a transferência de funcionários é necessário que efetue a cópia dos registros de horários de entre as coligadas envolvidas no processo.  
  
[RH - RM - FOP - Cópia de registros entre coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021778232-RH-RM-FOP-C%C3%B3pia-de-registros-entre-coligadas)  
  
**2.** Para que o erro **FKPFHSTHOR\_AHORARIO** não seja apresentado durante a transferência do funcionário deverá acessar a coligada de destino e verificar se possui o mesmo sindicato do RM Chronus, vinculado atualmente ao funcionário na coligada de origem.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13975384344983)

**3-** Depois que clicar em anexo, seguir o passo a passo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13975476551959)

**4-** Todos os horários cadastrados pela empresa  (coligada origem) deverão estar contidos na coligada destino. **(TODOS OS DADOS IGUAIS).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13975528620823)

**5-** Caso não exista é necessário que efetue a copia dos Sindicatos do Chronus da Coligada Origem para Destino. No módulo Automação de Ponto acesse **Automação de Ponto | Configurações | Parametrizador | Sindicato.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13971096272919)

**Importante**  
A transferência do funcionário é **irreversível**e não pode ser cancelada! Antes de executar o processo, tenha certeza das informações digitadas no cadastro da rescisão.  
  
Para evitar que apareçam mais erros futuros, peço que copie todos os registros entre as coligadas.  
  
**Saiba mais**[RH - RM - FOP - Cópia de registros entre coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021778232-RH-RM-FOP-C%C3%B3pia-de-registros-entre-coligadas?source=search)
