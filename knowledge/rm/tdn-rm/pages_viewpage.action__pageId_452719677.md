---
content_hash: b77244b558f6342629e31d38a96f9f6c40942e975448b832add5a0a297efbb1c
fetched_at: '2026-06-29T00:10:09.479605+00:00'
page_id: '452719677'
product: rm
source: tdn-rm
title: Importação Empréstimos FEBRABAN / Crédito do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719677
version: 56
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Layout FEBRABAN**
4. **Crédito do Trabalhador**
5. **Exemplo de Utilização**
6. **TELA Importa Empréstimos FEBRABAN / Crédito do Trabalhador**
7. **Definição de Campos**
8. **Importação de Múltiplos Empréstimos por Trabalhador**
9. **Tabelas Utilizadas**

## **01. VERSÕES**

**A partir dos patches:**

* 12.1.2406.296
* 12.1.2410.271
* 12.1.2502.174
* 12.1.2506.118 e superiores

## **02.****VISÃO GERAL**

Neste módulo será possível importar o valor do empréstimo para desconto em folha de pagamento baseado no layout CDC – Empréstimo Consignação em Folha – **Padrão FEBRABAN** e no **Crédito do Trabalhador**.

Para realizar a importação das informações acesse: Folha Mensal | Importação |Importa Empréstimos FEBRABAN / Crédito do Trabalhador.

Após acessar o módulo  o usuário deverá:

Selecionar o "Tipo de Importação" se: Layout FEBRABAN ou Crédito do Trabalhador

## **03. Layout FEBRABAN**

• Informar o caminho do arquivo a ser importado: O arquivo a ser importado deverá possuir extensão ".RET".  
• Informar o evento que fará o desconto do empréstimo:

Apenas o evento do tipo desconto e que possuir o código de cálculo 194 poderá realizar o processo.  
   
• Informar a ação que a importação deverá ter:

**Ignorar:** realiza a importação, mantendo a movimentação já existente;  
**Substituir:** sobrepõe a informação existente pela importada;  
**Somar:** somará os valores dos eventos que constam no arquivo importado aos valores dos eventos idênticos já existentes na movimentação.  
   
Quando realizamos a importação é possível fazer algumas parametrizações através dos campos:

• **Não recalcular:** marcando este parâmetro, o sistema não permitirá o recálculo da movimentação de nenhum funcionário.  
• **Importar demitido:** marcando este parâmetro, o sistema realizará a importação de valores para funcionários demitidos, caso estes possuam alguma informação.  
• **Informar data de pagamento:** marcando este parâmetro, o sistema irá ignorar as datas informadas no arquivo de importação e irá considerar a nova data informada.

É possível também escolher como o funcionário será identificado no momento da importação, por CHAPA ou pelo CPF do mesmo.

## **04. Crédito do Trabalhador**

Primeiramente o arquivo deve ser baixado No Portal Emprega Brasil:​

* Acesse o Portal Emprega Brasil.
* Faça login com sua conta:​ Utilize suas credenciais para acessar o sistema.

Após executar um recalculo o Evento o CC  "480 - DESCONTO EMPRÉSTIMO CRÉDITO DO TRABALHADOR", seguido da Natureza da rubrica eSocial "9253", existirá na base.

Com a existência deste Evento, deve-se informar os  parâmetros "Tipo de Empréstimo", "Máscara para Código Empréstimo" e "Fracionamento de Job's"  em " **Parametrizador | Folha Normal | [Crédito Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937259572)**". O parâmetro  “Qtde de Job´s” (destaque retangular em vermelho) define a quantidade de jobs para o fracionamento. Quando informando 0 (zero) ou 1 (um) a importação de arquivo ocorre sem fracionamento de jobs. Quando informado valor maior do que 1 (um), o sistema aciona o processo fracionado. Não há necessidade de informação do "Evento de Desconto do Empréstimo" (X em vermelho), pois o sistema agora verifica diretamente os Eventos. Se houver mais de um empréstimo a ser importado e realizado dentro da mesma vigência, deverá ser repetido o cadastro do código de cálculo "480" com a Natureza da rubrica eSocial "9253" com códigos distintos quantas vezes forem os empréstimos dentro desta vigência.

Forneça os dados para a importação do Crédito do Trabalhador.

• Informar o caminho do arquivo a ser importado: O arquivo a ser importado deverá possuir uma das seguintes extensões ".csv | .json | .xls".

O sistema apresenta o próximo passo do assistente, a tela para selecionar a coligada a que pertence o arquivo.

Como os dados do empréstimo do Crédito do Trabalhado é consolidado pela inscrição da matriz no eSocial, cada arquivo deve pertencer a uma coligada.

Para selecionar a coligada, acione a tela de parâmetros especifico da coligada  e então:

* Marque "Usar Parâmetros"
* Informe o "Arquivo de importação" que deverá possuir uma das seguintes extensões ".csv | .json | .xml"

Avance para a execução do processo. Uma tela de agendamento será exibida. Podendo executar a importação imediatamente ou agendar.

Importação para funcionários com categoria 721 do eSocial

Para funcionários com o CODCATEGORIA igual a 721 onde o funcionário não tem Matricula no eSocial, é utilizado o campo CPF para realizar a importação

## **05. EXEMPLO DE UTILIZAÇÃO**

FAQ -

## **06.** **TELA Importa Empréstimos FEBRABAN / Crédito do Trabalhador**

**Layout FEBRABAN selecionado**

Foi inserida, na correção, o campo Identificação da Coligada por Nº Empregador ou Nº Estabelecimento (canto inferior esquerdo da janela). Alguns clientes possuem particularidades no cadastro de coligadas, como neste caso, em que foi cadastrado CNPJ de raízes iguais. Para resolver esta questão, ao invés de utilizar o Número de Empregador, optou-se por utilizar o Número de Estabelecimento. Como essa particularidade ocorre em poucos clientes, o campo foi criado  em tela para que por default, continue pegando do Número do Empregador, mas que seja possível selecionar o Número do Estabelecimento caso seja necessário.

**Layout Crédito do Trabalhador selecionado**

**Layout Crédito do Trabalhador selecionado, contendo multi arquivos**

Matrícula eSocial

Quando a matrícula do eSocial contiver letras, o sistema foi orientado a aceitar tanto letras maiúsculas quanto minúsculas, sem gerar erros na importação decorrente desse tipo de dados.

Nº Empregador / Nº Estabelecimento

A Identificação da coligada pode ser realizada de duas maneiras diferentes:  
  
**Nº Empregador:** Esta opção utilizará o campo **"****numeroInscricaoEmpregador"** que é correspondente ao CNPJ da Coligada

**Nº Estabelecimento:** Esta opção utilizará o campo **"numeroInscricaoEstabelecimento"** que é correspondente ao CNPJ da Filial

Dica:

No fracionamento de JOBs é verificado da seguinte forma:

* No campo NumeroInscricaoEmpregador os primeiros 8 dígitos do CNPJ
* No campo NumeroInscricaoEstabelecimento tem que ser fornecido o CNPJ completo

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Tipo de Importação | Define se será a importação do layout "FEBRABAN" para gravar no movimento do funcionário ou se será "Crédito do Trabalhador" para gravar no cadastro de "Empréstimos" no anexo do cadastro do funcionário. |
| Arquivo de importação | Contendo os dados de um dos dois tipos de layout. No caso do layout "FEBRABAN" serão aceitos apenas os arquivos com a extensão ".RET" e no caso do layout "Crédito do Trabalhador" serão aceitos os arquivos com as extensões ".JSON", ".CSV", ".XLS" ou ".XLSX". Podem ser selecionados apenas um ou múltiplos arquivos para o Desconto registrado no cadastro de empréstimo. Além disso, a importação dos arquivos layout "Crédito do Trabalhador" pode ser feita mesmo quando não há programa Excel instalado na máquina. |
| Evento de Lançamento | Evento a ser utilizado para o "layout FEBRABAN". |
| Ação | Substituir, Ignorar, somar ao lançamento para o "layout FEBRABAN". |
| Identificação do Funcionário | Se "CPF" ou "CHAPA"  para o "layout FEBRABAN". |
| Parâmetros Importação | com as opções de "Não Recalcular", "Importar demitido", "Informar data de pagamento" e "Data de Pagamento" para o "layout FEBRABAN". |
| Identificação da Coligada por | Foi inserida, na correção, o campo Identificação da Coligada por Nº Empregador ou Nº Estabelecimento (canto inferior esquerdo da janela). Alguns clientes possuem particularidades no cadastro de coligadas, como neste caso, em que foi cadastrado CNPJ de raízes iguais. Para resolver esta questão, ao invés de utilizar o Número de Empregador, optou-se por utilizar o Número de Estabelecimento. Como essa particularidade ocorre em poucos clientes, o campo foi criado  em tela para que por default, continue pegando do Número do Empregador, mas que seja possível selecionar o Número do Estabelecimento caso seja necessário. Fica disponível apenas na opção Crédito do Trabalhador. |

## **07. DEFINIÇÃO DE CAMPOS**

**Empréstimo para o Crédito do Trabalhador**

**PFEMPRT - Empréstimos**

|  |  |  |
| --- | --- | --- |
| **Descrição** | **Campo** | **Regra** |
| Código da Aplicação | APLICACAO | Fixo 'P" indicando que é o "Folha de pagamento". |
| Código Identificador da Coligada | CODCOLIGADA | Obtido através do campo da importação **NumeroInscricaoEmpregador**, referente a identificação do empregador no eSocial, com base neste campo pesquisa no cadastro de coligada pelo  GCOLIGADA.CGC para obtenção do código da coligada GCOLIGADA.CODCOLIGADA. |
| Chapa do Funcionário | CHAPA | Obtido através  do campo da importação **Matricula**. Que representa a matricula do eSocial. O sistema procura no cadastro de funcionários PFUNC para retornar o campo CHAPA. Se o retorno for um registro usa o campo CHAPA direto, se não vai procurar a CHAPA que tenha sua situação diferente de 'D', se não vai retornar a CHAPA de demissão mais recente. |
| Código Identificador do Empréstimo Código do Empréstimo | CODIGO | Na inclusão, é criado de forma automática usando a concatenação dos parâmetros gerais "**Máscara para Código Empréstimo**" campos "**Prefixo**" e "**Sequencial**" em **Configurações \ Parametrizador \ Folha Normal \ Crédito Trabalhador.**  O Sequencial é obtido do auto incremento do serviço da GAUTOINC Para identificar se o empréstimo já foi cadastrado é usado o Código da Coligada e Chapa, explicando anteriormente, e o numero do contrato do campo da importação "**Contrato**". Então é pesquisado na tabela PFEMPRT por CODCOLIGADA, CHAPA, NUMCONTEMPCONS. |
| Matrícula da Instituição Consignatária Código do Banco concedente do empréstimo | MATINSTCONS | É obtido pelo campo da importação "**IfConcessoraCodigo**". |
| Código do Evento Evento para Desconto | CODEVENTO | É usado o valor informado no parâmetro parâmetros gerais "**Evento de Desconto do Empréstimo**"  em **Configurações \ Parametrizador \ Folha Normal \ Crédito Trabalhador**  O sistema irá alertar no log com a seguinte msg **"Para Coligada:{0} Chapa:{1} Evento:{2} Está associado a um empréstimo de mesma vigência com outro Contrato. Considere informar outro evento de mesmo código de cálculo e rubrica para o correto envio para o eSocial"**. Isso porque o Governo espera ser informado do desconto em folha do Trabalhador uma verba por contrato de empréstimo. |
| Número do contrato de empréstimo consignado Número do contrato de empréstimo consignado CEF Número do contrato de Crédito do Trabalhador eSocial | NUMCONTEMPCONS | Obtido pelo campo da importação **"Contrato"** |
| Data do Empréstimo | DTEMPRESTIMO | Obtido pelo campo da importação **"DataInicioContrato"** |
| Funcionário firmou contrato de empréstimo consignado com garantia de FGTS Modalidade do Emprestimo | EMPCONSGARANTFGTS | Valor fixo **2** - ‘Crédito do Trabalhador eSocial’ |
| Dt Início Desconto do Empréstimo Início Desconto | INICIODESCONTO | Obtido pelo primeiro dia referente a competência informada no campo da importação **"CompetenciaInicioDesconto"** |
| Mês competência final do empréstimo Comp. final desc. Mês | MESFINAL | Obtido pelo mês informado no campo da importação **"CompetenciaFimDesconto"** |
| Ano competência final do empréstimo Comp. final desc. Ano | ANOFINAL | Obtido pelo Ano informado no campo da importação **"CompetenciaFimDesconto"** |
| Número de Parcelas Nro. Parcelas | NROPARCELAS | Obtido do campo da importação **"TotalParcelas"** |
| Número de Parcelas Pagas Nro. Parcelas Pagas | NROPARCPAGAS | Obtido do campo da importação **"QtdPagamentos"** |
| Periodicidade Periodicidade (em meses) | PERIODICIDADE | Valor fixo **1 (um)** |
| Saldo Devedor | SALDODEVEDOR | Valor fixo **0 (zero)** |
| Tipo do Empréstimo | TIPOEMPRESTIMO | Valor informado no parâmetro parâmetros gerais "**Tipo do Empréstimo**"  em **Configurações \ Parametrizador \ Folha Normal \ Crédito Trabalhador** |
| Valor Original do Empréstimo Valor Original | VALORORIGINAL | Obtido do campo da importação **"ValorEmprestimo"** |
| Aplicar a margem consignável sobre a remuneração Aplicar percentual abaixo sobre remuneração líquida para o limite do desconto | APMARGEMCONSIGREM | Aplicar percentual: deverá sempre retornar **marcado na inclusão**  Caso seja atualização, não deve alterar este campo |
| Percentual da margem consignável sobre a remuneração | PERCMARGEMCONSIG | Valor fixo de **35** só informado na inclusão e não é modificado na atualização. |
| Valor da parcela do empréstimo crédito do trabalhador Percentual | PARCEMPRCREDTRAB | Obtido do campo da importação **"ValorParcela"** |
| **Competência atual - Mês** | **PFEMPRT.MESCOMPATUAL** | **Obtido do campo da importação "Competência" - mês e ano utilizado para validação do desconto.** |
| **Competência atual - Ano** | **PFEMPRT.ANOCOMPATUAL** | **Obtido do campo da importação "Competência" - mês e ano utilizado para validação do desconto.** |

Quando o contrato já existe o sistema atualiza os campos abaixo:

* Comp. final desc. Mês
* Comp. final desc. Ano
* Nro. Parcela
* Nro. Parcelas Pagas
* Valor Original
* Valor da Parcela
* Percentual
* Competência atual (mês e ano)

## **08. IMPORTAÇÃO DE MÚLTIPLOS EMPRÉSTIMOS POR TRABALHADOR**

Em se tratando da existência de um contrato de empréstimo, conforme a PORTARIA MTE Nº 933, DE 5 DE JUNHO DE 2025, o colaborador poderá solicitar mais de um empréstimo, inclusive dentro da mesma vigência. Conforme explicado mais acima, se houver mais de um empréstimo a ser importado e realizado dentro da mesma vigência, deverá ser repetido o cadastro do código de cálculo "480" com a Natureza da rubrica eSocial "9253" com códigos distintos quantas vezes forem os empréstimos dentro desta vigência. Seguem abaixo alguns exemplos de importação de empréstimos, sua relação com os códigos cadastrados e o resultado esperado:

Caso a importação ocorra com sucesso, a mensagem deverá seguir o seguinte modelo: "Incluído (ou Atualizado) o Empréstimo para Coligada: (0) Chapa: (1) Matricula esocial: (2) Código do Empréstimo: (3) Código do Contrato: (4) Código de Evento: (5).". Do contrário, caso ocorra erro, o alerta emitirá a seguinte mensagem: "Funcionário já possui empréstimo e não há mais eventos disponíveis no Cadastro de Eventos com código de cálculo 480 e natureza 9253 para a coligada: (1) (Chapa: (2))".

Em caso de **erro na importação** devido à falta de verbas com código de cálculo 480 suficientes para a quantidade de empréstimos do funcionário, **após a criação de novas verbas** com o CC 480, poderá ser **realizada novamente a importação** (utilizando o mesmo arquivo) para que o sistema faça o ajuste do cadastro do empréstimo, adicionando os registros não importados até então.

IMPORTANTE:

Quando existir mais de um empréstimo para o mesmo funcionário:

* O provisionamento nas férias e no adiantamento será realizado para todos os empréstimos. O provisionamento será realizado em um único evento, com o somatório dos valores a serem provisionados nos empréstimos. Sendo que nas férias será separado apenas para o 1º mês e 2º mês quando houver férias partidas.

+ Quando não houver saldo no adiantamento da folha será descontado o valor total do empréstimo

* O desconto do empréstimo na folha de pagamento e na rescisão será em ordem cronológica, ou seja, levando em consideração o mais antigo para o mais recente de acordo com a data do empréstimo em: Administração de Pessoal / Funcionários / Empréstimos.

+ Quando houver mais de um empréstimo na mesma data, será considerado o código de cadastro do empréstimo para fins de identificação, pois será a ordenação vinda do arquivo importado.

* No evento de base de insuficiência de saldo registrado no envelope de pagamento será somado o valor por contrato.
* Para o cálculo da Margem Consignável, inicialmente será considerada a margem total disponível, desconsiderando os empréstimos. Em seguida, o valor de cada empréstimo será subtraído sequencialmente: o primeiro empréstimo será descontado da margem, e o valor restante servirá de base para o desconto do próximo empréstimo, e assim por diante.

#### O desconto do crédito do trabalhador deverá ocorrer em **eventos distintos** para controle do eSocial, devido cada empréstimo ter um contrato separado.

## **09. TABELAS UTILIZADAS**

* GCOLIGADA
* PCODEMPRT
* PEVENTO
* PFDESCEMPRT
* PFEMPRT
* PFUNC

---

Layout FEBRABAN

[Layout Crédito do Trabalhador](https://hservicos.mte.gov.br/empregador/manuais/leiauteArquivoEmprestimos.html)
