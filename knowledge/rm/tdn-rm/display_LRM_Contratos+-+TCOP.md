---
content_hash: 4fe8cfc5ebc3a12cd081c0d2233e70891eafd98d84424a82a74d8a0ccfc48c7b
fetched_at: '2026-06-29T00:09:52.930095+00:00'
page_id: '439701370'
product: rm
source: tdn-rm
title: Contratos - TCOP
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+-+TCOP
version: 70
---

Assim que criado,  no botão novo o contrato assume o status "Em Negociação", sendo possível assumir outros status como "Em Andamento" , "Sem Status", "Paralisado", "Encerrado" ou "Cancelado".

O status do Contrato é obrigatório e pode ser definido pelo anexo .

1 – Se o contrato for de Prestação de Serviços e possuir itens associados ou se o contrato for Fornecimento de Material e possuir objetos associados não será possível excluir o mesmo.  
2 – Para Contratos de Prestação de Serviços que não possuírem itens associados, os contratos e suas dependências serão excluídas.   
3 – Para Contratos Fornecimento de Material que não possuem objetos associados, os contratos e suas dependências também serão excluídos.

ContratoIdentificaçãoDados do Contrato

**Dados do Contrato:**

**Finalidade do Contrato**: Define- se a finalidade do mesmo, podendo ser de prestação de Serviço , Fornecimento de Material , Parcelas Fixas, Marco , Contrato de Insumo e Extra - Histograma.

**Num. Contrato:** Informe o número do contrato para identificação.

**Num. Licitação:** Informe o número da licitação deste projeto.

**Tipo:** Informe se o contrato é "A Pagar" ou "A Receber".

**Posição Atual:**  
Inicialmente, ao inserir um novo contrato, a posição do mesmo será sempre "Em Andamento". Para alterar a posição do contrato, basta inserir uma nova posição através do anexo "Histórico do Contrato".  
Quando o contrato está com a posição "Paralisado", "Cancelado" ou "Concluído" não é possível efetuar inclusões, alterações e exclusões dos dados do mesmo.

Para contratos "A Receber" ficarão disponíveis as opções Planilha de Atividades e Planilha de Serviços onde suas informações poderão ser utilizadas para execução do projeto. Para esse tipo de contrato, não serão listados Clientes / Fornecedores com a classificação igual "Fornecedor".

**Valores do Contrato:**

Valores do Contrato

**Valor Contratado Inicial:**Informa o Valor Contratado Inicial no contrato. Ou seja, sem interferência dos valores de aditivos contratuais.

**Valor Aditivo:** Esse valor é calculado de acordo com os dados dos aditivos "Em Andamento"cadastrados para o contrato em questão.

**Valor Contrato:** Informe o valor do contrato ou deixe em branco para que seja calculado pelo Sistema.  
O aditivo e o realinhamento de preços alteram o valor do contrato. Esse valor será sempre a soma do valor dos aditivos com a soma dos valores dos itens de contrato. Esse valor interfere diretamente no valor do saldo contratual na tela de visão dos períodos de contrato.

**Valor Total da Medição:** Informa o valor Total da Medição considerando parametrizações.

**Valor Retenção :** Informa o valor que será retido .Esse valor é considerado no valor do contrato.

Para contratos que utilizarem valor do reajuste na medição (PI + R) a visão dos valores do contrato exibirá também os campos : Reajuste Devido , Valor Medido Reajuste, Saldo do Reajuste e Reajuste Previsto. [Veja mais](http://tdn.totvs.com/pages/viewpage.action?pageId=403048875)

Quando o aditivo for de supressão ao calcular o contrato o sistema calculará considerando o valor do contrato inicial  mais o valor de aditivo como valor do contrato . E o saldo considerará o valor do contrato menos o valor medido.

Posição Atual

**Código do Cliente / Fornecedor**: Informe o código do Cliente / Fornecedor do Contrato.

**Funcionário Responsável**  
Informe o responsável pelo contrato através do Anexo "Histórico do Contrato". 

Num. ART

Conforme lei n° 6.496/77 a resolução CONFEA n° 1.025/2009, determina que todo contrato para execução de obras ou prestação de serviços de engenharia conforme as profissões abrangidas pelo sistema CONFEA/CREA, civil, elétrica, hidráulica, mecânica etc, tanto para elaboração de projetos como execução, deve ter sua ART.

Por este motivo o sistema passará a permitir o cadastro deste campo ART tanto no cadastro de projetos quanto no cadastro de contrato

Nos contratos os usuários podem utilizar o campo para preencher o Código ART especifico. Essa informação será enviada para o BackOffice pois é utilizada na geração da NFs-e, ela não deve ser obrigatória, pois só deve ser preenchida quando for uma para cada contrato, **se tiver apenas uma ART para todos os contratos ele deve** **ser preenchida no cadastro do projeto.**

No backoffice Nucleus (RM) será possível visualizar o código do contrato que possuir campo ART através do item do movimento

Segue no link ao lado os procedimentos para visualizar :[Visualizar item do movimento](http://tdn.totvs.com/display/public/LRM/MATFATCMPCRM01-6183+DT+Editar+Contrato+no+item+de+Movimento)

O Totvs Obras e Projetos irá disponibilizar para o Backoffice RM um serviço que irá retornar o código ART do contrato ou do projeto. Este serviço terá como parâmetros de entrada código da coligada , projeto e a lista de contratos.

Regras

* Se os contratos estiverem com o campo ART vazio o Totvs Obras e Projeto irá retornar para o Backoffice RM o código ART do projeto.
* Quando o Totvs Obras e Projetos enviar a lista de contratos , ao buscar os códigos ART dos contratos e alguns contratos possuirem código ART informado e outros contratos não tiverem preenchidos, o TOP retornará para o backoffice o código ART do projeto.

**Datas do Contrato:**

Datas do Contrato

**Data do Contrato**: Informe a data da criação do contrato.

**Data do Início / Data do Término:** Informe a data de início e término deste contrato, sendo que, a data do término não é necessária.

**Dias Aditados:** Se desejar, poderá prolongar a data do contrato, informando o número de dias aditados. Com isso, é possível gerar períodos extras. Os períodos não podem ser gerados automaticamente, através do ícone 'Gerar Períodos'. Para gerar os períodos extras deve-se utilizar o botão 'Novo'. Os períodos são gerados utilizando a mesma periodicidade do contrato.

**Término com aditamento:** Esse campo é calculado pelo sistema e considera a maior data de aditamento, acrescida do número de dias aditados na janela de edição de contrato. O recálculo é feito ao editar o contrato e ao salvá-lo. Se a data de término do contrato for 06/05/2009 e o mesmo possuir um aditamento até o dia 10/05/2009, mais 5 dias aditados, a data de término com aditamento será 15/05/2009. Se não houver nenhum aditamento, a data de término com aditamento será igual a data de término do contrato.

Periodicidade do Contrato

**Periodicidade Medida:** Informe se as medições deste contrato serão em período: personalizado, único, semanal, semanal corrido, quinzenal, quinzenal corrido, mensal ou anual. Caso seja personalizado informe o n.º de Dias deste intervalo.

Campos Livres

**Fonte do Recurso:** Informe de onde veio o recurso para a execução do projeto.  
   
Campo Livre 1, 2: Campos livres para o contrato.

O nome desses campos podem ser alterados através do menu Opções | Parâmetros | Totvs Obras e Projetos, na Pasta Campos Livres.

Comentário

**Comentário:** Comentário livre para o contrato.

Fórmula

Através desta visão é possível definir uma fórmula a ser utilizada para o cálculo do valor a ser enviado para os módulos de Gestão de Estoque, Compras e Faturamento ou Gestão Financeira no momento da liberação da medição.  
Fórmula do valor de liberação da medição:  
Informe neste campo, a fórmula para o cálculo do valor a ser enviado para o Gestão de Estoque, Compras e Faturamento ou Gestão Financeira. Caso o usuário limpe este campo, o sistema deve obrigatoriamente preencher o campo com a letra A.  
Caso o contrato já possua período liberado, não será possível editar a fórmula de valor da liberação   
   
Foram criadas variáveis fixas para a montagem da fórmula:  
A - Valor default (C - G)  
B - Valor sem reajuste  
C - Valor com reajuste  
D - Valor do reajuste  
E - Valor das retenções  
F - Valor das deduções  
G - Valor total retido (E + F)  
Utilize as operações básicas juntamente com as variáveis fixas do sistema para criar as fórmulas.

Quando o valor da medição do período for igual ao valor das deduções, retenções e adiantamentos será gerado movimento zerado considerando o valor da liberação (de acordo com a fórmula do contrato).

Caso o parâmetro de "Discriminar Envio de quantidade e preço" estiver habilitada esta aba não será apresentada.

Reajuste

Na aba reajuste ao editar o contrato, temos a seguinte tela:

**Tipos de reajuste:**Inicialmente os contratos virão com a opção**Sem Reajuste** marcada, sinalizando que não utilizam reajuste.

Marcando a opção de reajuste **Por contrato**, os seguintes campos ficarão habilitados para preenchimento:

**Período de Reajuste:** Informe se o reajuste no valor do contrato será Mensal ou Anual. Sendo o período de reajuste mensal ou anual é obrigatório definir a data base do reajuste.

**Data Base do Reajuste:** Data a partir da qual será calculado o reajuste.

**Fator Contratual:** Informe qual o fator do reajuste (campo apenas informativo).

Clicando no símbolo de incluir  , será apresentada a tela abaixo, para preenchimento dos campos descritos logo na sequência:

**Moeda:** moeda(s) para reajuste. Defina pelo menos uma moeda para Reajuste. Caso sejam escolhidas mais de uma moeda, o coeficiente de todas devem fechar em 1 (um), ou seja, 100%.

**Coeficiente:** Informe o valor em percentual desta moeda para o reajuste, pois poderá ser reajustado por mais de uma moeda.

**Cotação Base Reajuste:** Informe a cotação da moeda na data base do reajuste.   
  
O número de casas decimais está fixado em 4.  
Os campos **Cotação Base Reajuste** e **Coeficiente** são campos de preenchimento obrigatório.  
  
Exemplo:  
Utilizando apenas um Índice: Considere que a Cotação na Data Base seja 1,16, a Cotação na Data do Reajuste (Data Base + 365 ou 30 dias (depende do tipo de reajuste: anual ou mensal)) 1,25, o Coeficiente 2 e o Valor da Medição Sem Reajuste 63.690,00. O Reajuste será calculado da seguinte maneira: Percentual de Reajuste = [Cotação na Data do Reajuste (Cotação na Data de Base + 365 ou 30 dias) - Cotação na Data Base)) / Cotação na Data Base] \* Coeficiente \* 100. Percentual de Reajuste = [(1,25 - 1,16) / 1,16] x 2 x 100 = 15,52 % Valor da Medição com Reajuste = Valor da Medição x Percentual de Reajuste Valor da Medição com Reajuste = 63.690,00 x 15,52 % = 73.574,69  
Utilizando mais de um Índice: Considere os seguintes Índices:  
  
Cotação na Data Base               Cotação na Data do Reajuste (Data Base + Número de dias para reajuste (365 ou 30 de acordo com o tipo de reajuste anual ou mensal)  
1,16                                          1,25  
1,10                                          1,12  
  
O Reajuste será calculado da seguinte maneira: Percentual de Reajuste do Dólar = [(1,25 - 1,16) / 1,16] x 0,6 x 100 = 4,655 % Percentual de Reajuste da UFIR = [(1,12 - 1,10) / 1,10] x 0,4 x 100= 0,727 % Percentual de Reajuste = 4,655 + 0,727 = 5,382 % Valor da Medição com Reajuste = 63.690,00 x 5,382 % = 67.116,52

**Por Item Associado**

Para consultar os detalhes desse tipo de reajuste [clique aqui.](https://tdn.totvs.com/display/LRM/Reajuste+do+Item+Associado+-+Processos)

Quando o período tiver somente reajuste, o período apresentará destacado na grid um novo ícone conforme imagem abaixo.

Defaults

São visualizados os defaults para geração de movimento para o Gestão de Estoque, Compras e Faturamento.  
   
**Mov. Liberação Período:** Selecione o tipo de movimento default para liberação da medição para o Gestão de Estoque, Compras e Faturamento.  
   
**Mov. Estorno:** Selecione o tipo de movimento default para liberação de medição de estorno para o Gestão de Estoque, Compras e Faturamento.  
   
**Cód. Filial Default:** Preenchimento do local de estoque que será usado na liberação do período medido com liberação no Gestão de Estoque, Compras e Faturamento. Caso não seja preenchido o valor que será apresentado na tela de liberação, será a filial preenchida na edição do projeto.  
   
**Mov. Liberação Retenção:**  
Selecione o tipo de movimento default para liberação da medição para o Gestão de Estoque, Compras e Faturamento.  
   
**Condição de Pagamento:** Selecione a condição de pagamento para o movimento.  
   
**Produto:** Selecione o produto default para o movimento.  
   
**Cód. Loc. Local:** Preenchimento do local de estoque que será usado na liberação do período medido com liberação no Gestão de Estoque, Compras e Faturamento.  
   
**Retenção Default**  
Defina uma retenção padrão para todos os itens de um contrato. Para isso basta colocar na edição do contrato, o tipo de retenção e deixar o campo de retenção dessa tela com valor 0.00, nessa pasta informe a retenção desejada.  
   
Caso seja informado apenas o "Tipo de detalhamento da retenção" será emitida mensagem informando que o percentual é obrigatório. O mesmo ocorre se apenas o percentual for informado, uma mensagem será exibida informando que "Tipo de detalhamento da retenção" é obrigatório.  
Para retenções onde os valores informados são superiores a 100%, será emitida mensagem informando que a soma dos valores das retenções do contrato não deve ultrapassar 100%.  
A definição de um default não impede a alteração do dado no momento da geração do movimento para o Gestão de Estoque, Compras e Faturamento.

As informações dessa aba também estarão disponíveis para edição mesmo utilizando status do Contrato, porém algumas regras serão consideradas, como por exemplo a interação com o Protheus.

Dados Fiscais: Campos referente a Reforma tributária (**Emenda Constitucional nº 132/2023** regulamentada pela **Lei Complementar nº 214/2025**, visando simplificar e modernizar a tributação aplicável às atividades econômicas) [Saiba mais](https://tdn.totvs.com/pages/releaseview.action?pageId=1025213020)

**Código Indicador da Operação (NFS-e)** Esse campo somete ficará visível para contratos do a receber. Quando o campo estiver preenchido, essa informação será automaticamente levada para o movimento no momento da geração da medição.

**Indicativo de Prestação de Serviços** Selecione uma das opções disponíveis:

* Não se aplica;
* Não é obra de construção civil ou não está sujeita a matrícula;
* Obra de construção civil - Empreitada Total;
* Obra de construção civil - Empreitada Parcial.

**Tipo de Projeto** Informe se é projeto próprio ou de terceiro.

**Regra Tributária** Traz registros da tabela DREGRATRIBUTARIA, do módulo fiscal, e estará visível apenas para integração com o Backoffice RM. sendo enviado para o item do movimento gerado a partir do respectivo contrato, na aba de Integrações>Fiscal.

Parâmetros

**Parâmetros específicos do contrato**

Para utilização é necessário definir a permissão no perfil do usuário:

Utiliza parâmetros por contrato:

Ao marcar o parâmetro "Utiliza parâmetros por contrato" o contrato passa a ser prioritário em relação aos parâmetros que nele existe, isto é, serão considerados os parâmetros do próprio contrato e não dos parâmetros de Projeto que continuam existindo para os demais contratos que não utilizam tal prioridade.

Assim como nos parâmetros de projeto, o comportamento desses parâmetros consideram a integração com o Protheus que implica em um comportamento específico.

Grandeza principal de medição de contrato:

Quando esse parâmetro estiver marcado, a grandeza informada é que será usada para os cálculos, tanto do acumulado quanto do saldo do contato; prevalecendo sobre a grandeza do projeto e diminuindo diferenças de arredondamento:

Obs: o campo **“Código indicador da operação (NFS-e)”**  só vai aparecer para contratos do tipo venda.  
Esse campo está disponível na aba **Default** e deve ser utilizado **exclusivamente em contratos do tipo Venda**.

Durante a geração do **Movimento** a partir de um contrato de venda, o valor informado nesse campo é **automaticamente enviado para o Movimento**, garantindo que a informação seja transportada sem necessidade de preenchimento manual adicional.

Observações

Comentário  de observações livre para o contrato.

Campos Complementares do Contrato

São visualizados os campos complementares cadastrados no menu Cadastros | Campos Complementares. Nessa janela os dados devem ser informados. Caso tenha sido definida uma validação do campo complementar com base numa tabela dinâmica, o mesmo será validado nesse momento.

# [Contrato Campos Livres](http://tdn.totvs.com/display/LRM/Contrato+Campos+Livres)

Períodos Contratos

São visualizados os períodos do contrato onde há possibilidade de incluir/alterar/excluir os períodos. 

Essa aba de Períodos de Contratos só aparece na visão de contratos quando o mesmo já esta salvo.

Comentário

 Informações Complementares

[Tipos de Contrato](http://tdn.totvs.com/display/LRM/Tipos+de+Contratos+-+TOP)

[Anexos - Contratos TOP](http://tdn.totvs.com/display/LRM/Anexos++-+Contratos+TOP)

[Processos - Contratos TOP](http://tdn.totvs.com/display/LRM/Processos+-+Contrato+TOP)
