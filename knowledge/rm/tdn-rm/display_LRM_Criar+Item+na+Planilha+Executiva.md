---
content_hash: bb0dc724611795e68f885094befe5b1718191f8ef433e4d22a6eaaf5feea0d7e
fetched_at: '2026-06-29T00:11:27.609636+00:00'
page_id: '727937245'
product: rm
source: tdn-rm
title: Criar Item na Planilha Executiva
type: documentation
url: https://tdn.totvs.com/display/LRM/Criar+Item+na+Planilha+Executiva
version: 12
---

**Criar item:** Ao abrir a planilha executiva pela primeira vez será exibida a seguinte mensagem:

Para criar item basta acionar o botão **"Criar Item"** ou poderá optar por **"Importar XLS"**. Para mais informações sobre a importação clique em: Importar Planilha Executiva do Excel**.**

**Criar Item:** Nesta opção serão exibidas 3 abas:

* **Dados do Item:** Nesta aba cadastramos todas as informações do item, e alguns desses campos são obrigatórios, por isso estes estão sinalizados e serão descritos na sequência:

**Código:** oCódigo é um campo obrigatório no cadastro do Item, não pode ser editado após salvar e, pode ou não possuir uma máscara, caso assim esteja definido no ;

**Nome:** Nome para identificação do Item que, assim como o código, é um campo obrigatório no cadastro;

**Descrição:** Descrição breve do Item;

**Descrição completa:** Descrição mais detalhada do Item;

**Código Auxiliar:** Código Auxiliar do Item caso deseje;

**Disciplina:** Disciplina do Item, caso queira classificar, assim como as tarefas, por área de atuação, por exemplo;

**Quantidade:** Quantidade do Item, que também é um campo obrigatório;

**Unidade:** Unidade de medida do Item, que deverá ser informada por ser mais um campo obrigatório;

**Valor Unitário:** Valor Unitário e obrigatório do Item;

**Valor Total:** Valor Total do Item com base na quantidade e valor unitário informados. É um campo calculado e por essa razão não é um editável.

* **Vínculos:**Na aba de Vínculos, será possível selecionar uma ou mais tarefas, que serão vinculadas ao item, informando seus respectivos percentuais:

Clicando na aba **Vínculos**, o usuário poderá **Localizar Tarefa,** bastando informar o código ou descrição, e preencher o **Percentual do item na tarefa**.

Caso o usuário não esteja de posse das informações da tarefa, ao clicar na lupa, disponível no campo de **Localizar Tarefa,** serão apresentadas as tarefas disponíveis para serem vinculadas:

Também é possível efetuar uma pesquisa nessa tela, quando a quantidade de tarefas for muito grande:

Em seguida, basta selecionar a tarefa:

Retornando à tela anterior, agora com a tarefa aparece preenchida e com o percentual disponível para a respectiva tarefa informado, podendo alterá-lo para menos caso preferir:

Clicando em **Aplicar,**  a tarefa estará vinculada ao item e visível na parte inferior da tela, que irá listar todas as Tarefas associadas ao item, e seu respectivo percentual for vinculado:

Clicando no ícone de um lápis localizado do lado direito da tarefa vinculada, é possível editar o percentual da tarefa associada ao item:

Será exibida a tela para informar o novo percentual e aplicar:

     Caso deseje desvincular uma tarefa que está associada ao item em criação/edição; será necessário clicar no ícone da Lixeira, localizado no canto direito, na linha da tarefa em questão, conforme destacado na imagem abaixo:

Será exibida uma mensagem com a opção de voltar para a edição ou confirmar a exclusão do item:

Optando pela exclusão, o vínculo será removido e a tarefa não estará listada entre as tarefas associadas ao item; porém, ainda será necessário clicar no botão Salvar do item, para efetivar a exclusão:

**Observações da Planilha Executiva:**

* A PlanilhaExecutiva permite a inclusão de item sem a obrigatoriedade de quantidade, valor unitário e unidade para os items que não são de último nível.
* Quando alterar um item da planilha para um nível que que não possuirá vínculos e planejamento o sistema passa a excluir os vínculos e planejamento.
* Se o item da planilha for de último nível porque foi ate o final da máscara irá obrigar o preenchimento da unidade, quantidade e valor.
* Se não for de último nível aceitará nulo nos campos quantidade , valor unitario e unidade.
* Se informar a quantidade maior que zero o item passa a ser considerado de último nível.
* Não será permitido passar um item da planilha para último nível quando a mesma possuir filhos.
* Não deixará cadastrar um filho para item de último nível.

* **Planejamento /Avanço Físico:**

Nessa aba, será possível informar as datas e durações, programadas e reais, assim como o percentual concluído do item.

Obs: Os campos:

* Data Início Cedo
* Data Fim Cedo
* Data Início Tarde
* Data Fim Tarde

Serão alimentados pelo PERT da Planilha Executiva.
