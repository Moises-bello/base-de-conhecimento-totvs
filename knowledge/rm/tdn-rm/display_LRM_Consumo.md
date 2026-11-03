---
content_hash: 16f408c46d684de5e46761819b60183a309de610d78f7375a84d625ee7861fc6
fetched_at: '2026-06-29T00:11:45.116534+00:00'
page_id: '819496901'
product: rm
source: tdn-rm
title: Consumo
type: documentation
url: https://tdn.totvs.com/display/LRM/Consumo
version: 2
---

## Apropriação Direta e Medição de Consumo

Alguns produtos que são utilizados pelos objetos de manutenção, principalmente equipamentos, são aplicados sem a necessidade de abertura de uma ordem de serviço. Isto ocorre devido à intensidade do processo (número de vezes que é realizado) e na maioria dos casos a simplicidade da intervenção.

Tais apropriações devem ser controladas para que seja possível mensurar o consumo, movimentar o estoque e apurar os custos destes materiais. Assim, o RM Officina dispõe de um recurso que proporciona controlar tal aplicação de maneira prática e atendendo a intensidade do processo que é a “Apropriação Direta de Produtos”. Os produtos objetos deste processo são chamados de “Produtos Apropriáveis”.

As peças com controle de vida útil são substituídas por meio de uma intervenção que demanda a emissão de uma ordem de serviço registrar a troca.

**Produtos Apropriáveis**  
Estes produtos são normalmente combustíveis, lubrificantes ou qualquer consumível utilizado para constantemente para o funcionamento de um equipamento, máquina, veículo e etc.

**Parametrização**  
Informe os Tipos de Objeto de Manutenção que recebem Produtos Apropriáveis em “Gerais / Parâmetros / Tipos de objeto de manutenção” marcando “apropriação direta de produto?”

Ao habilitar o tipo de Objeto de Manutenção para receber apropriação direta será disponibilizado no cadastro do Objeto de Manutenção Anexo – Produtos do Objeto de Manutenção o campo para informar o produto e a opção para informar que este é “Produtos Apropriável”, o seu consumo e qual é o seu índice de acompanhamento. Essa mesma parametrização pode ser feita no anexo “Produto(s)” do cadastro de Tipo de Objeto de Manutenção por Tipo, Modelo ou SubModelo. Para associar o produto ao Objeto de Manutenção é preciso executar o processo “Atualiza Produtos do Objeto de Manutenção”.

Acesse o menu Operações / Apropriação Direta de Produtos. Através do Wizard é possível realizar, de uma só vez, as apropriações de uma mesma data para vários Objetos de Manutenção.

Na primeira tela informa-se o movimento que será utilizado para registrar a apropriação direta.

Na segunda tela através do filtro selecionam-se os Objetos e efetuam-se os lançamentos. Com as teclas de atalho “Ctrl+0” e “Ctrl+P” é possível alternar entre o Objeto e os Produtos.

Na última tela tem-se o resumo da apropriação antes do processamento e ao editar a apropriação tem-se o resumo da mesma.

**Avaliação de Índice de Acompanhamento de consumo**  
Ao realizar a apropriação, se o produto apropriável estiver associado a um Índice de Acompanhamento de consumo, o sistema irá gerar um registro para o índice com o consumo. Este pode ser consultado na aba “Índice de Acompanhamento” do cadastro do Objeto de Manutenção. Na apropriação direta de produto, é possível informar os campos referentes às tabelas de classificação do produto, para que sejam levados para o movimento do RM Nucleus. No último passo da apropriação existem dois botões com a seguinte descrição “Campos opcionais do movimento” e “Campos opcionais do item” onde poderá informar as classificações para o movimento e para os seus itens.
