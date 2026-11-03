---
content_hash: a7547b364212bacd7a3c574e15d3503b2487b36bc6fde1aacb6cd5e8ecaead82
fetched_at: '2026-06-29T00:09:16.253727+00:00'
page_id: '421385494'
product: rm
source: tdn-rm
title: Geração de Pedido Extra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385494
version: 25
---

---

Com a finalidade de controlar os gastos de Pedido Extra, ou seja, Pedido além do planejado, foi criado o processo de Pedido Extra, onde são controladas todas as movimentações de pedidos, autorização do pedido, quantidade pedida para determinada tarefa e principalmente as pessoas envolvidas no processo.

Para realização do processo, toda a parametrização da integração da Requisição do TOTVS Obras e Projetos com o Gestão de Estoque Compras e Faturamento deverá ser realizada anteriormente, inclusive a integração de movimentos e inclusão de locais de estoque.

No Pedido Extra é possível definir a utilização do Preço Orçado:

**Utiliza preço orçado:** Este campo indica se o pedido usará o preço orçado no envio para suprimentos. (Geração do movimento)  
**Calculo do preço orçado:**O preço será recuperado do insumo respeitando o parâmetro de vigência de preço. (Será utilizado o campo Valor com Leis). Caso não seja possível recuperar o preço do Insumo o preço será recuperado do produto.

Preço Calculado

Para utilização do preço orçado é importante que o preço do insumo esteja calculado.

Também é possível definir a possibilidade de alteração de preço nos itens que não possuem insumo, ou seja realizar a definição do preço orçado no momento da inclusão do item.

Para ativar a integração com o Gestão de Estoque Compras e Faturamento, seguir os passos:

* Acessar os Parâmetros do Projeto | Integração | Integração CRM | Pedido Extra;
* Informar os campos;
* Para cadastro do Grupo de Atendimento no CRM, acessar CRM | Workflow | Grupos;
* Para cadastro do Tipo de Atendimento no CRM, acessar CRM | Workflow | Tipo de Atendimento;
* Para cadastro do parâmetro do tipo de atendimento, acessar Anexos | Parâmetros do Tipo de Atendimento;
* Para cadastro de Etapas do tipo de atendimento, acessar Anexos | Etapas;
* Para cadastro do Fluxo das etapas do tipo de atendimento, acessar Anexos | Fluxo de Etapas.

Para configuração de usuários no CRM, acessar o menu Atendentes, cadastrar um atendente e associar o usuário ao mesmo. Esse processo deve ser realizado tanto para o usuário aprovador quanto para o usuário não aprovador.

O atendente inicial deverá estar vinculado ao aprovador e o grupo deve ser um grupo para o qual esse mesmo atendente esteja vinculado.

Para envio de e-mail ao usuário aprovador, acessar CRM | Ambiente | Parâmetros Globais.  
Configurar os dados do e-mail do usuário remetente, para que ao ser enviado o Pedido Extra para aprovação, o usuário aprovador receba um e-mail de aviso desde que o mesmo possua um e-mail devidamente cadastrado no cadastro de atendentes. 

Para incluir um Pedido Extra no TOTVS Obras e Projetos, basta acessar a funcionalidade através do Menu Planejamento | Geração de Pedido Extra.  
Com a tela aberta, acionar o botão "Incluir" e informar os campos.

Os itens são incluídos através do anexo | Item de Pedido Extra, acionar o botão "Incluir", preencher os campos necessários e "salvar".

Após incluir os itens, é necessário enviar o pedido para aprovação, através do processo "Enviar Pedido Extra para Aprovação" e em seguida o Sistema deverá alterar o status do pedido para: "Em Aprovação".

Para itens que forem para uma tarefa de valor cotado e esta tarefa ainda possuir saldo e para os itens que forem de contrato e o mesmo ainda possuir saldo, o pedido será aprovado automaticamente.

Algumas opções podem ser parametrizadas, através dos Parâmetros do Projeto | Integração | Suprimentos / Faturamento | Geral:

* **Utilizar Fluxo de Aprovação para Pedido Extra:**Se o parâmetro estiver desmarcado, o Pedido Extra deverá ser criado com status de aprovado (Processo de aprovação deverá ficar desabilitado) e deverá permitir o processo de Gerar Movimento. Se o parâmetro estiver marcado, o Pedido Extra deverá passar pelo processo de aprovação antes do processo de gerar movimento (Não será possível o Processo de gerar movimento antes da aprovação finalizada).
* **Permitir Aprovação de Pedido Extra através de Senha:**Se o parâmetro estiver marcado, o usuário não aprovador poderá realizar o processo de aprovação através do Login e Senha do Aprovador.   
  O usuário sem permissão terá acesso ao processo de Aprovação**,** desde que o mesmo possua o Login e Senha do aprovador.  
  Neste caso, ao acessar a lista de pedidos ou itens do pedido, acionar o processo de aprovação, em seguida o sistema emitirá uma tela para Login e Senha do usuário aprovador, após realizar o login corretamente, o pedido ou item terá passado pelo processo de aprovação escolhido pelo usuário.
* **Aprovar Tarefa Valor Cotado pelo Saldo:** Se o parâmetro estiver marcado, o pedido será aprovado automaticamente apenas se existir saldo de verba para tarefa do Pedido Extra. Caso o parâmetro esteja desmarcado, sempre será solicitado a aprovação do Pedido Extra.
* **Permitir Motivo de Pedido Extra Vazio:**Com esse parâmetro selecionado, o usuário poderá deixar sem preenchimento o motivo do pedido extra.

Não serão permitidas alterações no Pedido Extra que já foi enviado para Aprovação.

**Aprovação do Pedido no TOTVS Obras e Projetos**

Quando um pedido possuir itens e somente um for analisado e aprovado o sistema exibirá mensagem informando que os demais estão pendentes.

**Exemplo:**

*Início do processo [Finalizar Aprovação de Pedido Extra]*

*Pedido 0000002 possui os itens (5,6) não analisados.*

*Fim do Processo [Finalizar Aprovação de Pedido Extra]*

Para realizar a aprovação, estão disponíveis as seguintes opções:

* **Aprovação do pedido como um todo:**Selecionar o pedido e acionar Processos | Aprovar Pedido Extra, ou Menu de atalho (Aprovar Pedido Extra), ou abrir o pedido no modo de edição e acionar botão "Aprovar", o sistema emite mensagem de sucesso, altera o status do pedido para: "Aprovação Finalizada", salva a data e o nome do aprovador e habilita os botões do processo Gerar Movimento.
* **Reprovação do pedido como um todo:**Selecionar o pedido e acionar processos | Reprovar Pedido Extra, ou Menu de atalho (Reprovar Pedido Extra), ou abrir o pedido no modo de edição e acionar botão "Reprovar" , o sistema emite mensagem de sucesso, altera o status do pedido para: "Aprovação Finalizada" e salva a data e o nome do aprovador.
* **Aprovação Item a Item:**Selecionar o pedido com status pendente e acionar o processo de aprovação desejado na barra de tarefas ou acessar cada item no modo de edição, acionar os botões: "Aprovar" para aprovação total, para aprovação parcial, acionar "Aprovação Parcial" e indicar a quantidade que deseja aprovar, para reprovação do item, acionar "Reprovar", ou acionar "Em analise" para que o item fique em analise, caso queira realizar o processo de aprovação posteriormente.

Caso desejar relatar a justificativa pela ação tomada, preencher o campo, após todos os itens analisados e realização do processo de aprovação, finalizar o processo em: Finalizar Aprovação, em seguida o sistema altera o status do pedido para: "Aprovação Finalizada".

**Envio do Pedido Extra**  
É possível enviar o Pedido Extra através das opções:

* **Gerar 1 Movimento:**Selecionar o pedido na visão de Geração de Pedido Extra, após selecionar o pedido, clique no botão Gerar 1 Movimento ou Processos | Gerar 1 Movimento**.**  
  Através deste processo, o Pedido Extra se tornará em apenas um pedido do Gestão de Estoque Compras e Faturamento. Se as obras tiverem locais de estoque diferentes, será gerado um movimento para cada obra. A data de entrega do movimento será a data de início do primeiro período previsto.  
  Após o processo, o sistema altera o status do pedido extra para "Enviado ".
* **Geração de Movimentos para o Protheus com Controle de Status - Integração (EAI 2.0):**Apesar de estar no mesmo processo, a geração do movimento foi separada internamente do processo de integração. Assim, caso haja erros de integração, os movimentos e consequentemente todos os cálculos efetuados continuam salvos na base e passíveis de serem reenviados para o sistema integrado.  
  Para esse controle, foi acrescentado um novo status no Fluxo dos Pedidos para que o usuário final visualize os movimentos pendentes de integração. Ou seja, caso sejam gerados movimentos no RM e algum desses não seja integrado corretamente, o usuário final deverá somente ajustar a inconsistência e reenviar o movimento para integração.  
  Enquanto esse movimento não for corrigido e reenviado pelo usuário, este ficará com o status: "Em Suprimento/Faturamento com Movimentos não Integrados".
* **Gerar Movimento por Data:**Selecionar o pedido na visão de Pedido Extra, após selecionar o pedido, clique no botão Gerar movimento por Data ou Processos | Gerar Movimento por Data**.**  
  Através desse processo, serão gerados N movimentos de acordo com os períodos planejados, onde para cada período o sistema criará um movimento correspondente no Gestão de Estoque Compras e Faturamento,   
  A data de entrega dos itens será a data correspondente ao inicio de cada período.

Em ambas as gerações de movimentos, será gerado um movimento por cada local de estoque e filial.

As quantidades dos produtos a serem enviadas ao faturamento, serão sempre as quantidades aprovadas.

Os produto reprovados não serão enviados ao faturamento.

No momento de enviar o pedido para o Suprimento/Faturamento gerando apenas um movimento ou gerando movimento por data, será possível informar manualmente o fator de conversão para insumos específicos, a fim de chegar-se o mais próximo possível da quantidade real necessária do insumo na etapa corrente do projeto. Para isso, basta acessar o TOTVS Obras e Projetos | menu Orçamento | Insumos | Cadastros | pasta Identificação e marcar o parâmetro "Fator de Conversão Variável".

**Edição de Pedido Extra**

Para editar um pedido de material extra, basta clicar no pedido desejado e realizar a edição dos campos habilitados.

**Item do Pedido Extra:**

Na edição do item do pedido extra, é possível visualizar se o item possui algum vínculo, com Contrato ou [Acordo Corporativo](https://tdn.totvs.com/display/LRM/Acordo+Corporativo):

Um pedido poderá ter itens com diferentes vínculos, dependendo da parametrização do projeto, e gerando diferentes tipos de movimentos.

No caso de um projeto que utiliza Acordo Corporativo, é possível definir nos parâmetros qual a [prioridade de utilização ou a ordem para seleção do acordo](https://tdn.totvs.com/pages/viewpage.action?pageId=421385497), assim como um [tipo de movimento específico para pedidos](https://tdn.totvs.com/display/LRM/Tipos+de+Mov.+de+Pedidos) que possuem item de acordo.

Apesar da inclusão do item sugerir o Acordo conforme definição dos parâmetros, o usuário poderá alterá-lo caso houver necessidade.

Os movimentos poderão ser gerados separadamente, dependendo do acordo, assim como da data de entrega.

**Copiar Pedido Extra:**

* Na tela do processo terá um loopkup para o Projeto, esse campo será preenchido com o Projeto atual e o cliente pode alterar.
* Na tela vai ter um campo de Local de estoque que virá com o local de estoque do pedido atual. Se trocar de projeto tem que validar se o novo projeto tem esse local de estoque
* Na final do processo, se não tiver a tarefa com o mesmo código vai logar a informação e não copiar o item
* No final do processo se não tiver o motivo, vai copiar o motivo para o projeto de destino.
* O objeto de contrato associado ao item será copiado apenas se o projeto de destino for o mesmo do projeto de origem.
* O preço orçado dos itens será o mesmo do pedido de origem.

**Exclusão de Pedido Extra**  
Para a execução do processo, acessar a lista de Pedidos Extra, selecionar o item ou o pedido que deseja excluir e acionar o botão "Excluir".  
Não será permitida a exclusão de um item pertencente a um pedido, cuja quantidade de itens do pedido seja = 1.  
Não será permitida a exclusão de um item ou do pedido cujos movimentos já foram processados pelo Gestão de Estoque Compras e Faturamento.

Para os movimentos com status "Em Suprimento/Faturamento com Movimentos não Integrados", a exclusão dos movimentos continuam de forma transparente para o usuário, não importando se o movimento já está Integrado ou com status de "Em Suprimento/Faturamento com Movimentos não Integrados", basta executar o processo de "Excluir Movimentos" para que esse movimento seja excluído e o pedido possa sofrer alterações novamente.  
Caso a exclusão do movimento não ocorra por inconsistências de integração, seguirá o mesmo fluxo de status apresentado anteriormente.

Informações Complementares

---

[Campos Complementares do Pedido de Material Extra](http://tdn.totvs.com/pages/viewpage.action?pageId=463822019&moved=true)

 

 

[Gerar Workflow de Aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=577914914)

[Cancelar Workflow de Aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=577924689)
