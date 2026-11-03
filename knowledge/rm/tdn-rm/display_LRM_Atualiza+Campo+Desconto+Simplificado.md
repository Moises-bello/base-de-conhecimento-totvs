---
content_hash: 4c5abcd6f7c1d4ae5767ef73408d77fb788202ffeea6fffdc7639919ee211d48
fetched_at: '2026-06-29T00:12:01.407787+00:00'
page_id: '895588595'
product: rm
source: tdn-rm
title: Atualiza Campo Desconto Simplificado
type: documentation
url: https://tdn.totvs.com/display/LRM/Atualiza+Campo+Desconto+Simplificado
version: 38
---

## 

## **CONTEÚDO**

1. **Versão**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Informações complementares**
5. **Tela Atualiza Campo Desconto Simplificado**
   1. **Principais Campos e Parâmetros**
6. **Tabelas utilizadas**

## **01. VERSÃO**

Válido para as versões superiores a 

* 12.1.2402.267
* 12.1.2406.222
* 12.1.2410.153
* 12.1.2502 e superiores

## **02. VISÃO GERAL**

Processo utilizado para atualização dos campos IRRFSIMPLIFICADOCAIXA, IRRF13SIMPLIFICADOCAIXA e IRRFFERSIMPLIFICADOCAIXA. 

IMPORTANTE:

**Esse processo serve apenas para preenchimento dos campos citados acima na tabela PEFPERFF portanto não altera nada em cálculo da folha.**

Outras informações importantes:

IMPORTANTE:

Caso apresente a mensagem abaixo no LOG após execução do processo, verifique na tabela de IRRF as faixas que foram cadastradas principalmente a última faixa que podem ter quantidade de 9 (nove) a menos que o valor da base de cálculo utilizada no cálculo.

Para a analise da isenção de IRRF não foi encontrada faixa na tabela de calculo de IRRF para o Funcionário: {CHAPA} com Base de Calculo de {VALOR} em {DATA}.

IMPORTANTE:

Existem diferenças entre os campos da tabela PFPERFF e por isso não há comparação entre o campo preenchido por esse processo e o detalhamento do log de cálculo.

**IRRFSIMPLIFICADO, IRRFFERSIMPLIFICADO, IRRF13SIMPLIFICADO** - Servem para o cálculo da folha de pagamento, são por período e o cálculo está detalhado no log de cálculo.

**IRRFSIMPLIFICADOCAIXA, IRRFFERSIMPLIFICADOCAIXA, IRRF13SIMPLIFICADOCAIXA** - São marcações para o processo de geração da DIRF informar ou não o valor do desconto simplificado de acordo com o mês caixa de pagamento das verbas.

Atenção:

Funcionários que tenham marcado o parâmetro Desconsiderar Desconto Simplificado do IRRF será considerado essa marcação para o ano todo então na geração da DIRF não haverá valor simplificado porque não tem histórico de quando marcou e desmarcou o parâmetro.  

Atenção:

Esse processo deve ser executado para o ano de 2024 porque os campos serão preenchidos para informações no processo da DIRF ano base 2024

## **03. EXEMPLO DE UTILIZAÇÃO**

Cenários fictícios criados em base exemplo.

Informação de simplificado quando tem mais de um período no mesmo caixa

Funcionário usou o valor do simplificado no cálculo da folha de pagamento da competência 10/2024 no período 1 com data de pagamento em 04/11/2024.

Funcionário não usou o valor do simplificado no cálculo da folha de pagamento da competência 10/2024 no período 2 com data de pagamento em 06/11/2024 porque o valor do INSS superou o valor do simplificado.

O resultado esperado após executar o processo:

PFPERFF.IRRFSIMPLIFICADOCAIXA 2

IMPORTANTE:

Veja que no cálculo por período que corresponde ao campo PFPERFF.IRRFSIMPLIFICADO está indicando 1 para o primeiro período que usou o valor do simplificado para calcular o IRRF folha e no período 2 está indicando 0 (zero) que não usou o simplificado para calcular o IRRF folha e ambos períodos foram pagos no mesmo mês caixa.

Nesse caso, no campo PFPERFF.IRRFSIMPLIFICADOCAIXA prevalece o indicativo de uso do simplificado referente ao último período. Para informa na DIRF o campo é preenchido com o valor do último período em todos os períodos de mesmo mês caixa da ficha financeira.

Usa simplificado somente na folha

Funcionário usou o valor do simplificado no cálculo da folha de pagamento da competência 12/2023 com data de pagamento em 05/01/2024.

O resultado esperado após executar o processo:  
PFPERFF.IRRFSIMPLIFICADOCAIXA 3  
PFPERFF.IRRF13SIMPLIFICADOCAIXA 2  
PFPERFF.IRRFFERSIMPLIFICADOCAIXA NULL - Porque será retornado de acordo com o campo PFUFERIASRECIBO.IRRFSIMPLIFICADO

Usa simplificado somente nas férias

Funcionário usou o valor do simplificado no cálculo das férias da competência 02/2024  com data de pagamento em 30/01/2024.

Atenção:

Para a DIRF:

No caso de férias é verificado o recibo de férias para obter a data de pagamento e inserida a informação de acordo com a informação do caixa comum do período da ficha financeira.

Nesse exemplo as férias iniciaram em 01/02/2024 e o pagamento foi em 30/01/2024, sendo assim será lançado na competência que tiver a informação do caixa comum no período da ficha financeira Janeiro/2024.

O resultado na PFPERFF após executar o processo:  
PFPERFF.IRRFSIMPLIFICADOCAIXA 2  
PFPERFF.IRRF13SIMPLIFICADOCAIXA 2  
PFPERFF.IRRFFERSIMPLIFICADOCAIXA NULL - Porque será retornado de acordo com o campo PFUFERIASRECIBO.IRRFSIMPLIFICADO

Usa simplificado somente no 13º salário

Funcionário usou o valor do simplificado no cálculo do 13º salário da competência 12/2024  com data de pagamento em 20/12/2024.

Observação:

Para o 13º salário é informado no campo de acordo com o cálculo da 2ª parcela 13º salário.

O resultado esperado após executar o processo:  
PFPERFF.IRRFSIMPLIFICADOCAIXA 2  
PFPERFF.IRRF13SIMPLIFICADOCAIXA 3  
PFPERFF.IRRFFERSIMPLIFICADOCAIXA - Porque será retornado de acordo com o campo PFUFERIASRECIBO.IRRFSIMPLIFICADO

Desconsiderar Desconto Simplificado do IRRF MARCADO

Funcionário com o campo Desconsiderar Desconto Simplificado do IRRF marcado, será considerado essa marcação para o ano todo então na geração da DIRF não haverá valor simplificado porque não tem histórico de quando marcou e desmarcou o parâmetro.  

Independente se usou ou não o simplificado o resultado esperado após executar o processo:  
PPFPERFF.IRRFSIMPLIFICADOCAIXA 2  
PFPERFF.IRRF13SIMPLIFICADOCAIXA 2  
PFPERFF.IRRFFERSIMPLIFICADOCAIXA - Porque será retornado de acordo com o campo PFUFERIASRECIBO.IRRFSIMPLIFICADO, sendo que nesse caso retornará que não usou o simplificado devido o campo Desconsiderar Desconto Simplificado do IRRF marcado.

Cálculo no limite inferior da tabela de IRRF

Considere as seguintes informações na DIRF de conferência

Porque que em maio considera o uso do desconto simplificado e em junho não considera?

Verificando os valores que incidem e deduzem no IRRF temos:

CÁLCULO = BASE IRRF MENOS INSS (NESSE CASO SÓ TEVE INSS)

MAIO USOU SIMPLIFICADO PORQUE

2460,53 - 200,26 = 2260,27 QUE É MAIOR QUE O LIMITE DA TABELA 2259,20

JUNHO NÃO USOU SIMPLIFICADO PORQUE

2451,36 - 199,44 = 2251,92 QUE É MENOR QUE O LIMITE DA TABELA 2259,20

LOG DE CÁLCULO DE JUNHO                                          LOG DE CÁLCULO DE MAIO

Tabela cadastrada na base de dados:

## **04.****INFORMAÇÕES COMPLEMENTARES**

Como o processo executa para toda a base de dados do ano de 2024 o mesmo tende a ser demorado a depender da quantidade de funcionários e fichas financeiras. Para isto fizemos algumas implementações para melhorar a performance da execução do processo:

**Fracionamento de JOBs:** Foi implementado o recurso de Fracionamento de Jobs e assim, quando configurado poderá ter até 70% de ganho no processamento. Mais informações: [TOTVS Folha de Pagamento - Fracionamento de Jobs](https://tdn.totvs.com.br/display/public/LRM/TOTVS+Folha+de+Pagamento+-+Fracionamento+de+Jobs)

Para Habilitar o recurso é necessário:

* O Host ou Service Host estar configurado com JobServer3Camandas = True
* Cadastrar a classe de processo FopAtualizaCampoDescontoSimplificadoProcess em Ambiente | Processos | Segurança de Jobs Fracionáveis, para o perfil que terá acesso, informando a quantidade máxima de Frações. No exemplo abaixo foi colocar 14, mas esta quantidade quem define é o usuário. Somente o mínimo de Frações que deve ser maior ou igual a 2:

Assim ao acessar o processo, antes da execução irá apresentar a tela abaixo, onde o usuário poderá alterar a quantidade de Jobs até o limite máximo configurado conforme o exemplo acima:

**Realizar o agendamento**: Outra recomendação é executar o processo em um horário alternativo, quando não tem usuários acessando o sistema. Para isto também disponibilizamos o recurso de agendamento, que pode ser usado junto com o fracionamento de Jobs:

**Flag '****Emitir Log de Execução'**: 

* **Marcado:** Quando o processo é executado é emitido em log de execução todos os valores que foram considerados e qual informação foi incluída nos campos.
* **Desmarcado:** Com este parâmetro desmarcado este log não será criado **(será criado somente na geração da DIRF caso a execução do processo seja feita por ela)**, sendo somente criado os logs de erro caso ocorra e de Resumo e assim terá um ganho de processamento em até 30%.

Observação

Por default, esta flag sempre retornará marcada e caso o usuário não queira emitir os logs, deverá desmarcar a mesma antes da execução do processo.

Atenção

Caso o usuário tenha restrições de perfil, o processo irá executar somente para os funcionários que o usuário tem acesso. Porém a mensagem não verifica estas restrições, somente se existe algum período da ficha financeira com os campos < 2 ou null que serão considerados na DIRF. Neste caso, é recomendado que o processo seja executado por um usuário que não tenha restrições configuradas no perfil/usuário. 

## **05.** **TELA **ATUALIZA CAMPO DESCONTO SIMPLIFICADO****

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Informar a quebra da seção |
| Seleção de funcionários | Informar a seleção de funcionários |
| Caixa Inicial | Informar o mês que iniciará o processo |
| Caixa Final | Informar o mês que finaliza o processo |
| Ano | Esse processo deve ser executado para o ano de 2024 porque os campos serão preenchidos para informações no processo da DIRF ano base 2024 |
| Atualizar Somente Campos diferente de 2 ou 3 | Analisa a ficha financeira do funcionário onde encontrar campos diferente de 2 ou 3 será atualizado referentes ao período solicitado |
| Atualizar Todos os Campos | Analisa a ficha financeira do funcionário e atualiza todos os campos referentes ao período solicitado |
| Emitir Log de Execução | Parâmetro para gerar ou não o log de execução. |

## **06. TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
* PFUFERIASRECIBO
* PFUNC
* PEVENTO
* PTABCALC
* PVALFIX
