---
content_hash: 81c7f3b68e84da53e49c9d75a4a7128642922f731aab7bd38152ceb9cfccf5b4
fetched_at: '2026-06-29T00:10:03.776629+00:00'
page_id: '452719154'
product: rm
source: tdn-rm
title: Histórico Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719154
version: 2
---

A informação de salário de um funcionário é primordial no ato de admissão. Este salário poderá ser alterado ao longo do contrato de trabalho, seja por convenção coletiva ou por concessão da empresa. As alterações salariais devem ser guardadas em um histórico salarial. Este histórico poderá ser utilizado para anotações na carteira profissional, para cálculos retroativos de possíveis diferenças, para relatórios e gráficos gerenciais.  
    
 O histórico salarial é acrescido de informações sempre que houver alteração diretamente no salário base do funcionário, tanto por alteração global de salário como por reprogramação salarial ou ainda individualmente, e também pode ser acrescentado diretamente linhas no histórico salarial, por motivo de migração ou outro motivo que seja necessário inclusão/alteração/exclusão diretamente no histórico.  
    
 O sistema gravará a data de alteração salarial com dez minutos de acréscimo nos campos Dt.processamento e Dt.mudança, caso seja alterado o salário do funcionário no mesmo dia que já ocorreu outra alteração.  
    
 A informação data de processamento deve ser editado caso seja inserido um novo registro manualmente com a existência de valores posteriores a essa inclusão. Esse campo somente estará habilitado caso o parâmetro do sistema "Edita data de processamento" esteja marcado.  
    
 A alteração do histórico salarial de funcionários que recebem salário Composto permite que sejam alteradas as informações de Tabela salarial, bem como informações de Faixa e Nível salarial (desde que os parâmetros   
 Utiliza Tabelas Salariais para evento de Salário Composto e Edita Tabelas Salariais nos Eventos de Salário Composto estejam marcados).  
 Estas informações são ocultas para aqueles funcionários que não recebem salário composto.  
     
 **Exemplo:**  
 Simulação:  
 No histórico salarial o ultimo registro é:   
 Data de processamento: 01/11/2000  
 Data da Mudança: 02/11/2000  
 Valor do salário: 291,50  
    
 Ao incluir um registro que estava faltando retroativo a este existente acima, deverá ser feito da seguinte forma:   
 Data de processamento: 28/02/1996  
 Data da mudança: 28/02/1996  
 Valor do salário: 270,00  
    
 **Atenção:**  
 A alteração dessa data influenciara nos cálculos de diferença salarial. Ou seja, para ser feito o cálculo de diferença salarial corretamente, é importante que os históricos salariais dos funcionários estejam corretos.  
 Para encontrar a diferença entre o salário atual e o salário anterior ordenam-se os dados conforme data de processamento.   
    
 **Exemplo 1:**  
 **Data de processamento**

|  |  |  |  |
| --- | --- | --- | --- |
| **Data de processamento** | **Data de mudança** | **Salário** | **Percentual** |
| 01/10/2008 | 01/10/2008 | R$ 1000,00 | 0% |
| 01/12/2008 | 01/12/2008 | R$ 1200,00 | 20% |

Neste caso o ultimo salário é R$ 1200,00. O seu salário em 10/2008 é R$ 1000,00  
    
    
 **Exemplo 2:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Data de processamento** | **Data de mudança** | **Salário** | **Percentual** |
| 01/09/2008 | 01/09/2008 | R$ 800,00 | 0 |
| 01/11/2008 | 01/11/2008 | R$ 1000,00 | 25% |
| 01/12/2008 | 01/10/2008 | R$ 1200,00 | 20% |

Neste caso o ultimo salário é R$ 1200,00. O seu salário em 01/10/2008 é R$ 1200,00, isso porque a data de processamento atual é última linha, mas a data de mudança se refere a 10/2008.   
 Se for efetuado um cálculo de diferença iniciando em 10/2008 o sistema considerará que o funcionário tem uma diferença de R$ 400,00, visto que o cálculo será a diferença entre R$ 800,00 e R$ 1200,00. Em relação ao salário de 01/10/2008 o funcionário teve um aumento de 50%.  
    
 No cálculo de diferença salarial retroativa o histórico salarial será preenchido da seguinte forma:  
 **Data da Mudança:** Data oficial em que ocorreu a alteração salarial.  
 **Data do Processamento:** Data em que foi processada a alteração salarial.  
    
 **Exemplo:**  
 Estando em 15/12/2008, realizamos uma alteração salarial com data de 01/10/2008.  
 O dia 15/12/2008 será a data do processamento.   
 O dia 01/10/2008 será a data da mudança.  
    
 O "Nro.Salário" serve para funcionários que possuem salários compostos, será enumerado os salários de acordo com o número do salário registrado na pasta Salário Composto. Para os demais funcionários será colocado como default o número "1".  
    
 **Atenção:**  
 Não será permitido incluir o "Nro. Salário" com o número de salário diferente de 1 quando não se utiliza salário composto para o funcionário.  
    
 **Exemplo:**  
 Funcionário com salário composto:  
 Número do salário = 1 para o salário composto 1 registrado na pasta Salário Composto.  
 Número do salário = 2 para o salário composto 2 registrado na pasta Salário Composto.  
 Número do salário = 3 para o salário composto 3 registrado na pasta Salário Composto.  
    
 Será informada a alteração de jornada automaticamente quando a alteração salarial for referente apenas ao campo "Jornada" e for processada através do módulo de alteração global salarial.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
