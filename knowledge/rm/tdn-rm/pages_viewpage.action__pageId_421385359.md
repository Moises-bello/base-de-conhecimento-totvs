---
content_hash: 9a8d0b2089a64012df040a5036cd36026d01c918318843a7c51f559679a5053d
fetched_at: '2026-06-29T00:09:15.374950+00:00'
page_id: '421385359'
product: rm
source: tdn-rm
title: Contratos (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385359
version: 60
---

Nessa página foram detalhados os inúmeros parâmetros de projeto aplicados aos contratos:

**Geral**

**Utilizar status do contrato:** Utiliza status definido para o contrato.

**Utilizar detalhamento de itens:** Quando marcado, esse parâmetro incidirá somente em contratos de serviço, marco contratual e parcela fixa, que forem do tipo a pagar.

**Histórico a ser inserido na criação do contrato:** Informe chapa do responsável e o status inicial do contrato, por default o contrato será "EM ANDAMENTO".

**Permite Alteração da Data na Prorrogação do contrato:** Com esse parâmetro marcado, ao alterar o histórico do contrato de "Paralisado" para "Em Andamento" a data de prorrogação será sugerida com a possibilidade de ser alterada, com o parâmetro desmarcado, o contrato e aditivos serão prorrogados considerando o cálculo de dias corridos em que o contrato ficou paralisado. Inicialmente o parâmetro estará marcado, aba geral.

Para obter uma melhor experiência e controle, aconselhamos a utilização do parâmetro de projeto ‘Utiliza Status do Contrato’ (Também localizado em Parâmetro de Projeto -> Contrato –> Geral –> Utiliza Status do Contrato).

**Utilizar Valor do Reajuste na Medição (PI + R):** Ao ativar este parâmetro o sistema passa a permitir a informação dos valores medidos/consumidos do preço inicial contratado e do reajuste dos itens/objetos separadamente.

Para os projetos que possuem contratos com o tipo de reajuste igual a "**Por Contrato**" ou a aplicação do reajuste á "**Valor Atual**" o parâmetro de Utiliza Valor do reajuste na medição (PI + R) estará desabilitado para marcação.

Caso o projeto já tenha algum contrato com período de reajuste, o parâmetro ficará desabilitado para marcação. Para conseguir efetuar essa alteração, será necessário , já que o sistema passa a se comportar de forma diferente, gerando saldo de reajuste que será abatido nas medições.

**Permite Produtos e Serviços no mesmo pedido de Faturamento Direto:** ao marcar será possível incluir produto e serviço num mesmo pedido de faturamento direto. Desmarcando deverá incluir um pedido para cata tipo de produto.

**Utilizar mais de um Cliente/Fornecedor no contrato:** Permite informar mais de um cliente/fornecedor, o campo para seleção poderá ser preenchido na tela de medição ou na tela de geração de movimento para Suprimento/Faturamento. O cadastro de  deverá ser realizado previamente no respectivo anexo de Contrato, ficando visível para seleção, seja na tela de medição, quanto na tela de geração do movimento.

**Histórico a ser inserido na criação do contrato:** Informa se a chapa do responsável e o status inicial do contrato.

Observação:

O campo Chapa do responsável não é um campo de preenchimento obrigatório e o status inicial do contrato será "Em andamento".

****Utilizar moeda no contrato:** Permite que o contrato tenha sua própria moeda a partir da data de base de conversão**

**Associação de itens e objetos**

**Não associar itens/objetos em mais de 100% da quantidade orçada (Contratos A Pagar):** Caso este parâmetro esteja habilitado, na associação itens/objetos ao contrato não será permitida a associação em quantidades superiores à quantidade orçada. A não ser que o contrato seja do tipo A Receber.   
**ATENÇÃO:** Essa validação não é realizada para insumos do tipo SOMENTE CONTRATAÇÃO.

**Permitir contratação com valor superior ao orçado (Contratos A Pagar: Serviços, Forn. de Material e Insumos):** Caso este parâmetro esteja habilitado, na associação itens/objetos ao contrato não será permitida a associação em valores superiores ao valor total orçado para o item/objeto. A não ser que o contrato seja do tipo A Receber.  
**ATENÇÃO:** Essa validação também é realizada para insumos do tipo SOMENTE CONTRATAÇÃO.

**Calcular contrato automaticamente após execução da associação de itens:** Calcula projeto após associação de itens.

**Utiliza insumos para contratação:** Ao habilitar este parâmetro, no cadastro de Insumos será apresentado o anexo de .

**Permitir associar ao Contrato itens com quantidade zero (Prest. Serviço, Parc. Fixas e Marco Cont.)** Quando habilitado, este parâmetro deve permitir associar ao contrato itens com quantidade zero. Este parâmetro contempla contratos dos tipos: Prestação de Serviços, Parcelas Fixas e Marco Contratual.

**Permitir que itens [Tarefas/Insumos] contratados sejam associads com outro preço unitário no aditivo** Ao habilitar esse parâmetro sistema permitirá a inclusao do mesmo itm com preços unitários diferentes no aditivo.

**Finalidade do Contrato Extra:**

Extra - Histograma: Ao marcar está opção, somente os insumos não planejados no projeto poderão ser associados ao contrato.

Extra: Ao marcar está opção, os insumos planejados e não planejados poderão ser associados ao contrato.

**Períodos**

**Bloquear a edição de períodos anteriores a períodos medidos e liberados:** Quando marcado esse parâmetro, os períodos anteriores ao último período liberado não poderão ser editados, ou seja, não poderão ser criados períodos complementares ou períodos de estorno. Neste caso se o período seguinte estiver simplesmente medido o sistema vai permitir a edição.

**Consistir Datas do Contrato com Datas do Projeto - (Inicio e Término):**

**Reprogramar os períodos subsequentes na prorrogação do contrato:** Com esse parâmetro marcado, ao alterar o histórico do contrato de "Paralisado" para "Em Andamento" os períodos que ainda serão medidos e liberados deverão ter suas datas reprogramadas considerando a nova data de prorrogação do contrato, com o parâmetro desmarcado, o contrato e aditivos serão prorrogados e o usuário terá a possibilidade de criar novos períodos para o contrato. Aba períodos.

**Medição**

**Considerar centros de custo da tarefa na medição:** Se habilitado este parâmetro o centro de custo informado na tarefa será considerado no momento da medição do período.

**Utilizar Status de Medição:**

* Caso esteja habilitado os períodos do contrato começam a ter os seguintes status: Fechado e Aberto.
  + Para alterar os status do período deve-se executar os processos: Encerrar período e Reabrir período.
  + Ao criar um período, o novo período tem status Aberto e nesse status é possível apenas realizar medições no período. Liberar Período e Gerar Integração com Suprimentos/Faturamento não são permitidos nesse status do período.
  + Períodos fechados não são passíveis de medição, serão permitidos somente os processos Liberar Período e Gerar Integração com Suprimentos/Faturamento.

**Permitir medição/consumo superior a 100%**

Sempre permitir: Permite que a medição acumulada até o período seja superior a quantidade total contratada.

Solicitar senha: Solicita senha quando a medição acumulada até o período for superior a quantidade total contratada.

Nunca permitir: Não permite que a medição acumulada até o período seja superior a quantidade total contratada somada a Aditivos de contrato caso o mesmo possua.

Situações possíveis:

Usuário Supervisor: Pode realizar medição acima de 100% estando definido qualquer parâmetro ('Sempre permitir', 'Solicitar senha', 'Nunca permitir').

Usuário Não supervisor, com acesso no perfil à: "Autoriza medição superior a 100% mediante senha". Parâmetro 'Sempre Permitir': Realiza medição acima de 100%. Parâmetro 'Solicitar Senha': Realiza medição acima de 100%. Parâmetro 'Nunca permitir': Não realiza medição acima de 100%

Usuário Não supervisor, sem acesso no perfil à: "Autoriza medição superior a 100% mediante senha". Parâmetro 'Sempre Permitir': Realiza medição acima de 100%. Parâmetro 'Solicitar Senha': Realiza medição acima de 100%, mediante senha. Parâmetro 'Nunca permitir': Não realiza medição acima de 100%.

**ATENÇÃO:** Para contratos do tipo A RECEBER, as validações de medição acima de 100% não se aplicam, pois contratos a receber não possuem trava de associações e medições acima de 100%.

Observações

* A senha de autorização deverá ser de um usuário supervisor ou de um usuário que tenha em seu perfil, definido o acesso: "Autoriza medição superior a 100% mediante senha".
* A permissão de acesso 'Autoriza medição superior a 100% mediante senha' definida no perfil do usuário, permite que o usuário efetue medições superiores a quantidade contratada, através de sua senha pode autorizar esse tipo de medição a outros usuários, durante o lançamento da medição.

Lembrando que para verificar a utilização do acesso à: "Autoriza medição superior a 100% mediante senha". Você deve ir em Cadastros -> Segurança -> Perfis, abrir o perfil desejado e na aba 'Acesso a Menus' verificar se a opção localizada em Cadastros -> Contratos -> Autoriza medição superior a 100% mediante senha, esta definida como 'Permitir Acesso' ou 'Proibir Acesso'.

* Os parâmetros "solicitar senha" e "nunca permitir" não se aplicam ao usuário supervisor.

**Utiliza aposentadoria especial** Parâmetro "Não Utiliza": Não será exibido o campo relacionado a aposentadoria especial no sistema Parâmetro "Apenas na Tarefa": O campo aposentadoria especial será exibido na aba "Outros" edição de tarefas (Serviços e Atividades) e no processo da planilha "Atualização Múltipla de Registros" Parâmetro "Apenas no Insumo": O campo aposentadoria especial será exibido na aba "Identificação" do insumo e no processo de "Alteração Geral de Insumo" Parâmetro "Na Tarefa e no Insumo": O campo aposentadoria especial será exibido na aba "Outros" edição de tarefas (Serviços e Atividades), no processo da planilha "Atualização Múltipla de Registros", na aba "Identificação" do insumo e no processo de "Alteração Geral de Insumo"

**Controle da última medição do contrato (encerramento)** Define a medição realizada como última do contrato e inicia o processo de encerramento. O usuário poderá configurar o comportamento do campo, com as seguintes opções:

* Não Utiliza - essa será a opção inicial, definida na criação do projeto;
* Default - Desmarcado: o campo será exibido desmarcado por padrão na tela, e o preenchimento não será obrigatório;
* Default - Marcado: o campo será exibido marcado por padrão na tela, também sem obrigatoriedade de preenchimento;
* Obrigatório Preenchimento: o usuário deverá, obrigatoriamente, selecionar uma das opções ao realizar a medição (marcado ou desmarcado); caso contrário, não será possível avançar para a próxima etapa do processo.

**Grandeza principal de medição do contrato** Selecione qual a grandeza será utilizada na medição **Quantidade** ou **Valor**, refinando os cálculos e saldos, afim de reduzir diferenças de arredondamento.

**Liberação**

**Permitir calcular retenção sobre valor total:**

Se parâmetro estiver habilitado a retenção da liberação de contratos é calculada sobre:

     \* VALOR TOTAL DA MEDIÇÃO + VALOR DE REAJUSTE (se houver).  
Ex.:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VLR. TOTAL DA MEDIÇÃO | %REAJUSTE | VLR. REAJUSTE | VLR. TOTAL MEDIÇÃO + VLR. REAJUSTE | % DEDUÇÃO | VLR. DEDUÇÃO | VLR TOTAL - VLR. DEDUÇÃO | %RETENÇÃO | VLR. RETENÇÃO |
| 100,00 | 50% | 50 | 150 | 10% | 15 | 135 | 50% | 75 |

Se o parâmetro estiver desabilitado a retenção da liberação de contratos é calculada sobre:

     \* (VALOR TOTAL DA MEDIÇÃO + VALOR DE REAJUSTE (se houver) ) - Valor de Dedução.  
Ex.:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VLR. TOTAL DA MEDIÇÃO | %REAJUSTE | VLR. REAJUSTE | VLR. TOTAL MEDIÇÃO + VLR. REAJUSTE | % DEDUÇÃO | VLR. DEDUÇÃO | VLR TOTAL - VLR. DEDUÇÃO | %RETENÇÃO | VLR. RETENÇÃO |
| 100,00 | 20% | 20 | 120 | 20% | 24 | 96 | 20% | 19,20 |

**Consistência entre Pedidos de Material e Contratos:** Consiste quantidade de pedido e contrato do mesmo item.

Quando marcado, os pedidos de material e contratos existentes serão considerados para que a quantidade contratada não seja maior que a quantidade orçada.

Se os parâmetros "Não associar itens/objetos em mais de 100% da quantidade orçada (Contratos A Pagar)"  e "Consistência entre Pedidos de Material e Contratos" estiverem marcados não será permitida a contratação de valor superior ao orçado, isso porque a consistência e feita entre os valores associados ao contrato e ao pedido de material.

**Desagrupar produtos do rateio ao enviar para Suprimentos / Faturamento:** Se na medição do item existir o mesmo produto de rateio default para varias tarefas, com o parâmetro "Desagrupar produtos do rateio ao enviar para Suprimentos / Faturamento" ativo ao liberar a medição para o Suprimentos / Faturamento será listado o mesmo produto de acordo com o número de tarefas que o tem como produto default.

Exemplo:

Tarefa A utiliza produto XX como Produto de rateio default.

Tarefa B utiliza produto XX como Produto de rateio default.

Tarefa C utiliza produto XX como Produto de rateio default.

Ao liberar medição para o Suprimentos/Faturamento este produto será listado 3 (três) vezes na tela de movimentos do Suprimentos/Faturamento.

Porém, se necessário Agrupar os produtos na tela de movimentos do Suprimentos/Faturamento  é necessário marcar nos parâmetros do tipo de movimento no Suprimentos / Faturamento possível o agrupamento de itens. (Outras movimentações - clique em parametrizar, Clique em item - identificação 2/2 e ative o parâmetro "Agrupar itens repetidos".

**ATENÇÃO:** Se o tipo de movimento estiver com o parâmetro ativado "Gera Apropriação" na integração com projetos, o parâmetro "Agrupar itens repetidos" não ficara habilitado.

**Não permitir que a data de liberação  da medição  seja menor  que a data do período:** Caso essa opção esteja habilitada, não será permitida a liberação para o TOP, Financeiro e para o Suprimentos/Faturamento quando a data da liberação for menor que a data final do período. Caso contrário o período é liberado sem restrições.

Apropriar Liberação em (Pedido ou Nota Fiscal):

Visando viabilizar fluxos alternativos para Apropriação de Custos quando integrado ao BackOffice Protheus serão criados novo parâmetro de projeto e na tela de contratos responsáveis por informar o momento da apropriação do mesmo. Atualmente o processo viabiliza somente a apropriação a partir da Nota Fiscal retornada pelo BackOffice Protheus, sendo este também informado como o valor padrão do novo parâmetro criado.

Produto da liberação (Contrato de insumos):

Produto associado ou default (quando não houver produto associado): Ao marcar está opção, o produto cadastrado na aba "Produtos de Suprimentos/Faturamento" do cadastro do insumo, será apresentado na tela do processo "Gerar integração com suprimentos/faturamento" do contrato, posteriormente enviado para o movimento. Caso o cadastro de insumo não possua produto informado na aba "Produtos de suprimentos/faturamento", será considerado o produto cadastrado na aba "Default" do contrato.

Produto associado: O produto cadastrado na aba "Produtos de Suprimentos/Faturamento" do cadastro do insumo, será apresentado na tela do processo "Gerar integração com suprimentos/faturamento" do contrato, posteriormente enviado para o movimento.

Produto default: O produto cadastrado na aba "Defaults" do contrato, será apresentado na tela de geração da integração suprimentos/faturamento para geração do movimento.

**Discriminar valores de retenção, dedução e adiantamento:** [Clique aqui e veja um exemplo do funcionamento do parâmetro na prática.](https://tdn.totvs.com/pages/viewpage.action?pageId=650484111)

Para utilizar esse parâmetro deverá ser configurada  a formula C . Nesse cenário o campo "Desconto" e "Retenção" do item de movimento terá sua edição bloqueada.   
Ao gerar o movimento com essa parametrização os valores de dedução e de retenção serão enviados ao Suprimentos/Faturamento e terão o seguinte comportamento:

O somatório das deduções vai para o campo "Valor Deduzido" do item do movimento no módulo Suprimentos/Faturamento. O somatório das retenções vai para o campo "Valor Retido" do item do movimento no módulo Suprimentos/Faturamento.

Caso tenha **Adiantamento**será enviado o valor para o campo Valores Financeiros - Valores - "Desconto" do movimento.

Para habilitar o campo  "Valor Retido" (Retenção) e "Valor deduzido" (Desconto) acesse o Totvs Gestão de Estoque, Compras e Faturamento | Parâmetros | Gestão de Estoque, Compras e Faturamento | Selecione o tipo de movimento desejado | Etapa: Item - Valores Financeiros 2/2 | Habilite o campo de "Retenção" e "Dedução" | informe a opção desejada "Usa Valor, percentual ou ambos".

Com o parâmetro discriminar marcado, no contrato de insumo o sistema irá considerar o parâmetro de "Produto da liberação (Produto associado ou default, associado e default)" enviando sempre a quantidade na criação do pedido.

**Enviar retenção como desconto na liberação do período:** Ao gerar o movimento com essa parametrização os valores de dedução e de retenção serão enviados ao Suprimentos/Faturamento e terão o seguinte comportamento:

O valor do campo "Valor total retido/deduzido" da liberação do período será enviado para o campo "Desconto" do movimento no módulo Suprimentos/Faturamento.

Somente para os contratos de insumo ao combinar os parâmetros "Considerar produtos associados no faturamento de contratos de insumos" e "Enviar retenção como desconto na liberação do período", o sistema consegue enviar a quantidade real consumida no faturamento do contrato, pois a dedução e a retenção serão descontadas apenas no movimento e não no Totvs Obras e Projetos. Será enviado o valor bruto e as deduções e retenções serão enviadas para o campo desconto do movimento, garantindo a integridade do valor e da quantidade consumida no contrato.

Observação

Se o parâmetro 'Discriminar valores de retenção e dedução' e 'Enviar retenção como desconto na liberação do período' estiverem desmarcados ao gerar o movimento com essa parametrização nenhum valor será enviado para os campos "Desconto" e "Valor retido" do movimento no módulo Suprimentos/Faturamento.

Se o parâmetro de 'Discriminar valores de retenção e dedução' estiver marcado, automaticamente o parâmetro 'Enviar retenção como desconto na liberação do período' será desmarcado.

**Discriminar quantidade e preço dos itens no movimento (Contrato de Insumos):**

Ao ser marcado esse parâmetro o sistema irá automaticamente travar o campo da fórmula dos contratos, considerando a formula C e passará a enviar a quantidade e preço dos itens consumidos no contrato de insumo. No envio dos itens ao movimento , o sistema respeitará a informação fornecida no campo Produto da Liberação (Contrato de Insumos).

Caso o sistema esteja integrado com o Protheus, a aba Fórmula no contrato não será exibida.

No processo de Medição:

Com o parâmetro desmarcado traz todos os itens associados ao contrato para realizar a medição.

Com o parâmetro marcado não traz as tarefas na grid, o usuário deve selecionar as tarefas na medição do contrato.

Ao associar mais de 1000 itens este parâmetro automaticamente será marcado.

**Controle de dedução do faturamento direto:**

* Vínculo por movimento (saldo contrato): A tela de associação de produtos faturados permite o preenchimento manual do Valor da Dedução, podendo ainda definir um percentual de aplicação em relação ao saldo da linha selecionada. O saldo será validado a partir do saldo do contrato.
* Vínculo por movimento (saldo tarefa): Na tela de associação de produtos faturados o sistema passa a preencher automaticamente a coluna Valor Dedução com base no saldo disponível da tarefa, considerando o que já foi medido. O saldo será validado a partir do saldo dos itens associados ao o contrato.
* Sem vínculo com movimento (somente valor): A possibilidade de manipulação dos dados na tela de associação de produtos faturados será bloqueada, pois as deduções de faturamento direto devem ser incluídas sem vínculo com movimento, definindo diretamente no grid o valor desejado.

**Produto da Liberação (Contrato de Insumo) :**

Permite informar de onde deseja buscar o produto que será enviado para a geração do movimento no suprimentos: se da associação, feita no cadastro do insumo contratado; ou do cadastro default do contrato (aba Defaults). As opções de envio são:

* Produto Associado ou Default (quando não houver Produto Associado);
* Produto Default ou Associado (quando não houver Produto Default);
* Produto Associado;
* Produto Default.

**Encerramento**

Consistência do Checklist de encerramento de Contratos à Pagar e Contratos à Receber.

**Legenda**

**Não Confere:** A verificação da consistência do item não ocorrerá no momento do encerramento do contrato.  
**Avisa:** Uma mensagem interativa será exibida no encerramento, perguntando se deseja verificar a consistência do item ou não.  
**Barra:** Se houver inconsistência no item analisado, o processo será interrompido e o contrato não será encerrado.

**Minhas Inspeções**

Esse parâmetro possibilita bloquear a liberação de período se não existir inspeção em conformidade. Deve-se escolher o tipo de contrato.

**Portal de Medição**

Nos parâmetros do Portal de Medição do projeto em questão, é possível selecionar os recursos do Smart View para os **Relatórios de Boletim de Medição,** **Relatório de Pré-Nota** e **Relatório de Pedido de Faturamento direto,** todos disponíveis através do TOTVS Compartilhamento.

Além disso, também é possível selecionar o **Repositório de arquivos utilizado no Portal de Medição do Fornecedor**.

**Visualizar hierarquia de tarefas nas medições**

Determina se as informações de obra/etapa serão exibidas na visão de medição. Esse comportamento também será aplicado ao arquivo Excel gerado ao baixar a planilha de medição.

**Solicitar Workflow (TAA ou Fluig) no envio para aprovação**

Marcando a opção **Manual**, ao mover o período para aprovação, ele irá direto para a coluna em liberação no portal. Isso ocorrerá quando os dados da liberação ainda serão preenchidos, antes do envio para aprovação. Dessa forma, ao concluir o preenchimento das informações de liberação, o WF será gerado de forma manual.  Marcando a opção Automático, após a medição, quando o usuário avançar o período para em Aprovação no portal, o WF será criado. E quando aprovado, poderá ser enviado para o Suprimento/Faturamento.

**Liberar período para Suprimento/Faturamento**

Oferece a opção de liberação **manual**, feita pelo usuário; ou **automática**, após a aprovação/assinatura o movimento é gerado automaticamente

**Gerar movimento do pedido de faturamento direto para Suprimento/Faturamento no Portal**

Disponibiliza a opção de gerar movimento do Pedido de faturamento direto para Suprimento/Faturamento de forma **manual**, feita pelo usuário; ou **automática**, após a aprovação/assinatura.

**Disponibilizar Menus de Gerar Movimento do Pedido para Suprimento/Faturamento no portal**

Exibe no menu do card a opção "Gerar movimento" para que o usuário envie de forma manual para gerar movimento do Pedido de faturamento direto para Suprimento/Faturamento.

**Fórmula de Validação de Medição (envio para aprovação)** Possibilita a criação de uma fórmula ao enviar a medição do período para aprovação.

Exemplo de Fórmula de Validação de Medição

Para esta fórmula, foi disponibilizada a função QUANTIDADEAQUIVOSPERIODO, que lista a quantidade de arquivos anexados no período do contrato. No exemplo abaixo, o alerta serve para lembrar o fornecedor de anexar algum arquivo antes de avançar a medição do período para aprovação:

Além dessa, a função TABMCNTPDO pode ser usada para trazer os campos da MPDO.

Exemplo:

TABMCNTPDO('CODCOLIGADA')

TABMCNTPDO('IDPRJ')

TABMCNTPDO('PERIODOMED')

**Fórmula de Validação de Faturamento Direto (envio para aprovação)** Permite a criação de uma fórmula que será executada ao enviar o pedido de faturamento direto para aprovação.

Exemplo de Fórmula de Validação de Faturamento Direto

Assim como detalhado logo acima, na fórmula de validação de medição, é possível usar a função TABMCNT para retornar os campos CODCOLIGADA, IDPRJ, IDCNT e IDPEDIDOEXTRA.

No exemplo abaixo, a fórmula cadastrada no parâmetro, valida a condição de pagamento informada no pedido de faturamento direto, impedindo que este fosse enviado para aprovação:

**Tabelas Adicionais de Metadados utilizadas pelo Portal de Medição:** Serão exibidas apenas as tabelas de Metadados do *TOTVS Construção Obras e Projetos,* que foram previamente cadastradas no módulo de Serviços Globais e que ao selecionadas poderão ser utilizadas no
