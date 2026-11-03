---
content_hash: 1017f1910db8001a45fa6d2baec1506027bd0436658dc31480c7b12aa270478b
fetched_at: '2026-06-29T00:09:14.136328+00:00'
page_id: '421385137'
product: rm
source: tdn-rm
title: Alteração Geral de Insumos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385137
version: 3
---

**Alteração Geral de Insumos**

Através dessa funcionalidade é possível realizar alterações em um conjunto de Insumos selecionados através dos filtros:

**Insumos:**

Informe os insumos cujas informações se deseja alterar.

**Grupos de Custo:** Informe os grupos de custo dos insumos que se deseja alterar as informações. Serão selecionados os insumos dos respectivos grupos de custo escolhidos.

**Unidades:**

Informe as unidades dos insumos cujos dados se deseja alterar. Neste caso, serão selecionados os insumos que possuem as unidades escolhidas.

**Por código:**

Informe o código dos insumos que se deseja alterar as informações.

**Todos:**

Esse tipo de filtro seleciona todos os insumos do projeto.

**Observação:**

No uso dos filtros a opção "E" é utilizada para seleção de insumos que atendam a todos os filtros selecionados ao mesmo tempo e a opção "OU" é utilizada para seleção de insumos que atendam a pelo menos um dos filtros utilizados.

**Alterações Gerais**  
    
 **Descrição:**

Informe se a descrição dos insumos alterados ficará em letra maiúscula, minúscula ou só com a 1ª letra maiúscula.

**Nova Unidade:**

Informe qual unidade os insumos selecionados irão adotar.

**Novo Grupo de Custo:**

Informe para qual grupo de custo os insumos selecionados serão alterados.

**Prazo de Ressuprimento:**

Informe a quantidade em dias para qual o Prazo de Ressuprimento dos insumos será alterado. O valor informado neste campo representa a quantidade em dias que o insumo deve chegar para que a tarefa seja entregue na data estipulada.

**% improdutividade:**

Informe qual percentual de improdutividade os insumos selecionados irão adotar.

**Nova Jornada de Trabalho:**

Informe para qual jornada de trabalho os insumos selecionados serão alterados. Somente insumos do grupo DNIT (definido no grupo de custo unitário) A (Equipamentos), B (Mão-de-obra) e F (Transporte) podem ter sua jornada de trabalho definida.

**Transformar Insumo Derivado em Insumo Normal:**

Esta opção realiza a alteração dos insumos que são do tipo derivado para insumo do tipo normal.

**Alteração de Fator k:**

Informe o coeficiente a ser aplicado sobre o fator k dos insumos selecionados e a ação (Adicionar, Multiplicar ou Substituir). O número de casas decimais para o coeficiente obedece ao parâmetro de casas decimais para os coeficientes conforme informado em "Opções | Parâmetros | RM Solum | Projetos". Essa opção só fica visível se o parâmetro de utilização de fator k "Somente Insumos Mão-de-obra de Composições por Produção ou Como Fator Multiplicador aos Coeficientes dos Insumos nas Composições" estiver ativo. Insumos com unidade % não possuem fator k.

**Alteração de Código - Código Inicial:**

Informe o código inicial para a alteração dos insumos. O primeiro insumo recebe este código e o sistema incrementa o código para os insumos subseqüentes. Para isso, é considerada a ordenação por código de insumos.  
 Caso a máscara de insumos esteja parametrizada no projeto, o processo de Alteração Geral de Insumos respeitará a máscara informada. A máscara de insumos pode ser parametrizada em "Parâmetros do projeto| Exibição| Máscaras".

Caso o projeto não possuaparametrização de máscara para o insumo, poderá ser informado qualquer código em até 30 caracteres.

O parâmetro "Usar auto-incremento" define se o código do insumo poderá ou não ser alterado pelo processo de Alteração Geral de Insumos. Caso o parâmetro estiver marcado, o código do insumo não poderá ser alterado pelo processo e se desmarcado, a alteração do código será habilitada no processo.

**Exemplos:**

Considerando que os insumos que serão alterados são AA234 e AA342, e que o código do insumo inicial é AA001, os códigos ficarão da seguinte maneira: AA234 será alterado para AA001 AA342 será alterado para AA002  
 Considerando que os insumos que serão alterados são AA234 e AA342, e que o código do insumo inicial é AA999, os códigos ficarão da seguinte maneira: AA234 será alterado para AA999 AA342 será alterado para AB000  
 Considerando que os insumos que serão alterados são 123AA e 345AA, e que o código do insumo inicial é 987ZZ, os códigos ficarão da seguinte maneira: 123AA será alterado para 987ZZ 345AA será alterado para 988AA

**Nova Condição de Pagamento:**

Informe para qual condição de pagamento os insumos selecionados serão alterados.

**Natureza orçamentária/financeira:**

Informe qual natureza orçamentária/financeira os insumos selecionados irão adotar.  
 **Novo Fracionamento de Insumos:**

Marque a opção "Insumos podem ser fracionados" se desejar que o campo "Este insumo não pode ser fracionado"seja desmarcado automaticamente em todos os insumos selecionados. Marque a opção "Insumos não podem ser fracionados" se desejar que o campo "Este insumo não pode ser fracionado" seja marcado automaticamente em todos os insumos do filtro em questão.

**Hora extra:**

Informe os campos "% min. Hora Extra", "% max. Hora Extra", "% custo unit. Hora Extra" e "Jornada Pdo" para cálculo da hora extra

**Nova Planilha de Custo Horário:**

Informe para qual planilha de custo horário os insumos selecionados serão alterados.

**Célula Valor Produtivo:**

Informe qual célula está localizado o valor produtivo do insumo.

**Célula Valor Improdutivo:**

Informe qual célula está localizado o valor improdutivo do insumo.

**Insumo para contratação:**

Informe para qual o "Tipo do Insumo para Contratação" será alterado o insumo.

**Alterações de Preços**  
 **Modificar preço:**

Selecione o tipo de ação a ser executada. As ações disponíveis são:

* Ativar: permite ativar um preço em todos os insumos selecionados. Informe qual preço dos insumos selecionados ficará ativo. Serão mostrados todos os tipos de preços cadastrados no projeto de acordo com a sua descrição.
* Mudar descrição: permite mudar a descrição de um determinado preço dos insumos selecionados.

**Descrição:**

Informe a descrição do preço a ser criado.

**Valor:**

Informe o valor do preço a ser criado.

**Moeda:**

Informe em qual moeda esse preço está.

**Moeda Indexadora:**

Informe em qual moeda esse preço está indexado. Essa informação não é obrigatória.

**Unidade:**

Informe a unidade em que está sendo criado o preço.

**Valor Improdutivo:**

Informe o valor improdutivo, se o insumo for do grupo A (Equipamentos).

**Moeda:**

Informe em qual moeda o preço está sendo criado.

**Data de Criação:**

Informe a data do preço que está sendo criado.

**Usar Vigência do Preço:**

Marque esse campo se você for fornecer informações referente à vigência do preço que está sendo criado.

**Data de Vigência:**

Informe a data de validade do preço.

**Vigência:**

Marque em quais cronogramas (previsto, realizado e/ou medido) o preço informado deve ser considerado.

**Ativar Preço Criado:**

Marque essa opção se o preço criado deve ser ativado.

**Excluir preço:**

Marque a opção para exclusão de preço.

* Todos os preços: A exclusão de preço acontecerá em todos os preços.
* Todos os que contenham na descrição o texto: Só serão excluídos preços que contenham o texto informado no campo.
* Somente preços inativos: Serão excluídos somente os preços inativos.
