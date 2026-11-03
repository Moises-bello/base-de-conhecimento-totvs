---
article_id: 360048767194
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 10b0503358803fb698e92b2b871c03f0c59c68072e8761eaa54010d2238e7866
fetched_at: '2026-06-28T22:39:30.596908+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - LIVROS FISCAIS -
  Exceção Fiscal '
type: support-article
updated_at: '2021-07-29T14:26:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048767194-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-LIVROS-FISCAIS-Exce%C3%A7%C3%A3o-Fiscal
---

**Dúvida**

Quais são os procedimentos para configuração da Exceção Fiscal - MATA540 no Protheus?  
  
**Ambiente**

Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Algumas Unidades de Federação ou tipos de clientes/fornecedores possuem regras específicas para tratar situações de tributação de impostos de seus produtos, situações essas que fogem à regra geral. Cada caso de exceção fiscal, avaliado e classificado, deve ser cadastrado por meio desta rotina.

Exemplo:

Determinado produto tem tributação normal de ICMS, desde que não seja vendido a revendedor, caso contrário, será tributado em 12%, independente do Estado destino.

As exceções no tratamento fiscal podem ser determinadas pelas Unidades da Federação (UF) e/ou Tipo de Cliente (revendedor, produtor, etc.), e referem-se a um produto ou a um grupo de produtos. Pode ser utilizado o caractere asterisco (**\*)** no campo Estado para generalizar a aplicação da exceção a todos os Estados ou a todos os tipos de clientes.

Os casos existentes pertencerão a grupos de tributação, que devem ser previamente cadastrados no ambiente Configurador, na tabela 21. Esses grupos devem ser indicados no cadastramento da exceção fiscal.

**IMPORTANTE:**

A exceção fiscal opera apenas quando vinculada a um produto. Dessa forma, após o cadastramento da exceção fiscal, deve-se associá-la ao produto, informando seu código no campo Grupo de Tributação (**B1\_GRTRIB**) presente no Cadastro de Produtos.

**Para cadastrar uma exceção fiscal:**

 1 - Em Exceções Fiscais selecione a opção Incluir.

2 - Preencha os dados conforme orientação do help de campo.

3 - Observe o tópico Principais Campos/Controles.

4 - Confira os dados e confirme a inclusão.  
  
Campos:

* **Grupo Trib:** Código do grupo de tributação cadastrado.
* **Sequencia:** Código sequencial do registro. Esse código não é de preenchimento automático e não necessita seguir uma ordem específica.
* **Estado:** Para exceções fiscais utilizadas em notas de saída (venda/remessa), esse campo representa o Estado do Cliente para o qual o produto está sendo enviado. Caso seja uma exceção para notas de entrada (compra/aquisição), esse campo representa o Estado do Fornecedor do qual a empresa está recebendo os produtos. Deve-se informar um estado válido, constante da tabela de estados (ambiente Configurador, tabela 12). Caso seja informado \*\* (dois asteriscos), o sistema identificará que a regra é válida para todos os estados.
* **Tipo de Cliente:** Tipo do cliente para o qual a regra se aplica. O tipo de cliente é uma informação inserida no Cadastro de Clientes. Caso informado \* (asterisco), a regra será válida para todos os clientes.
* **Aliq.Interna:** Representa a alíquota do ICMS para operações dentro do mesmo Estado. Por exemplo, tanto a empresa quanto o cliente são de São Paulo. Caso não seja preenchido, o sistema utilizará a alíquota padrão para o Estado em questão. Informando este campo, o sistema irá sobrepor a configuração de alíquota interna definida pelo parâmetro MV\_ICMPAD.
* **Aliq.Externa:** Representa a alíquota do ICMS para operações de fora do Estado. Por exemplo, a empresa é de São Paulo e o cliente/fornecedor de Minas Gerais. Caso não seja preenchido, o sistema utilizará a alíquota padrão para o Estado em questão. Informando este campo, o sistema irá sobrepor a regra geral para cálculo do ICMS. As alíquotas externas são válidas somente para operações efetuadas por contribuintes do ICMS (inscritos).
* **Margem Lucro:** Margem de Lucro Presumida. Informando este campo, o sistema irá sobrepor a configuração do campo **Margem de Lucro** do Cadastro de Produtos.
* **Al.ICMS Dest.:** É a alíquota do ICMS Retido (ou ICMS ST). Caso não seja preenchido, o sistema utilizará a alíquota padrão para o Estado em questão. Esta informação é utilizada para o cálculo de ICMS normal quando efetuada operação com ICMS solidário interestadual. Sobrepõe a configuração presente no parâmetro MV\_ESTICM.
* **Grp.Cli/For:** Junto com o tipo de cliente/fornecedor, faz a vinculação da exceção fiscal com o cadastro do cliente/fornecedor. Não existe um cadastro para grupo de cliente/fornecedor, portanto é necessário se atentar no valor preenchido nesse campo para que seja o mesmo no cadastro do cliente/fornecedor.
* **Iss:** Indica se as configurações informadas para os campos alíquota interna e alíquota externa do ICMS serão estendidas ao cálculo do ISS.
* **ICMS Pauta:** Valor de pauta fiscal utilizada para cálculo do ICMS-ST. O ICMS de pauta é um tipo diferenciado de cálculo de ICMS em que o valor do imposto é apurado pela multiplicação de um valor fixo pela quantidade comprada e vendida. Sobrepõe a configuração de campo com mesma função presente no Cadastro de Produtos.
* **IPI Pauta:** Valor de pauta fiscal utilizada para cálculo do IPI. O IPI de pauta é um tipo diferenciado de cálculo de IPI em que o valor do imposto é apurado pela multiplicação de um valor fixo pela quantidade comprada e vendida. Empregado nas operações com bebidas, por exemplo. Sobrepõe a configuração de campo com mesma função presente no Cadastro de Produtos.
* **PIS Pauta:** Valor de pauta fiscal utilizada para cálculo do PIS.
* **COFINS Pauta:** Valor de pauta fiscal utilizada para cálculo do COFINS.
* **ICMS Pauta Pro:**Indica o valor de pauto da ICMS Próprio na exceção fiscal.
* **Aliq. IPI:**Alíquota de IPI a ser aplicada. Este campo atende ao **Decreto 3.800** e deve ser preenchido com o valor da alíquota a ser tratada na exceção.
* **Aliq.PIS:** Alíquota do PIS que será utilizada sempre que a exceção fiscal for aplicada.
* **Aliq.Cof.:** Alíquota do COFINS que será utilizada sempre que a exceção fiscal for aplicada.
* **%Red.do ICMS:**Informe o percentual da redução da base de cálculo do ICMS. Quando informado, deve-se utilizar somente 'I' ou 'O' nas colunas de ICM.
* **%Red.do IPI:**Informe o percentual da redução da base de cálculo do ICMS. Quando informado, deve-se utilizar somente 'I' ou 'O' nas colunas de ICM.
* **Red.PIS:** Valor de redução da base do PIS. Este campo atende à **Lei 10485** e deve ser preenchido com o percentual de redução da base de cálculo do PIS para esta exceção fiscal.
* **Red.Cofins:** Valor de redução da base do COFINS. Este campo atende à **Lei 10485** e deve ser preenchido com o percentual de redução da base de cálculo da Cofins para esta exceção fiscal.
* **Pauta Prod:**Informe "Sim" para considerar o ICMS de Pauta do cadastro de produto ou "Não" para considerar a Margem de Lucro da exceção fiscal.

  O campo Pauta do Produto **F7\_ICMPAUT** define se o sistema irá considerar o ICMS de pauta do produto ou a margem de lucro da exceção fiscal.

  O sistema faz o tratamento da seguinte forma para o cálculo do ICMS de pauta:

  Se no produto existir o valor do ICMS de Pauta (B1\_VLR\_ICM) e existir uma exceção fiscal com valor de Margem de Lucro (F7\_MARGEM), o sistema sempre considera o valor do ICMS de Pauta (B1\_VLR\_ICM) do produto, desprezando a exceção fiscal.

  Veja detalhes do cálculo do ICMS de pauta utilizando o campo **Pauta Produto.**
* **UF Busca:** Apenas para as notas fiscais de entrada, esse campo irá indicar como o sistema deve se comportar no momento de selecionar a exceção fiscal. O padrão do sistema é buscar a exceção pela UF de destino da mercadoria (no caso das entradas, a UF a ser cadastrada deve ser a mesma do contribuinte, ou seja, a mesma informada no MV\_ESTADO). Esse campo poderá mudar a lógica de composição da exceção, considerando a UF do remetente da mercadoria, ou seja, a UF do fornecedor. Portanto, utilize: 1=Destino, para que a UF a ser selecionada na exceção fiscal das notas de entrada seja a do destino da mercadoria (MV\_ESTADO) 2=Origem, para que a UF a ser selecionada na exceção fiscal das notas de entrada seja a da origem da mercadoria (cadastro do fornecedor).
* **Tab.Nat.Rec:**Código da tabela da Natureza da Receita.
* **Cod.Nat.Rec:** Código da Natureza de Receita.
* **Grp. Nat. Rec:** Grupo da Natureza de Receita.
* **Dt. Fim N. R.:**Data Final de escrituração da Nat. Receita
* **Dt. Inclu:**Data de Inclusão da Exceção Fiscal.Campo não utilizado em qualquer controle do cadastro de exceção fiscal, apenas informativo.
* **Id. Hist:** ID do Histórico. Caso o parâmetro MV\_HISTFIS estiver habilitado Será registro o Id do histórico no para controle das alterações, por sua vez é feito na tabela SS1.   
  Este campo é transparente para o usuário, o mesmo não aparece em tela. Para mais informações: [FIS0002\_Historico\_de\_Operacoes\_Fiscais](http://tdn.totvs.com/display/PROT/FIS0002_Historico_de_Operacoes_Fiscais)
* **Origem:**Informe o Código de Origem do Produto que será utilizado como chave para utilização da Exceção Fiscal.
* **Sit Trib:** Informe o Código de Situação Tributária do ICMS que será utilizado como chave para utilização da Exceção Fiscal.
* **%Red.ICMS ST:**  Define o Percentual para o cálculo do ICMS Substituto (se houver base Reduzida).
* **Vl.Uni.Cig:**Informar o preço unitário de venda de cigarros para cálculo da substituição tributária para fabricantes de cigarros.
* **%Red.Base ICMS DIFAL:** Define o percentual da base para redução do cálculo do ICMS Complementar. Este campo visa atender Orientação Tributária DOLT/SUTRI nº 002/2016.
