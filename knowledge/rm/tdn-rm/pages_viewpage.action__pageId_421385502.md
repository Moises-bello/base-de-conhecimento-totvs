---
content_hash: e7d611cbcb9c7309baded88cf6ad635f8fe290dbf00ba62725b2ee68f757a973
fetched_at: '2026-06-29T00:09:16.283831+00:00'
page_id: '421385502'
product: rm
source: tdn-rm
title: Gerar Integração com Suprimentos/Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385502
version: 35
---

Este processo consiste em gerar integração do TOTVS Obras e Projetos com o Backoffice (Suprimento e Faturamento)

**Passos:**

Para liberar as medições realizadas no contrato para o Suprimentos/Faturamento o parâmetro Integração/ Surpimento/Faturamento deve estar ativo.

No processo de "Gerar Integração com Suprimentos/Faturamento" de um ou mais períodos de contratos, será gerado para o BackOffice (Protheus ou TOTVS Gestão de Estoque, Compras e Faturamento) um movimento com o tipo,  produto, condição de pagamento, Filial, local de estoque e Centro de custo selecionados ou de acordo com os valores defaults definidos no cadastro do contrato.

Ao acionar o processo Gerar Integração com Suprimentos/Faturamento, o usuário deve informar os seguintes dados para a execução do mesmo:

falseGeração integraçãoGeração completa da integração com Suprimento/Faturamento

O **valor a liberar** não fica editável para geração do movimento, conforme destacado na imagem abaixo. Mais detalhes sobre parametrização e comportamento estarão disponíveis na aba de [Geração parcial](https://tdn.totvs.com/pages/viewpage.action?pageId=421385502#Gera%C3%A7%C3%A3ointegra%C3%A7%C3%A3o-1794245150).

**Tipo de movimento a ser gerado:** Código do tipo de faturamento (parametrizado no *BackOffice*)

**Condição de pagamento:** condição de pagamento referente ao movimento. (Opcional)

**Filial:** Filial do movimento.

**Centro de custo do movimento:** centro de custo referente ao tipo de faturamento. Neste caso, a precedência é do rateio de centros de custos (se existir).

**Local de estoque:** Local de estoque do movimento.

**Produto/serviço:** Produto/serviço referente ao item de movimento. Neste caso, a precedência é do rateio de produtos (se existir). Ver detalhes sobre produto default ou associado [Contratos Parâmetros de Projeto (F6)](http://tdn.totvs.com/pages/viewpage.action?pageId=421385359)

**Data Lib. Medição (Quando utilizado).** O Campo Data Lib. Medição só será exibido caso o parâmetro "Permite data retroativa do faturamento de contratos" estiver selecionado (Obras e Projetos: Opções/Parâmetros/TOTVS Obras e Projetos/Gerais). Caso não esteja definido no parâmetro será utilizada a data atual para execução do processo.

**Estado e Municipio.** O Estado e Municipio devem ser informados no cadastro do projeto antes de liberar as medições para o Suprimentos/Faturamento, porém é possível durante o processo de geração de integração com o Suprimento/Faturamento editar ou inserir um novo Estado ou Município. [Saiba mais.](https://tdn.totvs.com/pages/viewpage.action?pageId=741844582)

**Cliente para Faturamento:** quando o parâmetro do projeto “Utiliza Cliente para Faturamento” estiver habilitado, o campo será exibido no processo de geração da integração com Suprimentos/Faturamento. O campo será preenchido automaticamente com o cliente informado no contrato, permitindo alteração pelo usuário no momento da liberação. Somente clientes cadastrados no anexo “Clientes para Faturamento” do projeto poderão ser selecionados. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=421385497)

**Observação:** Os dados inseridos no campo de observação são copiados para o campo de histórico do movimento, seja histórico curto ou longo, conforme a parametrização do tipo de movimento.

***Comportamento no Envio de Quantidade no processo de Liberação: (Contratos de Insumos e Extra Histograma)***  
1. *Envio da quantidade quando o BackOffice é RM:* Ao liberar movimentações para o **BackOffice RM** a quantidade enviada SEMPRE será 1.  
2. *Envio da quantidade quando o BackOffice é Protheus:* Ao liberar as movimentações para o **BackOffice Protheus** a quantidade enviada será SEMPRE a medida para os contratos de insumos e extra histograma. Os demais tipos de contratos, continuam enviando a quantidade igual a 1.

**Atenção:**  
Ao gerar o movimento integrado com Suprimento Faturamento, o sistema irá enviar o Departamento do Projeto, caso seja informado. Caso tenha informado Departamento no Anexo de Contrato, será enviado o departamento para o Rateio do Movimento.

Observações

Caso exista integração com Protheus/EMS, o campo referente ao "Tipo de movimento" ficará desabilitado. Caso exista integração com Protheus/EMS e o período for de estorno, o campo de observação ficará desabilitado.   
É importante ressaltar que os valores da aba Movimento podem ser preenchidos previamente na aba default, no cadastro do contrato. Assim, todas as liberações de todos os períodos de medição já serão inicializadas com os valores default devidamente preenchidos, agilizando o processo. Mas nada impede que no momento da liberação os dados sejam alterados.  
Além dos dados a serem preenchidos para a execução do processo, são exibidos também os seguintes valores (disponibilizados apenas para consulta):

**Valor sem reajuste:** valor total da medido do contrato.  
**Valor com reajuste:** valor total da medição do contrato acrescido do reajuste correspondente ao período (cadastrado na edição do contrato).  
**Valor das retenções:** valor total das retenções do período e da retenção por item de contrato.  
**Valor total da medição:** valor total medido acrescido das retenções, reajustado.  
**Valor calculado liberação:** valor a ser liberado, conforme fórmula definida no cadastro do contrato.

Informações Complementares

A aba "Tabelas opcionais" não será exibida quando houver integração com Protheus/EMS ou quando nenhuma tabela estiver sendo utilizada no movimento.  
A utilização ou não de uma tabela será definida no Suprimentos/Faturamento em: Parâmetros/RM Nucleus/Parâmetros Gerais/Tabelas/Classificação. Para uma tabela ser exibida, o parâmetro "Usar no movimento" deve estar selecionado.    
Em Parâmetros/RM Nucleus, após selecionar um Tipo de movimento e acessar a opção Mov - Tab – Classificação, é possível definir um valor default para cada tabela, valor com o qual a tabela vira preenchida.   
Será possível definir o tipo de edição de cada tabela:  
Não Edita: O campo referente à tabela não será exibido.  
Edita: O campo será exibido e poderá ser editado.  
Mostra: O campo será exibido, mas não poderá ser editado.  
O preenchimento dos campos da aba de "Tabelas opcionais" não é obrigatório.  
Os valores extras serão parametrizados de acordo com o tipo de movimento no Suprimento/Faturamento em: Parâmetros/RM Nucleus, após selecionar um Tipo de movimento e acessar a opção "Mov – Valores Financeiros".  
A aba "Valores extras" não será exibida quando não estiver sendo utilizado nenhum valor extra.  
O nome de cada campo poderá ser customizado de acordo com o nome definido no campo nome referente ao valor extra.  
A exibição dos campos Percentual e Valor de cada valor extra será definido através da opção "Tipo Valor Extra" sendo definida como:  
Percentual: só exibe o campo Percentual  
Valor: só exibe o campo Valor  
Ambos: exibe os campos Percentual e Valor  
O preenchimento dos campos da aba de "Valores extras" não é obrigatório.  
Os rateios de itens serão definidos de acordo com as seguintes regras:  
A obtenção dos itens do rateio por estado e município serão obtidos seguindo a seguinte precedência:

**Minhas Inspeções:**

* Se o parâmetro de projeto "Bloquear liberação de período se não existir Inspeção em conformidade" estiver marcado, um determinado período somente poderá ser liberado se existir alguma inspeção finalizada com o status de conformidade igual a "Conforme":
Informações - Contratos

**Contratos de serviço e parcela fixa**  
Obtém rateio de estado/município por item medido de contrato, gerando n movimentos;  
Caso não tenha obtido rateio no passo 1, obter rateio de estado/município por contrato, gerando n movimentos;  
Caso não tenha obtido rateio no passo 2,  obter  Estado/município cadastrados no projeto, gerando 1 movimento.  
Caso os itens de rateio não fechem em 100 %, o restante será associado ao estado/município cadastrado no projeto.  
**Contratos de insumos e marco contratual**  
Obter rateio de estado/município por contrato, gerando n movimentos;  
Caso não tenha obtido rateio no passo 1, obter Estado/município cadastrados no projeto, gerando 1 movimento.  
Caso os itens de rateio não fechem em 100 %, o restante será associado ao estado/município cadastrado no projeto.  
A obtenção dos itens do rateio por centro de custo respeitará a seguinte precedência:  
**Contratos de serviço e parcela fixa**  
Obtém rateio de centro de custo por item medido de contrato;  
Caso não tenha obtido rateio no passo 1, obter rateio centro de custo anexo contrato;  
Caso não tenha obtido rateio no passo 2, obter rateio centro de custo da tarefa associada ao item medido recursivamente (tarefa/etapa/obra);  
Caso não tenha obtido rateio no passo 3, obter centro de custo default (definido no processo).  
**Contratos de insumos e Extra- Histograma e Marco Contratual**  
Obter rateio centro de custo anexo contrato;  
Caso não tenha obtido rateio no passo 1, obter rateio centro de custo da tarefa associada ao item medido recursivamente (tarefa/etapa/obra);  
Caso não tenha obtido rateio no passo 2, obter centro de custo default (definido no processo)

**Observação:**  
Caso a soma dos centros de custo não fechem em 100%, o restante é atribuído ao centro de custo default.  
A obtenção dos itens do rateio por produto serão obtidos seguindo a seguinte precedência:

**Contratos de serviço e parcela fixa**  
Obtém rateio de produtos por item medido de contrato;  
Caso não tenha obtido rateio no passo 1 para um determinado item,  utiliza-se o  produto default (definido no processo) para aquele item.  
**Contratos de marco contratual**  
Produto default, definido na tela do processo. É considerado apenas o produto default, o que resultará na geração de apenas um item no movimento gerado.  
**Contratos de insumos**  
Caso o parâmetro Considerar produtos associados no faturamento de contrato de insumo estiver marcado, é exibida uma lista com o produto principal associado a cada insumo consumido. Dessa maneira, será gerada movimentação para cada produto principal do insumo. Se não existir produto principal no cadastro do insumo não é possível prosseguir com o processo até que seja associado um produto principal ao insumo informado.   
Caso o parâmetro Considerar produtos associados no faturamento de contrato de insumo estiver desmarcado, é enviado o produto principal associado a cada insumo consumido. Caso não exista um produto associado a um insumo, é utilizado o produto padrão (default) informado na própria tela de Geração de Integração com Suprimentos/Faturamento.  
Será então gerado um item de movimento por produto. As tarefas, bem como os centros de custo, estarão definidos como rateio do item de movimento.  
**Exemplo:**  
Se as atividades 1 e 2 estiverem rateadas entre os centros de custos 1 e 2, então no item de movimento será apresentado o seguinte rateio:  
Centro de custo1 - Valor/Percentual de rateio - Atividade1  
Centro de custo1 - Valor/Percentual de rateio - Atividade2  
Centro de custo2 - Valor/Percentual de rateio - Atividade1  
Centro de custo2 - Valor/Percentual de rateio - Atividade2

**Observação:**  
Contratos que tem itens associados, tarefas, é possível editar o valor para liberação parcial e para contratos que tem insumos associados é possível editar a quantidade a ser liberada.

Informações - Natureza Orçamentária

Para que a Natureza Orçamentária/Financeira seja enviada no item de movimento, é necessário que o Tipo de Movimento esteja parametrizado para utilizá-la:

A origem da Natureza Orçamentária/Financeira que será enviada no item do movimento, depende da parametrização definida nos Parâmetros de Projeto:

Algumas regras devem ser consideradas para a definição da Natureza:

* Contrato com itens associados (Tarefas):
  + Grupo de Custo/Insumo: Através do produto, o insumo é encontrado onde existe a Natureza definida ou no seu Grupo de Custo;
  + Projeto: Natureza definida no cadastro do Projeto;
  + Tarefa: Natureza definida no cadastro da Tarefa.

* Contrato com objetos associados (Insumos):
  + Grupo de Custo/Insumo: Deve ser considerada a Natureza do insumo consumido ou seu Grupo de Custo;
  + Projeto: Natureza definida no cadastro do Projeto;
  + Tarefa: Natureza definida no cadastro da Tarefa utilizada no consumo.

Geração parcial da integração com Suprimento/Faturamento

É possível determinar o valor da liberação a ser feita durante o processo de Geração de Integração com Suprimento/Faturamento. Para isso, é preciso acessar os parâmetros do projeto pressionando **F6** e, em seguida, ir para a aba Contrato/Liberação. Nessa aba, é necessário marcar o campo destacado abaixo:

**Observação:**  
É importante destacar que o parâmetro só ficará habilitado se não houver nenhuma liberação parcial após sua marcação.

Após a medição do período selecionado, é possível editar o campo "**Valor a Liberar**", permitindo que o valor seja reduzido para um montante menor do que o saldo atual. Nesse caso, é possível realizar uma nova liberação posteriormente para o mesmo contrato.

Os cálculos das retenções, deduções, faturamento e abatimentos de adiantamentos de contrato são realizados proporcionalmente em relação ao valor liberado parcialmente.

* O período somente será considerado totalmente liberado se todo o seu valor for liberado, podendo ser necessário realizar várias liberações parciais para atingir esse valor total.

Informações - Valores de dedução e retenção

Os valores de dedução e retenção preenchidos na tela de liberação do período são determinados com base na parametrização dos campos abaixo e nas definições dos parâmetros do tipo de movimento que será gerado. Esses valores são enviados como desconto para tal movimento, impactando diretamente o valor final.

**Estado/Município**

Outro campo editável é o de Estado e Município. Ao abrir esta tela, as localidades cadastradas no contrato serão exibidas. No entanto, é possível alterar esses dados e gerar uma nova liberação na nova localidade informada.

**Observação:**

* Os itens a serem liberados obedecem a hierarquia de Estado e Município, Produto e Natureza Orçamentária.
* A quebra por Estado e Município ocorrerá somente se o tipo de movimento utilizar Estado e Município. Caso contrário, haverá apenas uma quebra, em que o tipo de movimento será o agrupador dos itens.
* Quando habilitado o parâmetro “Utiliza Cliente para Faturamento”, o cliente definido no contrato será sugerido automaticamente na geração da integração com Suprimentos/Faturamento. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=421385497)
