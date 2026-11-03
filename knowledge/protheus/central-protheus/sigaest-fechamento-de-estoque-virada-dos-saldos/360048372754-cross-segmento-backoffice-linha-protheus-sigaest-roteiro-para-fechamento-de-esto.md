---
article_id: 360048372754
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: 8b51851d7b119b5dfcb950b5e8e90af62cdd9f65e59faf12efd5af697d696935
fetched_at: '2026-06-28T22:38:52.662024+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Roteiro para Fechamento
  de Estoque (virada de saldos)
type: support-article
updated_at: '2024-01-26T20:25:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048372754-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Roteiro-para-Fechamento-de-Estoque-virada-de-saldos
---

**Dúvida**

Qual o roteiro e maneira para fazer o Fechamento do Período do Estoque? Quais as finalidades dos parâmetros MV\_ULMES e MV\_DBLQMOV neste Processo?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

|  |
| --- |
| **Informação importante**  **A partir da release 12.1.33 foi implementada uma nova rotina - Acompanha Custos (MATA038) - que visa centralizar os processos obrigatórios contidos nessa FAQ: Recálculo do Custo Médio (MATA330), Contabilização do Custo Médio (MATA331 - se empresa contabiliza) e Virada de Saldos (MATA280 - esta última descontinuada para uso à parte).**  **Seção de Artigos da rotina Acompanha Custos - MATA038 - [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO)**    **Obs: Todas as demais orientações sobre os processamentos opcionais e avaliação de custo contidas nessa documentação permanecem as mesmas.** |

Esta documentação tem por objetivo um simples detalhamento dos processos de fechamento.

O ponto de partida para o fechamento de período é o parâmetro MV\_ULMES, este parâmetro é alimentado automaticamente pelo sistema de forma que não deve ser manipulado manualmente, a não ser em casos muito específicos como ao iniciar a utilizar as rotinas de fechamento já que o conteúdo padrão deste parâmetro no sistema é “20070101”, também é aconselhável utilizar o parâmetro MV\_DBLQMOV para bloquear movimentações no período que se está efetuando o fechamento já que movimentações durante as validações podem gerar inconsistência nos saldos iniciais do período seguinte, ao contrário do parâmetro MV\_ULMES que não deve ser manipulado o parâmetro MV\_DBLQMOV deve ser alterado conforme documentação abaixo.

[MP - SIGAEST - Como realizar o bloqueio de movimentações no estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844351-MP-SIGAEST-Como-realizar-o-bloqueio-de-movimenta%C3%A7%C3%B5es-no-estoque-?source=search)

## Cálculo do custo das notas de entrada

O cálculo do custo das notas de entrada no processo de fechamento é opcional e a critério do cliente executar ou não.

A rotina refaz do custo de entrada tem por objetivo fazer o cálculo do custo baseado nos impostos recuperáveis (ICMS, IPI, PIS/COFINS, despesas etc.).

Abaixo a documentação referente ao custo de entrada.

[MP - SIGAEST - Custo de entrada (MATA190) - Conceito e Exemplos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-MP-SIGAEST-Custo-de-entrada-MATA190-Conceito-e-Exemplos?source=search)

## Processo de inventário

O processo de inventário também é opcional e poderá ser feito quando o cliente tiver a necessidade de verificar o pareamento entre o estoque físico e o estoque constante no sistema, detalhes deste processo no link abaixo.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Processo de Inventário - Conceito, Exemplo e Dúvidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020799592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-Invent%C3%A1rio-Conceito-Exemplo-e-D%C3%BAvidas)

[MP - SIGAEST - COMO REALIZAR INVENTARIO DO SALDO ATUAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021388511-MP-SIGAEST-COMO-REALIZAR-INVENTARIO-DO-SALDO-ATUAL?source=search)

## Saldo atual

A rotina refaz saldos pode ser executada também embora não influencie de forma direta no processo de fechamento ficando a critério do cliente executar ou não.

## Refaz poder de terceiro

A rotina refaz poder de terceiro faz o ajuste dos saldos de/em terceiro e não é obrigatória, ficando a critério do cliente utilizar ou não.

## Recálculo do custo médio

A rotina recálculo do custo médio é uma das mais importantes para o processo de fechamento, para clientes que utilizam o custo off-line definido através do parâmetro MV\_CUSMED com o conteúdo M, indicando que é mensal, ou seja, através do recálculo do custo médio.

Uma das partes mais importantes é a definição dos perguntes da rotina recálculo do custo médio, é onde definimos boa parte da regra de negócio que atende à necessidade dos nossos clientes.

Devido à grande diversidade de formas de apuração de custo o sistema possui também parâmetros que ficam na SX6, alterados através do configurador, são parâmetros mais restritos pelos quais também podemos alterar o fluxo de informações, porém não entraremos em detalhes de todos somente dos mais usuais.

Para exemplificar na prática estes processos de fechamento iremos criar um exemplo em que compramos a matéria prima produzimos e vendemos o produto acabado.

Não detalharemos o custeio de MOD/GGF, a documentação abaixo já trata do assunto.

<https://tdn.totvs.com/pages/releaseview.action?pageId=366649055>

1 – Vamos criar os produtos (MATA010) MP1000, matéria prima e o produto PA1000, produto acabado.

![PRODUTO-MP1000.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072766253)

![PRODUTO-PA1000.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071578594)

2 – Dar saldo inicial (MATA220) para o produto MP1000 no armazém 01 com quantidade 1 e valor 10 e no armazém 02 com quantidade e custo zero e para o produto PA1000 com quantidade e custo zero no armazém 01.

![INICIAL-MP1000-01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071578674)

![INICIAL-MP1000-02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071578734)

![INICIAL-PA1000.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072766453)

3 – Agora vamos fazer um documento de entrada (MATA103) com quantidade 10 e custo unitário 11 da nossa matéria prima conforme print abaixo no armazém 02.

![COMPRA-MP1000.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072766553)

4 – Para demonstrar o método de apropriação diário vamos dar entrada só que com data base diferente e quantidade 10 e custo unitário 12 conforme print abaixo:

![COMPRA-MP1000_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071578914)

5 – Agora vamos realizar uma movimentação interna de transferência (MATA260/MATA261) do produto MP1000 do armazém 02 para o armazém 01, de quantidade 10 conforme print abaixo.

![TRANSFERENCIA-MP1000-02-01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072766633)

6 – Vamos realizar o mesmo processo acima só que em um dia diferente.

![TRANSFERENCIA-MP1000-02-01-02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072766773)

7 – Vamos criar uma estrutura (MATA200) para o produto PA1000 tendo o produto MP1000 em sua base.

![ESTRUTURA-PA1000.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072766873)

8 – Gerar uma ordem de produção (MATA650) com quantidade 10 para o produto PA1000, fechar a rotina e confirmar o empenho do produto MP1000.

![ORDEM-PA1000.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071579234)

9 – Gerar uma segunda ordem de produção em posterior com quantidade 10, veja abaixo:

![PRODUCAO-PA1000_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071582094)

10 – Realizar o apontamento da ordem de produção (MATA250) gerada anteriormente com quantidade 10.

![PRODUCAO-PA1000.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072937433)

11- Realizar outro apontamento de produção com quantidade 10.

![APONTAMENTO-PA1000_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071745734)

12 – Vamos realizar a venda do nosso PA através da rotina pedidos de venda (MATA410) com quantidade 5, após fazer a liberação do pedido.

![VENDA-PA1000.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071748554)

13 – Realizar uma nova venda com quantidade 15 do produto PA1000.

![VENDA-PA1000_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072940393)

14 – Após este processo podemos executar a rotina recálculo do custo médio, vamos listar apenas os parâmetros que influenciam no custo do produto.

Um dos parâmetros mais importantes para o custeio da OP é o MV\_PRODPR0, não vamos entrar em detalhes sobre o seu conceito, no link abaixo já tem este detalhamento.

<https://tdn.totvs.com/pages/releaseview.action?pageId=6085227>

No nosso teste utilizaremos o método 1 (MV\_PRODPR0 = 1) porém não influencia no fluxo de teste.

 Outro parâmetro fundamental é o MV\_CUSFIL, efetuaremos 1 exemplo nas 3 formas possíveis, por armazém (MV\_CUSFIL= A), por filial (MV\_CUSFIL= F) e por empresa (MV\_CUSFIL= E).

Iniciaremos com o parâmetro com o custo por armazém, neste caso todos os armazéns terão seu próprio custo, exemplificarei abaixo.

Após executar e rotina recálculo do custo médio (MATA330) surgem os parâmetros que são de suma importância, detalharemos apenas os mais importantes e que tenham influencia no custo do exemplo passado.

1 – Data limite final?

Devemos definir a data limite para processamento da rotina recálculo do custo médio, exemplo 30/11/2019.

2 – Atualiza arquivos de movimentos?

Devemos sempre definir como sim para que as movimentações internas (SD3) sejam processadas.

3 – Gerar estrutura pela movimentação?

            Fica a critério do cliente, porém quando temos ordens de produção onde possui algum produto que foi requisitado e não faz parte da estrutura (SG1) essa requisição acaba não agregando o custo para esta ordem de produção, aconselhamos a deixar como sim.

4 – Método de apropriação?

Este parâmetro é extremamente importante para definirmos a forma de apuração do custo da empresa, iniciaremos pelo método de apropriação mensal.

5 – Recalcula níveis de estrutura?

            Sempre que o parâmetro “Gerar estrutura pela movimentação? ” estiver como sim devemos colocar sim para que o sistema recalcule os níveis da estrutura.

6 – Movimentos internos valorizados?

Este parâmetro define se ao realizarmos uma movimentação interna valorizada se esta movimentação deve ser antes das movimentações internas ou após as movimentações internas.

Vamos executar o recálculo do custo médio com o método de apropriação mensal e o custo por armazém (MV\_CUSFIL = A).

![G_REC_MENS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071749874)

Após a execução do recálculo podemos utilizar o relatório MATR900 para a conferência do custo, veja abaixo como ficou o armazém 01.

Para podermos analisar a ordenação feita pela rotina recálculo do custo médio temos que parametrizar o relatório MATR900 com os perguntes "Doc Sequência? = S e Sequência de impressão = Cálculo" e o pergunte “Qual armazém? ”, quando o custo é por armazém devemos informar o armazém que se está analisando e quando o custo é por filial devemos informar o caractere “\*\*” e quando o custo é por empresa devemos utilizar o caractere “##”.

![MATR900_01.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071750114)

![MATR900_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072942133)

Vejamos agora o armazém 02.

![MATR900_02.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360072942613)

![MATR900_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071750774)

Agora vamos ver como funciona o custo por filial por filial (MV\_CUSFIL = F).

![MATR900_03.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360072942793)

![MATR900_03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071750954)

Para verificarmos o cauto por empresa vamos realizar uma entrada (Compra) na filial 02 com custo unitário de 13, vejam abaixo como altera o custo de ambas as filiais quando o custo é por empresa (MV\_CUSFIL=E).

![MATR900_05.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360072946233)

![MATR900_05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072948853)

Agora vamos analisar o método de apropriação diário, este método se assemelha com o método de apropriação mensal, porém calculado por dia, neste caso todos os dias terão seu custo apurado individualmente com base nos saldos do dia anterior e nas entradas que afetam o custo no dia.

Vamos executar o recálculo do custo médio com o pergunte “Método de apropriação? ” diário e custo por armazém (MV\_CUSFIL= A).

Veja como ficou o custo no armazém 01.

![MATR900_01.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071751314)

![MATR900_09.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072949473)

Vejamos também o armazém 02.

![MATR900_02.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360072949493)

![MATR900_06.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071752014)

Vejamos agora o custo médio por filial.

![MATR900_03.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071752054)

![matr900_07.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072949693)

Vejamos agora um exemplo do método de apropriação diário e custo por empresa (MV\_CUSFIL=E).

![MATR900_05.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360072949773)

![MATR900_08.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072949853)

O método de apropriação sequencial é o mais simples de todos, neste método o sistema não altera a ordenação dos movimentos, ou seja, da mesma ordem que foi digitado no sistema permanecem, veja abaixo o custo por armazém, armazém 01.

![MATR900_01.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071752234)

![MATR900_09.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071752294)

Vejamos também o armazém 02.

![MATR900_02.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071752394)

![MATR900_10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071752534)

Vejamos agora o custo por filial (MV\_CUSFIL=F).

![MATR900_03.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071752574)

![MATR900_11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071752714)

E por último o custo por empresa (MV\_CUSFIL=E).

![MATR900_05.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071752834)

![MATR900_12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072950393)

## 

## Ordenação de movimentos.

A ordenação de movimentos é uma parte importante para podermos apurar o custo, abaixo temos o print da ordenação padrão feita pelo sistema, disponível também na documentação abaixo na aba ordenação de movimentos.

<https://tdn.totvs.com/pages/releaseview.action?pageId=340361781>

![ORD_MOV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072950473)

Em alguns cenários o recálculo do custo médio pode não ordenar conforme o esperado, veja o cenário abaixo.

1 – Realizar uma devolução de venda do produto PA1000 através da rotina documento de entrada.

![DEV_VEND.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072950693)

2 – Agora vamos realizar a desmontagem (MATA242) do produto.

![DESMONT.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072950833)

3 – Agora vamos realizar a transferência do armazém 01 para o armazém 02 através da rotina de transferência múltiplas (MATA261).

![TRANSFERENCIA-MP1000-01-02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071753634)

Para exemplificar melhor como fica a ordenação no cenário acima vamos executar a rotina recálculo do custo médio (MATA330) e o custo por filial (MV\_CUSFIL =F), este problema nos métodos de apropriação mensal e diário.

![MATR900_03.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071753714)

![MATR900_13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072951253)

Veja que acima o movimento DE7 ficou ordenado abaixo dos demais movimentos, porém este cenário, na maioria de nossos clientes, não atenderia.

No padrão o parâmetro MV\_SEQ300 que quando habilitado ordena os movimentos conforme a digitação dos movimentos feita pelo usuário, ou seja, todos os movimentos que estão na ordem 300 não terão sua ordenação alterada da digitada pelo usuário.

Vejamos agora a ordenação após habilitar o parâmetro MV\_SEQ300.

![MATR900_14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071753874)

Caso esta ordenação também não atenda a necessidade do cliente será necessário utilizar o ponto de entrada MA330TRB, maiores detalhes na documentação abaixo na aba ordenação de movimentos.

<https://tdn.totvs.com/pages/releaseview.action?pageId=340361781>

## Apuração dos custos e quantidades processadas pela rotina recálculo do custo médio.

Para realizar a conferência do custo podemos utilizar o relatório MATR900 conforme já representado acima e também podemos utilizar os relatórios relação da posição do estoque (MATR260) e resumo das entradas e saídas (MATR320).

Vamos imprimir o relatório MATR260 do produto MP1000 porém pode ser feita uma range de produtos específica com o pergunte “Saldo do produto a considerar? ” como fechamento, neste caso o relatório busca o conteúdo dos campos B2\_QFIM e B2\_VFIM1 que são os campos que são atualizados pela rotina recálculo do custo médio, isto também se aplica ao relatório resumo das entradas e saídas (MATR320), veja a impressão dos dois relatórios abaixo.

![MATR260_FEC.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071885574)

![MATR260_FEC.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071755274)

![MATR320_FEC.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071876714)

![MATR320_MOV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072953933)

Os valores acima representam os valores apurados pela rotina recálculo do custo médio e abaixo vamos imprimir os mesmos relatórios só com a pergunta “Saldo do produto a considerar? ” por movimento e com data igual a data que se está realizando o fechamento, desta forma podemos verificar se o processamento da rotina recálculo do custo médio (MATA330) foi feito corretamente, veja abaixo a impressão dos relatórios.

![MATR260.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360072954353)

![MATR260_MOV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072954273)

![MATR320_MOV.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360073098693)

![MATR320_MOV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073098953)

Após as conferências podemos executar a rotina fechar períodos (MATA280), não detalharemos a execução da rotina pois ela é importante, porém simples, caso queira o cliente pode executar o relatório relação da posição do estoque (MATR260) por movimento e com data do fechamento e este relatório irar listar os valores inseridos na tabela de saldos iniciais (SB9).

![MATA280.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360071877194)

# Reabertura de estoque (para ambientes na release 12.1.27)

Atualmente não existe um programa padrão para reabertura de estoque, porem em casos específicos tal processo é realizado eliminando os registros da tabela SB9 e ajustam o parâmetro MV\_ULMES com a data do período anterior.

Não recomendamos a realização deste processo pois não e um processo padrão do sistema, porem quando não existe alternativa o cliente deve se atentar a seguinte situação:

Não se deve reabrir fechamentos de estoque quando em sua base de dados existem ordens de produção (Tabela SC2) que possuem movimentação de requisição/devolução de estoque contra OP entre os períodos de fechamento de estoque. Pois esta ação irá prejudicar o controle de custos destes produtos desestabilizando seus valores.

Veja o exemplo abaixo:

![MATR860_ANT_FEC.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071877474)

Foram feitas duas requisições sendo uma com quantidade 1 e outra com quantidade 2 e custo total 34,29 porém não geramos apontamento de produção.

A rotina de custo médio prepara o saldo que está em processo (no exemplo acima 34,29 – duas requisições) da seguinte forma:

SC2->C2\_VFIM1 = SC2->C2\_VINI1 + Movimentações internas (Requisição/Devolução) contra produção para esta ordem de produção.

No nosso exemplo ficara:

SC2->C2\_VINI1 = 0 (Pois a OP foi aberta neste mês)

Total de Requisições = 34,29

Resultado SC2->C2\_VFIM1 = 34,29

A rotina de virada de saldos prepara o saldo da tabela SC2 para o próximo período da seguinte forma:

SC2->C2\_VINI1 = Saldo em processo do período anterior

SC2->C2\_VINI1 = SC2->C2\_VFIM1, ou seja, SC2->C2\_VINI1 = 34,29 para o próximo período.

Ao realizar o procedimento de reabertura de estoque o cliente que possui ordem de produção que são utilizadas em dois ou mais fechamento não se atentam ao controle de saldos da tabela SC2 e ocorre o problema abaixo:

A rotina de custo médio prepara o saldo que está em processo (no exemplo acima 150,00 – duas requisições) da seguinte forma:

SC2->C2\_VFIM1 = SC2->C2\_INI1 + Movimentações internas (Requisição/Devolução) contra esta ordem de produção.

No nosso exemplo ficara:

SC2->C2\_VINI1 = 34,29 (***Pois ao reabrir o estoque o cliente não conhece a estrutura de nossas tabelas e não tem o controle do campo C2\_VINI1 do período anterior***)

Total de Requisições = 34,29

Resultado SC2->C2\_VFIM1 = 68,58 (AQUI ESTA O IMPACTO NA REABERTURA DE ESTOQUE, ONDE O CUSTO FICARA INCORRETO E SERA REPASSADO PARA OS APONTAMENTOS DE PRODUÇÃO).

![MATR860_ANT_REAB.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071878034)

# Reabertura de estoque (para ambientes que utilizam a rotina Acompanha Custos)

A partir da release 12.1.33, foi implementada a nova rotina Acompanha Custos, atendendo então a demanda de centralizar os processos obrigatórios na Jornada de Fechamento, e também incrementando no padrão o processo de Reabertura de Estoque. Todos os detalhes sobre o processo de Reabertura do Estoque estão contidos na documentação do link abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Processo de Reabertura de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6420543172247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Processo-de-Reabertura-de-Estoque)

Finalizamos assim este artigo para auxiliar nossos clientes na análise de seus custos e validações referentes ao fechamento.

**Saiba mais:**

*[Clique aqui e saiba mais sobre Fechamento de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012208793-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)*
