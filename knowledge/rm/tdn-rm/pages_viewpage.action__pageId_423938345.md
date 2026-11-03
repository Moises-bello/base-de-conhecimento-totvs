---
content_hash: 05c5c8e8ed649e49814350bc31774e4544c2a14c40602123fc7b2083ce418af6
fetched_at: '2026-06-29T00:09:26.634829+00:00'
page_id: '423938345'
product: rm
source: tdn-rm
title: Composição de Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938345
version: 6
---

A constituição de patrimônios a partir do item da nota, trata de um recurso opcional no processo de Integração com o Totvs Gestão de Compras. Disponível a partir da versão 12.1.9 do Totvs Gestão Patrimonial, o sistema possibilita através dessa parametrização, constituir um patrimônio especifico através de determinados itens de uma nota fiscal.  
   
Ver Exemplo 1  
   
A tela de composição de patrimônio está organizada da seguinte forma:  
**Informações da nota selecionada:**   
   
Informações da nota selecionada que posteriormente será integrada. Sistema não permitirá edição de nenhum campo apresentado.  
   
**Itens da Nota:**  
 Serão apresentados os itens que compõem a nota fiscal selecionada e que posteriormente serão manipulados pelo usuário para forma o patrimônio.

**Quantidade Original:** Quantidade que foi lançada na nota fiscal.  
**Valor Aquisição Original:** Esta informação será carregada conforme seleção da opção Considerar no Valor de Aquisição (Preço Unitário, Valor Unitário, Valor Financeiro, Fórmula valor do Patrimônio)  
**Valor Base Depreciação Original:** Esta informação será carregada conforme seleção da opção Considerar no Valor Base de Depreciação (Preço Unitário, Valor Unitário, Valor Financeiro, Fórmula valor do Patrimônio)  
**Valor Aquisição (Lançar):** Valor de aquisição que será considerado ao constituir o Patrimônio, este valor será preenchido automaticamente ao selecionar o item da nota e poderá ser alterado pelo usuário conforme necessidade.    
   
**Valor Base Depreciação(Lançar):** Valor base depreciação que será considerado ao constituir o Patrimônio, este valor será preenchido automaticamente ao selecionar o item da nota e poderá ser alterado pelo usuário conforme necessidade.    
**Quantidade(Lançar):** Quantidade que será considerada ao constituir o Patrimônio, esta informação será preenchida automaticamente ao selecionar o item da nota e poderá ser alterada conforme necessidade do usuário.

Observação:  
Quando no campo "Considerar no Valor de Aquisição" for selecionado "Valor Financeiro", o sistema não irá aplicar a regra Valor x Quantidade Informada, pois o Valor Financeiro já contempla o total do item da nota. Sendo assim, a regra inverte. O sistema irá considerar Valor / Quantidade Original para identificar o valor unitário de cada item, o resultado será o Valor x Quantidade Informada.  
   
 **Não calcular valor Aquisição (Lançar) ou valor Base depreciação (lançar) conforme a quantidade digitada**  
   
Quando a opção "Não calcular valor Aquisição/Base depreciação conforme a quantidade digitada" estiver marcada o sistema não irá alterar automaticamente o Valor Aquisição e Valor Base depreciação quando for alterado o campo quantidade.  
   
Exemplo:   
Quantidade 2, Valor aquisição: 662,00, Valor Depreciação: 662,00  
Quantidade 1, Valor aquisição: 662,00, Valor Depreciação: 662,00  
   
Quando a opção estiver desmarcada, ao informar a quantidade o sistema irá calcular automaticamente o campo "Vlr. Aquisição" e "Vlr. Base Depreciação".  
   
Quantidade 2, Valor aquisição: 662,00, Valor Depreciação: 662,00  
Quantidade 1, Valor aquisição: 331,00, Valor Depreciação: 331,00  
   
**Facilitadores:**  
**Botão Descrição:**  O sistema irá adicionar no campo "Descrição" do formulário de composição de Patrimônio a descrição correspondente ao item selecionado, respeitando a opção parametrizada no campo "Descrição do Patrimônio" informada na etapa tipos de campos.  
**Botão Unidade:** O sistema irá adicionar no campo "Unidade" do formulário de composição de Patrimônio a unidade correspondente ao item selecionado.  
**Botão Observação:** O sistema irá adicionar no campo "Observação" do formulário de composição de Patrimônio o histórico correspondente ao item selecionado.  
**Botão Item como único Patrimônio:** O sistema irá adicionar o item selecionado como um único patrimônio a ser integrado. Ou seja, o patrimônio será integrado isoladamente, não poderá ter a quantidade distribuída para outros patrimônios, a quantidade será a quantidade do item e não poderá ser alterada.  
   
**Constituição do Patrimônio:**Formulário que deverá ser preenchido com as informações que irão compor o novo patrimônio conforme os itens da nota fiscal que foram selecionados anteriormente.  
A medida que o usuário seleciona item que irá compor o patrimônio, algumas informações nesta tela serão preenchidas automaticamente e também poderão ser alteradas, outras informações deverão ser complementadas.   
   
**Centro de Custo:** Se a opção "Trazer o centro de custo do item da nota para o patrimônio" estiver marcada, o sistema irá preencher este campo. Selecionando mais de um item e o Centro de Custo entre os itens forem diferentes será emitida uma mensagem de aviso.  
**Localização:** Se existir amarração com o centro de custo, o sistema irá preencher automaticamente.  
**Departamento:** Se a opção "Trazer o departamento do item da nota para o patrimônio" estiver marcada, o sistema irá preencher o Departamento. Se for selecionado mais de um item e o Departamento entre os itens forem diferentes, será emitida uma mensagem avisando a diferença.  
**Responsável:** Se na etapa "Tipos de campos" estiver com o responsável preenchido, este campo será preenchido com a mesma informação.  
**Código do Grupo de Patrimônio:** O sistema irá preencher o grupo do patrimônio conforme o grupo informado no produto relacionado ao item da nota, se foi selecionado mais de um item e o código do grupo for diferente entre os itens, será emitida uma mensagem avisando a diferença.  
**Valor de Aquisição:**  Campo não editável.  
Este campo representa o somatório do valor de aquisição dos itens da nota que foram selecionados para compor o Patrimônio e posteriormente será o valor de aquisição do patrimônio que está sendo constituído.  
**Valor Base de Depreciação:** Campo não editável.  
Este campo representa o somatório do valor base de depreciação dos itens da nota que foram selecionados para compor o Patrimônio e posteriormente será o valor base de depreciação do patrimônio que está sendo constituído.  
   
**Gerar um patrimônio para cada item da quantidade:**O sistema desmembrará as quantidades dos itens da nota criando um cadastro para cada quantidade do item.  
   
**Botão Constituir patrimônio:**Sistema irá criar o patrimônio conforme as informações preenchidas.  
   
**Botão Limpar todas informações preenchidas:**Sistema irá limpar todos os campos preenchidos  
   
**Patrimônios Formados:**Nesta etapa da composição será apresentada a listagem dos patrimônios que serão constituídos. O usuário poderá conferir as informações de cada campo e havendo necessidade de alteração, o patrimônio deverá ser selecionado e excluído, para que seja realizada novamente a constituição deste registro.  
   
Caso a nota a ser integrada tenha notas de devoluções associadas, o sistema irá desconsiderar nas quantidades, a quantidade que consta na nota de devolução.  
   
Ver Exemplo 2  
   
Composição de Patrimônio marcando a opção "Trazer rateio de centro de custo do item de movimento para o rateio gerencial do patrimônio". O sistema irá agrupar os rateios dos itens que irão compor o patrimônio e recalcular o percentual conforme o valor base de depreciação do patrimônio formado.  
   
Ver Exemplo 3  
   
Uma vez que um item da nota foi distribuído para um patrimônio, o somatório do valor deste item nos patrimônios deve ser igual ao valor de aquisição original / valor base de depreciação original, levando em consideração a quantidade  
   
Ver Exemplo 4  
   
**Acesso a nota através do cadastro de patrimônio**  
No cadastro de patrimônio é possível ter acesso a nota através do anexo "Composição de Patrimônio (Nota fiscal de Compra)".
