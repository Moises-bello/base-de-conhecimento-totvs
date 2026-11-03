---
content_hash: acd242bc33155ced390bf74a3bab05db2e0fd9692b47b6980bddb0b8b5078cfd
fetched_at: '2026-06-29T00:06:21.252174+00:00'
page_id: '223166474'
product: rm
source: tdn-rm
title: DT_Analise_Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Analise_Curricular
version: 1
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Análise curricular* | *Informe o nome técnico da rotina.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Analise Curricular – Sistema | *-* | | Analise Curricular – Portal | - | | Book de relatórios - Analise Curricular | - | |
| **Ponto de Entrada:** | *Informe o ponto de entrada relacionado (link).* |
| **Requisito (ISSUE):** | PCREQ-8489 |
| **País(es):** | *Brasil* |
| **Versões/Release:** | *12.1.9* |

## Descrição

Essa implementação permite que na analise curricular sejam exibidas as informações do valor minimo do componente curricular seguido do valor já concluído.

#### Cenário atual:

As informações de componentes curriculares exibidas hoje na análise curricular são agrupadas apenas pelos componentes curriculares, conforme ode ser observado a seguir:

1. **Componentes curriculares:**

* 3        Modalidade Fluig                                      Concluído                              2015/1                     40,000                40,000  
               Fluig Social
* 3        Modalidade Fluig                                      Pendente                              2015/2                      30,000                30,000  
               Identity
* 4        Modalidade Fluig Advanced                    Pendente                               2015/2                      65,000                65,000  
               Workflow
* 1        Modalidade Inglês                                    Concluído                              2015/1                      40,000                40,000  
              Inglês intermediário

 

#### Cenário proposto:

A nova implementação altera a forma como essas informações são exibidas, passando a agrupá-las além de componentes curriculares como já era feito anteriormente, agora também pela modalidade, como pode ser observado no exemplo a seguir, além da exibição dos valores mínimo e concluído por componente, e mínimo e máximo por modalidade:

1. **Componente curricular:** **01 - FLUIG**              **Valor mínimo:** **150,000**                                                                         **Concluído:** **40,000**   
   **Modalidade: 3 - Fluig                         Valor mínimo:   1,000              Valor máximo: 260,000           Concluído: 40,000**      

   * Fluig Social                                      Concluído                              2015/1                     40,000                40,000
   * Identity                                              Pendente                               2015/2                     30,000                30,000**Modalidade: 4 -  Fluig Advanced            Valor mínimo:  1,000              Valor máximo: 100,000          Concluído:   0,000**    
   * Workflow                                          Pendente                               2015/2                      65,000                65,000
2. **Componente curricular: 02 - Língua Estrangeira          Valor mínimo: 400,000                              Concluído: 40,0000**  
           **Modalidade: 1 - Modalidade Inglês          Valor mínimo:  1,000               Valor máximo: 400,000          Concluído:     0,000**

   * Inglês intermediário                       Concluído                               2015/1                      40,000                40,000

Além dessas alterações, o resumo das atividades curriculares exibido na analise curricular também foi alterado de **Componentes curriculares** para  **Componentes curriculares (mínimos exigidos)**e os relatórios EDUREL0018 - Análise Curricular.TotvsReport e EDUREL0028 - Histórico do Ensino Superior.TotvsReport também foram alterados para contemplar a nova forma de visualização.

 

divs
