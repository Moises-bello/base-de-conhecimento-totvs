---
content_hash: a4df38d721046d502ab24b2190a73c651b18e01e6c60b1f332a1f35d417cd07c
fetched_at: '2026-06-29T00:10:11.067521+00:00'
page_id: '452719930'
product: rm
source: tdn-rm
title: Código de Cálculo 192 - Base INSS Férias Mês Anterior Outro Emprego
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719930
version: 2
---

Evento do tipo Base de Cálculo, Valor e sem incidências.   
 Neste Código de Cálculo deverá ser informado o valor da base de cálculo utilizada na outra empresa para desconto do Inss de férias referente ao mês anterior.  
 Quando o usuário informar este código de cálculo deverá informar também Código de Cálculo 193 - INSS DE FERIAS MES ANTERIOR OUTRO EMPREGO.

**Observação**

Este evento deverá ser informado em Cadastros | Funcionários | Férias | pasta Adicionais de Férias.

**Dicas**

Dicas para utilização dos eventos de Inss Férias Outro Emprego Complementar

1) Férias dentro do mês:

* Informar em Cadastros | Funcionários | Férias | pasta Adicionais de Férias os eventos com os códigos de cálculo e seus respectivos valores:    
   CC(159) INSS DE FERIAS OUTRO EMPREGO e   
   CC(186) BASE INSS FER MES OUTRO EMP DESC COMPL.
* Efetuar o cálculo das férias
* Lançar as férias no mês.   
      
   2) Férias partidas:
* Informar em Cadastros | Funcionários | Férias | pasta Adicionais de Férias os eventos com os códigos de cálculo e seus respectivos valores:    
   CC(159) INSS DE FERIAS OUTRO EMPREGO ,   
   CC(186) BASE INSS FER MES OUTRO EMP DESC COMPL,   
   CC(185) INSS FERIAS PROX MES OUTRO EMPREGO e   
   CC(187) BASE INSS FER PROX MES OUTRO EMP DESC COMPL
* Efetuar o cálculo das férias
* Lançar férias no mês
* Liberar competência
* Acessar Cadastros | Funcionários | Férias | pasta Adicionais de Férias retirar os eventos com códigos de cálculo:   
   CC(185) INSS FERIAS PROX MES OUTRO EMPREGO e   
   CC(187) BASE INSS FER PROX MES OUTRO EMP DESC COMPL
* Informar em Cadastros | Funcionários | Férias | pasta Adicionais de Férias os eventos com os códigos de cálculo e seus respectivos valores:    
   CC(192) - BASE INSS FERIAS MES ANTERIOR OUTRO EMPREGO e   
   CC (193) - INSS DE FERIAS MES ANTERIOR OUTRO EMPREGO
* Lançar férias mês anterior
* Liberar férias  
    

  |  |  |
  | --- | --- |
  |  | Informações Complementares |

  ---

  Códigos de Cálculo
