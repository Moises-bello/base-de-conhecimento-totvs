---
article_id: 360047488214
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 35b2660c272c477e258c381c0b361e77cbde4c7d277d2dcf3a9cdef34f6c9665
fetched_at: '2026-06-28T22:39:30.704354+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Exceções Fiscais (MATA540)
  - Todos os campos
type: support-article
updated_at: '2024-03-20T19:37:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047488214-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Exce%C3%A7%C3%B5es-Fiscais-MATA540-Todos-os-campos
---

**Dúvida**Campos do cadastro das Exceções Fiscais

**Ambiente**Protheus - Todas as versões

**Solução**

Algumas Unidades de Federação ou tipos de clientes/fornecedores possuem regras específicas para tratar situações de tributação de impostos de seus produtos, situações essas que fogem à regra geral. Cada caso de exceção fiscal, avaliado e classificado, deve ser cadastrado por meio desta rotina.

Exemplo:

Determinado produto tem tributação normal de ICMS, desde que não seja vendido a revendedor, caso contrário, será tributado em 12%, independente do Estado destino.

As exceções no tratamento fiscal podem ser determinadas pelas Unidades da Federação (UF) e/ou Tipo de Cliente (revendedor, produtor, etc.), e referem-se a um produto ou a um grupo de produtos. Pode ser utilizado o caractere asterisco (\*) no campo Estado para generalizar a aplicação da exceção a todos os Estados ou a todos os tipos de clientes.

Os casos existentes pertencerão a grupos de tributação, que devem ser previamente cadastrados no ambiente Configurador, na tabela 21. Esses grupos devem ser indicados no cadastramento da exceção fiscal.

 Campos:

Grupo Trib (F7\_GRTRIB): Código do grupo de tributação cadastrado.

Sequência (F7\_SEQUEN): Código sequencial do registro. Esse código não é de preenchimento automático e não necessita seguir uma ordem específica.

Estado (F7\_EST): Para exceções fiscais utilizadas em notas de saída (venda/remessa), esse campo representa o Estado do Cliente para o qual o produto está sendo enviado.

Caso seja uma exceção para notas de entrada (compra/aquisição), esse campo representa o Estado do Fornecedor do qual a empresa está recebendo os produtos.

Tipo (F7\_TIPOCLI): Nesse campo deve ser informado o tipo de cliente/fornecedor. Esse campo deve estar configurado exatamente como no cadastro do cliente/fornecedor ao qual a exceção será vinculado.

Aliq.Interna (F7\_ALIQINT): Representa a alíquota do ICMS para operações dentro do mesmo Estado. Por exemplo, tanto a empresa quanto o cliente são de São Paulo. Caso não seja preenchido, o sistema utilizará a alíquota padrão para o Estado em questão (MV\_ICMPAD).

Aliq.Externa (F7\_ALIQEXT): Representa a alíquota do ICMS para operações de fora do Estado. Por exemplo, a empresa é de São Paulo e o cliente/fornecedor de Minas Gerais. Caso o campo não seja preenchido, o sistema utilizará a alíquota interestadual padrão (12% ou nos casos em que a UF de destino estiver no parâmetro MV\_NORTE será aplicado 7%).

Margem Lucro (F7\_MARGEM): Margem de Lucro para o cálculo do ICMS ST.

Al.ICMS Dest. (F7\_ALIQDST): Alíquota do ICMS Retido (ou ICMS ST). Caso não seja preenchido, o sistema utilizará a alíquota padrão para o Estado em questão (MV\_ESTICM).

Grp.Cli/For (F7\_GRPCLI): Junto com o tipo de cliente/fornecedor, faz a vinculação da exceção fiscal com o cadastro do cliente/fornecedor. Não existe um cadastro para grupo de cliente/fornecedor, portanto é necessário se atentar no valor preenchido nesse campo para que seja o mesmo no cadastro do cliente/fornecedor. Esse campo não é de preenchimento obrigatório para validação da Exceção Fiscal.

Iss (F7\_ISS): Alíquota do ISS. Atualmente orientamos que as alíquotas do ISS sejam tratadas pela rotina FISA052. Para melhores informações consultar a documentação com o título: MP – FIS – ISS -> Utilizando a rotina FISA052 para Notas Fiscais de Entrada / Saída.

ICMS Pauta (F7\_VLR\_ICM) : Valor de pauta fiscal utilizada para cálculo do ICMS-ST.

IPI Pauta (F7\_VLR\_IPI): Valor de pauta fiscal utilizada para cálculo do IPI.

PIS Pauta (F7\_VLR\_PIS): Valor de pauta fiscal utilizada para cálculo do PIS.

COFINS Pauta (F7\_VLR\_COF): Valor de pauta fiscal utilizada para cálculo do COFINS.

ICMS Pauta Pro (F7\_VLRICMP): Indica o valor de pauta do ICMS Próprio.

Aliq. IPI (F7\_ALIQIPI): Alíquota de IPI a ser aplicada.

Aliq.PIS (F7\_ALIQPIS): Alíquota do PIS que será utilizada sempre que a exceção fiscal for aplicada.

Aliq.Cof. (F7\_ALIQCOF): Alíquota do COFINS que será utilizada sempre que a exceção fiscal for aplicada.

%Red.do ICMS (F7\_BASEICM): Informe o percentual da redução da base de cálculo do ICMS. Quando informado, deve-se utilizar somente 'I' ou 'O' no campo L. Fisc. ICM (F4\_LFICM).

%Red.do IPI (F7\_BASEIPI): Informe o percentual da redução da base de cálculo do ICMS. Quando informado, deve-se utilizar somente 'I' ou 'O' no campo L. Fiscal IPI (F4\_LFIPI).

Red.PIS (F7\_REDPIS): Valor de redução da base do PIS.

Red.Cofins (F7\_REDCOF): Valor de redução da base do COFINS.

Pauta Prod (F7\_ICMPAUT): Informe "Sim" para considerar o ICMS de Pauta do cadastro de produto ou "Não" para considerar a Margem de Lucro da exceção fiscal.

UF Busca (F7\_UFBUSCA): Apenas para as notas fiscais de entrada, esse campo irá indicar como o sistema deve se comportar no momento de selecionar a exceção fiscal. O padrão do sistema é buscar a exceção pela UF de destino da mercadoria (no caso das entradas, a UF a ser cadastrada deve ser a mesma do contribuinte, ou seja, a mesma informada no MV\_ESTADO). Esse campo poderá mudar a lógica de composição da exceção, considerando a UF do remetente da mercadoria, ou seja, a UF do fornecedor. Portanto, utilize: 1=Destino, para que a UF a ser selecionada na exceção fiscal das notas de entrada seja a do destino da mercadoria (MV\_ESTADO) 2=Origem, para que a UF a ser selecionada na exceção fiscal das notas de entrada seja a da origem da mercadoria (cadastro do fornecedor).

Tab.Nat.Rec (F7\_TNATREC): Código da tabela da Natureza da Receita.

Cod.Nat.Rec (F7\_TNATREC): Código da Natureza de Receita.

Grp. Nat. Rec (F7\_GRUPONC) : Grupo da Natureza de Receita.

Dt. Fim N. R. (F7\_DTFIMNT): Data Final de escrituração da Nat. Receita

Dt. Inclu (F7\_DTINCLU): Data de Inclusão da Exceção Fiscal.Campo não utilizado em qualquer controle do cadastro de exceção fiscal, apenas informativo.

Id. Hist (F7\_IDHIST): ID do Histórico. Caso o parâmetro MV\_HISTFIS estiver habilitado será registrado o Id do histórico para controle das alterações, por sua vez é feito na tabela SS1.

Este campo é transparente para o usuário, o mesmo não aparece em tela. Para mais informações: FIS0002\_Historico\_de\_Operacoes Fiscais.

Origem (F7\_ORIGEM): Informe o Código de Origem do Produto que será utilizado como chave para utilização da Exceção Fiscal.

Sit. Trib. (F7\_SITTRIB): Informe o Código de Situação Tributária do ICMS que será utilizado como chave para utilização da Exceção Fiscal.

%Red.ICMS ST (F7\_BSICMST):  Define o Percentual para o cálculo do ICMS Substituto (se houver base Reduzida).

Vl.Uni.Cig (F7\_PRCUNIC): Informar o preço unitário de venda de cigarros para cálculo da substituição tributária para fabricantes de cigarros.

%Red.Base ICMS DIFAL (F7\_BASCMP): Define o percentual da base para redução do cálculo do ICMS Complementar. Este campo visa atender Orientação Tributária DOLT/SUTRI nº 002/2016.

É importante que o tamanho dos campos abaixo estejam corretos para que a exceção fiscal possa funcionar.

F7\_GRTRIB = CARACTER, 6

F7\_GRPCLI = CARACTER, 3

A1\_GRPTRIB = CARACTER, 3

A2\_GRPTRIB = CARACTER, 3

B1\_GRTRIB = CARACTER, 6
