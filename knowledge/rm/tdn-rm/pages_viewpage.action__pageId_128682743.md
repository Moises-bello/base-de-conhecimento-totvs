---
content_hash: 9c2dd2915afa4524661996bab904e35b8b3ebbf1e67767f5c8eac033cb779361
fetched_at: '2026-06-29T00:05:55.262945+00:00'
page_id: '128682743'
product: rm
source: tdn-rm
title: Comparativo de fórmulas delphi x .net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=128682743
version: 2
---

FAQ: **Comportamento das fórmulas delphi x .net**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.5x ou superior |

**Arredondamento**

O arredondamento no valor do evento é sempre a partir da 3ª casa decimal, porém, quando a 3ª casa decimal é “5” (cinco), o DELPHI ora arredonda para cima, ora arredonda para baixo, característica da linguagem de fórmula DELPHI. O .NET sempre arredonda para cima.

Exemplo:

Resultado da fórmula => 184,**635**

DELPHI => 184,63

.NET => 184,64

Dízimas

No caso de dízimas, ao invés de entender como “18,635”, o DELPHI entende como “18,6344444444444”.

Essas diferenças de centavos poderão ocorrer em todos os processos de cálculos do sistema.

**Comandos e Operadores**

**Parênteses ()**

*Em DELPHI*

Não valida a falta de parênteses às funções.

Exemplo:

C ‘1111’

C (‘1111’

Na validação de fórmula, DELPHI deveria acusar erro, pois, a função C exige que o valor a ser retornado esteja entre parênteses.

*Em .NET*

Acusaria erro, pois o correto seria usar os parênteses, veja:

C **(**‘1111’**)**

**Comando DECL**

*Em DELPHI*

Não valida à atribuição de valores indevidos.

Exemplo:

DECL(FLAG,0)

Na validação de fórmula, DELPHI deveria acusar erro, pois, o comando DECL serve apenas para declarar variáveis, ou seja, não podemos atribuir valores ao mesmo.

*Em .NET*

Acusaria erro, pois o correto seria usar o comando SETVAR para atribuição de valores à variável declarada, veja:

DECL(FLAG); SETVAR(FLAG,0)

**Operadores E / OU**

Tenhamos como exemplo a seguinte fórmula:

SE CSIND=’0002’ OU CSIND=’0005’ E C(‘0003’)> 0 ENTAO 10 SENAO 0 FIMSE

Suponhamos que o funcionário de chapa “XXXXX” está vinculado ao sindicato “0002”.

*Em DELPHI*

Os operadores E / OU sempre são executados na ordem inserida no texto da fórmula, sendo assim, a fórmula será executada conforme abaixo:

Variável CSIND 0002

Constante literal 0002

Comparacao (=) 0002 0002

Resultado Comparacao (=) 1,0000

Variável CSIND 0002

Constante literal 0005

Comparacao (=) 0002 0005

Resultado Comparacao (=) 0,0000

**OU** logico 1,0000 0,0000

Resultado **OU** logico 1,0000

Constante literal 0003

Chamada a funcao C 0003

Resultado da funcao C 0,0000

Constante literal 0,0000

Comparacao (>) 0,0000 0,0000

Resultado Comparacao (>) 0,0000

**E** logico 1,0000 0,0000

Resultado E logico 0,0000

Executa SENAO

Constante literal 0,0000

Resultado da formula 0,0000

Perceba que a execução em Delphi, segue a ordem de inserção dos operadores no texto.

*Em .NET*

O .NET respeita a lógica, primeiro executa o operador ‘E’ para depois executar o ‘OU’, desta maneira, a fórmula será executada conforme abaixo:

Iniciando execução de fórmula Testing às 15:25:48

Comparação (=)

Constante literal 0002

**Operador lógico (ou)**

Comparação (=)

Constante literal 0005

**Operador lógico (e)**

Constante literal 0003

Comparação (>)

Constante literal 0

Chamando função CSIND()

Retorno da função CSIND 0002

Chamando função CSIND()

Retorno da função CSIND 0002

Chamando função C(0003)

Retorno da função C 0

Condição CSIND = 0002 ou CSIND = 0005 e C ( 0003 ) > 0 **aceita**

Em .NET o operador **E**, apesar de estar inserido após as condições dos operadores **OU**, foi executado primeiro, é como se tivesse sido executado da seguinte forma:

*O valor do evento “0003” é maior que zero, **OU**, o sindicato do funcionário é igual a “0002” **OU** “0005”?*

Uma maneira de acertar esta fórmula seria incluir parênteses nas condições que deseja agrupar, veja:

SE **(**CSIND=’0002’ OU CSIND=’0005’**)** E C(‘0003’)> 0 ENTAO 10 SENAO 0 FIMSE

Assim, a fórmula será executada da seguinte forma:

*O sindicato do funcionário é igual a “0002” **OU** “0005”, **E**, o valor do evento “0003” é maior que zero?*

Outra maneira seria marcar o parâmetro *‘Manter compatibilidade com versões Win32’*. Com este parâmetro marcado a lógica é igual ao DELPHI.

**Funções**

Com a migração do cálculo, algumas funções de fórmula foram ajustadas para uma melhor aplicação da função. Clique aqui e veja maiores detalhes. (expande as funções abaixo)

**NDDSRPER(DATA,DATA,STRING)** - Passa a verificar admissão, demissão, afastamento, férias e histórico de seção.

O DELPHI contabiliza apenas o último período de gozo de férias que consta no histórico. O Cálculo .NET verifica todos os períodos de gozo.

No DELPHI, o sistema considera sempre o sábado, no cálculo .NET o sistema verifica a escala de horário do funcionário.

Serão contabilizados os dias de feriado mais os dias cadastrados como ‘Descanso’ na escala de horário. Seria como se fosse (Feriados + variável NDIASDESC).

O parâmetro ‘*ConsideraSabados*’, existente na variável será verificado para considerar os dias cadastrados como ‘Compensado’ na escala de horário. Com este parâmetro confirmado seria como se fosse (Feriados + variável NDIASDESC + variável NDIASCOMP).

**DUTEISMES, DUTPROXMES e NDTRAB**

O sistema irá verificar o horário cadastrado para o funcionário. Nos dias em que houver apenas a batida de saída cadastrada, ou seja, o final da jornada do dia anterior, e não houver uma batida de entrada posterior, não serão considerados como dias úteis.

**NDTRAB** - retorna o número de dias que o funcionário deverá trabalhar no mês de competência conforme calendário, afastamento, horário e histórico do funcionário.

Em .NET passa a verificar, também, o histórico de seção. Em cálculo de rescisão para o próximo mês, irá verificar os dias trabalhados do mês da rescisão.

**NDTRABPER e NDTRABPER2**

Para a contagem de dias nestas funções, o sistema considera a batida de entrada cadastrada no horário.

Neste caso, se um horário tem batida de entrada em um dia e batida de saída em outro, este dia também será considerado para a contagem de dias.

**NJTRAB e NJTRABPXMES**

Para que estas funções funcionem corretamente, é necessário que a jornada do horário esteja cadastrada.

**MEDCOMISDATA( , , ) e CALCMEDDATA( , , )**

O Cálculo .NET irá verificar o panorama da data informada na variável, para detectar se as férias são vencidas ou proporcionais.

**DATANULA**

Em DELPHI retorna o valor em branco.

Exemplo:

DATANULA

Resultado será igual a ‘ ‘ (vazio).

Em .NET, monta uma data referente ao 1º dia, do 1º mês, do 1º ano.

Exemplo:

DATANULA

Resultado será igual a 01/01/0001.

**BASEIRRF, BASEIRRFFF(,), BASEIRRF13, BASEIRRF13FF(,) e BASEIRRFFERIASFF(,)**

O DELPHI busca os valores da base de IRRF da tabela de períodos da ficha financeira (PFPERFF) observando o caixa comum e não considera o período atual no momento do cálculo, porém, quando testamos a fórmula, o sistema considera o período atual.

O .NET busca os valores conforme incidência dos eventos, observando a data de pagamento dos eventos.

**DIADIRFER(3)** - retorna os dias de direito de férias real.

O DELPHI conta como dias de direito de férias o período em que o funcionário está afastado por “Aposentadoria por Invalidez” ou “Serviço Militar”, sendo que esses tipos de afastamento acarretam uma interrupção no contrato de trabalho, ou seja, durante o período de afastamento o funcionário não recebe os direitos trabalhistas. O .NET projeta o

período de afastamento e desconsidera este período na contagem dos dias de direito de férias.

**VFER**

Função alterada para retornar o valor do evento no Recibo de Férias.

**Observação I:**

Caso a variável seja utilizada no processo de Cálculo de Férias, o sistema busca o valor calculado em memória, e quando é utilizado em qualquer outro processo, o sistema busca o valor do evento gravado no banco, inclusive no cálculo da provisão.

**Observação II:**

O evento cujo cálculo necessite que as médias já estejam calculadas, precisa ter prioridade 70.

Todos os eventos com prioridade 70 serão recalculados após o cálculo da média.

**Atenção:**

O cálculo da média não segue prioridade, sempre é calculado por último, o sistema calcula todo o envelope e depois calcula a média. Porém, para atender situações em que o evento precisa do cálculo da média já calculada, este evento deve ter prioridade 70, assim, o sistema entende que este evento precisa ser recalculado após as médias.

**Observação III:**

Quando a variável é utilizada fora do cálculo de férias, serão considerados os valores do recibo com a maior data de pagamento anterior ao último dia da competência atual

**LIQFERIAS**

Quando a variável LIQFERIAS é utilizada no recibo de férias, o .NET sempre busca o valor daquele recibo. Quando a variável LIQFERIAS é utilizada no envelope de pagamento, o .NET sempre busca o líquido do primeiro recibo de férias que tem data de pagamento menor ou igual ao último dia da competência e que está com a situação de férias diferente de ‘F-Finalizadas’.

**MES e ANO**

Esta variável verifica o mês e ano do cálculo, porém em DELPHI, quando utilizada em férias para competências futuras, é retornado o mês e ano da competência atual. Em .NET é verificado o mês e ano do gozo das férias.

**CALCMED**

Quando passado o parâmetro 1 (um) para essa variável, ou seja, retorna valor de média das férias vencidas, o DELPHI sempre considera o período aquisitivo para o período de apuração das médias, independente dos parâmetros do sindicato. Já o .NET verifica os parâmetros do sindicato.

*Exemplo:*

No sindicato está parametrizado para buscar os 3 (três) últimos meses para apuração das médias. Ao utilizar a fórmula CALCMED(1), o DELPHI considera o período aquisitivo para apuração das médias, o .NET considera os últimos 3 meses.

**Retorno de Históricos**

Todas as variáveis que verificam o histórico do funcionário, quando nesse não existir as informações necessárias, como, por exemplo, o ‘índice do horário’, o DELPHI dará um retorno incorreto, já o .NET, na ausência da informação no histórico, irá buscar do cadastro atual do funcionário.

**Observação I:**

O .NET utiliza este recurso apenas quando o cálculo é referente ao mês corrente
