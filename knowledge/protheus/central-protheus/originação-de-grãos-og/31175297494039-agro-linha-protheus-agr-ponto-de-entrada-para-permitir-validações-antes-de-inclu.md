---
article_id: 31175297494039
category: Originação de Grãos (OG)
content_hash: 3ac37850c7a27245f96fbcd18855219ba35c933b5665f6e2a9d3a79868084cf4
fetched_at: '2026-06-28T22:45:43.073223+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para permitir validações antes
  de Inclusões ou Alterações
type: support-article
updated_at: '2025-07-14T19:50:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31175297494039-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-permitir-valida%C3%A7%C3%B5es-antes-de-Inclus%C3%B5es-ou-Altera%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31175284309783) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**O que indica a tabela **Ponto de Entrada para permitir validações antes de Inclusões ou Alterações**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA200 | Previsões de Aplicações | |
| **Ponto de Entrada:** | AGRA200CO |
| **País(es):** | Todos |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | O Ponto de Entrada "AGRA200CO" permite validações antes da gravação de uma inclusão ou alteração. |
| **Localização:** | Rotina de inclusão de previsões de aplicações. |
| **Eventos:** | O Ponto de Entrada é executado antes do Begin Transaction de cada ação (inclusão ou alteração). |
| **Programa Fonte:** | AGRA200 |
| **Função:** | AGRA200B |

****Exemplo:****

****#Include '[Protheus.ch](http://protheus.ch/)'  
  
User Function AGRA200CO()  
         Local nOpcao := PARAMIXB //OPCOES 3=Inclusão, 4=Alteração, 5=Exclusão  
         Local lRetorno := .F.  
  
         If nOpcao == 3  
                  ALERT("Ponto de Entrada INCLUIR - AGRA200CO")  
                   //PARA A OPÇÃO 3=INCLUSAO ESTA RETORNANDO VERDADEIRO .T.  
                  // ASSIM A INCLUSAO SERÁ FEITA  
                  lRetorno := .T.  
         ElseIf nOpcao == 4  
                  ALERT("Ponto de Entrada ALTERAR - AGRA200CO")  
                  //PARA A OPÇÃO 4=ALTERACAO ESTA RETORNANDO FALSO .F.  
                  //ASSIM A ALTERACAO NÃO SERÁ FEITA  
                  lRetorno := .F.  
          EndIf  
Return(lRetorno)****
