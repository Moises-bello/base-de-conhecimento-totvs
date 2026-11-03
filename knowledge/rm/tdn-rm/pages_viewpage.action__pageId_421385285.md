---
content_hash: 4df1f0bfa2ab769c7e6b5961eee5e6d76fc6f37ccdde474f0dc64b57ff95b970
fetched_at: '2026-06-29T00:09:14.863861+00:00'
page_id: '421385285'
product: rm
source: tdn-rm
title: Efetuando Alteração Geral de Composições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385285
version: 3
---

Após ter escolhido quais composições deseja alterar, informe os dados que serão alterados nestas composições. Essa pasta se subdivide em duas subpastas: Cabeçalho e Recursos.  
A pasta Cabeçalho permite as seguintes alterações:  
-Alteração de Código:  
Código Inicial: Informe o código inicial para a alteração. A primeira composição recebe este código e o sistema incrementa o código para as composições subsequentes. Para isso, é considerada a ordenação por código de composições. Se houver composição cadastrada com um código na faixa dos novos códigos, a operação será abandonada.

**Exemplo:**  
Considerando que as composições que serão alteradas são AA234 e AA342, e que o código da composição inicial é AA001, os códigos ficarão da seguinte maneira:AA234 será alterado para AA001AA342 será alterado para AA002  
Considerando que as composições que serão alteradas são AA234 e AA342, e que o código da composição inicial é AA999, os códigos ficarão da seguinte maneira:AA234 será alterado para AA999AA342 será alterado para AB000  
Considerando que as composições que serão alteradas são 123AA e 345AA, e que o código da composição inicial é 987ZZ, os códigos ficarão da seguinte maneira:123AA será alterado para 987ZZ345AA será alterado para 988AA  
   
-Descrição: Informe se a descrição das composições alteradas ficará com as letras todas maiúsculas, todas minúsculas ou só com a 1ª letra maiúscula.  
   
-Nova Unidade: Informe qual unidade as composições selecionadas irão adotar.  
-Tipo da Composição: Informe o tipo da composição desejada (CPU, Por Produção, Por Unidade de Serviço, Turma Típica). Se o tipo informado for "Por Produção", preencha o valor da "Produção por hora".  
-Habilitar Composição Auxiliar: Esta opção fará com que o campo 'Não pode ser Comp. Auxiliar', no cadastro das composições, seja marcado ou desmarcado. Dessa forma, as composições que tiverem esse campo desmarcado podem ser inseridas como recursos em outras composições (composições auxiliares). A composição com este campo marcado não pode ser inserida como recurso de outra composição. Se a composição já estiver cadastrada como recurso de outra composição, ao marcar este campo não será possível a sua inserção em novas composições e as que já estavam cadastradas não sofrerão nenhuma alteração.  
-Fator k: Coeficiente: Informe o coeficiente a ser considerado. Para editar este campo é necessário ser feita parametrização (Aperte F6 ou acesse: "Projeto" > "Construção e Projetos" > "Projetos F6").  
Ação: Informe se o coeficiente informado substitui, adiciona ou multiplica o fator k já existente na composição.  
   
A pasta Recursos permite as seguintes alterações:  
-Substituição de Recursos:   
De: Composição Auxiliar: Selecione a composição auxiliar a ser substituída. Insumos: Selecione o Insumo a ser substituída.  
Para: Composição Auxiliar: Selecione a Composição que substituirá o recurso anterior. Insumos: Selecione o Insumo que substituirá o recurso anterior.  
-Insumos Específicos: Informe qual insumo deseja incluir, excluir ou desativar dos recursos das composições selecionadas.  
-Composições Auxiliares: Informe qual composição deseja incluir, excluir ou desativar dos recursos das composições selecionadas.  
-Fator a ser aplicado na quantidade dos insumos selecionados: Informe a quantidade a ser aplicada sobre os coeficientes dos insumos selecionados e a operação (Multiplicar, Dividir, Somar ou Subtrair) ou informas uma Fórmula do Fator.  
**Observação:**  
Para alterar os coeficientes de insumos ou composições auxiliares, de determinadas composições, utilize os filtros para informar a composição E o insumo/composição auxiliar. A seguir, informe o fator e a operação.
