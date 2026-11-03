---
content_hash: 02a8af53150816ad1f8d9b8a9bb4dcd7166fa2685e3941ab3c022cfa52b8aa64
fetched_at: '2026-06-29T00:09:18.473170+00:00'
page_id: '421388703'
product: rm
source: tdn-rm
title: FIN - Retorno Cobrança Eletrônica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388703
version: 16
---

**Tipo de retorno de Cobrança**

**Retorno de Cobrança registrada**

Esta opção deverá ser utilizada na importação de arquivos de retorno de cobrança gerados em padrões diversos, exceto no padrão CNAB240. Se o arquivo tiver 240 colunas, você deverá optar pela opção "Retorno de Cobrança CNAB 240".

Ao importar o retorno, o sistema irá identificar o lançamento pelo código da coligada + a referência do Lançamento ou pelo Código da Coligada seguido do numero 1 (que caracteriza o IDBOLETO) + a referência do Boleto.

Exemplo

001000000000000000006973, onde:

001 = Código da Coligada

000000000000000006973 = referência do Lançamento Financeiro  
Ou

0011000000000000000006974, onde:

001 = Código da Coligada

1 = Caracteriza que é um IDBOLETO

000000000000000006974 = referência do Boleto

**Observação**

Ao importar o arquivo de retorno, o sistema identifica os lançamentos de mesmo IDBOLETO e produz a baixa total ou parcial de todos os Lançamentos de mesmo IDBOLETO.

Deve ser gravado o código de barras, caso o campo não esteja preenchido no boleto, após o processo de retorno de cobrança, para os boletos onde o nosso número for gerado pelo banco (convênio parametrizado para gerar nosso número pelo Banco).

**Retorno de Cobrança não registrada**

Esta opção deverá ser utilizada na importação de arquivos de retorno de cobrança gerados em padrões diversos, exceto no padrão CNAB240. Se o arquivo tiver 240 colunas, você deverá optar pela opção "Retorno de Cobrança CNAB 240". Ao importar o retorno, o sistema irá identificar o lançamento pelo campo "Nosso Numero" ou  de acordo com as definições dos parâmetros de Integração Bancária referente a Cobrança Eletrônica (Usar Numero Documento no retorno de Cobrança Sem registro).

**Retorno de Cobrança CNAB 240**

Esta opção deverá ser utilizada para importação de arquivos de retorno no padrão CNAB 240, com adequações ou não, desde que o tamanho do arquivo seja 240 posições. Se o tamanho for diferente de 240 colunas, você deverá utilizar uma das opções citadas acima, conforme o tipo de Cobrança (registrada ou não). Ao importar o retorno neste padrão, será oferecida uma opção para que você possa definir se a cobrança é registrada ou não. Feita esta opção, o comportamento para identificar o lançamento será conforme explicado nas opções acima.

**Dados da importação**

É necessário indicar o local onde está o arquivo a ser importado;  o código da Filial,  Código da Conta Caixa para a baixa dos Lançamentos. Informando a Conta Caixa, o Banco será atualizado (Banco correspondente ao arquivo que será importado). Informe também o Evento Contábil para a contabilização da baixa e se não informado será utilizar o evento parametrizado para o processo de Baixa. Indique também o Histórico para os registros do extrato, e se não for indicado será utilizado e "Histórico default  de Baixas a receber" parametrizado pelo Assistente de Implantação de processos, etapa 02.02 Contas a Receber / Baixas a Receber.

**Parâmetros da Importação**

Nesta tela do retorno tem a opção para definirmos a ação ser adotada quando o valor pago for a menor ou a maior e esta definição pode ser fixada nos parâmetros de cobrança eletrônica (Opções /Parâmetros/ 02.02 - Cobrança Eletrônica). Portanto, esta opção somente será aplicada se a diferença entre o valor liquido do Lançamento e o valor do crédito no arquivo de retorno for inferior ao valor estipulado para baixa parcial ou Adiantamento definidos pelos parâmetros.

Atenção: Os Valores de Integração do Educacional também afetam as configurações dos parâmetros "Se diferença A Maior" e "Se diferença A Menor". Caso sejam configurados no módulo Educacional os valores nesses campos serão gravados nos Valores de Integração respectivos, sobrepondo a parametrização feita no processo de retorno de cobrança, exceto para os campos "Juros", "Multa", "Desconto" e "Não baixar" que se selecionados matém o comportamento do processo. Para saber mais detalhes da configuração no Educacional consulte .

Exemplo

Valor líquido do Lançamento                 = 600,00

Valor do crédito do arquivo de retorno = 500,00

Parametrização

* Diferença para geração da baixa parcial = 50,00. Nesse caso, ao importar o retorno será gerada uma baixa parcial de 500,00, indiferente se for informado "valor a menor = desconto", porque a diferença de 100,00 é superior ao valor indicado nos parâmetros. Se o valor do crédito no arquivo de retorno fosse 560,00 a diferença equivalente a 40,00 seria reconhecida como "Desconto" ou outro valor que você determinasse no momento da importação do retorno.
* Diferença para geração de Adiantamento = 150,00. Ao importar um arquivo de retorno cujo valor do credito for superior ao valor liquido do Lançamento, a ação será tomada conforme o valor informado nesse parâmetro.

Exemplo

Valor líquido do Lançamento                 = 600,00

Valor do crédito do arquivo de retorno = 800,00

O lançamento será totalmente quitado e será gerado um lançamento do tipo "Adiantamento" pelo valor de 200,00 baixado. Consequentemente será gerado um Lançamento tipo Crédito de Adiantamento no mesmo valor. Se o valor da diferença for inferior a 150,00, o sistema irá reconhecer essa diferença no campo indicado no momento da importação do retorno.

O lançamento de adiantamento criado, terá um default no histórico com a seguinte informação: "Adiantamento referente ao recebimento a maior do retorno bancário Documento Número XXX", onde XXX terá o Número do Documento do lançamento lido no arquivo e baixado.

**Observação:**

O sistema oferece outro recurso (localizado nos parâmetros relacionados a Integração Bancária) que é considerar os valores do arquivo de retorno sobrepondo os do Lançamento. Nesse caso, os acréscimos e descontos serão destacados no arquivo de retorno e serão reconhecidos em cada lançamento no momento da importação.

Exemplo:

Valor original = 100,00

Juros              =     1,00

Valor liquido  = 101,00

No arquivo de retorno os juros informados foram  de 1,20. Após a importação do retorno, o valor dos juros do lançamento será reconhecido por 1,20.

**Importante**: Caso exista mais de um lançamento no boleto contido no arquivo de retorno, o sistema irá proporcionalizar o valor dos juros em cada lançamento. O mesmo vale para os campos nativos "Multa" e "Desconto"). No caso dos valores opcionais, o sistema irá considerar os valores somente do lançamento que possuir tal valor. Se existir valor no arquivo de retorno referente aos valores opcionais mas não existir no (s) lançamento (s) vinculado (s) ao boleto, o sistema irá proporcionalizar tais valores em cada lançamento.

Caso a flag 'No retorno bancário utilizar os valores (juros, multa, desconto e opcionais) do arquivo (layout), sobrepondo os do lançamento' esteja desmarcada e a opção 'Data do vencimento do boleto' esteja selecionada no campo "Data para cálculo do valor líquido dos lançamentos do boleto não vencido", quando o arquivo de retorno de cobrança for importado, o sistema irá calcular o valor líquido do lançamento conforme a data de vencimento do boleto.  
  
Utilizar Conta/Caixa do Lançamento: A baixa será realizada utilizando a conta caixa do lançamento ao invés de usar a conta caixa informada no momento da importação do retorno.

Cobrança Registrada

Ao selecionar o tipo de cobrança registrada essa opção ficará habilitada no sistema e não permitirá alteração.

Para o tipo de cobrança não registrada essa opção também será apresentada desabilitada, porém o sistema respeitará e seguirá a opção selecionada do tipo e cobrança não registrada.

Para a o tipo de cobrança Cnab240 a opção de cobrança registrada será apresentada com opção de seleção, sendo que:

* Quando marcada, ao importar o retorno, o sistema irá identificar o lançamento pelo código da coligada + referência do Lançamento ou pelo Código da Coligada seguido do numero 1 + a referência do Boleto.
* Quando desmarcada, ao importar o retorno, o sistema irá identificar o lançamento pelo campo “Nosso Numero” ou de acordo com as definições dos parâmetros de Integração Bancária referente a Cobrança Eletrônica (Usar Numero Documento no retorno de Cobrança Sem registro).

Ao parametrizar para usar o reajuste online no processo de baixa é necessário que o parâmetro "Permitir alterar lançamentos a receber remetidos ao banco." esteja setado como verdadeiro para que a baixa seja realizada.

Consistir Nosso Número apenas para Lançamento em aberto

Essa opção permanece funcional apenas para Cobrança não registrada, pois a numeração do nosso número pode ser reiniciada.   
Será usada para, ao procurar o lançamento pelo Nosso Número para cobrança não registrada, o sistema procura apenas nos lançamentos em aberto.

Usar Data Compensação como data de Contabilização da Baixa

Marcando essa opção, a "Data de Contabilização de Baixa" dos lançamentos, será a "Data de Compensação" informada no arquivo bancário.

Gerar um extrato para todos os Lançamentos

Com essa opção marcada, ao importar o arquivo de retorno será gerado apenas um registro no Extrato de Caixa pelo valor total dos lançamentos recebidos pelo banco. Obs: Esta opção fica indisponível ao utilizar a cobrança partilhada, pois nesse caso um extrato é gerado para cada lançamento envolvido no boleto partilhado e em suas respectivas coligadas.

Cobrança partilhada (disponível apenas para o Padrão 400 posições do Banco Santander - Febraban 033)

O sistema também processará os registros de partilha contidas no arquivo de retorno importado. Ressaltamos a necessidade de preencher as posições correspondentes a Partilha no [layout bancário](https://tdn.totvs.com/pages/viewpage.action?pageId=421388586) do cadastro do Banco **Santander (033)**. 

A importação do arquivo de retorno para a cobrança eletrônica está disponível para os seguintes Bancos:

* Banco do Brasil
* Banco Nordeste
* Banco Real Banco
* Rural Bandeirantes
* Bandepe
* Banespa
* BankBoston
* Banrisul
* BCN
* Bradesco
* CEF
* HSBC
* Itaú
* Real
* Safra
* Santander
* Unibanco
