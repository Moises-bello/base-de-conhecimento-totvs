---
content_hash: 0492742d1a8b0477a0895ac6968635f135fd5ac3011e2e1a531f673743ee2131
fetched_at: '2026-06-29T00:10:08.777459+00:00'
page_id: '452719577'
product: rm
source: tdn-rm
title: Ficha Financeira RHU
type: documentation
url: https://tdn.totvs.com/display/LRM/Ficha+Financeira+RHU
version: 10
---

Na ficha financeira serão visualizadas as informações mensais referentes a ocorrências verificadas nos pagamentos dos salários, ou seja, eventos (proventos e descontos) lançados na folha de pagamento do funcionário ao longo dos anos.  
 

**Atenção:**  
1.    Os dados estarão disponíveis após ter sido feita a entrada de dados e o lançamento automático ou recálculo, esses dados serão visualizadas na ficha financeira.   
2.    É preciso estar atento para o fato de que, para fazer a liberação de um período e iniciar outro, é necessário alterar os dados referentes a período e caixa.  
   
**Observação:**  
Através da edição da ficha financeira no cadastro de funcionários é possível controlar:

* Ficha Financeira
* Centro de Custo
* Base AAS
* Verbas Geradas por Diferenças
* Substituição

**Campo Dissídio**

Este campo será preenchido na execução do processo "Diferença Salarial". Será preenchido com "Sim", sempre que:

* O parâmetro***"Dissídio/Convenção/Acordo"***estiver marcado; ou
* O campo ***"Dados do Dissídio/Convenção/Acordo"*** na rescisão complementar estiver preenchido com o tipo ***"F - Outras verbas de natureza salarial ou não salarial devidas após o desligamento"***

Caso contrário o campo será preenchido com "Não".

**ATENÇÃO:** Ao calcular a rescisão complementar selecionando:

* + - * Parâmetro "Dissídio/ Convenção / Acordo coletivo" marcado como "Não"
      * Parâmetro "Calcular somente eventos informados" marcado
      * Parâmetro "Pagamento de verbas de natureza salarial ou não salarial devidas após o desligamento" marcado
      * Selecionar "Dados do dissidio / convenção / acordo coletivo" com tipo de acordo "F - Outras verbas de natureza salarial ou não salarial devidas após o desligamento"

Serão inseridos os eventos de IRRF com flag marcada como "Não" para o parâmetro "Dissidio" dentro da edição do evento na ficha financeira e na geração do XML periódico serão informados os eventos no XML S1200 do e-Social.

Serão tratados os códigos de cálculo de IRRF abaixo:

* + Código de cálculo 4  - IRRF
  + Código de cálculo 49 - IRRF 13º SALARIO
  + Código de cálculo 61 - IRRF FÉRIAS ENVELOPE
  + Código de cálculo 127 - IRRF PARTICIPACAO NOS LUCROS

As informações de Base AAs são atualizadas automaticamente pelo sistema a cada liberação de competência. Entretanto,  pode ser feita a manutenção, se necessário (por exemplo, em caso de conversão da base do RM FOLHA ou implantação do Folha de Pagamento). Somente não será permitida a inclusão na competência atual e competências posteriores.  
   
Quando o parâmetros "Usa AAS Discriminado" não estiver marcado as informações são apenas colocadas no grupo de AAS totalizador dos valores - Grupo 00.   
   
As verbas visualizadas em Verbas Geradas por Diferenças  não necessariamente foram pagas na competência consultada, elas são devidas à competência. Para saber em qual competência/ano as verbas foram pagas, consulte os campos "Mês de referência" e "Ano de Referência".  
   
O sistema consulta o cadastro de substituições dos funcionários para calcular o valor das horas de substituição. O valor de cada hora de substituição é valorizado de acordo com a diferença entre o salário de quem é substituído e o valor do salário de quem substitui.   
   
Os campos "Nro. Dependentes IRRF", "Nro. Dependentes Salário Família" e "Líquido", são apenas para facilitar a emissão de relatórios e a visualização da quantidade de dependentes utilizada nos cálculos.

Na edição do período da ficha financeira, o campo "Ordem Cálculo" será preenchido apenas quando o funcionário possuir mais de um vínculo na base de dados e estiver utilizando o cálculo de INSS conforme o eSocial. Esse campo será utilizado no cálculo da tag indMV dos eventos periódicos para envio ao governo.

   
**Atenção:**  
Como o histórico de dependente somente é atualizado na liberação de competência, ou quando é realizada alguma alteração no cadastro do dependente, e no cálculo de IRRF utiliza o caixa de pagamento para considerar ou não o dependente, com este campo fica mais fácil obter a informação correta. O mesmo ocorre com o salário familia, o cálculo verifica o panorama (quantidade de dependentes) atual, com este campo fica mais fácil obter a informação correta.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários

|  |  |
| --- | --- |
|  | Veja Também |

---

[Cálculo das Horas de Substituição](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719387)
