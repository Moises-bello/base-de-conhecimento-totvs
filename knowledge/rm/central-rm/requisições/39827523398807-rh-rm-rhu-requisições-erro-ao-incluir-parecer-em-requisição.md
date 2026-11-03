---
article_id: 39827523398807
category: Requisições
content_hash: 161d4f61572e873bd79c6058ad201552e7e00ada0890ec70ce08e1ed157910d8
fetched_at: '2026-06-28T22:47:25.263115+00:00'
product: rm
section_id: 1500000861382
source: central-rm
title: 'RH - RM - RHU - Requisições: Erro ao incluir parecer em requisição'
type: support-article
updated_at: '2026-04-17T16:59:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39827523398807-RH-RM-RHU-Requisi%C3%A7%C3%B5es-Erro-ao-incluir-parecer-em-requisi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39827555260311) Tempo aproximado para leitura: **00:03:00min**  
  
**Ocorrência**  
Ao inserir um parecer em uma Requisição por meio da biblioteca RM (MDI), é apresentada a mensagem de erro abaixo:  
   
"Ocorreu um erro ao efetuar a leitura das definições da tabela: A requisição já se encontra no fluxo do Agilis. Não é possível criar novos pareceres."  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **Todas as versões.**  
  
**Causa**  
O erro é apresentado, pois a Requisição encontra-se com status diferente de Pendente.  
  
**Solução**  
Quando a Requisição já se encontra inserida no fluxo de aprovações, os novos pareceres poderão ser incluídos somente por meio do Portal RH ou pelo Meu RH por meio dos processos de avanço das etapas, visto que a Requisição já se encontra no fluxo de aprovações.

Neste caso avalie possibilidade de ajuste de qualquer dado da Requisição através do próprio Meu RH ou Portal RH. Estando a Requisição em andamento (ainda não aprovada ou reprovada), o Aprovador Atual poderá alterar dados da Requisição por meio de um dos portais mencionados.

**Importante**

Um parecer pode ser incluído em uma Requisição pelo RM somente enquanto ela estiver com status Pendente, ou seja, a Requisição foi criada pelo sistema (biblioteca) e ainda não foi inserida no fluxo de aprovação (execução através do processo de Inserir no Fluxo).
