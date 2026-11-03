---
content_hash: 8e134120ce7918b49e5a9a90e63c523fd7f23b489ee5c1a0b68eb37c645e8563
fetched_at: '2026-06-29T00:11:55.939521+00:00'
page_id: '864986476'
product: rm
source: tdn-rm
title: Apropriar Custos
type: documentation
url: https://tdn.totvs.com/display/LRM/Apropriar+Custos
version: 2
---

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Equipamentos \ Apontamentos de Equipamentos \ Processos \ Apropriar Custos;
* O parâmetro “Integrado com o SIGA-MNT” deve estar DESABILITADO;  |
* Os Bens só podem estar associado a um insumo preço ativo para que os apontamentos sejam apropriados (caso um Bem esteja associado em mais de um insumo, o apontamento não será apropriado e uma mensagem no apontamento vai informar os insumos onde aquele Bem está associado). Na associação os bens podem ser associados por título ou patrimônio.
* O usuário seleciona na visão os registros para os quais deseja efetuar a apropriação. A apropriação será realizada considerando como valor o preço ativo do insumo associado ao bem no projeto.
* Somente serão apropriados apontamentos cujo status seja igual a Pendente. São selecionadas tarefas associadas ao centro de custo informado no apontamento;
* As seguintes informações serão utilizadas para geração da apropriação:
  + INSUMO: será identificado através da associação do equipamento/bem ao insumo do projeto;
  + QUANTIDADE: a quantidade apropriada é dada diretamente pela quantidade do apontamento (cálculo entre hora inicial e final), ou através de rateio, conforme descrito nos próximos parágrafos;
  + TAREFA: será utilizada a tarefa informada para o apontamento.
* Para apontamentos de horas improdutivas, uma tarefa para apropriação poderá ser previamente parametrizada por projeto;
* Quando existe uma tarefa parametrizada, as horas improdutivas serão apropriadas nesta tarefa;
* Quando não existe uma tarefa parametrizada, as horas são apropriadas da seguinte forma:
  + Recupera-se o somatório dos apontamentos produtivos cujo equipamento, centro de custo e data sejam os mesmos do apontamento improdutivo que se está processado;
  + Para cada apontamento produtivo calcula-se o percentual rateado e a quantidade (rateada) a ser apropriada:

    - Percentual rateado = Quantidade do apontamento produtivo atual / somatório dos apontamentos produtivos;
    - Quantidade apropriada = Quantidade do apontamento improdutivo \* Percentual rateado.
* Caso alguma das informações necessárias para a apropriação não tenha sido informada, a mesma não será realizada, sendo o motivo informado no log do processo. Posteriormente, o usuário deverá informar o dado solicitado na tela edição de apontamentos e executar o processo novamente. Estas informações só poderão ser editadas, caso o registro tenha status “Pendente”;
* Logo após o processo de apropriação, caso a apropriação tenha sido realizada com sucesso, o status dos registros são alterados para “Apropriado” e é salvo na base o Identificador da apropriação realizada.
