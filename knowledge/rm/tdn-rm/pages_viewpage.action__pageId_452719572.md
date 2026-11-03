---
content_hash: e9d0e89d79305d3282809637e4cbaa88b6eb698d1efcf349200fbcde43f6d07b
fetched_at: '2026-06-29T00:10:08.753941+00:00'
page_id: '452719572'
product: rm
source: tdn-rm
title: Empréstimos Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719572
version: 22
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Empréstimos**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Para o controle de empréstimos, é possível incluir e/ou atualizar informações dos empréstimos do funcionário, permitindo o gerenciamento do valor original, número de parcelas, periodicidade e saldo devedor.

Atenção:

Para as bases que tem o campo "Utiliza Lançamento Automático de Empréstimo de Férias" marcado nos parâmetros de férias, o sistema automaticamente criará o novo código no cadastro de empréstimo do funcionário, seguindo os seguintes exemplos:

|  |  |
| --- | --- |
| **Último código** | **Código de Empréstimo para o próximo registro** |
| 0001 | 0002 |
| 0001-02A | 0001-02A1 |
| 0002A | 0002A1 |
| 0002 - 1A | 0002 - 1A1 |
| 0002 - 1A1 | 0002 - 1A2 |
| EMP/01 | EMP/02 |
| EMP/9 | EMP/90 |
| EMP/99 | EMP/990 |
| EMP/990 | EMP/991 |
| ABC | ABC1 |
| A01 | A02 |
| fgh | fgh1 |
| FERIAS.A1 | FERIAS.A2 |

 

Tipo do empréstimo  
Os tipos de empréstimos são cadastrados em uma tabela dinâmica que poderá ser alterado de acordo com a necessidade. Esta informação serve para agrupar por quais motivos o funcionário solicitou empréstimo.  
 

Evento para desconto  
A indicação do evento para desconto do empréstimo é essencial para visualizar o lançamento na movimentação. No caso de parcelamento, o campo "Fórmula Referência" no cadastro do evento deve utilizar a função **tabemprestimo**, que exibe a quantidade de parcelas já pagas.

Dica:

Para colocar o total de parcelas pagas na coluna "Ref" do evento de desconto de empréstimos, crie a seguinte fórmula:  
TABEMPRESTIMO ('NROPARCPAGAS' , 'V' , 'XXXX')   
   
Onde XXXX é o código do empréstimo.

IMPORTANTE:

1.Cada contrato deve estar vinculado a um evento específico.

Caso o evento selecionado já esteja sendo utilizado em outro empréstimo da modalidade "Crédito do Trabalhador eSocial", o sistema apresentará a seguinte mensagem:

Dica:

Caso sejam contratos diferentes altere o código do evento para que cada contrato seja descontado em eventos diferentes. Caso o contrato anterior tenha finalizado poderá continuar com o mesmo evento cadastrado.

Veja também o procedimento para o evento na [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677&draft=true) no item Definição de Campos - Código do Evento  
Evento para Desconto.

2. Para a modalidade de empréstimo "Crédito do Trabalhador eSocial", o evento informado deve possuir natureza da rubrica **"9253-Empréstimos eConsignado - Desconto".**

Caso o usuário selecione um evento sem essa rubrica, o sistema exibirá a mensagem de alerta abaixo ao tentar salvar:

IMPORTANTE:

**ATENÇÃO:**

Recomendamos a criação de um novo evento de empréstimo para utilização da natureza de rubrica **"9253 - Empréstimos eConsignado - Desconto"**.

Não altere a rubrica de um evento já existente e utilizado para outras modalidades, reutilizando o mesmo código. Caso haja necessidade de retificação de meses anteriores em que esse evento foi utilizado para outra modalidade, isso poderá gerar erros no processamento.

Inicio Desconto   
A Data Inicio Desconto Empréstimo é o mês de início de desconto do empréstimo do funcionário, isto é, controla o desconto do empréstimo de acordo com a data de desconto. Esta data de início do desconto não pode ser nula e deve ser maior ou igual ao primeiro dia do mês e ano de competência. E o número de parcelas pagas deve ser menor que o número de parcelas que serão divididas para o pagamento do empréstimo pelo funcionário. Também o saldo devedor deve ser maior que zero.  
 

Nro Parcela Pagas 

Será incrementado no cálculo do desconto do empréstimo exceto para a  modalidade "Crédito do Trabalhador eSocial" para a qual será atualizada com o valor informado na [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677&draft=true)

Saldo Devedor  
O Saldo devedor inicializará com o valor do empréstimo. Entretanto, poderá  ser alterado utilizando o campo "Fórmula de Correção". O saldo devedor deve maior que zero e deverá ser preenchido com valor total do empréstimo, quando for cedido o primeiro empréstimo.

Exemplo de como fazer uma correção no saldo devedor de um empréstimo

**Exemplo de como fazer uma correção no saldo devedor de um empréstimo:**

* + Crie uma sentença SQL em Utilitários | Consultas SQL que retorne o saldo devedor do empréstimo. SELECT SALDODEVEDOR FROM PFEMPRT WHERE PFEMPRT.TIPOEMPRESTIMO = '0003' AND PFEMPRT.CODIGO = '01' AND CHAPA = '0001'

* + Crie uma fórmula que utilize o resultado da sentença SQL acima, para reajustar o saldo devedor do empréstimo. SE EXECSQL ('emprestimo') =1 ENTAO ( RESULTSQL ('emprestimo' , ' SALDODEVEDOR')) \* 0.10 SENAO 0 FIMSE

O valor retornado pela fórmula é somado ao saldo devedor atual antes da cobrança da parcela. Por exemplo, se o saldo devedor for **R$ 100,00**, e a fórmula retornar **R$ 10,00**, o novo valor considerado será **R$ 110,00**.

Essa funcionalidade permite aplicar reajustes ao saldo devedor, multiplicando-o pelo fator de correção definido na fórmula.

Atenção:

Esse campo ficará desabilitado para a modalidade "Crédito do Trabalhador eSocial".

Após o lançamento do empréstimo no movimento do funcionário, será preenchido o anexo .

**ESOCIAL -****MODALIDADE DE EMPRÉSTIMO**

**1) Empréstimo consignado com garantia de FGTS**

Selecionando essa opção o empréstimo consignado será considerado no evento S-2299 - Desligamento.

* + **Matrícula da Instituição Consignatária**

Preencher com a Matrícula cadastrada na Caixa Econômica Federal. Validação: Deve ser um código válido, conforme tabela do Banco Central. 

* + **Número do contrato de empréstimo consignado CEF**

Número do contrato referente ao empréstimo CEF. 

**2) Crédito do Trabalhador eSocial**

Selecionando essa opção o sistema irá considerar as informações de desconto do empréstimo em folha, na geração dos eventos (S-1200, S-1202, S1207, S-2299 ou S-2399)

* + **Banco**

Preencher com o Código da Instituição Financeira concedente do empréstimo. Validação: Deve ser um código válido, conforme tabela do Banco Central. 

* + **Número do contrato do Crédito do Trabalhador eSocial**

Número do contrato existente na Instituição Consignatária.

* + **Observação**

Outras informações do desconto. 

Dica:

Veja também como importar arquivos para o empréstimo do crédito do trabalhador em [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677).

## **02. EXEMPLO DE UTILIZAÇÃO**

FAQ -

## **03. TELA Empréstimos**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Código do Empréstimo | Código sequencial |
| Tipo de Empréstimo | O preenchimento deste campo é obrigatório para que os empréstimos sejam lançados automaticamente.  Na importação da modalidade "Crédito do Trabalhador eSocial" seguirá conforme parametrização no parametrizador em folha normal em [Crédito Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937259572). |
| Evento para desconto | Este é o evento que será registrado no envelope do funcionário no momento do lançamento. IMPORTANTE: Para a modalidade Crédito do Trabalhador eSocial deve conter Código de Cálculo 480 - DESCONTO EMPRÉSTIMO CRÉDITO DO TRABALHADOR e Rubrica eSocial 9253 - Empréstimos eConsignado - Desconto. |
| Modalidade do empréstimo | Selecionar de acordo com a modalidade do empréstimo:  Empréstimo consignado com garantia de FGTS Crédito do Trabalhador eSocial |
| Matricula da Instituição Consignatária  Código do banco concedente do empréstimo | Deve ser um código válido, conforme tabela do Banco Central.  Será considerado de acordo com a modalidade do empréstimo  Empréstimo consignado com garantia de FGTS = Matricula da Instituição Consignatária Crédito do Trabalhador eSocial = Código do banco concedente do empréstimo |
| Número do contrato de empréstimo consignado CEF Número do contrato do Crédito do Trabalhador eSocial | Este número é fornecido pela concedente do empréstimo  Será considerado de acordo com a modalidade do empréstimo  Empréstimo consignado com garantia de FGTS = Número do contrato de empréstimo consignado CEF Crédito do Trabalhador eSocial = Número do contrato do Crédito do Trabalhador eSocial |
| Data do Empréstimo | Informar a Data de Início do Contrato |
| Início Desconto | Informar a Data de Inicio do Desconto |
| Comp. final desc. | Somente será editável para a modalidade Crédito do Trabalhador eSocial e deve ser preenchido com da competência final do desconto |
| Periodicidade (em meses) | Informar sempre 1 para que seja descontado a cada mês. Informe outra quantidade de meses caso queira que o desconto seja feito com intervalo maior de meses. |
| Nro. Parcelas | Preencher com o número de parcelas. Verificar exemplo no item 02 - Exemplo de Utilização link "**Cálculo da Folha/Rescisão**" |
| Nro. Parcelas Pagas | Preencher com o número de parcelas pagas. Verificar exemplo no item 02 - Exemplo de Utilização link "**Cálculo da Folha/Rescisão**" |
| Valor Original | Informar o valor do empréstimo ou informar o valor da parcela existente no arquivo baixado no site da **Emprega Brasil**. |
| Saldo Devedor | Informar o valor do empréstimo ou informar o valor da parcela existente no arquivo baixado no site da **Emprega Brasil**. IMPORTANTE: Esse campo estará desabilitado quando a modalidade for Crédito do Trabalhador eSocial. |
| Valor da parcela | Informar o valor do empréstimo ou informar o valor da parcela existente no arquivo baixado no site da **Emprega Brasil**. |
| Aplicar percentual abaixo sobre remuneração líquida para o limite do desconto | Marcar o parâmetro para acrescentar um percentual que será considerado no cálculo da remuneração líquida de desconto do funcionário. Por exemplo se o empréstimo ficará limitado a um percentual do líquido da folha de pagamento do funcionário. IMPORTANTE: Esse campo ficará habilitado quando a modalidade for Crédito do Trabalhador eSocial. |
| Percentual | Informar o percentual que será considerado no cálculo da remuneração líquida de desconto do funcionário. |
| Competência Atual | Informar os valores que estão no campo "competencia" dentro do arquivo de importação. |
| Fórmula de cálculo | Fórmula utilizada para cálculo de um empréstimo. IMPORTANTE: Esse campo estará desabilitado quando a modalidade for Crédito do Trabalhador eSocial. |
| Fórmula de correção | Fórmula utilizada para cálculo de um empréstimo . IMPORTANTE: Esse campo estará desabilitado quando a modalidade for Crédito do Trabalhador eSocial. |
| Observação | Campo para acrescentar alguma observação. |

## **04. TABELAS UTILIZADAS**

* PFEMPRT
* PFDESCEMPRT
* PGRPLANC
* PREMCREDTRAB
* PFREMCREDTRAB

---

Funcionários
