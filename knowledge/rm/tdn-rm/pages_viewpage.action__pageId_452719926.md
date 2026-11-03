---
content_hash: a82acc88aed584b9e4e6b584533346508101ac57c9d005f6650cbbe4596c6a08
fetched_at: '2026-06-29T00:10:11.054679+00:00'
page_id: '452719926'
product: rm
source: tdn-rm
title: Código de Cálculo 187 - Base INSS Férias Próx. Mês Outro Emprego Desc. Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719926
version: 3
---

Evento do tipo Base de Cálculo, Valor e sem incidências.

Neste Código de Cálculo deverá ser informado o valor da base de cálculo utilizada na outra empresa para o cálculo do desconto do INSS de Férias do Próximo mês (da outra empresa ).

Quando o usuário informar este código de cálculo deverá informar também Código de Cálculo 185 - INSS DE FÉRIAS PROXIMO MÊS OUTRO EMPREGO.

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
      
   2) Férias Partidas
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
