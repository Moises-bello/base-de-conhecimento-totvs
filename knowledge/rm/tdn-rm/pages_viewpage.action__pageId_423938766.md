---
content_hash: 0f3bbf4cd0ea81a458ffc0df8941c3fd7c9a0ba1b0512ca6189b820e40d370a2
fetched_at: '2026-06-29T00:09:28.714386+00:00'
page_id: '423938766'
product: rm
source: tdn-rm
title: Controle de Retenções Contratuais (Integração Gestão de Construção e Projetos
  x Gestão de Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938766
version: 8
---

O processo de controle de retenções contratuais permite enviar ao TOTVS Gestão de Estoque, Compras e Faturamento o valor total da medição de um contrato gerado pelo TOTVS Construção e Projetos, sem subtrair as retenções, preenchendo separadamente os campos específicos com os valores redutores. O Controle de Retenções terá na gestão de Materiais, basicamente três tipos de movimentos, sendo:

* 1. 1.1.XX Medição a pagar ou 2.1.XX Medição a receber
* 2. 1.2.YY NF Entrada ou 2.2.YY NF Saída
* 3. 1.2.ZZ Retenção a pagar
* ou 2.2.ZZ Retenção a receber

**Medição a Pagar (1.1.XX) ou Medição a Receber (2.1.XX)**

Esses tipos de movimentos podem ser gerados através da integração com o TOP (Gerar integração com Suprimentos/Faturamento) ou incluídos diretamente na gestão de Materiais.   
O preço unitário do item será o valor do serviço medido, ou seja, valor cheio, sem qualquer redução.   
Ele será parametrizado para utilizar Retenção por item de movimento, na etapa Item – Valores Financeiros 2/2, que poderá ser registrado em Percentual, Valor ou Ambos.   
Quando informado em Percentual o sistema irá calcular o valor aplicando o % informado sobre o Preço Unitário do respectivo item de movimento.   
Se o tipo de movimento estiver parametrizado para integração com o TOP, etapa Projeto |Integração Projetos, o valor do serviço e o valor da Retenção serão carregados através da integração e não poderão ser editados no módulo de Materiais.   
Somente tipos de movimentos não integrados com o TOP poderão editar esses campos no módulo de Materiais.

**NF Entrada (1.2.YY) ou NF Saída (2.2.YY)**

Esses tipos de movimentos serão gerados através do recebimento ou faturamento dos movimentos de Medição (processo nativo do Materiais).   
Ele será parametrizado para utilizar Retenção por item de movimento, na etapa Item – Valores Financeiros 2/2, que poderá ser registrado em Percentual, Valor ou Ambos.   
Deverá ser parametrizada a etapa Vinculações | Classificação de Vinculação = Retenção.   
Este tipo de movimento que irá alimentar o controle de vinculações entre movimentos da gestão de Materiais.   
Este movimento, além da integração com o TOP terá também integração: Fiscal, Financeira e Contábil. Para facilitar a utilização do valor da Retenção nos processos de integração, será criada uma função de fórmula para retornar a soma do valor de Retenção de todos os itens do movimento.  
***Observações***: O movimento de NF a ser vinculado aos itens de movimento de retenção deve ter as informações referente a estado e município preenchidas para que a liberação da retenção será realizada.

**Retenção a Pagar (1.2.ZZ) ou Retenção a Receber (2.2.ZZ)**

Esses tipos de movimentos podem ser gerados através da integração com o TOP (processo de Liberação de Retenção) ou incluídos diretamente na gestão de Materiais.   
Para que o movimento gere integração com TOP é necessário que o tipo de movimento esteja com o parâmetro "Informa Projeto|Tarefa" diferente de "Não Informa" (etapa Projetos).   
Além dos parâmetros de utilização da Retenção citados acima, deverá ser parametrizado quanto à etapa Vinculações |Tipo de Vinculação = Controlar Retenção.   
O preço unitário do item será o valor da retenção. Em movimentos integrados com o TOP, esse campo será carregado através da integração e não poderá ser editado na gestão de Materiais.  
Observação: O movimento 1.X.ZZ (Retenção a pagar) e 2.X.ZZ(Retenção a receber), não necessariamente precisa ser de Nota Fiscal, os mesmos podem ser de outro tipo, como Ordem de compra/Ordem de venda.  
O controle de retenções contratuais integrado ao TOTVS Construção e Projetos funcionará da seguinte maneira:

* O movimento de medição (1.1.XX/2.1.XX) é enviado ao BackOffice através da integração com TOP, onde o valor do contrato será enviado integralmente e os valores referentes a retenção será enviado para o campo Retenção no Item de movimento|aba Valores.
* Em seguida, o movimento de medição deve ser faturado para Nota Fiscal (1.2.YY/2.2.YY). Para completar o processo, o terceiro movimento (1.2.ZZ/2.2.ZZ) deverá ser gerado através do recurso de Liberação de Retenção do TOTVS construção e Projetos já vinculado automaticamente a Nota Fiscal (1.2.YY/2.2.YY).
* A relação entre os movimentos poderá ser visualizada através da edição do item de movimento |aba Vinculações.
* A solução da Retenção dentro do TOTVS Estoque, Compras e Faturamento funcionará independentemente da integração com o TOTVS Construções e Projetos, ou seja, se os tipos de movimentos forem parametrizados corretamente, a retenção poderá ser utilizada mesmo se o usuário não possuir o TOP.
* Se o tipo de movimento estiver integrado com o TOP, o campo Retenção permanecerá desabilitado, não permitindo sua edição a partir do BackOffice Materiais. Caso o tipo de movimento não esteja integrado, esses campos poderão ser editados.

Informações Adicionais

* [Especificação - Controle de Deduções Contratuais](http://tdn.totvs.com/display/LRM/DT_controle_de_retencoes_e_deducoes_contratuais)
