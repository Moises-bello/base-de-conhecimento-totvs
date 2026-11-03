---
content_hash: f1d83299bd1a8c709322a32e71f8b389106b05dd15f1e218ea235ec4eaff0c44
fetched_at: '2026-06-29T00:09:16.031639+00:00'
page_id: '421385445'
product: rm
source: tdn-rm
title: Insumo Derivado – Aba Insumo Derivado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385445
version: 2
---

---

Para se realizar o acompanhamento da obra com um nível maior de detalhamento e uma maior precisão no controle de gastos, foi criado no sistema um conceito de insumo derivado, onde um insumo pode derivar de outro ou de uma composição.  
 Na aba insumo derivado do cadastro do insumo, foi criado o campo "Tipo do Insumo", com as opções Normal, Derivado ou Receita.

* Insumo Normal: Será tratado como um insumo comum, com hoje é tratado no sistema.
* Insumo Derivado: Caso for este o tipo do insumo, uma aba chamada Insumo Derivado fica habilitada para que seja informados o tipo da derivação, a prioridade de cálculo e a regra de derivação.
* Insumo Receita: Este Insumo será usado somente em associações diretas com serviço e o valor dele quando associado será considerado somente para derivação, não devendo afetar o custo do Projeto. A tarefa se comporta como se estivesse desativada. Em relatórios como a curva ABC o usuário realizará filtro por Grupo de Custo para evitar que ele apareça. O Grupo de Custo é quem informa que os insumos deste grupo são do tipo receita ou normal.

O insumo deriva de acordo com uma regra. Associando de uma forma indireta vários insumos, grupos de custo ou composições ao insumo derivado como itens de derivação.   
 O preenchimento da regra de derivação é simples bastando informar o item de derivação e o percentual.  
 Aba Insumo Associado: para se associar um insumo do tipo normal diretamente ao insumo do tipo derivado, na regra de derivação basta apontar o insumo e o seu percentual de derivação.

**Observação:**

Na aba insumo associado também pode conter um insumo derivado.  
 Outra forma de realizar a derivação é através do Grupo de Custo. Na regra de derivação deve ser informado o Grupo de Custo e o seu percentual de derivação. Neste caso todos os insumos que fazem parte do grupo farão parte da regra de derivação.

**Tipo de derivação**  
 Derivação de quantidade para a composição, Derivação de valor para a composição e Derivado para Tarefa x Cronograma.  
 A fórmula utilizada nos tipos de derivação são cadastradas no menu cadastro Fórmulas

**Derivação de quantidade para a composição** – O campo fórmula deve ser preenchido com uma fórmula capaz de buscar a informação da quantidade de cada insumo dentro da composição conforme regra de derivação.  
 Exemplo:  
 Vale Transporte, EPI, Refeição, etc : Com base na quantidade de pessoas calculada pelo módulo de equalização o Insumo Derivado Vale Transporte diz período a período a quantidade e o valor do total de vale-transporte necessário para aquele período.  
 Combustível: Com base no número de horas de veículos e equipamentos na composição o insumo derivado de Combustível irá ser incluído como uma linha na composição derivando um determinado percentual da quantidade em função do coeficiente dos veículos e equipamentos na composição.

**Derivação de valor para a composição** – O campo fórmula deve ser preenchido com uma fórmula capaz de buscar a informação do valor de cada insumo dentro da composição conforme regra de derivação.   
 Exemplo:  
 Encargos Sociais, Impostos, Adiantamentos e Retenções. Pelos exemplos dados a derivação de valor se dará sempre com um insumo derivado associado a uma tarefa.

**Derivação de quantidade e valor para a composição -** O campo fórmula deve ser preenchido com uma fórmula capaz de buscar a informação do valor e da quantidade de cada insumo dentro da composição conforme regra de derivação.  
 Exemplo:  
 Combustível: Com base no número de horas e custo horário de veículos e equipamentos na composição o insumo derivado de Combustível irá ser incluído como uma linha na composição derivando um determinado percentual de quantidade e valor em função do coeficiente dos veículos e equipamentos na composição.

**Derivado para Tarefa x Cronograma** – O campo fórmula deve ser preenchido com uma fórmula capaz de buscar a informação dos insumos derivados associados às tarefas, pode ser feito da seguinte forma:

* Cada insumo derivado seria associado para um item da planilha de serviços pelo usuário;
* A quantidade do serviço desse insumo derivado será calculada através de fórmula que considere a quantidade ou valor dos seus itens de derivação do projeto, conforme cadastrado. Neste caso esta fórmula irá retornar o valor/quantidade de cada período onde este será transportado para o cronograma do serviço. O Somatório de todos os valores dos períodos dará a quantidade daquele serviço.  
  **Exemplo de Cálculos:** TABTRFPLANDERIVADO('VALORPLANEJADO')   
  **Observações:**

Não é permitido criar Insumos Derivados Globais ou Inserir Itens de Derivação para Insumo Globais. Não é permitido criar Insumos Derivados Globais ou Inserir Itens de Derivação para Insumo Globais. Para associar itens de derivação é preciso que o Insumo seja do Tipo Derivado. Ao alterar um insumo derivado o sistema faz: Se o Insumo se tornou do tipo Normal, nada é feito no sentido de removê-lo das composições que atualmente está presente. Mas ao calcular o projeto, não haverá mais o cálculo com base nas fórmulas de derivação e a relação de itens de derivação será apagada. Se o Insumo Derivado teve um ou mais itens de derivação retirados: Se o tipo de Insumo Derivado é de "Quantidade ou Valor na Composição" todas as composições onde ele aparece serão reavaliadas. Caso não exista na composição um recurso que seja parte da lista de itens de derivação, o insumo derivado será retirado. Sempre ao manter (modificar, incluir, excluir) os itens de derivação deverá: excluir todos os insumos derivados de composições que não mais fazem sentido e incluir nas composições que por ventura entram no critério de derivação. Somente faz isto para insumos derivados do tipo Quantidade ou Valor na Composição. Sempre ao manter uma composição (modificar, incluir, excluir recursos) deverá avaliar a necessidade de um insumo derivado. Isto vale para Importações, Cópias, Alteração Geral ou alterações no cadastro de composição. Na regra de derivação os insumos derivados poderão se "desativar" os itens de derivação, e desta forma, ele passará a se comportar como se tivesse sido excluído.  
 **Exemplo de utilização do insumo derivado:**  
 O insumo derivado pode ser usado para se calcular a quantidade de vales transportes que serão usados pelo grupo de custo mão de obra, para isso siga os passos:

1. Inclua um insumo e defina o seu tipo do insumo como "Derivado";
2. Defina os campos Descrição, Unidade e Grupo de Custo da mesma maneira como é feito para Insumo Normal;
3. Na aba Insumo derivado defina o tipo de derivação, para este exemplo vamos colocar como Derivado para Tarefa x Cronograma;
4. No campo Fórmula de Tarefa, devemos definir uma fórmula que traga a quantidade de recursos do tipo mão de obra que estão alocados no projeto, para obtermos a quantidade exata de vales transportes que serão gastos no projeto: Neste caso vamos utilizar a fórmula:

EQUALIZDERIVADO(NUMPERIODO, 'EFETIVOADOTADO');  
 EQUALIZ\_DERIVADO (*Período,Campo*) : Retorna o valor do *Campo* na tabela MEQUALIZACAOINSUMO para o insumo derivado de uma tarefa para o *Período* passado, considerando os percentuais da regra de derivação. O Insumo derivado e projeto considerado são os que estiverem no contexto de cálculo.  
 Se o grupo de custo e o insumo na regra de derivação ocasionarem repetição o cálculo da função deve considerar a repetição.

* Após o cadastro da fórmula devemos inserir a Regra de Derivação, neste nosso exemplo vamos colocar o grupo de custo mão de obra como regra de derivação;  
  Ao finalizar o cadastro do Insumo Derivado, devemos associá-lo a tarefa na planilha de atividades.  
    
  **Sugestão para fórmula de Cálculo de Insumos derivados(Menu cadastros Fórmulas)**:  
    
   Exemplo: Insumo Derivado do tipo Vale Transporte:  
   EQUALIZ\_DERIVADO(NUMPERIODO, 'EFETIVOADOTADO'). Retorna a quantidade de efetivos que serão adotados nos períodos do projeto, definido na equalização de insumos.  
    
   Exemplo: Insumo Derivado do tipo Encargos Sociais:  
   EQUALIZ\_DERIVADO(NUMPERIODO, 'CUSTOADOTADO'). Retorna o total do custo adotado de cada insumo por periodo, CUSTOADOTADO é o custo levando em consideração o Efetivo Adotado, Jornada, Custo do Insumo e Hora Extra Adotada.   
    
   Exemplo de Cálculos Para Insumos Derivados na Composição:  
    
   COMPIMSDERIVADO ('QUANTIDADE') Utiliza a quantidade do recurso associado a tarefa.  
   COMPIMSDERIVADO('VALORUNIT') Utiliza o valor unitário do recurso associado a tarefa.  
   COMPIMSDERIVADO ('VALORTOTAL') Utiliza o valor parcial do recurso associado a tarefa.
