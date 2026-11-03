---
content_hash: 729a0f8897b4e9c423e634b932fdb6ac97c1769f956851d59f13ae1af86689de
fetched_at: '2026-06-29T00:06:20.028321+00:00'
page_id: '221546643'
product: rm
source: tdn-rm
title: ER_PCREQ-8791_Paralizacao_de_Contrato_Adicionando_Periodo_sem_Criar_Aditivo
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8791_Paralizacao_de_Contrato_Adicionando_Periodo_sem_Criar_Aditivo
version: 135
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP009 | **IRM1** | PCREQ-8788 |
| **Requisito1** | PCREQ-8791 | **Subtarefa1** | PDR\_CP\_TOP009-62 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |
| **Integração** | Não se aplica | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

|  |  |  |  |
| --- | --- | --- | --- |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP009 | **IRM1** | PCREQ-8788 |
| **Requisito1** | PCREQ-8789 | **Subtarefa1** | PDR\_CP\_TOP009-26 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |

## Objetivo

Possibilitar aos usuários do módulo de contratos do TOTVS Obras e Projetos, a prorrogação automática do prazo de um contrato, em caso de suspensão do mesmo.

## Definição da Regra de Negócio

A prorrogação de contrato acontece no momento em que, no histórico, o mesmo passa da situação de "Paralisado" para novamente estar "Em Andamento".

Nesse momento é realizado o cálculo de quantos dias o contrato ficou paralisado e em seguida uma nova data é sugerida para que o usuário possa alterá-la caso se faça necessário, desde que ela não seja menor que a data final do contrato, com aditamento, se houver.

Quando o contrato possuir um ou mais aditivos, devem ser prorrogadas e alteradas todas as datas de término: a data do contrato e as datas do aditivo. Os aditivos serão prorrogados pela quantidade de dias contabilizados.

Um log é registrado automaticamente, no momento da prorrogação, que o adiamento foi realizado.

**1-Melhoria na aba de contrato nos parâmetros de projeto**

Com a criação deste modulo em contratos, foi identificado que a tela de parâmetros de projeto, na aba contrato, ja não está atendendo a criação de novos parâmetros. Assim foi definido pelo comitê da Totvs a divisão deste parâmetro, de acordo com as funcionalidades do modulo de contrato.

 A definição ficou nos seguintes subitens, conforme mostrado no (protótipo 01):

* Geral : Esta aba contemplará os parâmetros que influenciam todo o contrato
* Associação de itens e objetos: Esta aba contemplará os parâmetros que influenciam o processo de associação de itens ou objetos ao contrato
* Períodos: Esta aba contemplará os parâmetros que influenciam a criação e alteração de períodos
* Medição:  Esta aba contemplará os parâmetros que influenciam a medição de itens ou consumo de objetos
* Liberação: Esta aba contemplará os parâmetros que influenciam a liberação do contrato
* Encerramento: Esta aba contemplará o Checklist do encerramento de contrato.

**2-Melhoria na funcionalidade de prorrogação de contratos**

Algumas melhorias deverão ser realizadas nessa funcionalidade, com a criação de parâmetros e o comportamento como um todo:

* + Deverão ser criados dois novos parâmetros (Protótipo 01):
    - aba Geral > Permitir Alteração de Data na Prorrogação do Contrato : Com esse parâmetro marcado, ao alterar o histórico do contrato de "Paralisado" para "Em Andamento" a data de prorrogação será sugerida com a possibilidade de ser alterada, com o parâmetro desmarcado, o contrato e aditivos serão prorrogados considerando o cálculo de dias corridos em que o contrato ficou paralisado. Inicialmente o parâmetro estará marcado;
    - aba Períodos > Reprogramar os períodos subsequentes na prorrogação do contrato: Com esse parâmetro marcado, ao alterar o histórico do contrato de "Paralisado" para "Em Andamento" os períodos que ainda serão medidos e liberados deverão ter suas datas reprogramadas considerando a nova data de prorrogação do contrato, com o parâmetro desmarcado, o contrato e aditivos serão prorrogados e o usuário terá a possibilidade de criar novos períodos para o contrato conforme o exemplo:  
        
      Exemplo 1:  
        
        
        
      Exemplo 2:

Exemplo 3:

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Contratos | [Alteração] | Controle -> Contrato -> Contratos | - |

## Protótipo de Tela

**Protótipo 01**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
