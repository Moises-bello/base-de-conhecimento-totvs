---
content_hash: ce9203b00bab20c0a7b63120f68255e262d97c2c6dc36a7febf5718041dafa01
fetched_at: '2026-06-29T00:09:49.417282+00:00'
page_id: '435105285'
product: rm
source: tdn-rm
title: Comissão - Processo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105285
version: 48
---

ATENÇÃO!!!

A partir do momento em que a [Comissão com novas funcionalidades](https://tdn.totvs.com/pages/viewpage.action?pageId=665033766) estiver ativa no TCGI, as funcionalidades descritas a seguir no documento abaixo e também o cadastro de vendedores não estarão mais disponíveis para acesso, pois a Comissão com novas funcionalidades é uma evolução destes processos.  
Se chegar até a release 12.1.2310 e ainda não tiver executado atualizador de comissão, ao clicar no menu da comissão, será aberta a tela para executar a ferramenta do [Conversor de Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=784209752). 

**Comissão**   
O Processo de Comissão é integrado com TOTVS Gestão de Estoques, Compras e Faturamento, Folha de Pagamento ou Gestão Financeira.

ComissãoSobre Comissão |

### Sobre Comissão

Antes da realização da comissão é necessário definir os parâmetros dessa funcionalidade.  
Para a comissão temos os parâmetros de Faturamento, Folha de Pagamento e/ou Gestão Financeira.   
Uma vez definidos estes parâmetros as comissões posteriores podem ser realizadas descartando a necessidade de alteração dos parâmetros.  
    
**Aba Identificação**  
**Código da Comissão:** Código da comissão realizada.  
**Situação comissão:** Situação da Comissão que está sendo editada. O sistema dispõe de 2 status, sendo: Integrada ou Não Integrada.   
**Tipo Comissão:** Exibe se a comissão será integrada com o Nucleus ou com o RH.  
**Venda/Aluguel:** Exibe qual a venda que está gerando a comissão.  
**Vendedor:** Exibe para qual vendedor a comissão será gerada.  
**Fórmula:** É a Fórmula que poderá ser utilizada para o cálculo do valor da comissão.  
**Valor total comissão:** Esse campo mostra o valor total da comissão. Quando o campo "Fórmula" está preenchido, o presente campo fica bloqueado para edição e exibe o resultado da execução da fórmula como valor da comissão. Quando o campo "Fórmula" não é preenchido, ele possibilita a inserção manual do valor da comissão.   
**Nro de Parcelas:** Informe o número de parcelas que serão geradas para a comissão.  
**Histórico do Movimento:** É apresentado o histórico do movimento de comissão.  
**Memória de cálculo da comissão:** Este campo mostra o cálculo realizado para a comissão.  
**Tipo de Comissão de Cálculo:**Este campo permite que seja definido como será feito os cálculos para a comissão, valor fixo não vinculado ao recebimento ou percentual/fórmula vinculados ao recebimento.  
   
**Parcelamento da Comissão:**  
   
A partir da versão 12.1.22 será possível realizar o parcelamento do valor da comissão.   
Este processo é habilitado tanto para a geração da comissão para o Fornecedor (Gestão de Estoque, compras e faturamento) quanto para o Funcionário (Folha de Pagamento).  
A partir da versão 12.1.34.111 ou superior também poderá ser feito diretamente para Fornecedor (Gestão Financeira).  
  
A tela de cadastro foi alterada para que seja possível definir o valor da comissão e quantas parcelas serão geradas. As parcelas podem ser incluídas manualmente ou então, ao salvar a comissão, o RM vê quantas parcelas foram definidas e as criam automaticamente.  
As parcelas são integradas com os respectivos sistemas gerando Movimento ou então um item no Envelope de pagamento do funcionário ou Lançamentos a pagar diretamente no Financeiro.  
Foi criado um novo campo de Fórmula para a validação da integração das parcelas da comissão. Com esta fórmula será possível escolher quais parcelas serão integradas e também canceladas da integração.  
Cada parcela possui os seguintes campos:

**Identificação**  
**Código da Comissão:** Este campo trará automaticamente o código de qual comissão está gerando esta parcela.  
**Venda/Aluguel:** Este campo trará a informação de qual venda está sendo gerada a comissão.  
**Vendedor:** Este campo mostrará para qual o vendedor está sendo gerada a comissão.  
**Nro Parcela:** Informe qual será o número da parcela.  
**Valor Parcela:** Informe qual será o valor da parcela.  
**Situação Comissão:** Será exibido se a parcela está integrada ou não com o BackOffice.  
**Fórmula de Validação para integração da comissão:** Para escolher quais parcelas serão integradas ao BackOffice, utilize este campo.   
**Observação:** A fórmula de validação define quais parcelas serão integradas ao BackOffice, para isto foi criada uma função de fórmula TABCOMISSAOPARCELA que pode acessar qualquer dado da tabela XCOMISSAOPARCELAMENTO. Para mais informações sobre como fazer, acesse: [Como Fazer Parcelamento de Comissão](http://tdn.totvs.com/pages/viewpage.action?pageId=404916462)  
   
**Para a integração com RH - Folha de Pagamento, aparecerão os seguintes campos:**  
**Evento Folha:** Informe qual o evento folha que será enviado para o envelope de pagamento.  
**Competência:**

* Mês: Informe o mês de competência da parcela
* Ano: Informe o ano de competência da parcela.

**Id. Movimento:** Após a integração com o BackOffice será gerado o número do movimento da parcela de comissão. O movimento será exibido no próprio produto Folha de Pagamento.

**Para a integração com Gestão de Estoque, os seguintes campos estão disponíveis:**  
**Id. Movimento:** Após a integração com o BackOffice será gerado o número do movimento da parcela de comissão. O movimento será exibido no próprio produto Gestão de Estoque.  
   
**Observação:** As parcelas podem ser tanto incluídas, quanto editadas e excluídas, isto, enquanto a comissão não estiver integrada ao BackOffice. O valor da comissão e o número de parcelas devem coincidir com a quantidade de parcelas incluídas na comissão e o valor deve ser igual ao somatório das parcelas criadas.  
   
Para mais informações sobre como realizar o parcelamento de comissões, acesse: [Como Fazer Parcelamento de Comissão](http://tdn.totvs.com/pages/viewpage.action?pageId=404916462)  
   
**Aba Campos Complementares:**  
Nesta aba serão mostrados os campos complementares utilizados. Lembrando que os campos complementares de comissão são criados e habilitados em: Cadastros | Campos Complementares | Comissão .Net.  
 

Integração TOTVS Gestão Financeira

### Integração TOTVS Gestão Financeira

Funcionalidade liberada na versão 12.1.34.111 ou superior.

A comissão de venda do TCGI passa a ser integrada diretamente ao backoffice, gerando os lançamentos financeiro diretamente para o TOTVS Gestão Financeira, além das opções já existente para a comissão de "Tipo de Integração" (TOTVS Compras e Faturamento, TOTVS Folha de Pagamento) tem a nova opção (TOTVS Gestão Financeira) .  
A nova opção de integração com o TOTVS Gestão Financeira, irá gerar um lançamento financeiro a pagar diretamente no módulo TOTVS Gestão Financeira.

Para que se possa utilizar a geração de lançamentos financeiro de comissão diretamente para o TOTVS Gestão Financeira será disponibilizado na parametrização dos parâmetros gerais da coligada no menu 'Ambiente|Parâmetros|Gestão de Imóveis|22.02 - Contrato|22.02.09 - Comissão|Comissão → Geral com Financeiro' o campo "Parâmetro de Integração Financeira:" e ainda o mesmo campo nas entidades 'Empreendimento', 'Unidade', 'Comissao' como será demonstrado a seguir:

Parâmetros de Comissão:

Empreendimento:

Unidade:

Comissão:

### **Parametrização:**

Acessado o ambiente TOTVS Incorporação | Menu Ambiente | Parâmetros | Totvs Incorporação | Contrato | Comissão  
**Etapa 1 – Integração da Comissão**  
Observado que o campo Fontes do Parâmetro dispõe de três opções: Parâmetros, Empreendimento e Unidade. De acordo com esta parametrização que o sistema irá buscar os dados para gerar a comissão.  
**Etapa 2 – Integração da Comissão com o TOTVS Gestão de Estoque, Compras e Faturamento**  
Os parâmetros desta etapa serão utilizados quando o parâmetro do campo Fonte do Parâmetro na etapa 1 for preenchido como Parâmetros.  
Quando a comissão for gerada para um "Fornecedor" estes parâmetros serão utilizados para a integração da comissão ao módulo de Gestão de Estoque, Compras e Faturamento.  
É necessário que seja cadastrado no módulo Totvs Gestão de Estoque, Compras e Faturamento, o Tipo de Movimento e Produto/Serviço.  
Na tela de cadastro de comissão irão aparecer os parâmetros referentes à integração, como:  
**Tipo Movimento:**  É o tipo de movimento existente no TOTVS Gestão de Estoques, Compras e Faturamento.  
   
**Produto/Serviço:** Informe o produto ou serviço será utilizado para a geração da comissão.  
**Filial:** Informe qual a filial será utilizada na integração da comissão.  
**Centro de Custo:** Informe qual o centro de custo será utilizado na integração da comissão.  
Observação: Todos os campos acima já são preenchidos previamente pelos parâmetros do TIN ou pelas informações do Empreendimento, mas podem ser alterados também no momento de cadastrar a comissão.  
   
Parametro de [Tipo de Movimento](http://tdn.totvs.com/pages/viewpage.action?pageId=461921700)  
[Produto/Serviço](http://tdn.totvs.com/pages/releaseview.action?pageId=423938817)  
   
   
**Etapa 3 – Integração da Comissão com o TOTVS Folha de Pagamento**  
Quando a comissão for gerada para um "Funcionário" estes parâmetros serão utilizados para a integração da comissão ao módulo Folha de Pagamento.  
É necessário que seja cadastrado no módulo Totvs Folha de Pagamento, o Evento Folha e o Centro de Custo.  
Na tela de comissão, poderá ser alterado esses parâmetros e deve ser informada qual a competência base da comissão para enviar para o envelope de pagamento correto.  
   
[Evento Folha](http://tdn.totvs.com/pages/viewpage.action?pageId=452719144)  
[Centro de Custo](http://tdn.totvs.com/display/LRM/Cadastro+Centros+de+Custos)

**Etapa 4 –** **Definição****para geração dos lançamentos de comissão**

**Tipo de Comissão:**

* **Valor fixo não vinculado ao recebimento das parcelas:** Os valores do lançamentos de comissão serão fixo e não irão possuir vinculo com as parcelas do financiamento.
* **Percentual máximo vinculado ao recebimento das parcelas**: Os valores dos lançamentos de comissão serão gerados por percentual ou fórmula e estão diretamente ligados ao recebimento das parcelas de financiamento.

**Processo:**  
   
Para gerar uma comissão, é necessário ter incluído um contrato de venda contendo vendedor.  
Incluir Venda  
Incluir Vendedor  
   
Acessado o menu Contratos | Contratos de Vendas e Aluguéis | Selecionada a venda desejada | Anexos | Vendedores | Editar | Anexos | Comissões | Incluir   
**Observação**:   
Os campos desta tela de comissão são preenchidos de acordo com a parametrização feita. Sendo que o sistema pode buscar informações dos Parâmetros, do Empreendimento e da Unidade.  
Observado que o campo Memória de Cálculo só é preenchido após salvar a tela de comissão.  
Ainda dentro da tela de comissão | Processos | Gerar Comissão(ões) | Executar  
*Atenção:* *Quando integrado ao Backoffice Protheus o TIN não disponibilizará a opção de Evento Folha para ser utilizado.*  
**Observação**:   
**Gestão de Estoque, Compras e Faturamento**  
Após a execução do processo, observa-se que o campo Situação da Comissão foi alterado para Integrado a Gestão de Estoque, Compras e Faturamento. Neste momento foi criado no módulo TOTVS Gestão de Estoque, Compras e Faturamento o movimento referente a comissão.  
**Folha de Pagamento**

* ---

  Log da Comissão  
   Após a execução do processo, observa-se que o campo Situação da Comissão foi alterado para "Integrado a folha de Pagamento". Neste Momento foi criado no módulo Folha de Pagamento uma solicitação de pagamento ao funcionário na tabela PFMOVTEMP.  
     
  **Cancelamento da comissão:**  
    
  Acessado o menu Contratos | Contratos de Vendas e Aluguéis | Selecionada a venda desejada | Anexos | Vendedores | Editar | Anexos | Comissões | Selecionada a comissão | Editar | Processos | Cancelar Comissão(ões) | Executar   
     
  **Observação**:   
  Após a execução do processo, observa-se que o campo Situação da Comissão voltou para Não Integrado.  
  Neste momento, no módulo TOTVS Gestão de Estoque, Compras e Faturamento o movimento referente a comissão foi excluído.

  ---

  Gerar Comissão(ões)  
  Cancelar Comissão(ões)

Fonte de Parâmetros

**Fonte de parâmetros da cobrança de Comissão**

Parâmetro para definir de qual a cadastro iremos utilizar os valores "Default" da Comissão.

Cliente pode optar por 3 opções como é informado acima:

* Parâmetros
* Empreendimento
* Unidade
* **SubUnidade  ( Opção de SubUnidade - VERSÃO 12.1.35 em Diante !! )**

**Informando o parâmetro utilizado para a integração desejada nas entidades: (Parâmetros gerais, Empreendimento, Unidade, )**

Define, no Parâmetro, qual o tipo de cálculo que a comissão será paga: Valor Fixo não vinculado ao recebimento das Parcelas (padrão utilizado hoje) ou Percentual máximo vinculado ao recebimento das parcelas (Novo tipo de cálculo de parcelas).

**Empreendimento:**

Define, no Empreendimento, qual o tipo de cálculo que a comissão será paga: Valor Fixo não vinculado ao recebimento das Parcelas (padrão utilizado hoje) ou Percentual máximo vinculado ao recebimento das parcelas (Novo tipo de cálculo de parcelas).

**Unidade:**

Define, na Unidade, qual o tipo de cálculo que a comissão será paga: Valor Fixo não vinculado ao recebimento das Parcelas (padrão utilizado hoje) ou Percentual máximo vinculado ao recebimento das parcelas (Novo tipo de cálculo de parcelas).

Importante!

O sistema não validará o total de comissão com o valor das parcelas geradas que está sendo integrado ao faturamento quando o novo parâmetro "Percentual máximo vinculado ao recebimento das parcelas" for utilizado para a geração da comissão.  
Mas mantendo o comportamento que havia antes no sistema, apenas com o parâmetro "Valor Fixo não vinculado ao recebimento das Parcelas" o sistema somente permitirá gerar a integração das parcelas para o faturamento, desde que o valor total da comissão seja igual ao total das parcelas geradas para integrar.

**SubUnidade:**

Parâmetros de Comissão : Informar o valor da % de Comissão.

Sobre Parâmetros |

Ao marcar o Parâmetro, o tipo de cálculo Percentual máximo vinculado ao recebimento das Parcelas , são habilitados os campos 'Percentual máximo vinculado ao recebimento' e a 'Fórmula de % máximo vinculado ao recebimento' para que possam ser feito o cálculo do valor da parcela com base no valor da baixa do lançamento recebido. Só é permitido o preenchimento de uma das duas opções, ficando desabilitado a outra opção ao seu preenchimento.

Ao colocar valor em Porcentagem , o campo Fórmula fica inativo.

Ao preencher o filtro de parcelas abaixo, o sistema vinculará ao recebimento apenas as parcelas com o filtro explicito nesse campo, caso esteja em branco, o sistema vinculará todas as parcelas ao recebimento da comissão.

Neste exemplo acima, apenas os tipos parcela 1 e 2 serão vinculados ao recebimento a comissão

**Exemplo sobre cobrança de Comissão.**

**Percentual:**

Neste exemplo  foi configurado o campo % máximo vinculado ao recebimento com 50% e foi gerado um plano de financiamento com parcelas no valor de R$1.000,00, com esta configuração serão geradas parcelas de comissão no valor máximo de R$500,00, desde que o cliente pague o valor integral das parcelas, senão será calculado o valor proporcional ao recebido do cliente.

**Por Fórmula:**

Exemplo com a utilização da Fórmula para comissão.

Nesta Fórmula, temos um exemplo que faz o seguinte calculo:

Se o Vendedor for = 8 ou 9, então utiliza 12.5% de comissão para a parcela

Senão = 50% de comissão para a parcela.

Observação!

Este exemplo é usado para caso de Comissão diferente para Imobiliária que paga um valor X para Gerente/Diretor e outro valor para Vendedor.

Neste exemplo, o Vendedor, código 10, entraria no 'Senão' da fórmula,  utilizando 50%

E neste exemplo já entraria nos 12.5% de comissão da parcela da fórmula.

Pagamento Valor fixo não vinculado ao recebimento das parcelas |

O tipo de Comissão de Cálculo por valor fixo não vinculado ao recebimento das parcelas é a forma padrão que o sistema calcula as os valores das parcelas fixas, independente de das baixas de lançamentos realizadas nesta venda. É informado um valor fixo de comissão e a quantidade de parcelas, então o sistema calcula todas as parcelas.

**Exemplo do Valor fixo:**

Informo um valor fixo na Tela de Comissão , e é habilitado o campo de Número de Parcelas para informar a quantidade de parcela desejada.

Sistema pega o valor total de Comissão informado e divide pelo número de parcelas .

Percentual máximo vinculado ao recebimento das parcelas |

Neste exemplo foi configurado para buscar a parametrização pelo Empreendimento, utilizando o tipo de cálculo da comissão 'Percentual máximo vinculado ao recebimento das parcelas'

A parametrização para buscar o Percentual Máximo foi realizada através de fórmula, onde utiliza 12.5 % do valor da baixa, para gerar a parcela de comissão para os vendedores ( 8 e 9 ) e 50% para os demais.

Neste caso o vendedor é 10, então utilizará 50% do valor baixado para gerar a parcela de comissão.

Ao editar o Vendedor na venda - Clicar em ( Comissão ) - Clicar NOVO  , o sistema busca a parametrização de Comissão no cadastro do Empreendimento.

Neste exemplo, o valor da comissão é de R$5.000,00 e tem o mesmo saldo devedor, e utiliza o tipo de cálculo de comissão com o 'Percentual máximo vinculado ao recebimento das parcelas' para calcular os valores das parcelas com base na baixa dos lançamentos financeiro do contrato de venda. O número de parcelas fica em aberto nesta configuração, pois a sua geração está vinculada ao pagamento das parcelas por parte do cliente, que através do processo "Gerar Parcelas de Comissão" criará as parcelas de comissões até finalizar o saldo devedor da comissão.

Este campo vai reduzindo o valor na medida que o cliente for pagando suas parcelas e executando o processo "Gerar Parcelas de Comissão".

O contrato já encontra-se com as parcelas pagas na mesa data de vencimento da parcela.

Neste exemplo são:

* Outubro 2020
* Novembro 2020
* Dezembro 2020
* Janeiro 2021
* Fevereiro 2021

O processo "**Gerar Parcela de Comissão**" pode ser agendado, de preferência sempre após o retorno bancário das baixa de lançamentos, que poderá ser diário, desta forma o sistema irá gerar as parcelas de comissão com base no pagamento destas parcelas. A geração das parcelas pode ser informado uma competência da baixa ou usar sempre a atual para realizar o agendamento.

Este processo encontram-se  na visão de Comissão, menu processos e é Global, ou seja, é executado para as baixas de **todas** as Comissões na competência especificada na execução deste processo.  
Processo de Gerar/cancelar Parcela de Comissão irá :  
Buscar **todas** as baixas em uma determinada competência para as comissões que tenham o tipo de cálculo atrelado a baixa.  
Ao realizar a baixa de uma parcela que esteja associada a comissão através do contrato de venda, o sistema irá buscar o percentual da máximo vinculado a parcela para gerar a parcela de comissão na competência da baixa, da mesma forma. o sistema irá cancelar a parcela de uma competência específica.  
Buscar **todas** as comissões que tem o tipo cálculo Valor Parcela Fórmula e tenha saldo devedor do comissionado para gerar a parcela com base na fórmula. **\*12.1.2310**   
O sistema irá executar a fórmula para definir o valor da parcela e esse valor não poderá ser maior que o saldo devedor do comissionado.

Neste exemplo, vou voltar no tempo, informar uma competência específica e gerar uma parcela que teve a baixa no mês de **Outubro de 2020**.

O lançamento financeiro tem o valor de baixa de R$500,00, a fórmula está parametrizada para usar 50% do valor da baixa, desta forma, o valor da parcela de comissão será de R$250,00.

Como código do Vendedor é 10 - Ganhando 50% de Comissão e o Saldo Comissão reduzindo o valor em R$250,00 Reais .

**Gerando Segunda Parcela de Comissão ( Novembro 2020 )**

Parcela no valor de baixa R$1.000,00

Gerada parcela agora no valor de R$500,00 (50% do valor da baixa do lançamento financeiro, conforme fórmula ) e o Saldo Comissão reduzindo para R$4.250,00 .

Foram geradas as Parcelas de comissão ( **Dezembro 2020 e Janeiro 2021** ) fincando com uma saldo devedor de R$3250,00 e o número de parcelas igual a 4.

Estamos no mês de fevereiro de 2021 ,com a baixa do lançamento realizada, e utilizaremos o parâmetro 'Mês Corrente' para executar e também poder agendar a geração de futuras parcelas de comissão.

Executando processo para Mês Competência.

Atualizado o valor de Saldo Comissão - Número de Parcelas e gerada uma nova parcela do Mês competência.

As parcelas serão geradas até chegar concluir o saldo devedor de R$2.750,00.

**Se por exemplo, o saldo da comissão estivesse com R$250,00 e o cliente efetua-se uma baixa de R$1.000,00, com 50% sober o valor da baixa, a parcela de comissão seria de R$500,00, mas o seu saldo é de 250,00, então a parcela seria gerada neste caso com o valor de R$250,00, e não seria gerada mais parcelas de comissão.**

**Exemplo : Nova comissão de R$1.000,00 e as parcelas sendo geradas.**

**Parcela competência Outubro**

**Parcela Competência Novembro.**

**Parcela Competência Dezembro**

**Ao gerar Parcela de Competência Janeiro o sistema já informa que não existe parcela de Comissão a ser Processada.**

Gerar Comissão |

**Gerar comissão** : O processo de se gerar a comissão integra as parcelas de comissões com TOTVS Gestão de Estoque, Compras e Faturamento,  TOTVS Folha de Pagamento ou TOTVS Gestão Financeira.

Importante!!

O Processo para ***Gerar Comissão(ões)*** só será integrado com o *Gestão de Estoque, Compras e Faturamento*, caso as **Parcelas da Comissão** já estejam criadas!

Através do campo "Fórmula de validação para integração da comissão" é possível criar a fórmula que conterá a regra para à integração de apenas uma parcela, ou várias parcelas, conforme regra de validação do cliente.

**Neste exemplo será utilizada uma Fórmula que verifica se a parcela for igual  1, então Integra , senão não integra.**

Processado e sismtema mostra apenas que Parcela 1 foi integrada conforme fórmula de Validação.

Parcela mostra o Id Movimento

## Gerando Comissão ( Parametro Financeiro ) a partir da versão 12.1.34.111

Hoje a comissão de venda do TCGI pode ser integrada ao backoffice, gerando um pedido de compra para o módulo de Compras ou integrada à Folha de Pagamento, gerando um evento na folha.

A nova opção de integração com o financeiro irá gerar um lançamento financeiro a pagar diretamente no módulo financeiro, sem a geração do movimento ou nota fiscal.

Se o usuário optar por trabalhar com o tipo de integração financeira na comissão, deverá ser informado o parâmetro de integração financeira e poderão também ser informados a filial, o centro de custo e o histórico, para isso o cadastro de "Parâmetro de Integração Financeira" também foi evoluído para receber cadastros com o tipo de 'comissão', assim será utilizado os mesmos campos usados para a integração com o backoffice.

Ao integrar a comissão, deverá ser gerado um lançamento financeiro a pagar, utilizando os dados do parâmetro de integração informado.   
O campo "Competência base:" defini o mês e ano para inicio da competência de pagamento da comissão, o dia será utilizado para a geração das parcelas a pagar.

Na comissão cadastrada com o campo "Tipo de Integração" com o valor 'TOTVS Gestão Financeira' selecionado no momento da sua criação.  
Vá em: Processos| Gerar comissão(ões)

Após o fim do processo, o log de execução demonstrará a chave gerada no financeiro de cada lançamento que ficou vinculado a cada parcela da comissão processada.

Na tela abaixo podemos verificar que quando selecionamos uma das vendas e pedimos para visualizar a parcela, iremos conseguir visualizar a chave do lançamento vinculado a parcela de comissão.

Comissões geradas e lançamento vinculado com todos os dados informados de acordo com Parâmetro "Parâmetro de Integração Financeira" informado para a comissão.

Exclusão de Comissão |

Exclusão da Comissão pode ser pelo Processos | Excluir Parcela de Comissão ou apenas marcar as parcelas que deseja excluir e em seguida : 

Pelo Processo , cliente pode selecionar as comissões e a competência da baixa que deseja excluir as parcelas.

Após a exclusão , o sistema volta os valores das parcelas para o saldo devedor da comissão.

**Se tiver parcela Baixada no TOTVS Gestão Financeira , será preciso primeiro cancelar a baixa para que se possa executar o processo de Excluir Parcelas de Comissão.**

**O TCGI não permite a exclusão de Parcelas de Comissão que estejam integradas ao Gestão de Estoque, Compras e Faturamento!**

Neste  cenário é preciso executar previamente o Processo Cancelar Comissão(ões) e excluir as Parcelas que serão excluídas da Integração:

Ao término deste Processo, o Sistema exibirá uma mensagem informando que as Parcelas selecionadas foram excluídas do Backoffice:

Rastreabilidade |

Rastreabilidade é utilizada apenas para Tipo de Comissão de Cálculo : **PERCENTUAL MÁXIMO VINCULADO AO RECEBIMENTO DAS PARCELAS**

**Comissão paga por baixas sendo realizadas.**

**Editar parcela de comissão gerada.**

Selecionar Baixa do Lançamento.

Rastreabilidade informando a Memória de Cálculo | lançamento | Baixa Lançamento do TIN | Valor Baixa

LOG |

# Sobre os Logs de Comissão

No processo de Comissões existem 3 Logs como a imagem mostra acima.

* **Log da Comissão**
* **Log do Parcelamento da Comissão**
* **Log do Parcelamento Recebimento da Comissão.**

# Log da Comissão

Criada Comissão = Exemplo ( R$1.000,00 ) Reais

Criado o Log da Criação da Comissão

Alterando o valor para 2.000 Reais

Log de Comissão Alterado.

# Log do Parcelamento da Comissão

Gerada a Parcela de Comissão

Log da Parcela Criado

# Log do Parcelamento Recebimento da Comissão

Editando a Parcela de comissão gerada - A Baixa do lançamento vinculada a Parcela de Comissão
