---
content_hash: 09c18145bd8700cea5b99ab9e4238a5723aa98152365b7652b6cbaf41e8e3786
fetched_at: '2026-06-29T00:09:14.238794+00:00'
page_id: '421385163'
product: rm
source: tdn-rm
title: Preço do Insumo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385163
version: 2
---

---

Ao cadastrar um insumo pela primeira vez os campos abaixo aparecerão separadamente a direita da tela e no anexo "Preço do Insumo", sendo que este será inicialmente o preço ativo, podendo trocar.

Se desejar cadastrar mais de uma cotação para o insumo, salve o primeiro e aparecerá uma tabela, onde os outros preços serão cadastrados.

Os campos são:

* **Descrição Preço:** Informe uma descrição para o preço cadastrado do insumo. Este campo será preenchido, por padrão, por "Preço em "data do sistema"", podendo ser alterado.
* **Valor:** Informe o preço unitário do insumo. Não é possível criar preços negativos para insumos.
* **Valor Improdutivo:** Este campo aparecerá apenas para insumos que podem ser utilizados em composição por produção e do tipo "A – Equipamento". Informe o preço deste insumo quando improdutivo.
* **Data Atualização:** Este campo será preenchido automaticamente com a data de atualização do preço unitário.
* **Moeda:** Informe a moeda do preço unitário.
* **Unidade:** Informe a unidade para o preço do insumo.

**Observação**

Caso a unidade do insumo seja alterada, e a nova unidade não possua uma unidade base compatível com a unidade da lista de preços, pode-se alterar a unidade da lista de preços para a unidade do insumo automaticamente.  
 Moeda Indexadora: Informe, se houver, a moeda indexadora do preço do insumo. Ao informar uma moeda indexadora o preço do insumo considerado no cálculo será o preço indexado. O preço indexado de um insumo é o preço ativo dividido pelo fator da moeda de indexação na data de atualização do preço, multiplicado pelo fator da moeda de indexação definida no parâmetro (Data base para indexação). O cálculo do insumo e do projeto levará em consideração a indexação, somente se o parâmetro "Utiliza indexação" estiver habilitado. Parâmetros do Projeto > cálculo > Outros

**Exemplo:**  
 Considere o valor ativo do insumo como 57,17, o fator da moeda na data de atualização do preço como 1,25 e o fator na data atual como 1,87.

Nesse caso, o valor a ser considerado no cálculo do valor do projeto será 57,17 / 1,25 \* 1,87 = 85,53.

**Observações**

* Ao inserir um preço, ele será ativado automaticamente se não existir nenhum preço ativo.
* Ao modificar um preço, a data de atualização será atualizada, automaticamente.
* Aparecerá um ícone de preços na 1ª coluna da listagem, identificando se o preço esta ativo ou não.
* Se o insumo for global, pode-se cadastrar um preço local que será visualizado somente no projeto onde foi criado. Os insumos globais e seus preços globais são cadastrados através do projeto global.   
  Basta estar no projeto global para que os insumos e seus preços sejam globais. O preço global do insumo global só pode ser ativado ou desativado através do projeto global, pois, afetará todos os projetos que o utiliza.
* Quando é feita a edição de um insumo, para alterar os preços do mesmo, as informações modificadas no insumo serão salvas automaticamente.

**Vigência****de preço:**

A vigência é utilizada para que os preços dos insumos possam assumir valores diferentes para diferentes períodos de execução da obra. Todo preço com vigência tem além do valor, dois outros atributos para que se trabalhar: Cronograma de aplicação e Período de Vigência. Para um mesmo cronograma de Aplicação (Previsto, por exemplo) podemos ter mais de um preço vigente. A data da Vigência define o período máximo de aplicação do preço. Além disto, o preço que estiver ativo é usado como preço de períodos que não possuem vigência.

**Exemplo:**

Preço Ativo = R$ 6,00

Vigência até Período 3 = R$ 4,00

Vigência até Período 6 = R$ 5,00

Vigência: Informe, se houver, a data de vigência (validade) do preço do insumo no cronograma indicado no campo 'Aplicação'.

Aplicação: Informe, em qual cronograma (previsto, realizado e medido) a vigência do preço do insumo.

**Observação**

Não é permitido cadastrar duas ou mais vigências com o mesmo período e aplicação para um insumo.

**Vigência em percentual:**

Vigência em percentual permite definir um percentual em um preço vigente, e este percentual ser replicado para os demais preços vigentes cadastrados nos períodos decorrentes do projeto. O percentual pode ser definido para o cronograma previsto, realizado e/ou medido. O preço vigente de menor período (menor data) de um dado Cronograma seja cadastrado com o valor e os demais sejam informados somente por percentual de incremento e decremento. O percentual deverá ser informado em valores absolutos e com sinal. Caso seja negativo implicará em decremento. Para que o projeto trabalhe com vigência em percentual, nos parâmetros do projeto deve-se escolher se utiliza vigência "somente o cronograma" ou "todo o projeto", para qualquer um ficará habilitado à opção "aplicar preços em percentual".

O Parâmetro "aplicar preços em percentual" segue a regra:

1º regra - Criação de um preço para o insumo. Este preço pode ou não esta ativo.

2º regra - Ao criar novos preços, os mesmos serão calculados de acordo com percentuais   
 Alteração no preço de menor período de vigência fará com que ao salvar, os preços dos demais períodos sejam recalculados com base no percentual aplicado.

**Exemplo:**  
  
 1º preço            2º preço                                   3º preço                               4º preço  
 20,00                10% do 1º preço = 22,00           15% do 2º preço = 25,30       -30% do 3º preço =  17,71  
  
**Observações:**

Mesmo trabalhando com vigência em percentual, deve-se informar um preço ativo. Pois quando não definido uma vigência para determinada data, para fins de calculo o sistema busca o preço ativo.

No primeiro preço, caso o usuário informe somente um percentual o valor ficará zerado até que um primeiro preço vigente seja informado.

No segundo preço e demais, caso o usuário não informe um percentual, o sistema calculará o percentual com base no valor.

Será gravado um percentual com até 8 casas decimais. Este processo poderá ser utilizado para informar um preço vigente para o período que já ocorreu.

Neste caso, é inserido um preço com o valor praticado do insumo. Em caso de exclusão do Preço 1, o Preço 2 assumirá como base de cálculo com o valor atual.

Todos os preços serão recalculados. No caso de inclusão de um preço vigente de período menor que o Preço 1, o Preço 1 irá assumir o valor deste preço, caso não tenha percentual, pois o default é 0.

Caso o Preço 1 tenha percentual atrelado (diferente de 0) isto irá alterar o Preço 1 e todos os demais. Isto, porque a inclusão de um novo preço de período vigente menor que o Preço 1 dispara o recálculo dos demais preços.

Caso um preço vigente novo seja criado entre dois preços, todos os preços de período de vigência maior que o período atual serão atualizados por efeito deste novo preço.

Para preço Global, não se define vigência em percentual. Se definido nos parâmetros do projeto, aplicar vigência para todo o projeto, apenas refletira no cronograma previsto.
