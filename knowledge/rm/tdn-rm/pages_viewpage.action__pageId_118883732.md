---
content_hash: 50ced17b17e16e923e79598fa6252e4851ee212d544dfc7849b2a6b50294009a
fetched_at: '2026-06-29T00:05:54.946536+00:00'
page_id: '118883732'
product: rm
source: tdn-rm
title: Dicas e Soluções - Contabilização .Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=118883732
version: 3
---

**Produto:** TOTVS Folha de pagamento          **Versão:** 11.40 e superiores  
**Processo:** Contabilização.Net

Esse manual tem o intuito de sanar dúvidas e auxiliar na correção de erros que geralmente ocorrem no novo processo de contabilização.Net.

###### Situações mais comuns que ocorrem no processo de Contabilização.Net Um dos erros mais comuns que ocorre ao se efetuar a rotina de contabilização é esse:

----------------------  
***AgrupamentoContabil: Erro ao obter conta Saldus.***  
***Grupo contábil: 2112001, Integração contábil: , Integração funcionário: - Conta***  
***Saldus:***  
---------------------

Esse erro acontece porque na montagem dos dados para saber qual o agrupamento será utilizado no lançamento contábil foi encontrado um agrupamento que não existe em *Cadastros / Contabilização / Agrupamento* de contas contábeis.  
Existem duas situações: ou o agrupamento realmente precisa ser criado, ou então existe um agrupamento com o mesmo código, mas que tem o campo Código de integração preenchido, e está sendo buscado um agrupamento sem o código preenchido.  
  
Para se saber qual a origem da busca desse agrupamento, verifique o final do log de Execução do processo, onde será exibido o código do evento ou encargo que está sendo contabilizado no momento e que originou o erro.

**Exemplo do log de Execução**  
  
---------------------  
***Lote: 1220120***  
***Chapa: 00001 Nome: ITAMAR MENDES DA SILVEIRA***  
***Contabilização por Seção***  
***Contabilizando Evento***  
***Verba : 0002***  
***Valor : 10000,00***  
---------------------  
  
Nesse caso, a execução está no evento 0002. No cadastro do evento 0002 está informado o agrupamento  
2112001 a Crédito, e tem integração contábil. ( vide imagem a seguir)

Quando se trabalha com integração contábil, o código de integração será retornado com base na seguinte regra: se o RMLabore não estiver parametrizado para utilizar cálculo por centro de custo *(Opções / Parâmetros / RM Labore / Parâmetros de Cálculo)* ...

... o código de integração será verificado no cadastro da seção do funcionário, aba Dados contábeis, campo Integração contábil.

Se o parâmetro Utiliza cálculo por centro de custo estiver marcado, o local onde o sistema irá buscar o código de integração contábil será dentro do cadastro do centro de custo *(Cadastros / Centros de Custo RM Labore)* do evento, que está informado na movimentação por centro de custo no envelope de pagamento ( vide abaixo).

Movimentação por centro de custo do envelope:

Cadastro do centro de custo 01.4:

Nesse caso deveria ser informado um código de integração contábil, de forma a se obter um agrupamento que exista no cadastro de Agrupamentos de contas contábeis.

**Obs.:** O processo de **integração por funcionário** irá seguir os mesmos passos da rotina acima, incluindo o código de integração que está informado no cadastro do funcionário, na aba Base de cálculo / Dados contábeis, caso no cadastro de eventos e/ou encargos seja marcado na aba Dados contábeis o flag “Tem integração por funcionário”. Assim sendo, o sistema também irá verificar se no cadastro de Agrupamentos de contas contábeis os agrupamentos possuem os códigos de integração por funcionário informados.

**Rateio gerencial**  
Outra situação que comumente se observa no processo de contabilização é relacionado ao rateio gerencial. A mensagem que geralmente aparece é:  
  
***Foi informado um rateio para a Conta 1.1.1.1.001, porém a mesma não utiliza rateio.***  
  
Esse erro acontece quando o evento ou encargo que está sendo contabilizado tem alguma conta gerencial informada, mas a conta contábil referenciada não tem rateio. Veja exemplo a seguir:

O evento em questão tem uma conta gerencial informada a Débito. Isso quer dizer que a conta contábil a débito ( a conta que aparece na mensagem do erro) será rateada para a conta gerencial. O que ocorre é que no cadastro da conta 1.1.1.1.001 (Cadastros / Contabilização / Plano de contas contábeis), o flag Rateio não está marcado, o que indica que a conta não possui rateio.

A regra em questão é a seguinte: se for informada alguma conta gerencial em algum encargo ou evento, a conta contábil referenciada deve possuir rateio.  
  
**Obs.:** O campo “Rateio” dentro do cadastro da conta contábil não pode ser marcado diretamente, e por isso o motivo dele ficar sempre desabilitado. Para que se possa definir que a conta utiliza rateio, é necessário selecioná-la e executar o processo “Alteração do campo – Tem Distribuição gerencial”. Outro detalhe é que esse processo é visto mediante permissão dada ao usuário no RM Saldus ( Totvs Gestão Contábil).

No processo, basta informar que a conta passará a ter Distribuição gerencial, e qual será o rateio gerencial da mesma.

Após a execução do processo, o campo Rateio ficará marcado dentro do cadastro da conta, e aparecerá a aba Distribuição gerencial, contendo as contas gerenciais selecionadas no processo.

Reforçando, então fica definido o seguinte: se o encargo / evento tiver conta gerencial, as contas contábeis que forem referenciadas deverão possuir rateio.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**Rateio não informado no evento/encargo, mas conta contábil com rateio**

Uma situação contrária também pode acontecer, quando a conta possui rateio ( conforme explicado nas etapas anteriores), e não for informada a conta gerencial no evento ou encargo. Se for assim, ocorrerá o erro:  
  
***Erro ao validar a partida 0. O rateio a débito para a Conta 1.1.1.1.001 deve ser informado***  
  
Esse erro acontece caso o parâmetro “Segue regras do RM Saldus na geração de lançamentos”, em Opções / Parâmetros / RM Labore / Outros Parâmetros / Parâmetros II, esteja desmarcado, pois assim, será necessário que o evento/encargo defina o rateio, através da conta gerencial informada neles.

##### **Período contábil**

Ao gerar a contabilização, se aparecer a mensagem abaixo:

***A data da contabilização está fora do período contábil do RM Saldus. Confirma a geração do lote?***  
  
Se a data informada no campo Data da contabilização realmente é a que deve ser na geração do lote, deve-se alterar a Data Final do período contábil dentro da etapa 6 dos parâmetros do RM Saldus, e isso pode ser feito no RM Labore, através do menu *Cadastros / Contabilização / Parâmetros do RM Saldus*, ou então diretamente no RM Saldus, no menu *Opções / Parâmetros / RM Saldus*.

Outro erro relacionado à data é:  
  
***Não é permitido efetuar manutenção em partidas na data (xx/xx/xxxx) fora do período de Lançamentos permitido para o usuário de (xx/xx/xxxx a xx/xx/xxxx).***  
Nesse caso, a data informada está dentro do período contábil, mas fora do período para digitação de lançamentos para o usuário logado no sistema. Para ajustar a data, basta acessar no RM Saldus o menu *Cadastros / Segurança / Usuários*, editar o usuário em questão e alterar o “Período Para Digitação de Lançamentos” com um intervalo que compreenda a data da contabilização a ser efetuada pelo usuário (vide imagem a seguir).

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

###### Código da filial

Quanto ao erro relacionado ao código da filial:  
  
***O código da filial não foi informado, não é permitido incluir partida sem filial***  
  
Caso não for informada a filial contábil dentro dos agrupamentos de contas contábeis, e o código da filial é verificado nos seguintes locais:  
  
- no cadastro da seção do funcionário - quando não se utiliza cálculo por centro de custo, ou quando se utiliza cálculo por centro de custo e o flag “Usa filial contábil da seção quando utiliza cálculo por C.Custo” estiver marcado em *Opções / Parâmetros / RM Labore / Outros Parâmetros/ Parâmetros II*.  
  
- no cadastro do centro de custo para o qual foi rateado o encargo / evento - quando se trabalha com centro de custo e o flag “Usa filial contábil da seção quando utiliza cálculo por C.Custo” estiver desmarcado.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

###### Centro de custo global desativado

Na versão 11.20, em bibliotecas anteriores à 11.20.25, quando o centro de custo global de algum centro de custo (RM Labore) está desativado, ocorre o erro:  
  
***Index was out of range. Must be non-negative and less than the size of the collection.***  
***Parameter name: índex***  
  
A mensagem em português é:  
  
***O índice estava fora do intervalo. Ele deve ser não-negativo e menor que o tamanho da coleção.***  
***Nome do parâmetro: index***

Da versão 11.20.25 e 11.40 em diante, essa mensagem já foi tratada, e é exibida da seguinte forma:  
  
***Erro: C. Custo do Labore 01.4 corresponde a um C. Custo Global Desativado***

Para correção, basta acessar o cadastro do centro de custo global do centro de custo referenciado na  
mensagem e marcar o flag “Ativo”.

Caso a mensagem de erro exibida seja a primeira ( sem o tratamento informando o centro de custo), será necessário localizar o centro de custo através da verificação do final do log de execução, onde aparecerá o funcionário e qual evento/encargo está sendo contabilizado, e com base nisso, fazer a ativação em Cadastros / Centros de Custos.

         
Cadastros/Centros de Custos (RM Labore)                                               Cadastros / Centros de custos  
  
  
**Observações:**  
**A partir da versão 11.40**, o sistema permite que seja feita a contabilização sem enviar direto para o RM Saldus, para que seja possível fazer a conferência ou ajustes no lote gerado. Para isso, basta acessar o menu *“Opções / Parâmetros / RM Labore / Outros Parâmetros / Parâmetros II”* e deixar o flag “Gerar contabilização no Labore antes de enviar para o Saldus” marcado.

Assim sendo, quando se fizer a contabilização, o lote será gravado no menu “Cadastros / Contabilização / Lançamentos contábeis Labore”, para os devidos ajustes e conferências que se julgar necessários, e após  
isso, é possível enviar o lote para o Saldus, sendo que para isso, basta executar o processo “Integrar lote contábil com o Saldus”.

Outra informação importante é que mesmo que o parâmetro para enviar o lote direto ou não para o Saldus esteja desmarcado, quando ocorrer alguma ressalva ( erro, aviso) na geração da contabilização, o lote será criado e enviado para o menu Lançamentos contábeis Labore para que se faça o acerto necessário e após isso a integração para o Saldus. Quando isso acontecer ( ressalva na geração da contabilização), o sistema emitirá a seguinte mensagem:

###### --------------------- ***Os Lançamentos Contábeis não foram gravados no Saldus por terem inconsistências.*** ***Estes lançamentos encontram-se no Menu Cadastros|Contabilização|Lançamentos Contábeis Labore*** ---------------------

###### \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

###### Diferenças entre crédito e débito:

Se porventura ao efetuar a geração ocorrer mensagem de diferença entre valores de crédito e débito, de uma coisa pode se ter certeza: está se trabalhando com contabilização parcial.

Exemplo:

Suponha-se que tenho todos os meus proventos contabilizados somente a débito, e os descontos e encargos contabilizados a crédito.

**ENVELOPE DO FUNCIONÁRIO:**

**MOVIMENTAÇÃO POR CENTRO DE CUSTO:**

**ABA DADOS CONTÁBEIS NO CADASTRO DE EVENTOS:**

**ENCARGO DE LÍQUIDO SALARIAL:**

Vamos supor que não foi feita a geração de encargos para o encargo de líquido salarial. Assim sendo, ocorreria erro de diferença entre crédito e débito.

Então nesse caso o que é necessário e verificar se já foi feita a geração de encargos, e ainda observando se algum encargo é calculado por fórmula, para saber se a fórmula em questão está retornando valores corretos.

No exemplo acima, se eu estivesse contabilizando o período 3 da folha, mas estivesse no período 4 e fizesse a geração de encargos, o valor dos encargos seria com base no líquido da folha do período 4, e não do período 3. Isso com certeza acarretaria em divergência nos valores de crédito e débito.

Nessas situações, cabe analisar mais detalhadamente. Uma forma mais fácil de descobrir onde estão as diferenças, é gerando a contabilização, por exemplo, para apenas um funcionário, para se descobrir se a diferença seria de um encargo não gerado, ou valor incorreto retornado pela fórmula do encargo, ou o período, etc.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**CENTRO DE CUSTO E DEPARTAMENTO:**

Dois erros que ocorrem e que são muito semelhantes são:

***A partida 1-0 não deve possuir Centro de Custo pois a Contabilidade está parametrizada para não usar Centro de Custo***

e

***A partida 1-0 não deve possuir Departamento pois a Contabilidade está parametrizada para não usar Departamento***

Essa parametrização é definida através do menu Cadastros / Contabilização / Parâmetros do RM Saldus, ou então diretamente no RM Saldus, no menu Opções / Parâmetros / RM Saldus, na etapa 8 – Manutenção dos Lançamentos Contábeis.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[R@RH](https://totvs.byyou.com/?space=rrh)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 011 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 4 – (Recursos Humanos)
