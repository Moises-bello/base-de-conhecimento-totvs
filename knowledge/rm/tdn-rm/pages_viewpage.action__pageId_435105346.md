---
content_hash: f66aa36d3358ea4868ac7484ba7beacb539367067f107249bc78d7708006fb96
fetched_at: '2026-06-29T00:09:49.690022+00:00'
page_id: '435105346'
product: rm
source: tdn-rm
title: Gestão - Funções de Fórmulas - Aluguel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105346
version: 34
---

**PARMQRY**    
Retorna o conteúdo de um campo.

* **Sintaxe**PARMQRY( ' CAMPO ' )
* **Exemplo**Exemplo da função **PARMQRY**  retornando campos dos [fatores de CRD:](https://tdn.totvs.com/pages/viewpage.action?pageId=435105196)

**EXTENSODATA**  
Retorna uma data por extenso

**Contexto**  
Independente do contexto**VALORLIQUIDOPFTIN**

**Sintaxe**  
EXTENSODATA ( DATA )  
A sintaxe da função EXTENSODATA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA – Data a ser retorna por extenso

**Exemplo**  
EXTENSODATA('20/03/2010')

**EXTENSONUMERO**  
Retorna um número por extenso

**Contexto**  
Independente do contexto

**Sintaxe**  
EXTENSONUMERO ( VALOR )  
A sintaxe da função EXTENSONUMERO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Número a ser retornado por extenso

**Exemplo**  
EXTENSONUMERO(1453)

**EXTENSOVALOR**  
Retorna um valor por extenso

**Contexto**  
Independente do contexto

**Sintaxe**  
EXTENSOVALOR ( VALOR )  
A sintaxe da função EXTENSOVALOR tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Valor a ser retornado por extenso

**Exemplo**  
EXTENSOVALOR(156.14)

**FORMATANUMERO**  
Retorna um número formatado em inteiro

**Contexto**  
Independente do contexto

**Sintaxe**  
FORMATANUMERO ( VALOR )  
A sintaxe da função FORMATANUMERO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Valor a ser formatado para o padrão inteiro

**Exemplo**  
FORMATANUMERO(156.14)

**FORMATAVALOR**  
Retorna um valor formatado em moeda

**Contexto**  
Independente do contexto

**Sintaxe**  
FORMATAVALOR ( VALOR )  
A sintaxe da função FORMATAVALOR tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Valor a ser formatado para o padrão moeda

**Exemplo**  
FORMATAVALOR(152.6)

**DIFERENCADIAS**  
Retorna a Diferença de dias entre duas datas

**Contexto**  
Independente do contexto

**Sintaxe**  
DIFERENCADIAS ( DATA1, DATA2 )  
A sintaxe da função DIFERENCADIAS tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA1 – Primeira Data
  + DATA2 – Segunda Data

**Exemplo**  
DIFERENCADIAS('10/03/2012','10/02/2012')

**DIFERENCAMESES**  
Retorna a Diferença de meses entre duas datas

**Contexto**  
Independente do contexto

**Sintaxe**  
DIFERENCAMESES ( DATA1, DATA2 )  
A sintaxe da função DIFERENCAMESES tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA1 – Primeira Data
  + DATA2 – Segunda Data

**Exemplo**  
DIFERENCAMESES('10/03/2012','10/02/2012')

**ADICIONADIAS**  
Adiciona Dias a uma Data

**Contexto**  
Independente do contexto

**Sintaxe**  
ADICIONADIAS ( STRING, DATA1, DATA2, DATA3, VALOR1, VALOR2 )  
A sintaxe da função ADICIONADIAS tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA – Data para adicionar dias
  + DIAS – Dias a ser adicionado a uma data

**Exemplo**  
ADICIONADIAS('10/03/2012',10)

**ADICIONAMESES**  
Adiciona Meses a uma Data

**Contexto**  
Independente do contexto

**Sintaxe**  
ADICIONAMESES ( DATA, MESES)  
A sintaxe da função ADICIONAMESES tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA – Data para adicionar dias
  + MESES – Meses a ser adicionado a uma data

**Exemplo**  
ADICIONAMESES('10/03/2012',10)

**ADICIONAANOS**  
Adiciona Anos a uma Data

**Contexto**  
Independente do contexto

**Sintaxe**  
ADICIONAANOS ( DATA, ANOS )  
A sintaxe da função ADICIONAANOS tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

DATA – Data para adicionar anos

ANOS – Anos a ser adicionado a uma data

**Exemplo**  
ADICIONAANOS('10/03/2012',10)

**ALGTABELAEVENTOFINANCEIRO**  
Retorna informações sobre o registro da tabela XALGEVENTOFINANCEIRO carregada no contexto

**Contexto**  
Chave da tabela "XALGEVENTOFINANCEIRO"

**Sintaxe**  
ALGTABELAEVENTOFINANCEIRO  
A função de formula espera como parâmetro o nome da coluna e o tipo do dado que será retornado. (Tipo de dados: D => Data | I => inteiro | S => string | V => valor).

**Exemplo**  
ALGTABELAEVENTOFINANCEIRO('DATAEVENTFIN','D')

**ALGTABELAEVENTOFINANCEIRODISTRIBUICAO**  
Retorna informações sobre o registro da tabela XALGEVENTOFINANCEIRODISTRIBUIC carregada no contexto

**Contexto**  
Chave da tabela "XALGEVENTOFINANCEIRODISTRIBUIC"

**Sintaxe**  
ALGTABELAEVENTOFINANCEIRODISTRIBUICAO   
A função de formula espera como parâmetro o nome da coluna e o tipo do dado que será retornado. (Tipo de dados: D => Data | I => inteiro | S => string | V => valor).

**Exemplo**  
ALGTABELAEVENTOFINANCEIRODISTRIBUICAO('CODEVENTFIN','I')

**ALGVALORESLANCAMENTOFINANCEIRO**  
Retorna informações sobre o lançamento em uma dada data e com referência nos dados da tabela XALGEVENTOFINANCEIRODISTRIBUIC carregada no contexto

**Contexto**  
Usa como contexto a chave da tabela "XALGEVENTOFINANCEIRODISTRIBUIC" e permite ao usuário consultar possíveis valores do lançamento financeiro respectivo à distribuição. Esta informação é obtida chamando o serviço disponível do modulo financeiro (IFinLanMod.ValorLiquido)

**Sintaxe**  
ALGVALORESLANCAMENTOFINANCEIRO(DataReference, ValorRetorno)

* + DataReference: Data de Referência para cálculo dos valores do lançamento
  + ValorRetorno: Pode ser um dos valores abaixo:

DESCONTO  
DESCONTOBX  
INSS  
INSSBX  
IRRF  
IRRFBX  
MULTAATRASO  
MULTAATRASOBX  
JUROSMORA  
JUROSMORABX  
LIQUIDO  
LIQUIDOPARCIAL  
ORIGINAL  
ORIGINALBX  
RETENCOES  
RETENCOESBX

**Exemplo**  
ALGVALORESLANCAMENTOFINANCEIRO('20/12/2018','MULTAATRASO')

**ALGVALORESINTEGRACAONAOPARTICIPAODIMOBLANCAMENTOFINANCEIRO**  
A função se baseia no retorno de um serviço do modulo de gestão financeira para retornar os valores desejados

**Contexto**  
Usa como contexto a chave da tabela "XALGEVENTOFINANCEIRODISTRIBUIC" e permite ao usuário consultar possível saldo de valores de integração do lançamento financeiro que não participam do DIMOB. Para encontrar este saldo devemos verificar se o valor de integração está configurado como "Acrescenta" ou "Desconta" para conseguirmos calcular o saldo.

**Sintaxe**  
ALGVALORESINTEGRACAONAOPARTICIPAODIMOBLANCAMENTOFINANCEIRO  
Esta informação é obtida chamando o serviço disponível do modulo financeiro (IFinLanMod.ValorLiquido) e caso tenha algum valor de integração fazendo o rastro no TIN se o evento agregado que o originou esta configurado para participar do DIMOB. A função de formula espera como parâmetro uma data de referencia que será utilizada para calcular valores variáveis em função da data. (DataReference: DateTime)

**ALGITEMBAIXALANCAMENTOFINANCEIRO**

**Contexto**  
Retorna dados do item de baixa do lançamento financeiro.   
Obs.: Apenas é passível de execução no processamento do DIMOB de locação onde o item de baixa é passado por parâmetros da função.

**Sintaxe**  
ALGITEMBAIXALANCAMENTOFINANCEIRO(Valor desejado, Tipo do valor)

* + Valor desejado que aceita os seguintes valores:  
    IDBAIXA  
    STATUSBAIXA  
    DATABAIXA  
    VALORBAIXA  
    VALORORIGINALBAIXA  
    VALORDESCONTOBAIXA  
    VALORMULTAATRASOBAIXA  
    VALORJUROSMORABAIXA  
    VALORIRRFBAIXA
  + Tipo do valor

Tipo de Valor ('D' => Date; 'I' => Inteiro; 'S' => String; 'V' => Valor

**ALGDATACONTABIL**

Retorna a data informada no processo de contabilização de Aluguel

**Contexto**  
Contexto de contabilização de Aluguel

**Sintaxe**  
ALGDATACONTABIL

**ALGSALDOCREDOREVENTOFINLOCATARIO**

**Contexto**  
Retorna saldo credor dos eventos financeiros para o locatário no contrato de locação

**Sintaxe**

ALGSALDOCREDOREVENTOFINLOCATARIO

**ALGSALDODEVEDOREVENTOFINLOCADOR**

**Contexto**  
Retorna saldo devedor dos eventos financeiros para o locador no contrato de locação.

**Sintaxe**

ALGSALDODEVEDOREVENTOFINLOCADOR

**ALGSALDODEVEDOREVENTOFINLOCATARIO**

**Contexto**  
Retorna saldo devedor dos eventos financeiros para o locatário no contrato de locação.

**Sintaxe**

ALGSALDODEVEDOREVENTOFINLOCATARIO

**ALGTABALUGUELCONTRATOLOCACAOCOMISSAO**

Retorna o valor de qualquer campo da tabela de comissão do contrato de locação

**Contexto**

Comissão de contrato de locação

**Sintaxe**

ALGTABALUGUELCONTRATOLOCACAOCOMISSAO(Campo, Tipo Valor)  
Parametros da função:

* + Campo (Nome da coluna desta tabela)
  + TipoValor ('D' => Date; 'I' => Inteiro; 'S' => String; 'V' => Valor)

**ALGTABALUGUELCONTRATOLOCACAOENCERRAMENTO**

Retorna o valor de qualquer campo da tabela de encerramento do contrato de locação

**Contexto**

Encerramento / Rescisão do contrato de locação

**Sintaxe**

ALGTABALUGUELCONTRATOLOCACAOCOMISSAO(Campo, Tipo Valor)

Parâmetros da função:

* + Campo (Nome da coluna desta tabela)
  + TipoValor ('D' => Date; 'I' => Inteiro; 'S' => String; 'V' => Valor)

**ALGCAMPOCOMPLCONTRATOLOC**

Retorna os valores dos campos complementares do contrato de locação

**Contexto**

Contrato de Locação

**Sintaxe ALGCAMPOCOMPLCONTRATOLOC(Campo, Tipo Valor)**  
Parâmetros da função:

* + Campo (Nome da coluna desta tabela)
  + TipoValor ('D' => Date; 'I' => Inteiro; 'S' => String; 'V' => Valor)

**COMPETENCIAALGCOMPLEMENTAR**

Retorna a competência que está sendo processada na geração de aluguel complementar. Se for processado fora do contexto, irá retornar a data atual

**Contexto**

Contrato de Locação

**Sintaxe**

COMPETENCIAALGCOMPLEMENTAR

**VALORBASEALUGUEL**

Retorna o valor base do aluguel para uma determinada Competência. O valor base considera os valores de Escalonamento ou Aluguel em Dobro, caso os mesmos estejam aplicados na competência informada

**Contexto**

Contrato de Locação

**Sintaxe**

VALORBASEALUGUEL(VALOR)  
Parâmetros da função:

* + VALOR - Data da competência

**FATURAMENTOALGCOMPLEMENTARVALOR**

Retorna o valor do faturamento da competência

**Contexto**

Contrato de Locação

**Sintaxe**

FATURAMENTOALGCOMPLEMENTARVALOR(VALOR)  
Parâmetros da função:

* + VALOR - Data da competência

**PERCENTUALFATURAMENTOALGCOMPLEMENTAR**

Retorna o percentual (Conforme faturamento) da Competência

**Contexto**

Contrato de Locação

**Sintaxe**

PERCENTUALFATURAMENTOALGCOMPLEMENTAR(VALOR)  
Parâmetros da função:

* + VALOR - Data da competência

*Além das fórmulas criadas (81, 82, 83 e 84) foram incluídas algumas informações no contexto do processo, que podem ser usadas para cálculo: DATACOMPETENCIA VALORBASEALUGUEL PERCENTUALALUGUELDOBRO VALORALUGUELCOMPLEMENTAR VALORFATURAMENTO PERCENTUALFATURAMENTO*

**algcontexto**

**ALGCONTEXTO**

Retorna o dados de acordo com os contextos do processo no qual a fórmula está sendo executada

**Contexto**  
No caso de Reajuste do Aluguel, pode ser usada nas seguintes situações:

* + Reajuste do Imóvel Contrato de Locação
  + Reajuste do Desconto do Contrato de Locação
  + Reajuste do Escalonamento

**Sintaxe**  
**ALGCONTEXTO('PARAMETRO')**  
Possui os seguintes parâmetros para essa função de fórmula:

**VALORORIGINAL**: Ao inserir esse parâmetro, a função de fórmula retorna o primeiro valor do contexto no qual está sendo executado. Segue alguns exemplos conforme o contexto:

* + Reajuste do Imóvel do Contrato de Locação: retornar o valor de locação do momento da Efetivação do Contrato de Locação. Mesmo que o contrato possua Aditivos onde é alterado o seu valor de Locação, ainda sim será retornado o Valor de Efetivação do Contrato de Locação;
  + Reajuste do Desconto do Contrato de Locação: retorna o valor de desconto do Contrato de Locação no momento da Efetivação do Contrato. Mesmo que o contrato possua Aditivos onde é alterado o desconto, ainda sim será retornado o valor do desconto no momento da Efetivação do Contrato
  + Reajuste do Escalonamento: retorna o valor do Escalonamento no momento da sua Efetivação. Como o valor do Escalonamento não pode ser alterado por Aditivos, essa parâmetro sempre retorna o valor original do Escalonamento

**VALORPRINCIPAL**: Ao inserir esse parâmetro, a função de fórmula retorna o valor principal atual sem o reajuste do contexto no qual está sendo executado. Segue alguns exemplos conforme o contexto:

* + Reajuste do Imóvel do Contrato de Locação: retornar o valor de locação sem reajuste do Contrato de Locação. Caso o contrato possua Aditivos onde é alterado o seu valor de Locação, será retornado o valor de locação do aditivo mais atual
  + Reajuste do Desconto do Contrato de Locação: retorna o valor de desconto sem reajuste do Contrato de Locação no atual do Contrato de Locação. Caso o contrato possua Aditivos onde é alterado o desconto, será retornado o valor de desconto do aditivo mais atual
  + Reajuste do Escalonamento: retorna o valor do Escalonamento no momento da sua Efetivação. Como o valor do Escalonamento não pode ser alterado por Aditivos, essa parâmetro sempre retorna o valor original do Escalonamento

**DTCONTRATOLOC**: retorna a Data do Contrato de Locação do contexto  
**DTVENCCONTLOC**: retorna a Data de 1° vencimento do Contrato de Locação do contexto  
**TAXAADMCONTLOC**: retorna o percentual da Taxa de administração do Contrato de Locação do contexto  
**TAXAINTERMEDCONTLOC**: retorna o percentual da Taxa de Intermediação do Contrato de Locação do contexto  
**DEFASAGEMCOTACAOLOC**: retorna o valor da Defasagem da Cotação que será utilizada no reajuste do contexto  
**COTACAOACUMULADA**: retorna se é verdadeiro ou falso o parâmetro "Capitalizado (Correção sobre Correção)" do Contrato de Locação do contexto  
**DTVIGENCIAINICONTLOC**: retorna a Data do Início de vigência do Contrato de Locação do contexto  
**DTVIGENCIAFINCONTLOC**: retorna a Data do Final de Vigência do Contrato de Locação do contexto  
**DTVIGENCIAPRORROGCONTLOC**: retorna a Data da Prorrogação de Vigência do Contrato de Locação do contexto  
**DTPROXIMOREAJUSTELOC**: retorna a Data do Próximo Reajuste do Contrato de Locação do contexto  
**DTLOCACAOINICONTLOC**: retorna a Data do Início de locação (período) do Contrato de Locação do contexto  
**DATABASECONTLOC**: retorna a Data base do Contrato de Locação do contexto  
**TXREPASSEJUROS**: retorna o percentual de Taxa de Repasse dos Juros do Contrato de Locação do contexto  
**TXREPASSEMULTA**: retorna o percentual de Taxa de Repasse de Multa do Contrato de Locação do contexto  
**TXREPASSEDESCONTO**: retorna o percentual de Taxa de Repasse do Desconto do Contrato de Locação do contexto  
**PERCDESCONTOCONTLOC**: retorna o percentual de Desconto do Contrato de Locação do contexto  
**TIPODESCONTO**: retorna o valor do Tipo de Desconto do Contrato de Locação do contexto  
**REAJUSTADESCONTO**: retorna verdadeiro ou falso de acordo com o parâmetro "Aplica reajuste no desconto" do Contrato de Locação do contexto  
**DATAPRIMEIROPERIODO**: retorna a Data do Fim do primeiro período do Contrato de Locação do contexto  
**CARENCIAALUGUEL**: retorna o número de dias da carência do Contrato de Locação do contexto;   
**AREALOCADA**: retorna o valor da Área Locada do Contrato de Locação do contexto, caso o mesmo possua imóveis do tipo "Áreas Fracionadas" ou "Áreas Unificadas";  
**CODCOLIGADACONTRATOLOCACAO**: retorna o número da Coligada do Contrato de Locação do contexto;  
**CODCONTRATOLOCACAO**: retorna o número do Código do Contrato de Locação do contexto;  
**VALORBASE**: retorna o valor atual a ser reajustado do Contrato de Locação do contexto;  
**DATREAJUSTE**: retorna a data do Reajuste do Contrato de Locação do contexto;  
**PERIODICIDACONTLOC**: retorna o número da Periodicidade do Reajuste do Contrato de Locação;  
**SIMBOLOCONTLOC**: retorna a moeda do índice do Reajuste do contexto;  
**VARIACAOPERIODO**: retorna a variação do período de um reajuste do Contrato de Locação do contexto;

**ALGSOMATORIODESCONTOSCONTRATO**

Retorna o somatório dos valores de descontos aplicados aos lançamentos baixados do contrato de locação.

Para lançamentos totalmente ou parcialmente baixados, são considerados descontos os escalonamentos que diminuem o valor do aluguel, seja pelo valor direto do escalonamento ou por desconto no próprio escalonamento, eventos financeiros a pagar ao locatário que gerem valores no lançamento que diminuam o valor do aluguel e ,por fim, apenas para lançamentos totalmente baixados, são considerados também os descontos financeiros dados no momento da baixa.

**Contexto**

A fórmula não depende de um contexto específico pois recebe todas as informações necessárias para o cálculo nos parâmetros

**Sintaxe**  
ALGSOMATORIODESCONTOSCONTRATO(CODCOLIGADA, CODCONTRATOLOCACAO, CONSIDERAVLRINTEGRACAO)

* + CODCOLIGADA  - Coligada do contrato de locação do qual se deseja o somatório
  + CODCONTRATOLOCACAO - Código do contrato de locação do qual se deseja o somatório
  + CONSIDERAVLRINTEGRACAO - Caso o valor passado seja **true** os valores de integração com ação desconta no lançamento serão considerados, caso o valor seja **false**, estes serão ignorados. Por exemplo, valores provenientes de Eventos Financeiros agregados com ação a pagar ao locatário são representados por valores de integração com ação desconta.

Importante: Quando esta função de fórmula é usada, por exemplo, numa fórmula que é utilizada para calcular a multa rescisória de um determinado contrato, este cálculo sempre será realizado baseado na data de encerramento do contrato, respeitando o período dos aditivos de prorrogação de contrato caso existam.

**Exemplo:**

Contrato com duas prorrogações feitas através de aditivos:

* Primeiro aditivo **01/01/21 à 31/12/2021**
* Segundo aditivo **01/01/22 à 31/12/2022**
* Data de encerramento: **01/04/22;**

Todos os lançamentos baixados no período do segundo aditivo **01/01/22 à 31/12/2022** serão considerados no cálculo da multa.

**ALGSOMATORIODESCONTOSESCALONAMENTOCONTRATO**

Retorna o somatório dos **descontos provenientes de escalonamentos** no contrato de locação. A função tomará como base para o cálculo a **data do distrato**do contrato de locação, ou seja, na data de distrato, se houver algum escalonamento que já foi iniciado e ainda **não foi concluído**, os descontos concedidos nos mesmos serão somados e o valor será retornado na função. Por "**escalonamento não concluído**", entende-se todos aqueles escalonamentos que possuírem, antes do fim de seu período, pelo menos um lançamento com status diferente de baixado.  Serão considerados distratos as rescisões e/ou aditivos de exclusão de imóvel do contrato.

No cálculo do somatório, para cada escalonamento não concluído, serão verificados quais dos lançamentos foram **baixados** e os respectivos valores de desconto concedidos via escalonamento serão somados. Exemplo:  
  
**Escalonamento 1 |** 01/01/2020 - 31/05/2020

**Data do Distrato:**20/05/2020

**Valor de desconto:** R$ 100,00

**Lançamento 1** - Baixado

**Lançamento 2** - Baixado

**Lançamento 3** - Baixado

**Lançamento 4** - Em aberto

**Lançamento 5** - Em aberto

Neste caso, o valor retornado na função seria **R$ 300,00** referente a R$100,00 de desconto concedido em cada um dos três primeiros lançamentos.

Obs.:

* Somente serão considerados como descontos, aqueles escalonamentos que possuírem o campo "**Valor**" ou "**Percentual**" preenchido e não forem do tipo **acréscimo**. Caso contrário a função considerará que não houve desconto.
* Caso o escalonamento tenha sido reajustado, o valor de desconto considerado será o do **último reajuste** antes da data de rescisão.
* Caso o escalonamento seja por metro quadrado, o valor de desconto considerado será o **produto do valor de desconto pela área total do contrato** no período do lançamento em questão.
* Caso exista mais de um escalonamento no mesmo período de um lançamento, será considerado o escalonamento de **maior prioridade**.
* No contexto do Aditivo de Exclusão de imóvel, a função de fórmula precisa estar incluída na fórmula da multa do aditivo, contudo não é possível executar a função a partir do cadastro da multa, somente do cadastro de aditivo. Isto acontece pois uma multa pode estar associada a mais de um aditivo, o que torna inviável saber qual aditivo deve ser considerado no momento do cálculo.

**Contexto**

Rescisão do Contrato de Locação, Aditivo de Exclusão de Imóvel

**Sintaxe**  
ALGSOMATORIODESCONTOSCONTRATO

**ALGTABELACONTRATOLOCACAO**

Retorna o valor de qualquer campo da tabela de contrato de locação, como por exemplo:

* Data de prorrogação de vigência;
* Início de vigência.

**Sintaxe:**

ALGTABELACONTRATOLOCACAO(Campo, Tipo Valor)

**Parâmetros da função:**

Campo (Nome da coluna desta tabela)  
TipoValor ('D' => Date; 'I' => Inteiro; 'S' => String; 'V' => Valor)

**Exemplos:**

ALGTABELACONTRATOLOCACAO('DTVIGENCIAPRORROGCONTLOC', 'D')  
ALGTABELACONTRATOLOCACAO('DTVIGENCIAINICONTLOC', 'D');

**ALGTABELAADITIVOCONTRATOLOCACAO**

Retorna o valor de qualquer campo da tabela de aditivos do contrato de locação.

**Sintaxe:**

ALGTABELAADITIVOCONTRATOLOCACAO(Campo, Tipo Valor)

**Parâmetros da função:**

Campo (Nome da coluna desta tabela)  
TipoValor ('D' => Date; 'I' => Inteiro; 'S' => String; 'V' => Valor)

**Exemplos:**

ALGTABELAADITIVOCONTRATOLOCACAO('DATAADITIVOCONTLOC', 'D'));

**VALORDISTRATOADITIVOEXCLUSAOIMOVEL**

Retorna o valor do distrato no aditivo de exclusão de imóveis.

**Contexto**  
Calculo de multa no aditivo de exclusão de imóvel.

**Sintaxe**

VALORDISTRATOADITIVOEXCLUSAOIMOVEL

Abaixo um modelo de fórmula utilizando as funções VALORDISTRATOADITIVOEXCLUSAOIMOVEL, ALGTABELAADITIVOCONTRATOLOCACAO e ALGTABELACONTRATOLOCACAO:

jsConfluence

```

```
