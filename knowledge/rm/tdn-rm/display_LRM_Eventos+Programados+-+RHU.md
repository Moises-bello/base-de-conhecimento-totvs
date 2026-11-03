---
content_hash: 8bac6833e12e1db1061ac02a3803455ae811d1e222ebede357106711618d6273
fetched_at: '2026-06-29T00:10:07.939862+00:00'
page_id: '452719478'
product: rm
source: tdn-rm
title: Eventos Programados - RHU
type: documentation
url: https://tdn.totvs.com/display/LRM/Eventos+Programados+-+RHU
version: 2
---

Eventos programados são eventos da folha de pagamento que tem uma competência inicial e final para lançamento, semelhante aos códigos fixos do funcionário, porém este cadastro tem um campo para informar o centro de custo do evento programado e a competência inicial e final, e o evento poderá ser cadastrado mais de uma vez para o mesmo funcionário.  
 **Observações:**  
 1. Os campos 'Complemento 1' e 'Complemento2' são apenas informativos.  
 2. Serão visualizados apenas os centros de custos 'Ativos'.  
    
 **Atenção:**  
 Sempre que alterar/excluir o centro de custo de algum evento, e os eventos programados já estiverem sido lançados, deverá cancelar o movimento do funcionário, devido o campo EDITADO ser igual 1, e é regra do sistema sempre que os valores não podem ser alterados.  
 Foram criadas as fórmulas abaixo, com a mesma funcionalidade do código fixo:

|  |  |
| --- | --- |
| **Evento Programado** | **Código Fixo** |
| EP - Valor do Evento Programado | CF – Valor do Código Fixo |
| EXISTEEP - Existe Evento Programado | EXISTECF – Existe Código Fixo |
| NEPRG - Número de vezes do Evento Programado | NCFIX - Número de vezes do Código Fixo |
| TABEVTPROG - Valor de um campo da Tabela de Eventos Programados | TABCODFIX - Valor de um campo da Tabela de Código Fixo |

Na Tabela Dinâmica existe o tipo 'TPEVTPROG-Tipo de Eventos Programados', para definir os grupos para lançamento dos eventos programados.  
    
 Na rotina de alteração global de eventos programados poderá realizar a alteração/inclusão/exclusão de Eventos Programados para um ou mais funcionários simultaneamente. Este módulo irá auxiliar na atualização dos Eventos Programados referente aos campos de 'Competência Inicial', 'Competência Final', 'Valor', 'Tipo', 'Centro de Custo' e 'Complementos'.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
