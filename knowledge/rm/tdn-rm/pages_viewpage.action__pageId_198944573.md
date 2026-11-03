---
content_hash: 32e9c546035f8495713b0cb6c4608ba1e52c9bc3341d0661def2af071f46fa8e
fetched_at: '2026-06-29T00:06:02.207398+00:00'
page_id: '198944573'
product: rm
source: tdn-rm
title: Controle de Retenções Contratuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198944573
version: 6
---

**Visão Geral**

O processo de controle de retenções contratuais permite enviar ao TOTVS Gestão de Estoque, Compras e Faturamento o valor total da medição de um contrato gerado pelo TOTVS Construção e Projetos, sem subtrair as retenções, preenchendo separadamente os campos específicos com os valores redutores.

 O Controle de Retenções terá na gestão de Materiais, basicamente três tipos de movimentos, sendo:

* 1.1.XX - Medição a pagar ou 2.1.XX - Medição a receber
* 1.2.YY - NF Entrada ou 2.2.YY  - NF Saída
* 1.2.ZZ - Retenção a pagar ou 2.2.ZZ -  Retenção a receber

O controle de retenções contratuais funcionará da seguinte maneira:

O movimento de medição (1.1.XX/2.1.XX) é enviado ao BackOffice através da integração com TOP(Gerar integração com Suprimentos/Faturamento), onde o valor do contrato será enviado integralmente e os valores referentes a retenção serão enviados para os campos específicos no Item de movimento|aba Valores. Em seguida, o movimento de medição deve ser faturado para Nota Fiscal (1.2.YY/2.2.YY).  
Para completar o processo, o terceiro movimento (1.2.ZZ/2.2.ZZ) deverá ser gerado através do recurso de Liberação de Retenção do TOTVS Obras e Projetos e depois vinculado a Nota Fiscal (1.2.YY/2.2.YY).  
***Observações***: A solução da Retenção dentro do TOTVS Estoque, Compras e Faturamento funcionará independentemente da integração com o TOTVS Construções e Projetos, ou seja, se os tipos de movimentos forem parametrizados corretamente, a retenção poderá ser utilizada mesmo se o usuário não possuir o TOP.  
Se o tipo de movimento estiver integrado com o TOP, os campos da Retenção permanecerão desabilitados, não permitindo sua edição a partir do BackOffice Materiais. Caso o tipo de movimento não esteja integrado, esses campos poderão ser editados.

**Principais Campos e Parâmetros**

**Medição a Pagar (1.1.XX) ou Medição a Receber (2.1.XX)**

Esses tipos de movimentos podem ser gerados através da integração com o TOP (Gerar integração com Suprimentos/Faturamento) ou incluídos diretamente na gestão de Materiais.  
O preço unitário do item será o valor do serviço medido, ou seja, valor cheio, sem qualquer redução.  
Ele será parametrizado para utilizar Retenção por item de movimento, na etapa Item – Valores Financeiros 2/2, que poderá ser registrado em Percentual, Valor ou Ambos.   
Quando informado em Percentual o sistema irá calcular o valor aplicando o % informado sobre o Preço Unitário do respectivo item de movimento.  
***Observação***: como os movimentos gerados pelo TOP enviam somente o Valor da Retenção, quando tipo de movimento for parametrizado para trabalhar com Percentual(%) o valor da retenção será calculado como zero, pois ao recalcular ele considera o percentual como zero.   
Sendo assim o tipo de movimento utilizado pelo TOP deverá ser parametrizado para Usar Retenção \ Tipo de Retenção igual a Valor ou Ambos.  
Se o tipo de movimento estiver parametrizado para integração com o TOP, etapa Projeto|Integração Projetos, o valor do serviço e o valor da Retenção serão carregados através da integração e não poderão ser editados no módulo de Materiais.   
Somente tipos de movimentos não integrados com o TOP poderão editar esses campos no módulo de Materiais.

**NF Entrada (1.2.YY) ou NF Saída (2.2.YY)**

Esses tipos de movimentos serão gerados através do recebimento ou faturamento dos movimentos de Medição (processo nativo do Materiais).  
Ele será parametrizado para utilizar Retenção por item de movimento, na etapa Item – Valores Financeiros 2/2, que poderá ser registrado em Percentual, Valor ou Ambos.  
Deverá ser parametrizada a etapa Vinculações | Classificação de Vinculação = Retenção.   
Este tipo de movimento que irá alimentar o controle de vinculações entre movimentos da gestão de Materiais.  
Este movimento, além da integração com o TOP terá também integração: Fiscal, Financeira e Contábil.   
Para facilitar a utilização do valor da Retenção nos processos de integração, será criada uma função de fórmula para retornar a soma do valor de Retenção de todos os itens do movimento.

**Retenção a Pagar (1.2.ZZ) ou Retenção a Receber (2.2.ZZ)**

Esses tipos de movimentos podem ser gerados através da integração com o TOP (processo de Liberação de Retenção) ou incluídos diretamente na gestão de Materiais.  
Para que o movimento gere integração com TOP é necessário que o tipo de movimento esteja com o parâmetro “Informa Projeto|Tarefa” diferente de “Não Informa” (etapa Projetos do parametrizador).  
Além dos parâmetros de utilização da Retenção citados acima, deverá ser parametrizado quanto à etapa Vinculações |Tipo de Vinculação = Controlar Retenção.  
O preço unitário do item será o valor da retenção.   
Em movimentos integrados com o TOP, esse campo será carregado através da integração e não poderá ser editado na gestão de Materiais.  
Deverá ser criada uma fórmula com base na função TVIM que permitirá que se some todas as retenções dos itens a partir do movimento, para que sejam feitos os cálculos necessários.

**Exemplo: MVB - TVIM('VALORRETENCAO')**

Para definir a Fórmula acesse o módulo Serviços Globais | Administração | Fórmulas, Selecione o contexto de sistema: Gestão de Estoque, Compras e Faturamento e inclua um novo registro.  
Nos parâmetros de tipo de movimento (1.2.XX/2.2.XX - Nota Fiscal) Etapa Fin-Faturamento 3/6 campo Fórmula do Valor a Ratear informe a fórmula cadastrada.   
Para realizar a integração com o TOP deve ser selecionada a opção “Discriminar valores de retenção e dedução” nos parâmetros de Projetos | Contratos para que os valores informados para dedução sejam carregados no movimento.  
Na inclusão do Contrato, aba Fórmula deve ser utilizada a fórmula “C – valor com reajuste” para que seja enviado ao módulo de materiais o valor bruto do contrato.   
Na aba Defaults do Contrato, deve ser informado o tipo de movimento que será gerado no BackOffice.

|  |  |
| --- | --- |
| **Tabelas:** | **Descrição** |
| TMOV  TITMMOV  TTMVEXT  TMOVRELAC  TVINCULOMOV   TVINCMOVRELAC | Movimentos  Itens de Movimento  Tipos de Movimento  Relacionamento entre Movimentos  Movimentos Vinculados  Vínculo de Movimentos de Nota Fiscal e Adiantamentos |

Informações Adicionais

* [Controle de Deduções Contratuais](http://tdn.totvs.com/pages/viewpage.action?pageId=198944190)
* [Como Fazer:Processo Medição de contrato/ Liberar Retenção](http://tdn.totvs.com.br/pages/viewpage.action?pageId=173082042)
