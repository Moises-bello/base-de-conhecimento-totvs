---
content_hash: 8f762726f1617293c76ca14192fd41cdffbfa998cee2f0cc7827ee103faa6ff5
fetched_at: '2026-06-29T00:06:17.133718+00:00'
page_id: '212904973'
product: rm
source: tdn-rm
title: ER_PCREQ-8489_Analise_Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8489_Analise_Curricular
version: 10
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | WBS\_R\_EDU016\_1219 | **IRM1** | PCREQ-8488 |
| **Requisito1** | PCREQ-8489 | **Subtarefa1** | [PDR\_EDU\_EDU016-2](http://jira.totvs.com.br/browse/PDR_EDU_EDU016-2) |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Possibilitar que na analise curricular seja exibida as informações do valor minimo do componente curricular seguido do valor já concluído.

## Definição da Regra de Negócio

1. Alterar a  apresentação dos dados da análise curricular no sistema, no portal e no book de relatórios, para que as informações sejam apresentadas agrupadas pelos componentes curriculares e modalidades. Desta forma a visualização da informação da analise curricular passa de:  

   **Componentes curriculares:**

   * 3        Modalidade Fluig                                      Concluído                              2015/1                     40,000                40,000  
                  Fluig Social
   * 3        Modalidade Fluig                                      Pendente                              2015/2                      30,000                30,000  
                  Identity
   * 4        Modalidade Fluig Advanced                    Pendente                               2015/2                      65,000                65,000  
                  Workflow
   * 1        Modalidade Inglês                                    Concluído                              2015/1                      40,000                40,000  
                 Inglês intermediário

   Para: 

   **Componente curricular:** **01 - FLUIG**              **Valor mínimo:** **150,000**                                                                         **Concluído:** **40,000**   
   **Modalidade: 3 - Fluig                         Valor mínimo:   1,000              Valor máximo: 260,000           Concluído: 40,000**      

   * Fluig Social                                      Concluído                              2015/1                     40,000                40,000
   * Identity                                              Pendente                               2015/2                     30,000                30,000**Modalidade: 4 -  Fluig Advanced            Valor mínimo:  1,000              Valor máximo: 100,000          Concluído:   0,000**    
   * Workflow                                          Pendente                               2015/2                      65,000                65,000
2. **Componente curricular: 02 - Língua Estrangeira          Valor mínimo: 400,000                              Concluído: 40,0000**  
           **Modalidade: 1 - Modalidade Inglês          Valor mínimo:  1,000               Valor máximo: 400,000          Concluído:     0,000**

   * Inglês intermediário                       Concluído                               2015/1                      40,000                40,000
3. A parte do resumo da analise curricular terá as seguintes alterações:   
   * Nomenclatura do resumo
     + **Componentes curriculares** para  **Componentes curriculares (mínimos exigidos)**
   * Somatório concluídas dos componentes curriculares 
     + Devem respeitar o campo "valor mínimo" do cadastro de componentes da matriz aplicada (os valores serão somados até o atingimento do valor minimo)
     + Devem respeitar os campos de valores mínimo e máximo do cadastro de itens curriculares.
4. Book de relatórios

* + EDUREL0018 - Análise Curricular.TotvsReport
  + EDUREL0028 - Histórico do Ensino Superior.TotvsReport

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Analise Curricular – Sistema | Alteração | TOTVS Educacional -> Matrícula e Avaliação -> Matrículas -> Matrículas no curso -> Anexos -> Análise Curricular | - |
| Análise Curricular - Portal | Alteração | Portal Educacional -> Acadêmico -> Histórico | - |
| Book de relatórios - Analise Curricular | Alteração | * EDUREL0018 - Análise Curricular.TotvsReport * EDUREL0028 - Histórico do Ensino Superior.TotvsReport |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
