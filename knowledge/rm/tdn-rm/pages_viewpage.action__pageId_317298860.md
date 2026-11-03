---
content_hash: 8d7028be3af8e1f42bd8e7078bd8d3c4eca26de1af08dd935eac2f1f99319918
fetched_at: '2026-06-29T00:08:46.446800+00:00'
page_id: '317298860'
product: rm
source: tdn-rm
title: 1473314  RMSAU-1356 DT Valores de referência de parâmetros na digitação/liberação
  de laudo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317298860
version: 3
---

# VALORES DE REFERÊNCIA DE PARÂMETROS NA DIGITAÇÃO/LIBERAÇÃO DE LAUDO

**Características do Requisito**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | Controle de Pedido de Exames |
| **Cadastros Iniciais:** | Cadastros de Exames e serviços, Cadastro de Métodos e Parâmetros, Cadastro de valores de referência dos parâmetros |
| **Parâmetro(s):** | *-* |
| **Tickets relacionados** | 1473314 |
| **Issue:** | RMSAU-1356 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Tabelas Utilizadas:** | SZLABEXAME, SZLABPARAMDADOSREF |
| **Sistema(s) Operacional(is):** | Windows® |

## **Descrição**

Esta implementação consiste em exibir mensagem de validação somente quando o valor digitado está fora dos valores de referência parametrizados. Caso exista alguma faixa que o valor esteja dentro e outras que esteja fora, o sistema não exibirá a mensagem de confirmação do valor.

## **Procedimento para Utilização**

1. Acesse a aba Dados de Referência do parâmetro de exame
2. Crie um novo e/ou edite um dado de referência existente.
3. Faça as parametrizações conforme desejado.
4. Faça o pedido de exame com o exame cadastrado.
5. Acesse o menu Unidades Diagnóstico -> Controle de Pedido de Exames
6. Selecione um exame em status "Em Digitação" que seja um exame de laboratório
7. Digitar um resultado que esteja englobado pelos alertas dos parâmetros de exames
8. Parâmetros configurados:  
   Desejável  <= 10;  
   Aceitável   12-15;  
   Pânico\*      18-19  
   Os valores configurados podem ser digitados, no entanto, os valores do tipo FAIXA DE PÂNICO, quando digitados, exibirão o alerta para o usuário.  
     
     
   Desejável  <= 10;  
     
   Aceitável   12-15;  
     
   Pânico\*      18-19 : Neste caso a mensagem é exibida  
     
   Valores fora da faixa
