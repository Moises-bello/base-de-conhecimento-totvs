---
content_hash: 19fdac154bcbf7a14d301746348e9fdbf8d5d9da0994deea56ce5ed868a5ae1d
fetched_at: '2026-06-29T00:11:10.549451+00:00'
page_id: '644000466'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Importador de Contratos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=644000466
version: 70
---

### ***Para o treinamento, clique [aqui](https://youtu.be/K2aTdMh45KM).***

Por que utilizar o Importador de Contratos ?

**A incorporadora que adquira o sistema TCGI e já utiliza controle de contratos em outros sistemas, conseguirá trazer a informação do sistema legado para o sistema da TOTVS de uma forma simples e prática, evitando que o usuário cadastre os contratos todos na manualmente e faça o reajuste mês a mês.  É****possível importar aditivo de renegociador e somente históricos de compradores.  Os demais aditivos não serão importados os aditivos.**

***Tabelas que serão importadas:** XVENDA, XCOMPRADOR, XITEMVENDA, XREGRACOMPONENTEVENDA, XVENDAPARCELA, FLAN, FLANINTEGRACAO*

**Para realizar as baixas, favor utilizar o Importador de Baixas, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=493647927).**

### **Na versão 12.1.2602, tem um novo campo no Excel para informar a data do último reajuste aplicado no sistema legado, ou seja, se for anual, tem que ser a data dó ultimo aniversario.  O sistema ira fixar o valor importado para a data do último reajuste do cliente e não recalculará os valores antes dessa data. Desta forma, sempre informo o valor de juros e cm, pois o sistema manterá o valor do cliente. [Fixar Valor Base Tipo De Reajustes - Linha RM - TDN](https://tdn.totvs.com/display/LRM/Fixar+Valor+Base+Tipo+De+Reajustes)**

Modelo de Arquivo de Importação

***B******aixe  o modelo***

***Exemplo de Consulta SQL para extrair dados dos contratos do sistema legado, clique .*** ***Essa consulta foi feita na base RM como exemplo, mas deve ser refeita na base do sistema legado para extrair os dados e importar na base RM.***

**O arquivo de importação pode ser único para todos os empreendimentos, mas será processado apenas o empreendimento selecionado no processo. Devendo repetir essa importação por empreendimento.**

***Pré-requisitos para importação de contratos: Realizar os ca******dastros abaixo ou importar via conceito***

* ***Cliente/Fornecedores;***
* ***Empreendimentos, unidades e subunidades;***
* ***Cadastro de Componentes;***
* ***Índices de reajustes das Moedas de INCC, IGPM e IPCA.***
Importador de ContratosPermissão Perfil |

Habilitar o perfil do usuário TCGI para que possa utilizar a Funcionalidade ( Importador de contratos )

Gestão de Imóveis => Utilitários => 07.01.03 - Importador de Contrato de Venda.

Menu - Utilitários . Tela na versão superior 12.1.2306.134

Estrutura do Arquivo de Importação |

**Arquivo deve ser elaborado no Excel (ou alguma outra ferramenta) e salvo como xls ou xslt durante a manipulação do arquivo.**

**Baixe no link acima o modelo completo do arquivo de importação de contrato de venda**

**Somente após a manipulação dos dados  que o arquivo deverá ser salvo na extensão ( CSV ), se precisar manipular o arquivo novamente, altere no arquivo original xls e converta novamente para CSV. Isso evita que o CSV perca a formatação dos dados.**

Os campos devem ser salvos com a seguinte formatação no **Excel**.

* **Contrato** = Geral
* **Empreendimento** = Número
* **Unidade** = Texto
* **Subunidade** = Texto
* **Total\_Venda** = Número
* **Data\_Venda** = Data
* **Data\_assinatura** = Data
* **Cpf1** = Geral
* **Cpf2** = Geral
* **Cpf3** = Geral
* **Cpf4** = Geral
* **Cpf5** = Geral
* **Data de Entrada** = Data
* **Data de Saída** = Data
* **Grupo** =  Número
* **Comp\_princ** = Número
* **Modelo** = Número
* **Compoe\_venda** = Número
* **Vencimento** = Data
* **Vr\_parc** = Número
* **Vr\_origem** = Número
* **Nro\_parc** = Geral
* **Compn\_juros** = Geral
* **Taxa\_juros** = Número
* **Juros\_composto** = Geral
* **Database\_juros** = Data
* **Periodicidade\_juros** = Geral
* **Tipo\_base\_juros** = Geral
* **Vr\_juros** = Número
* **Compn\_CMAntes** = Geral
* **Moeda\_CMAntes** = Geral
* **Capitalizado\_CMAntes** = Geral
* **Database\_CMAntes** = Data
* **Periodicidade\_CMAntes** = Geral
* **Tipo\_base\_CMAntes** = Geral
* **Vr\_CMAntes** = Geral
* **Compn\_CMApos** = Geral
* **Moeda\_CMApos** = Geral
* **Capitalizado\_CMApos** = Geral
* **Database\_CMApos** = Data
* **Periodicidade\_CMApos** = Geral
* **Tipo\_base\_CMApos** = Geral
* **Vr\_CMApos** = Número
* **Comp\_seguro** = Geral
* **Vr\_seguro** = Número
* **Taxa\_seguro** = Número
* **Compn\_desc** = Geral
* **Vr\_desc** = Número
* **Data Fixa**= Data Fixa do último reajuste aplicado no valor, fique atento com reajuste anual, tem que ser do último aniversário
* **Compn\_taxa** = Geral
* **Vr\_tx** = Número
* **Cod\_formula\_outros** = Texto
* **Taxa\_outros** = Número
* **Aditivo Cancelou** = Texto
* **Aditivo Criou**= Texto
* **Data Aditivo** = Data

Observação!

Cada linha do Arquivo importado represente uma parcela no contrato do TCGI.

Neste exemplo o arquivo contém 2 contratos ( 5626 e 5627 )

O primeiro contrato contém duas linhas para Grupo 1 , tipo Entrada, e 5 linhas para Grupo 2, tipo Mensal.

O segundo contrato contém 7 linhas para Grupo 1, sendo  2 parcelas de Entrada e 5 parcelas Mensais.

**Detalhes do arquivo Importado no TCGI , em ( Sobre o arquivo de Importação )!**

Sobre o arquivo de Importação |

**No arquivo de Importação de um contrato para o TCGI existem as seguintes informações abaixo.**

**Campos da Venda**

* **Número do contrato do cliente**
  + Será associando a venda no cadastro de contrato para ter a rastreabilidade com o sistema legado
* **Empreendimento**
* **Unidade**
* **Subunidade**
* **Total da Venda**
* **Data da Venda**
* **Data de Assinatura**
* **Compradores (CPF1 ao CPF5)**
  + Pode incluir até 5 compradores para uma venda e a proporção será dividida pela quantidade de compradores informados no arquivo de importação.
  + Exemplo: Se informar 1 comprador, será efetivada com 100% para este único comprador , se for informado 5 compradores, 20% para cada comprador e 2 Compradores, 50% para cada um dos compradores. Lembrando que sempre o primeiro comprador inserido no arquivo será o comprador Principal.
* **Data de Entrada**
  + Ser ficar em branco será usado a data da venda como entrada no plano;
  + Tem que respeitar as mesmas regras do cadastro de comprador via RM.exe;
  + Não pode haver interseção de datas com outros compradores;
  + Usar este campo caso deseje importar o histórico de compradores  desse contrato, se não existir outros compradores deixar esse campo em branco;
  + Exemplo está abaixo com o título  ***Exemplo do preenchimento dos dados dos Compradores***
* **Data de Saída**
  + Ser ficar em branco que dizer que o comprador está ativo;
  + Tem que respeitar as mesmas regras do cadastro de comprador via RM.exe;
  + Não pode haver interseção de datas com outros compradores;
  + Usar este campo caso deseje importar o histórico de compradores  desse contrato, se não existir outros compradores deixar esse campo em branco;
  + Exemplo está abaixo com o título  ***Exemplo do preenchimento dos dados dos Compradores***

**Campos da Condição de Financiamento**

* **Grupo** 
  + Grupo da Condição de Financiamento, pode usar 1 para todos, ou separar por tipos de componentes, Entrada 1, Mensal e anual 2.
* **Código do Componente Principal (Tipo Componente - 1 ou 2)**
  + Componente que gerou a parcela, verificar o código no cadastro de componentes (1 ou 2, ou algum outro que esteja utilizando)
* **Modelo de Cálculo**
  + 0 - Entrada;
  + 1 - SAC;
  + 2 - Price;
  + 9 - Juros Mensal;
  + 13 - Modelo Padrão.
  + 15 - Minha Casa Minha Vida.

* **Compõe o Valor da Venda**
  + 0 - não compõe;
  + 1 - compõe.
* **Data de Vencimento da Parcela**
* **Valor Total da Parcela**
  + Somatório de todos os componentes informados nesse arquivo
* **Valor Original da Parcela** 
  + Valor principal da parcela, sem juros, sem CM, somente o valor financiado correspondente a esta parcela.
* **Número da Parcela (Nota Promissória)**
  + Exemplo:  001/100 - 1 parcela de 100, 2 parcela de 100 e etc.

**Campos sobre o Juros (Tipo Componente - 3)**

* **Código do Componente de Juros**
  + Informar o código para o  componente de Juros (3 ou 12, ou algum outro que esteja utilizando)
* **Taxa de Juros**
  + Informar a taxa que será associada a este componente em decimal sem o %
  + Exemplo:  1,9875%  => informar 1,9875
* **Juros Composto**
  + 0 - Simples;
  + 1 = Composto;
* **Data Base do Juros**
  + Normalmente é a mesma data da venda, ou seja, quando irei cobrar esse juros.
* **Periodicidade do Juros**
  + 1- Mensal;
  + 2 - Bimestral;
  + 6 - Semestral;
  + 12 - Anual.
* **Tipo Base de Cálculo do Juros**
  + 0 - Principal ;
  + 1 - Principal + CM Anterior ;
  + 2 - Principal + CM Atual;
* **Valor do Juros na Parcela**
  + Informar o valor dos juros da parcela, somente quando for Price que deve ser informado.
  + **Nos demais caso pode deixar com ZERO ou com o valor, pois o sistema irá RECALCULAR.**

**Campos sobre o CM Antes (Tipo Componente - 4)**

* **Código do Componente de CM Antes**
  + Informar o código para o  componente de Cm (11 ou algum outro que esteja utilizando)
* **Código da Moeda do CM Antes**
  + Informar o código da moeda utilizado: INCC, IPCA ou algum outro que esteja na base de dados
* **Capitalizado - CM Antes**
  + 0 - não;
  + 1 = Sim;
* **Data Base do CM Antes**
  + Normalmente é a mesma data da venda, ou seja, quando irei cobrar esse CM.
* **Periodicidade do CM Antes**
  + 1- Mensal;
  + 2 - Bimestral;
  + 6 - Semestral;
  + 12 - Anual.
* **Tipo Base de Cálculo do CM Antes**
  + 0 - Principal ;
  + 1 - Principal + Juros Anterior;
  + 2 - Principal + Juros Atual;
* **Valor do CM Antes na Parcela**
  + Pode deixar com zero ou com o valor, pois o sistema irá recalcular.
  + **Futuramente iremos utilizar esse valor para criar a foto, mas hoje não utilizamos, o reajuste sobrepõe o valor informado.**

**Campos sobre o CM Após (Tipo Componente - 4)**

* **Código do Componente de CM Após**
  + Informar o código para o  componente de CM (11 ou algum outro que esteja utilizando)
* **Código da Moeda do CM Após**
  + Informar o código da moeda utilizado: IGPM ou algum outro que esteja na base de dados
* **Capitalizado - CM Após**
  + 0 - não;
  + 1 = Sim;
* **Data Base do CM Após**
  + Normalmente é a mesma data da venda, ou seja, quando irei cobrar esse CM.
* **Periodicidade do CM Após**
  + 1- Mensal;
  + 2 - Bimestral;
  + 6 - Semestral;
  + 12 - Anual.
* **Tipo Base de Cálculo do CM Após**
  + 0 - Principal ;
  + 1 - Principal + Juros Anterior;
  + 2 - Principal + Juros Atual;
* **Valor do CM Após na Parcela**
  + Pode deixar com zero ou com o valor, pois o sistema irá recalcular.
  + Futuramente iremos utilizar esse valor para criar a foto, mas hoje não utilizamos

**Campos sobre o Seguro (Tipo Componente - 19)**

* **Código do Componente de Seguro**
  + Informar o código para o componente de Seguro de Empreendimento (190, ou algum outro que esteja utilizando)
* **Valor do Seguro na Parcela**
  + Informar o valor do Seguro, caso ele já esteja calculado na parcela ou deixar 0.
* **Taxa do Seguro**
  + Informar a taxa que será associada a este componente em decimal divido por 100 sem o %
  + Exemplo:  1,25%  => informar 0,0125

**Campos sobre Outros Componentes (Tipo Componente - 99 ou 100 ) ou do Tipo Desconto (Tipo Componente - 900 )**

* **Código do Componente do Tipo Outros ou de Desconto**
  + Informar o código para esse Componente (14, 900 ou algum outro que esteja utilizando desse tipo)
* **Valor do Componente**
  + Informar o valor do componente

**Campos sobre a Data do Último Reajuste Aplicado no sistema Legado**

* **Data Fixa**= Data Fixa do último reajuste aplicado no valor, fique atento com reajuste anual, tem que ser do último aniversário

**Campos sobre Outros Componentes (Tipo Componente - 99 ou 100 )  ou do Tipo Seguro  (Tipo Componente - 19)**

* **Código do Componente**
  + Informar o código para o componente de Seguro de Empreendimento (14, 190, ou algum outro que esteja utilizando)
* **Valor do Componente**
  + Informar o valor do componente, caso ele já esteja calculado na parcela ou deixar 0 para usar o valor da fórmula.
* **Código da Fórmula - Utilizar somente se o componente for do tipo de seguro por empreendimento**
  + Informar o código da fórmula para calcular o valor do seguro, essa fórmula tem que estar cadastrada em todas as coligadas que serão importadas.
* **Taxa do Seguro - Utilizar somente se o componente for do tipo de seguro por empreendimento**
  + Informar a taxa que será associada a este componente em decimal divido por 100 sem o %
  + Exemplo:  1,25%  => informar 0,0125

**Campos sobre Aditivo Renegociador - Tela na versão superior 12.1.2306.134**

* **Aditivo Cancelou**   
  + Informar o código do aditivo que criou a parcela, pode ser inteiro ou string ( não é obrigatório, pode existir apenas parcela criada)
  + o importador irá cancelar a parcela que tenha esse código preenchido e criará um aditivo com essa parcela cancelada na data do aditivo
* **Aditivo Criou**  
  + Informar o código do aditivo que cancelou a parcela, pode ser inteiro ou string ( não é obrigatório, pode existir apenas parcela cancelada)
  + o importador irá criar a parcela que tenha esse código preenchido e criará um aditivo com essa parcela criada na data do aditivo.
  + se informar a parcela cancelada será associada ao mesmo aditivo
* **Data Aditivo**  
  + Informar a data do aditivo que cancelou e/ou criou.

Atenção

Os campos de valor da parcela e quantidade de parcelas serão calculados com base dos dados da parcela importados

O cliente do lançamento financeiro será o comprador principal.

As informações em Condições de Financiamento de integração com o financeiro serão informados na aba do processo de importação

## **Campos do Arquivo de Importação no Contrato de Venda do TCGI.**

## **Exemplo do preenchimento dos dados dos Compradores**

Neste exemplo, o cliente 1 e 2 entrarão no plano na data entrada/saída 25/05/12 a 04/08/12 com pagamento de 4 parcelas.

Depois houve uma troca de comprador dos clientes 1 e 2  para o cliente 4 que ficou na venda do dia 04/08/12 a 30/08/2012 e não pagou nenhuma parcela (deixar todos os campos em branco de campo DataSaida);

Depois houve uma troca de comprador do cliente 4  para o cliente 5 que entrou na venda do dia 30/08/2012 e está até hoje .

## **Exemplo do preenchimento dos dados da Condição de Financiamento**

Neste exemplo , o arquivo importado tem Grupo 1 ( Duas parcelas no valor de 5.000 Reais ) , no sistema mostrando o valor total de 10.000.

O Grupo 2 Mensal , o arquivo tem 5 parcelas no valor de 18.000 Mil Reais e no sistema , condições de financiamento o valor total de 90.000 Reais.

## **Exemplo do preenchimento do Componente Principal ou de Entrada**

## **Exemplo do preenchimento dos dados da Parcela, Data de Vencimento, Valor Original e Etc.**

No exemplo acima ainda, veja que, a parte com cor preta é do tipo de Entrada, então não preenchemos os campos de juros, cm antes e cm após.

A parte com cor vermelha é do tipo mensal, então é preenchido o juros, cm antes e cm após.

## **Exemplo do preenchimento de Juros**

## **Exemplo do preenchimento de CM Antes ou CM Após**

## **Exemplo do preenchimento do Seguro por Empreendimento**

## **Exemplo do preenchimento dos dados do Componente de** **Desconto**

## **Exemplo do preenchimento dos dados do Seguro por****Empreendimento com uso de Fórmulas**

**Preenchendo****o campo Taxa, o componente só pode ser do Tipo de Seguro por Empreendimento**

Pode se informar no arquivo de Importação código da Fórmula, caso deseja que o seguro seja calculado via fórmula

## **Exemplo do preenchimento de Componente do Tipo Outros - Lançar um Taxa Administrativa**

**Importando****o campo Taxa - Neste exemplo , o componente usado é ( Taxa Administrativa )**

Importando um novo contrato |

Localizar o arquivo que será importado para dentro do TCGI.

Utilitários | Importador de Contrato de Venda

Sobre os campos do Arquivo de importação nos parâmetros do TCGI.

Exemplo das posições com o Arquivo de Importação:

1. hyperlink da documentação do no TDN e com o modelo do arquivo, depois tem 1º botão a esquerda que configura as posições dos campos conforme a imagem do quadro 3, e o botão a direita que limpa as posições dos campos, caso deseje fazer uma configuração diferente;
2. Localizar o arquivo de extensão CSV para importar os contratos;
3. Posição dos campos no arquivo de Importação : Essa parametrização é super importante , pois ai será informada a ordem de campo a campo de todos os dados da Planilha para importação. Neste exemplo , 1 é contrato de venda , se o campo 1 da planilha for por exemplo CPF , a importação não será realizada;
4. Perfil - Informar um nome e clicar no botão verde para salvar a configuração da tela realizada e no vermelho para excluir o perfil configurado. Pode cadastrar diversos perfis com informações diferentes, basta colocar nomes diferentes e clicar no verde para salvar logo em seguida.
5. A importação é feita por empreendimento, mas o arquivo pode ser único com todos os contratos de todos empreendimentos que o sistema irá filtrar automaticamente.

Nesta próxima tela , o sistema informa todos os dados dos campos que serão importados para dentro do TCGI , um checklist para que o Usuário possa avaliar antes de avançar.

As demais configurações das regras são informadas nessa tela - Tela na versão superior 12.1.2306.140

Pro-Rata

## Novidade no Importador de Contrato de Venda – Opção de Pro-Rata e Data de Reajuste dos Valores Importados

Foi incluída no **Importador de Contrato de Venda** a possibilidade de escolher a forma de aplicação do **Pro-Rata**.

Agora, além do cálculo padrão, o usuário pode optar por:

* **Pro-Rata Juros** → quando o objetivo for considerar o ajuste proporcional sobre os juros do contrato.
* **Pro-Rata CM** → quando o ajuste proporcional deve ser aplicado sobre o **Componente Mensal (CM)**.

Será obrigatório informar a da "Data de Reajuste dos Valores Importados" para que o sistema armazene os valores de reajuste do CM e juros para essa data, sendo assim quando o sistema for calcular o líquido para datas anteriores e até essa data, o sistema sempre retornará o valor importado. Para datas posteriores, o valor líquido será calculado utilizando a base do valor definido e reajustando mês a mês ;

**1 - Neste etapa , é configurado no Perfil os dados da venda.**

* Tabela de Preço
* Modalidade
* Conta Caixa
* Filial
* Departamento
* Centro de Custo
* Natureza Financeira a Receber
* Natureza Financeira a Pagar
* Tipo de Documento a Receber
* Tipo de Documento a Pagar

**2 - Gerar o lançamento financeiro com os valores da Planilha**

Com este parâmetro marcado , no final do processo de importação , os contratos serão criados já com as parcelas geradas.

**3 - Dados do Componentes - Parametrização de como ficará a referência de entrega para o componente.**

* Data da entrega do Empreendimento
* Data da entrega da chave
* Data do habita-se
* Data de assinatura

**4- Aplicar Reajuste em:**

* Somente parcelas vincendas
* Ambas ( Vincendas e vencidas )
* Somente parcelas vencidas

**5 - Correção Monetária**

* Informa o tempo desejado ( meses ) para defasagem
* Ignorar ou não deflação
* Tipo de Moeda
  + Índice acumulado
  + Índice mensal

**6 - Tabela Opcional do Financeiro**

* Informa os valores das tabelas opcionais do financeiro

Contratos criados no TCGI
