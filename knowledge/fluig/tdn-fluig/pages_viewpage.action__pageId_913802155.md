---
content_hash: c2c46c3c1a33c8e4242e1c9fcd8a455b7e4f68ccf3494de8bd7c082624852aef
fetched_at: '2026-06-28T21:35:31.305546+00:00'
page_id: '913802155'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Exclusivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=913802155
version: 81
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse .

3.\*ndice

# Falando de componente Exclusivo...

---

O componente **Exclusivo** representa um ponto onde o processo pode tomar um caminho ou outro automaticamente, dependendo das condições definidas e dos dados obtidos para atender a uma das condições. Dessa forma, ele permite automatizar decisões e aumentar a produtividade, flexibilizando a personalização de processos e reduzindo possíveis falhas. Ele também facilita a resolução de exceções em tempo real e garante conformidade com normas de governança.

Esse componente permite definir regras claras para compor as condições que serão consideradas para determinar uma rota única na qual o processo deve seguir a partir desse ponto, decidindo assim, o seu destino. Ou seja, ele funciona como uma porta – *gateway* – que direciona a solicitação para a próxima etapa baseando-se em dados que atendam à uma condição.

Para determinar essa rota, ele considera uma informação já existente no contexto da solicitação quando ela chega nesse ponto e, a partir dessa informação, verifica qual condição é atendida por ela e direciona a solicitação para o fluxo correspondente à condição atendida.

As condições são verificadas na ordem em que foram criadas. Assim que uma das condições for atendida, as demais não são verificadas. Como cada condição possui um fluxo de destino vinculado, a solicitação é movimentada para a primeira etapa do fluxo correspondente à condição que foi atendida.

Quando um processo é dividido em duas ou mais rotas utilizando o componente **Exclusivo**, cada rota a ser seguida é determinada por um dado com valor diferente.

#ebecf0

trueExemplo 1  
Em um processo de **Envio de mercadoria**, é preciso decidir qual método de envio utilizar dependendo da região para onde a mercadoria será enviada. Sendo assim, o dado a ser analisado é a **região**, que pode ser **Metropolitana** ou **Interior**. Se for **Metropolitana**, o método de envio será o **Express**. Se for **Interior**, o método de envio será o **Padrão**.

trueExemplo 2  
Em um processo de **Aprovação de despesas**, o gestor responsável por aprovar cada despesa varia de acordo com sua categoria, que pode ser **Equipamento**, **Publicidade**, **Contratação** etc. Dessa forma, o dado a ser analisado é a **categoria** da despesa. Quando a categoria for **Equipamento**, a aprovação deve ser enviada para o gestor de **Infraestrutura**. Se for **Publicidade**, para o gestor de **Marketing** e, quando for **Contratação**, para o gestor de **RH**.

Quando o processo possui um fluxo sincronizado utilizando esse componente, é importante ressaltar que, dentre as entradas que chegam no ponto de sincronização, apenas uma é suficiente para que a solicitação siga adiante, ou seja, não serão aguardados outros fluxos para movimentar a solicitação.

Importante!

Ao utilizar o componente **Exclusivo**, o resultado é auto excludente, ou seja, não há possibilidade da solicitação seguir por mais de uma rota do processo, ela sempre seguirá pela rota da primeira condição atendida. Desse conceito se origina o nome do componente: **Exclusivo**.

## Requisitos para utilização

---

Para utilizar o componente **Exclusivo**, é necessário atentar-se a alguns pontos:

* o fluxo de **entrada** para ele não pode ter retorno, pois como ele se comporta como uma atividade automática, a solicitação sempre seguirá para o fluxo de saída que corresponder à condição atendida;

* se um dos fluxos de **saída** possuir retorno, quando a solicitação retornar, a decisão será executada de forma automática novamente;

* para criar as **condições**, é necessário que já exista um **formulário** vinculado ao processo e, pelo menos, uma **etapa**/**atividade** posterior a ele. Isso porque, para construir as regras de cada condição, é necessário selecionar os campos do formulário que devem ser considerados na verificação da condição e a etapa para a qual a solicitação será enviada quando a condição for atendida;

* ele precisa de, pelo menos, **uma condição** para funcionar corretamente.

## Condição simples

---

A condição simples permite criar as regras a partir da própria interface, definindo a origem dos dados e os operadores para determinar o que deve ser validado. Para cada regra, é necessário definir:

* o **campo** do formulário vinculado ao processo do qual será obtido o valor que será utilizado na comparação e verificação da regra;

* o **operador** que vai determinar qual tipo de comparação será feita: **vazio**, **i****gual a**, **diferente de**, **contendo**, **m****aior que**, **maior ou igual a**, **m****enor que**, **m****enor ou igual a**, **proibido** e **q****ualquer um**;

* a **origem** do valor que será comparado com o valor do campo do formulário, podendo ser um valor vindo de outro campo do mesmo formulário ou um valor fixo inserido manualmente em um campo da regra;

* o **outro campo** do formulário ou o **valor** **fixo** que será comparado com o primeiro campo do formulário, dependendo do que foi definido na **origem do valor**.

A validação da regra ocorre da seguinte forma em relação ao segundo valor a ser comparado:

* se a origem do valor é um **campo de formulário**, ela será feita comparando o **valor** dos **dois campos** do formulário que foram selecionados;

* se a origem é um **valor fixo**, ela será feita comparando o valor do primeiro **campo** do formulário selecionado com o **valor** **fixo** inserido manualmente na regra.

É possível criar múltiplas regras para compor cada condição. E, também, é possível criar múltiplas condições para cada componente Exclusivo.

Importante!

As regras são validadas considerando o operador **E**, ou seja, todas as regras que compõem a condição precisam ser verdadeiras para que a condição seja atendida.

Quando existe apenas uma regra criada para uma condição, essa regra não pode ser excluída, pois é necessário que exista pelo menos uma regra em cada condição para que o componente funcione corretamente.

Dica!

[Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=913802155#Plataforma%E2%9D%99Exclusivo-Adicionarcondi%C3%A7%C3%A3osimples) e saiba como adicionar uma condição simples.

### Exemplos de uso

---

Reunimos aqui alguns cenários utilizando as condições simples no componente Exclusivo. Os exemplos contam com a necessidade de decisão do processo, as condições que serão verificadas pelo componente e o resultado de acordo com a condição atendida.

Clique em cada cenário para ver seus detalhes.

(function() {
function toggleAreas(isExpand, $parent) {
var $items = $parent.find('.panel');
$.each($items, function(idx, el) {
var $arrow = $(el).find('span.cloakToggle').find('span');
var $content = $(el).find('span.cloak');
if (isExpand) {
$arrow.removeClass('cloakDefaultOpen').addClass('cloakDefaultClose');
$content.show();
} else {
$arrow.addClass('cloakDefaultOpen').removeClass('cloakDefaultClose');
$content.hide();
}
});
}
$(document).on('click', '#toggleAll-1', function(ev) {
ev.preventDefault();
var isExpand = $(this).data('expand');
var $parent = $(this).nextAll('.sectionColumnWrapper').first();
toggleAreas(isExpand, $parent);
$(this).data('expand', !isExpand);
});
})();
[Abrir/fechar todos os exemplos](#)]]>#ebecf0

#### @simples1 Reclamação de cliente sobre um pedido na ouvidoria.

@simples1

---

trueCenário  
Em um processo de **Abertura de ouvidoria**, quando um cliente abre uma reclamação, ele precisa informar qual é a categoria do seu problema, se é **qualidade** do produto, **entrega** do produto ou problemas no **atendimento**. Com base nisso, depois da análise prévia da ouvidoria e o envio de um parecer para o cliente, a reclamação é encaminhada para a área responsável pela sua resolução, de acordo com a categoria do problema.

trueCondição 1  
**trueBlueRegra 1**  
→ Campo do formulário **Categoria da reclamação** precisa conter um dado **igual a** **Campo valor qualidade**.

trueCondição 2  
**trueBlueRegra 1**  
→ Campo do formulário **Categoria da reclamação** precisa conter um dado **igual a** **Campo valor entrega**.

trueCondição 3  
**trueBlueRegra 1**  
→ Campo do formulário **Categoria da reclamação** precisa conter um dado **igual a** **Campo valor atendimento**.

Significa que, quando a reclamação chegar no componente Exclusivo, será analisada a categoria do problema do cliente e, a partir disso, a reclamação será encaminhada para o fluxo correspondente à área responsável pela sua resolução.

Vamos supor que o cliente selecionou **Entrega** como a categoria do problema no formulário da reclamação. Nesse caso, a **Condição 2** é atendida e a reclamação é encaminhada para a área de Logística, que precisa analisar o ocorrido e enviar uma solução para o cliente.

#ebecf0

#### @simples2 Aprovação de compra com faixas de valor.

@simples2

---

trueCenário  
Em um processo de **Aprovação de compra**, é necessário que a aprovação seja feita pelo responsável pela alçada de acordo com o valor da compra. Ou seja, se for uma compra de **até R$ 5.000,00**, o próprio **gestor** pode aprovar. Se for entre **R$ 5.001,00** e **R$ 10.000,00**, precisar ser aprovado pelo **diretor**. E, **acima** de **R$ 10.000,00**, é necessário que o **diretor** da área aprove.

trueCondição 1  
**trueBlueRegra 1**→ Campo do formulário **Valor da compra** precisa conter um dado **menor ou igual a** **Campo valor 5000**.

trueCondição 2  
**trueBlueRegra 1**→ Campo do formulário **Valor da compra** precisa conter um dado **maior que** **Campo valor 5000**.  
**E  
trueBlueRegra 2  
→** Campo do formulário **Valor da compra** precisa conter um dado **menor ou igual a Campo valor 10000**.

trueCondição 3  
**trueBlueRegra 1**→ Campo do formulário **Valor da compra** precisa conter um dado **maior que** **Campo valor 10000**.

Significa que, quando a solicitação chegar no componente Exclusivo, será avaliado o valor da compra e será verificada qual condição é atendida com base nesse valor, encaminhando a solicitação para o aprovador correspondente.

Vamos supor que o valor da compra em questão é **R$ 6.500,00**. Nesse caso, a **Condição 2** é atendida, visto que o valor é **maior que R$ 5.000,00** e **menor que R$ 10.000,00**.

#ebecf0

#### @simples3 Solicitação de suporte técnico para o serviço de Internet.

@simples3

---

trueCenário  
Em um processo de **Suporte técnico** de uma prestadora de serviço de Internet, quando um cliente abre uma solicitação de suporte, o primeiro nível de atendimento precisa identificar a possível origem do problema, para que ela seja encaminhada para a área correta oferecer uma solução. Sendo assim, na análise do atendente do primeiro nível, é necessário determinar se a causa está relacionada à ***software***, ***hardware*** ou **conectividade**.

trueCondição 1  
**trueBlueRegra 1**  
→ Campo do formulário **Possível causa** precisa conter um dado **igual a** **Campo valor *software***.

trueCondição 2  
**trueBlueRegra 1**  
→ Campo do formulário **Possível causa** precisa conter um dado **igual a** **Campo valor *hardware***.

trueCondição 3  
**trueBlueRegra 1**  
→ Campo do formulário **Possível causa** precisa conter um dado **igual a** **Campo valor conectividade**.

Significa que, quando a solicitação de suporte chegar no componente Exclusivo, será analisada a possível causa do problema do cliente e, a partir disso, a solicitação será encaminhada para o fluxo correspondente à área responsável pela possível causa.

Vamos supor que o atendente analisou o que o cliente reportou e selecionou **Conectividade** como a possível causa do problema no formulário da solicitação. Nesse caso, a **Condição 3** é atendida e a solicitação é encaminhada para a área de Manutenção de redes, que é a responsável por problemas de conectividade.

## Condição avançada

---

A condição avançada permite criar as regras a partir de codificação, flexibilizando a criação de condições para pessoas mais técnicas que saibam programar e desejam criar expressões avançadas para as condições usando JavaScript.

Para esse tipo de condição, é disponibilizada uma IDE embutida, ou seja, um editor de código onde as expressões avançadas podem ser escritas. O ambiente para codificação permite a escrita de códigos de forma estruturada.

A condição avançada deve ser escrita utilizando expressões **JavaScript** e seguindo a estrutura:

* **Propriedade**: campo do formulário ou variável do processo;

* **Condição**: operadores como ===, >, <, != etc.;

* **Valor**: valor fixo ou outra variável.

No ambiente para codificação, também são disponibilizados ***snippets*** prontos com as **hAPIs** da plataforma para facilitar a criação das condições. Assim, é possível inserir facilmente chamadas e manipulação de dados. Esses *snippets* ajudam a reduzir erros de codificação e aceleram a configuração das condições avançadas.

Além disso, o ambiente para codificação exibe um exemplo de condição avançada para facilitar o entendimento da construção das regras.

Dicas!

[Clique aqui](https://tdn.totvs.com/display/fluig/hAPI) e veja todos os métodos que estão disponíveis por meio da **hAPI** e que podem ser utilizados na criação de condições avançadas.

[Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=913802155#Plataforma%E2%9D%99Exclusivo-Adicionarcondi%C3%A7%C3%A3oavan%C3%A7ada) e saiba como adicionar uma condição avançada.

### Exemplos de uso

---

Reunimos aqui vários cenários utilizando as condições avançadas no componente Exclusivo. Os exemplos contam com a necessidade de decisão do processo, as condições que serão verificadas pelo componente e o resultado de acordo com a condição atendida.

Clique em cada cenário para ver seus detalhes.

(function() {
function toggleAreas(isExpand, $parent) {
var $items = $parent.find('.panel');
$.each($items, function(idx, el) {
var $arrow = $(el).find('span.cloakToggle').find('span');
var $content = $(el).find('span.cloak');
if (isExpand) {
$arrow.removeClass('cloakDefaultOpen').addClass('cloakDefaultClose');
$content.show();
} else {
$arrow.addClass('cloakDefaultOpen').removeClass('cloakDefaultClose');
$content.hide();
}
});
}
$(document).on('click', '#toggleAll-2', function(ev) {
ev.preventDefault();
var isExpand = $(this).data('expand');
var $parent = $(this).nextAll('.sectionColumnWrapper').first();
toggleAreas(isExpand, $parent);
$(this).data('expand', !isExpand);
});
})();
[Abrir/fechar todos os exemplos](#)]]>#ebecf0

#### @avancada1 Aprovação de compra por valor.

@avancada1

---

trueCenário  
Em um processo de **Aprovação de solicitação de compra**, um colaborador preenche um formulário para solicitar uma compra. A solicitação é então analisada pelo componente Exclusivo que verifica o valor total da compra: se o valor for até **R$ 5.000**, vai direto para o **gestor** aprovar, mas se for **acima de R$ 5.000**, vai para a diretoria aprovar.

trueCondição 1  
→ hAPI.getCardValue("vl\_totalCompra")) <= 5000

trueCondição 2  
→ hAPI.getCardValue("vl\_totalCompra")) > 5000

Significa que, quando a solicitação chegar no componente Exclusivo, será avaliado o valor da compra que consta no campo **vl\_totalCompra** do formulário e será verificada qual condição é atendida com base nesse valor, encaminhando a solicitação para o aprovador correspondente.

Vamos supor que o valor da compra em questão é **R$ 4.500,00**. Nesse caso, a **Condição 1** é atendida, visto que o valor é **menor que R$ 5.000,00**.

#ebecf0

#### @avancada2 Aprovação conforme o tipo do item (perecível/não perecível).

@avancada2

---

trueCenário  
Em um processo de **Compras de itens para uso interno**, o colaborador da empresa precisa responder se algum dos itens solicitados é perecível, pois neste caso, precisa passar pela aprovação do setor de Qualidade. Se não, vai direto para aprovação do setor Comercial.

trueCondição 1  
→ hAPI.getValue("itemPerecivel") === "SIM"

trueCondição 2  
→ hAPI.getValue("itemPerecivel") === "NAO"

Significa que, quando a solicitação chegar no componente Exclusivo, será avaliado se existe ou não um item perecível considerando a resposta que consta no campo **itemPerecivel** do formulário e será verificada qual condição é atendida com base nessa resposta, encaminhando a solicitação para o aprovador correspondente.

Vamos supor que **não** existem itens perecíveis na solicitação. Nesse caso, a **Condição 2** é atendida e a solicitação vai diretamente para a aprovação do setor Comercial, sem a necessidade de passar pelo setor de Qualidade.

## Configurar componente Exclusivo

---

**100%true5%**

**01.** No  do processo, clique no componente **Exclusivo** que deseja configurar.

#f2f2f2#f2f2f2

As configurações disponíveis são exibidas na lateral direita.

**02.** Defina um título ou nome para o componente que representa o direcionamento automático da solicitação para uma das etapas possíveis do fluxo do processo, de acordo com o resultado obtido.

#f2f2f2#f2f2f2

O nome também pode ser alterado diretamente no componente, clicando sobre seu nome atual e depois em **Editar**– localizado no lado direito.

#ebecf0

trueExemplo de uso  
Em um processo de **Aprovação de despesas** de acordo com a categoria, o componente poderia receber o nome **Aprovação por categoria**.

**03.** Clique em  **Adicionar condição** para definir as condições que precisam ser atendidas para que a solicitação seja direcionada para a etapa correspondente.

**04.** Em **Nome da condição**, insira um nome para identificar a condição depois de criada.

#f2f2f2#f2f2f2

O nome da condição pode ter até 100 caracteres.

**05.** Selecione o tipo de condição que deseja criar.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Condição simples**: quando selecionada, permite criar as regras a partir da própria interface, definindo a origem dos dados e os operadores para determinar o que deve ser validado. Obtenha mais detalhes em [Condição simples](https://tdn.totvs.com/pages/viewpage.action?pageId=913802155#Plataforma%E2%9D%99Exclusivo-Condi%C3%A7%C3%A3osimples).

* **Condição avançada**: quando selecionada, permite criar as regras a partir de codificação com expressões avançadas usando JavaScript. Obtenha mais detalhes em Condição avançada.

**06.** Se o tipo selecionado foi **Condição simples**, clique em **Regra 1** para expandir e construir a primeira regra para compor a condição.

#f2f2f2#f2f2f2

Se o tipo selecionado foi **Condição avançada**, obtenha as informações desejadas para configuração no .

**07.** Selecione os dados necessários para construir a regra.

#f2f2f2#f2f2f2

**Campo do formulário**  
Campo do formulário vinculado ao processo do qual será obtido o valor que será utilizado para comparação e verificação da regra.

**Operador**Determina o tipo de comparação que será feita. As opções disponíveis são: 

* **vazio**;
* **igual a**;
* **diferente de**;
* **contendo**;
* **maior que**;
* **maior ou igual a**;
* **menor que**;
* **menor ou igual a**;
* **proibido**;
* **qualquer um**.

**Origem do valor para comparação**De onde será obtido o valor que será comparado com o valor do campo do formulário selecionado anteriormente. As opções disponíveis são:

* **Campo do formulário**: quando selecionada, determina que o valor a ser comparado será obtido de outro campo do formulário vinculado ao processo. Nesse caso, é necessário selecionar esse outro campo do formulário no último campo de composição da regra, que é o **Valor a ser comparado**.

* **Campo valor**: quando selecionada, determina que o valor a ser comparado é um valor fixo e será obtido da própria regra. Nesse caso, é necessário inserir manualmente o valor desejado no último campo de composição da regra, que é o **Valor a ser comparado**.

**Valor a ser comparado**O outro campo do formulário ou o valor fixo da regra, dependendo do que foi selecionado na origem do valor:

* se a origem selecionada foi **Campo de formulário**, é necessário selecionar o outro campo do formulário do qual o valor para comparação será obtido;

* se a origem selecionada foi **Campo valor**, é necessário inserir manualmente o valor fixo que será utilizado para comparação.

  Dicas!

  Para os tipos de campos que possuem a propriedade **Valor**, o valor que deve ser inserido aqui é o mesmo que foi inserido no campo **Valor** das propriedades do campo do formulário selecionado para comparação.

  #ebecf0

  trueExemplo  
  Se o campo do formulário selecionado para comparação é o **Categoria da despesa**, do tipo **Combo**, o valor a ser inserido aqui é o mesmo valor inserido no campo **Valor** de uma das opções de seleção definidas para o campo. 

  trueimageVer exemplogreenINLINE

  Se o campo selecionado é um campo simples do tipo numérico, mesmo que ele contenha alguma máscara – como moeda, CPF etc. – o valor a ser inserido aqui é apenas o número, sem pontos, vírgulas ou outros caracteres.

  #ebecf0

  trueExemplo  
  Se o campo do formulário selecionado para comparação é o **Valor da compra**, do tipo **Simples**, **Numérico** e com máscara de **Moeda** em Reais (**R$**), o valor a ser inserido aqui é apenas o número, sem ponto, sem vírgula e sem casas decimais. 

  trueimageVer exemplogreenINLINE

@regras trueClique aqui e veja alguns exemplos de regras

@regras#ebecf0

Em um processo de **Aprovação de despesa**:  
→ Campo do formulário **Categoria da despesa** precisa conter um dado **igual a** **Campo valor publicidade**.

Significa que, quando o solicitante selecionar **Publicidade** como **Categoria da despesa** no formulário, essa condição será atendida e a solicitação será enviada para o fluxo correspondente a ela.

Em um processo de **Aprovação de compra**:  
→ Campo do formulário **Valor da compra** precisa conter um dado **menor que** **Campo valor** **5000**.

Significa que, quando o solicitante informar o **Valor da compra** menor do que **R$ 5.000,00**, essa condição será atendida e a solicitação será enviada para o fluxo correspondente a ela.

Em um processo de **Suporte técnico**:  
→ Campo do formulário **Usuário de abertura** precisa conter um dado **diferente de** **Campo do formulário** **Solicitante**.

Significa que, se uma pessoa (**Usuário de abertura**) está abrindo um chamado solicitando suporte para outra pessoa (**Solicitante**), essa condição será atendida e a solicitação será enviada para o fluxo correspondente a ela.

**08.** Se for preciso adicionar mais regras, clique em  **Adicionar regra** e configure quantas regras forem necessárias para compor a condição.

#f2f2f2#f2f2f2

As regras são validadas considerando o operador **E**, ou seja, todas as regras que compõem a condição precisam ser verdadeiras para que a condição seja atendida.

#ebecf0#f2f2f2

trueExemplo de uso  
→ Campo do formulário **Categoria da despesa** precisa conter um dado **igual a** **Campo valor publicidade**.  
**E**→ Campo do formulário **Valor da despesa** precisa conter um dado **menor que** **Campo valor 5000**.

Significa que o campo **Categoria da despesa** do formulário precisa estar preenchido com o dado **publicidade** **E** o campo **Valor da despesa** precisa estar preenchido com um valor menor do que **R$ 5.000,00** para que essa condição seja atendida e a solicitação seja enviada para o fluxo correspondente a ela.

Para excluir uma regra adicionada, basta clicar em **Excluir**  – localizado no lado direito do quadro da regra. Porém, essa opção não é exibida quando existe apenas uma regra para a condição, visto que ela não pode ser excluída porque é necessário que exista, pelo menos, uma regra para cada condição para o correto funcionamento do componente.

**avancada**

**09.** Se o tipo selecionado foi **Condição avançada**, no editor de códigos, insira a expressão em JavaScript contendo propriedade, condição e valor.

#ebecf0#f2f2f2

trueExemplo

**hAPI.getCardValue("Responsável****") == "Gestor"** → significa que o campo de formulário "Responsável*"* deve ter um valor igual a "Gestor" para atender a condição.

**10.** Por fim, em **Ao atender a condição, segue para a atividade:**, selecione a etapa/atividade para a qual a solicitação deve ser encaminhada quando essa condição for atendida.

**11.** Clique em **Salvar** para salvar a condição e suas regras.

#f2f2f2#f2f2f2

As condições são listadas na ordem em que foram criadas, da primeira para a última.

A validação das condições também considera a ordem em que foram criadas, ou seja, primeiramente é verificada a primeira condição criada. Se ela for atendida, as demais não são verificadas. Se ela não for atendida, segue para a verificação da segunda e assim por diante.

**12.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente **Exclusivo**.

**13.** Na mensagem exibida, clique em **Ok, entendi**.

## Adicionar condição simples

---

**100%true5%**

**01.** No  do processo, clique no componente **Exclusivo** para o qual deseja adicionar uma condição simples.

**02.** Clique em  **Adicionar condição**.

**03.** Em **Nome da condição**, insira um nome para identificar a condição depois de criada.

#f2f2f2#f2f2f2

O nome da condição pode ter até 100 caracteres.

**04.** Selecione a opção **Condição simples**.

**05.** Clique em **Regra 1** para expandir e construir a primeira regra para compor a condição.

**06.** Selecione os dados necessários para construir a regra.

#f2f2f2#f2f2f2

**Campo do formulário**  
Campo do formulário vinculado ao processo do qual será obtido o valor que será utilizado para comparação e verificação da regra.

**Operador**Determina o tipo de comparação que será feita. As opções disponíveis são: 

* **vazio**;
* **igual a**;
* **diferente de**;
* **contendo**;
* **maior que**;
* **maior ou igual a**;
* **menor que**;
* **menor ou igual a**;
* **proibido**;
* **qualquer um**.

**Origem do valor para comparação**De onde será obtido o valor que será comparado com o valor do campo do formulário selecionado anteriormente. As opções disponíveis são:

* **Campo do formulário**: quando selecionada, determina que o valor a ser comparado será obtido de outro campo do formulário vinculado ao processo. Nesse caso, é necessário selecionar esse outro campo do formulário no último campo de composição da regra, que é o **Valor a ser comparado**.

* **Campo valor**: quando selecionada, determina que o valor a ser comparado é um valor fixo e será obtido da própria regra. Nesse caso, é necessário inserir manualmente o valor desejado no último campo de composição da regra, que é o **Valor a ser comparado**.

**Valor a ser comparado**O outro campo do formulário ou o valor fixo da regra, dependendo do que foi selecionado na origem do valor:

* se a origem selecionada foi **Campo de formulário**, é necessário selecionar o outro campo do formulário do qual o valor para comparação será obtido;

* se a origem selecionada foi **Campo valor**, é necessário inserir manualmente o valor fixo que será utilizado para comparação.

  Dicas!

  Para os tipos de campos que possuem a propriedade **Valor**, o valor que deve ser inserido aqui é o mesmo que foi inserido no campo **Valor** das propriedades do campo do formulário selecionado para comparação.

  #ebecf0

  trueExemplo  
  Se o campo do formulário selecionado para comparação é o **Categoria da despesa**, do tipo **Combo**, o valor a ser inserido aqui é o mesmo valor inserido no campo **Valor** de uma das opções de seleção definidas para o campo. 

  trueimageVer exemplogreenINLINE

  Se o campo selecionado é um campo simples do tipo numérico, mesmo que ele contenha alguma máscara – como moeda, CPF etc. – o valor a ser inserido aqui é apenas o número, sem pontos, vírgulas ou outros caracteres.

  #ebecf0

  trueExemplo  
  Se o campo do formulário selecionado para comparação é o **Valor da compra**, do tipo **Simples**, **Numérico** e com máscara de **Moeda** em Reais (**R$**), o valor a ser inserido aqui é apenas o número, sem ponto, sem vírgula e sem casas decimais. 

  trueimageVer exemplogreenINLINE

@regras-2 trueClique aqui e veja alguns exemplos de regras

@regras-2#ebecf0

Em um processo de **Aprovação de despesa**:  
→ Campo do formulário **Categoria da despesa** precisa conter um dado **igual a** **Campo valor publicidade**.

Significa que, quando o solicitante selecionar **Publicidade** como **Categoria da despesa** no formulário, essa condição será atendida e a solicitação será enviada para o fluxo correspondente a ela.

Em um processo de **Aprovação de compra**:  
→ Campo do formulário **Valor da compra** precisa conter um dado **menor que** **Campo valor** **5000**.

Significa que, quando o solicitante informar o **Valor da compra** menor do que **R$ 5.000,00**, essa condição será atendida e a solicitação será enviada para o fluxo correspondente a ela.

Em um processo de **Suporte técnico**:  
→ Campo do formulário **Usuário de abertura** precisa conter um dado **diferente de** **Campo do formulário** **Solicitante**.

Significa que, se uma pessoa (**Usuário de abertura**) está abrindo um chamado solicitando suporte para outra pessoa (**Solicitante**), essa condição será atendida e a solicitação será enviada para o fluxo correspondente a ela.

**07.** Se for preciso adicionar mais regras, clique em  **Adicionar regra** e configure quantas regras forem necessárias para compor a condição.

#f2f2f2#f2f2f2

As regras são validadas considerando o operador **E**, ou seja, todas as regras que compõem a condição precisam ser verdadeiras para que a condição seja atendida.

#ebecf0#f2f2f2

trueExemplo de uso  
→ Campo do formulário **Categoria da despesa** precisa conter um dado **igual a** **Campo valor publicidade**.  
**E**→ Campo do formulário **Valor da despesa** precisa conter um dado **menor que** **Campo valor 5000**.

Significa que o campo **Categoria da despesa** do formulário precisa estar preenchido com o dado **publicidade** **E** o campo **Valor da despesa** precisa estar preenchido com um valor menor do que **R$ 5.000,00** para que essa condição seja atendida e a solicitação seja enviada para o fluxo correspondente a ela.

Para excluir uma regra adicionada, basta clicar em **Excluir**  – localizado no lado direito do quadro da regra. Porém, essa opção não é exibida quando existe apenas uma regra para a condição, visto que ela não pode ser excluída porque é necessário que exista, pelo menos, uma regra para cada condição para o correto funcionamento do componente.

**08.** Por fim, em **Ao atender a condição, segue para a atividade:**, selecione a etapa/atividade para a qual a solicitação deve ser encaminhada quando essa condição for atendida.

**09.** Clique em **Salvar** para salvar a condição e suas regras.

#f2f2f2#f2f2f2

As condições são listadas na ordem em que foram criadas, da primeira para a última.

A validação das condições também considera a ordem em que foram criadas, ou seja, primeiramente é verificada a primeira condição criada. Se ela for atendida, as demais não são verificadas. Se ela não for atendida, segue para a verificação da segunda e assim por diante.

**10.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente **Exclusivo**.

**11.** Na mensagem exibida, clique em **Ok, entendi**.

## Adicionar condição avançada

---

**100%true5%**

**01.** No  do processo, clique no componente **Exclusivo** para o qual deseja adicionar uma condição avançada.

**02.** Clique em  **Adicionar condição**.

**03.** Em **Nome da condição**, insira um nome para identificar a condição avançada depois de criada.

**04.** Selecione o tipo **Condição avançada**.

**05.** No editor de códigos, insira a expressão em JavaScript contendo propriedade, condição e valor.

#f2f2f2#f2f2f2#ebecf0#f2f2f2

trueExemplo

**hAPI.getCardValue("Responsável****") == "Gestor"** → significa que o campo de formulário **Responsável** deve ter um valor igual a **Gestor** para atender a condição.

**06.** Em **Ao atender a condição, segue para a atividade:**, selecione a etapa/atividade para a qual a solicitação deve ser encaminhada quando essa condição for atendida.

**07.** Clique em **Salvar**.

**08.** Ao concluir a inclusão de todas as condições avançadas desejadas, clique em **Fechar**– localizado no canto superior direito.

## Editar condição

---

**100%true5%**

**01.** No  do processo, clique no componente **Exclusivo** do qual deseja editar uma condição.

**02.** Em **Condições criadas**, localize a condição que deseja editar e clique em **Ações**– localizado no seu lado direito.

**03.** Clique em **Editar**.

**04.** Altere os dados desejados nas regras da condição.

**05.** Clique em **Salvar**.

**06.** Ao concluir a edição de todas as condições desejadas, clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Exclusivo**.

**07.** Na mensagem exibida, clique em **Ok, entendi**.

## Excluir condição

---

100%true5%

**01.** No  do processo, clique no componente **Exclusivo** do qual deseja excluir uma condição.

**02.** Em **Condições criadas**, localize a condição que deseja excluir e clique em **Ações**– localizado no seu lado direito.

**03.** Clique em **Excluir**.

**04.** Na mensagem de confirmação exibida, clique em **Excluir condição** para confirmar a exclusão da condição em questão.

#f2f2f2#f2f2f2

Ao excluir uma condição, todas as configurações existentes para ela também são excluídas e não é possível restaurá-las.

**05.** Ao concluir a exclusão de todas as condições desejadas, clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no componente **Exclusivo**.

**06.** Na mensagem exibida, clique em **Ok, entendi**.

## Dúvidas frequentes

---

Confira aqui algumas dúvidas frequentes sobre o componente Exclusivo.

(function() {
function toggleAreas(isExpand, $parent) {
var $items = $parent.find('.panel');
$.each($items, function(idx, el) {
var $arrow = $(el).find('span.cloakToggle').find('span');
var $content = $(el).find('span.cloak');
if (isExpand) {
$arrow.removeClass('cloakDefaultOpen').addClass('cloakDefaultClose');
$content.show();
} else {
$arrow.addClass('cloakDefaultOpen').removeClass('cloakDefaultClose');
$content.hide();
}
});
}
$(document).on('click', '#toggleAll-3', function(ev) {
ev.preventDefault();
var isExpand = $(this).data('expand');
var $parent = $(this).nextAll('.sectionColumnWrapper').first();
toggleAreas(isExpand, $parent);
$(this).data('expand', !isExpand);
});
})();
[Abrir/fechar todas as dúvidas](#)]]>#ebecf0

#### @saiba-mais-1 Qual a diferença entre os componentes Exclusivo, Paralelo e Inclusivo?

@saiba-mais-1

---

Basicamente, a diferença entre esses componentes é:

* **Exclusivo**: decide o destino da solicitação baseado em condições e a direciona para o fluxo da primeira condição atendida. A partir disso, ela segue adiante em um fluxo único.

  #ebecf0

  **trueExemplo**Em um processo de **Aprovação de crédito**, um cliente faz uma solicitação de crédito para um banco e o processo precisa determinar se a solicitação é aprovada ou rejeitada. Para tomar essa decisão, esse componente analisa a pontuação de crédito que o cliente possui no mercado. Se a pontuação for **maior** que **700**, o crédito é concedido e a solicitação segue para as etapas necessárias para que seja liberado ao cliente. Caso contrário, o crédito é negado e a solicitação é finalizada.
* **Paralelo**: divide o fluxo em várias etapas que podem ser executadas em paralelo e, depois de finalizadas, o fluxo se torna único novamente.

  #ebecf0

  **trueExemplo**Em um processo de **Lançamento de produto**, as etapas **Marketing**, **Logística** e **Treinamento de vendas** podem ser feitas simultaneamente. Dessa forma, esse componente divide o fluxo em três etapas e indica o início dessas etapas que serão executadas em paralelo. Quando finalizadas, as três etapas são unificadas pelo componente *Join* e o fluxo volta a ser único.
* **Inclusivo**: é uma junção do Exclusivo e do Paralelo, ou seja, divide o fluxo no número de etapas correspondente ao número de condições que foram atendidas.

  #ebecf0

  **trueExemplo**Em um processo de **Análise de renda**, o banco verifica qual é a renda familiar do cliente para que diferentes tipos de crédito ou investimentos sejam aprovados ou oferecidos. Existem 3 condições:

  1. se a renda for **maior** que **R$ 8.000,00**, o financiamento de automóvel é liberado para o cliente;
  2. se a renda for **maior** que **R$ 15.000,00**, o financiamento de imóvel é liberado para o cliente;
  3. se a renda for **maior** que **R$ 20.000,00**, a compra de títulos do governo é oferecida como investimento para o cliente.

  Vamos supor que um cliente possua a renda de **R$ 18.000,00**. Quando sua renda for analisada, as duas primeiras condições serão atendidas. Neste caso, o fluxo seguirá paralelamente por dois caminhos: o que leva para a etapa **Liberar financiamento automóvel** e o que leva para a etapa **Liberar financiamento imóvel**. A terceira condição não é atendida, por isso, o fluxo não seguirá pelo caminho correspondente a ela.
#ebecf0

#### @saiba-mais-2 O componente Exclusivo pode afetar o desempenho do processo?

@saiba-mais-2

---

Não. O componente Exclusivopor si só não costuma comprometer o desempenho de um processo de forma significativa. No entanto, o impacto no desempenho depende mais do contexto em que ele é utilizado e das decisões associadas a ele.

Se houver muitas condições complexas sendo avaliadas ou se o processo tiver muitos componentes Exclusivos com decisões complicadas em cada passo, isso pode, de fato, afetar o desempenho de forma indireta, mas não por causa do componente em si, mas pela lógica de decisão ou pela quantidade de validações necessárias.

Além disso, em ambientes que exigem processamento de alta carga ou baixa latência, o número excessivo de validação de condições em componentes Exclusivos pode, em alguns casos, aumentar o tempo de execução do processo. Isso seria mais um reflexo da lógica e da complexidade da aplicação do que do componente em si.

No geral, o componente Exclusivo não costuma ser a causa direta de baixo desempenho, mas a forma como ele é aplicado, em conjunto com outras práticas e a complexidade das condições envolvidas, pode influenciar no tempo de execução do processo.

#ebecf0

#### @saiba-mais-3 É possível utilizar múltiplas regras no mesmo componente Exclusivo?

@saiba-mais-3

---

Sim, é possível criar múltiplas regras para cada condição, bem como, criar múltiplas condições para serem validadas em cada componente Exclusivo de um processo.

Porém, vale ressaltar que as condições são validadas na ordem em que são criadas. Por isso, é importante garantir que a lógica de decisão seja clara para evitar que rotas inadequadas sejam seguidas.

Também é importante que exista um fluxo padrão, que funciona como um escape e será seguido quando nenhuma das condições for atendida.

Em resumo, é possível utilizar várias regras e condições, desde que cada rota tenha sua própria expressão condicional. A escolha da rota a ser seguida é feita de forma exclusiva com base na validação dessas condições.

#ebecf0

#### @saiba-mais-4 Quais linguagens são suportadas para criar *scripts* na condição Avançada?

@saiba-mais-4

---

Apenas a linguagem **JavaScript** pode ser utilizada para criar as expressões para compor as condições.

#ebecf0

#### @saiba-mais-5 Como testar se as condições definidas estão corretas?

@saiba-mais-5

---

Para testar se as condições criadas para o componente Exclusivo estão corretas, é possível seguir algumas abordagens:

* **validação manual**: revisar as condições – analisando as expressões e verificando se são lógicas e se não existe sobreposição ou ambiguidades entre elas – e compreender os dados envolvidos – entendendo quais variáveis ou dados são avaliados para garantir que as condições estejam de acordo com o esperado em cada situação;

* **testes**: criar um conjunto de entradas (valores das variáveis) que abrangem as possibilidades de decisão que o componente pode tomar. Depois, executar o processo com essas entradas e verificar se ele segue a rota correta;

* **ferramentas de teste de BPMN**: utilizar alguma ferramenta que ofereça recursos específicos para validação e testes do componente Exclusivo. Essas ferramentas permitem simular a execução do processo, analisar os fluxos e verificar se as decisões tomadas pelo componente estão corretas;

* **revisão lógica de negócio**: contar com a análise colaborativa dos especialistas no negócio pode ajudar a validar se as condições criadas fazem sentido para o objetivo do processo.
#ebecf0

#### @saiba-mais-6 Por que a solicitação parou depois do componente Exclusivo?

@saiba-mais-6

---

Existem alguns motivos pelos quais uma solicitação pode ficar "presa" no componente Exclusivo e geralmente eles estão associados à forma como as condições e lógicas de decisão foram configuradas. Os motivos mais comuns são:

* **condição não atendida**: nenhuma das condições configuradas para o componente foi atendida e não existe um fluxo padrão de escape. Isso pode ocorrer quando as condições não foram configuradas corretamente, não consideraram algum cenário mais específico ou a lógica das condições não foi definida de forma adequada;

* **dados ou variáveis de entrada ausentes ou inválidos**: quando dados ou variáveis que são utilizados para determinar a rota que a solicitação deve seguir não estão presentes no processo ou são inválidas. Por exemplo, um dado ou variável que deveria ter sido preenchida anteriormente e não foi;

* **inconsistência de execução**: se ocorrer alguma inconsistência ou falha técnica na plataforma que está executando o processo no momento de avaliar as condições do componente, o fluxo pode ser interrompido sem ser direcionado para uma rota válida. Isso também pode ocorrer por questões de *timeout* – se o fluxo envolve tempos de espera ou tempos máximos e esses tempos tenham sido atingidos sem que existam definições sobre como lidar com esses casos – e por questões de integração – quando o fluxo depende de dados de uma fonte externa (como API, banco de dados ou integração com outros produtos) e ocorrer alguma falha nessa fonte;

* **falta de fluxo padrão**: não há um fluxo padrão por onde a solicitação possa seguir caso nenhuma das condições seja atendida. É uma boa prática sempre definir um fluxo padrão, pois garante que o fluxo não seja interrompido quando nenhuma condição foi atendida;

* **falhas em subprocesso ou etapas anteriores**: se antes do componente um subprocesso ou etapa falhou ou não foi completada corretamente – não fornecendo as informações necessárias para a decisão, por exemplo – pode afetar a validação das condições e impedir o avanço da solicitação.

Para resolver essas questões, é importante revisar as regras e condições, garantir que as variáveis de entrada estão sendo corretamente inseridas e sempre definir um fluxo padrão para que sempre haja uma rota válida para a solicitação seguir adiante.

Fique atento!

Esta documentação é válida a partir da atualização**Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
