---
content_hash: de821d703ab836f2d720d72ba13e95c23ec3085865f045ddbc6425e5c78c5498
fetched_at: '2026-06-29T00:10:48.405394+00:00'
page_id: '561848185'
product: rm
source: tdn-rm
title: Parâmetros de Cálculo 2/2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561848185
version: 9
---

**Utiliza Cálculo por Centro de Custo**  
Para utilizar centro de custo é necessário marcar esta opção fazendo com que todos os campos referentes a centro de custo sejam habilitados no sistema.  
   
Antes de definir os parâmetros do cálculo por centro de custo, é necessário definir o conceito de Rateio Editado.  
O evento é considerado com rateio editado quando o centro de custo é forçado no evento, ou seja, o rateio não é feito considerando o rateio fixo do funcionário, nem o centro de custo parametrizado no evento. O centro de custo pode ser forçado através da Entrada de Dados por Centro de Custo, Importação do Movimento por Centro de Custo, Gerenciador de Movimento, Eventos Programados, ou através de Integrações com outros sistemas. Com rateio editado, o evento ficará registrado na tabela de movimento por centro de custo (PFMOVCC) com o campo EDITADO igual a 1.  
   
**Distribuir diminuição do movimento considerando apenas o rateio editado**  
Com esse parâmetro marcado, quando existir evento com rateio editado, caso seu valor seja diminuído por fórmula existente no evento, ao recalcular o envelope a distribuição por centro de custo será apenas para o Centro de Custo editado. Com isso o sistema não distribui a diferença negativa no rateio fixo do funcionário, ele apenas altera o valor do evento no movimento por centro de custo(PFMOVCC).  
**Exemplo:**  
Inserimos via entrada de dados por centro de custo o evento 0084 com centro de custo 1.01.  
Rateio fixo do funcionário:  
CC 1.02       60%  
CC 1.03       40%  
   
Movimentação:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Envelope (PFFINANC) | | Envelope Centro Custo (PFMOVCC) | | | |
| Evento | Valor | Evento | CC | Valor | Editado |
| 84 | 100,00 | 84 | 1.01 | 100,00 | 1 |

Caso diminuir através de fórmula o valor do evento para 80,00 a distribuição será:  
   
Com parâmetro marcado:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Envelope (PFFINANC) | | Envelope Centro Custo (PFMOVCC) | | | |
| Evento | Valor | Evento | CC | Valor | Editado |
| 84 | 80,00 | 84 | 1.01 | 80,00 | 1 |

Com parâmetro desmarcado:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Envelope (PFFINANC) | | Envelope Centro Custo (PFMOVCC) | | | |
| Evento | Valor | Evento | CC | Valor | Editado |
| 84 | 80,00 | 84 | 1.01 | 100,00 | 1 |
|  |  | 84 | 1.02 | -12,00 | 0 |
|  |  | 84 | 1.03 | - 8,00 | 0 |

**Observação**  
Apenas é possível diminuir o valor de um evento com rateio editado através de fórmula. Diminuições manuais do valor diretamente feitas no envelope do funcionário não serão realizadas, permanecendo o valor do rateio editado.

**Distribuir aumento do movimento considerando apenas o rateio editado**  
Com esse parâmetro marcado, quando existir evento com rateio editado, caso seu valor seja aumentado, a distribuição por centro de custo será apenas para o Centro de Custo editado. Com isso o sistema não distribui a diferença no rateio fixo do funcionário, ele apenas altera o valor do evento no movimento por centro de custo(PFMOVCC).  
   
**Exemplo**  
Inserimos via entrada de dados por centro de custo o evento 0084 com centro de custo 1.01.  
Rateio fixo do funcionário:  
1.02       60%  
1.03       40%   
   
Movimentação:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Envelope (PFFINANC) | | Envelope Centro Custo (PFMOVCC) | | | |
| Evento | Valor | Evento | CC | Valor | Editado |
| 84 | 100,00 | 84 | 1.01 | 100,00 | 1 |

Caso aumentar o valor do evento para 200,00 a distribuição será:  
   
Com parâmetro marcado:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Envelope (PFFINANC) | | Envelope Centro Custo (PFMOVCC) | | | |
| Evento | Valor | Evento | CC | Valor | Editado |
| 84 | 200,00 | 84 | 1.01 | 200,00 | 1 |

Com parâmetro desmarcado:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Envelope (PFFINANC) | | Envelope Centro Custo (PFMOVCC) | | | |
| Evento | Valor | Evento | CC | Valor | Editado |
| 84 | 200,00 | 84 | 1.01 | 100,00 | 1 |
|  |  | 84 | 1.02 | 60,00 | 0 |
|  |  | 84 | 1.03 | 40,00 | 0 |

**Rateio fixo por valor**  
Com este parâmetro ativado, o cálculo de rateio por centro de custo utiliza valores brutos para se chegar aos percentuais usados para gerar o valor do rateio de cada centro de custo. Caso contrário, utilizará percentuais para rateio por centro de custo. Os valores ou percentuais deverão ser informados em Administração de Pessoal | Cadastros | Funcionários | Anexos | Folha de Pagamento | Rateio Fixo.

**Obs:** Com o parâmetro 'Rateio fixo por Valor' desmarcado, o rateio fixo será considerado por percentual, desta forma somente será possível cadastrar rateios em que o resultado da soma não ultrapasse 100%

**Utiliza Gerenciador de Movimento**  
Ao marcar o parâmetro é habilitado o menu de '' Gerenciador de Movimento'' em Folha Mensal que possibilita a análise e validação dos processos executados que vão para o envelope.  
Este processo tem o objeto de gerenciar os lançamentos dos eventos na folha de pagamento, possibilitando o rastreamento das informações e garantindo a origem dos valores e que não sejam lançados em duplicidade.  
Através deste recurso, todas as movimentações de eventos digitadas ou lançadas pelo usuário serão armazenadas em uma tabela e lançadas posteriormente para o envelopes e para o envelope por centro de custo.

**Exemplo:**

Se estiver com o parâmetro marcado e lançar folha para algum funcionário ou até mesmo para a empresa toda, o sistema primeiro leva as informações para esse menu '' Gerenciador de Movimento'' é necessário verificar se as informações estão corretas e realizar o ''lançamento'' após essa validação.  
Caso o parâmetro esteja desmarcado, o sistema lança direto para o envelope do funcionário e para o envelope por centro de custo caso exista.

**Deduz valor por dependente na base de IRRF PL**  
Com este parâmetro marcado será deduzido da base de cálculo do evento de Código de Cálculo 126 - Participação nos Lucros, o valor referente a dedução de Imposto de Renda por dependente, cadastrado em Administração Pessoal | Cadastros | Cálculos | Valores Fixos, registro com a finalidade 'Valor deduzir de IRRF por dependente' e com a vigência dentro da competência de cálculo da folha.  
Caso este parâmetro esteja desmarcado, não será considerado o valor da tabela cálculo de valores fixos na dedução para Imposto de Renda.

**Observação**  
01 - Para que a dedução ocorra, é necessário que o funcionário tenha dependente cadastrado em Administração de Pessoal | Cadastros | Funcionários | Anexo | Folha de Pagamento | Dependentes, com o parâmetro marcado 'IRRF' na aba incidências do cadastro do dependente e que o mesmo seja elegível pela receita federal, como menores de 21 anos, filho inválido, etc.

02 - Esse parâmetro também será considerado no cálculo do imposto de renda da pensão que incide na participação dos lucros. sendo que terá o mesmo comportamento feito no cálculo do imposto de renda sobre a participação dos lucros.

Atenção

Quando o parâmetro 'Deduz valor por dependente na base de IRRF PL' estiver marcado, pode ocasionar divergências no eSocial (S-1.2). Certifique-se de que o valor calculado está correto conforme as orientações do leiaute e/ou MOS do eSocial."

**Ignora fórmulas adicionais no cálculo de médias**

Parâmetro Desmarcado:

* As fórmulas adicionais são consideradas no cálculo de médias.
* Não utilize funções relacionadas a médias (CALCMED, CALCMEDHIST, CALCMEDPROV), porque ocorre recursividade durante a execução, ocasionando erro de processamento.
* Uso indicado apenas quando as fórmulas adicionais forem simples (valores fixos, cálculos matemáticos diretos ou condicionais sem dependência de médias).

Parâmetro Marcado:

* As fórmulas adicionais são consideradas no cálculo de médias.
* O sistema calcula as médias apenas com base nas regras definidas no parametrizador e nos acordos do sindicato do colaborador.
* Evita recursividade e garante estabilidade na geração de históricos de provisão e cálculos que envolvem médias.
* Observação: eventuais ajustes que o usuário aplicar via fórmula adicional não serão considerados nas médias.

Na execução da rotina de histórico de provisão, existindo uma fórmula adicional, o parâmetro "Ignora fórmulas adicionais no cálculo de médias" deverá ser marcado, pois haverá um controle se as fórmulas adicionais cadastradas no **Parametrizador** devem ou não ser consideradas na composição das médias utilizadas em processos da Folha de Pagamento, tais como:

* Cálculo de férias
* Cálculo de 13º salário
* Geração de provisões
* Histórico de provisões

Dito isso, é importante se atentar para as recomendações sobre as fórmulas adicionais:

* Utilizar fórmulas adicionais apenas para complementos pontuais e cálculos diretos.
* Evite inserir funções de médias dentro de fórmulas adicionais, especialmente quando utilizadas em provisões.
* Sempre que houver necessidade de considerar médias complexas, configurar diretamente no parametrizador ou via regras sindicais, em vez de fórmulas adicionais.
* Para cenários onde seja imprescindível manter fórmulas adicionais que chamam funções de médias, é obrigatório marcar a flag "Ignora fórmulas adicionais no cálculo de médias".

Por fim, entende-se que o parâmetro "Ignora fórmulas adicionais no cálculo de médias" garante segurança no processo de cálculo, evitando falhas de execução por recursividade, e quando levamos em conta os cálculos feitos com o parâmetro marcado ou desmarcado, temos

* Marcado: cálculos mais seguros, porém sem fórmulas adicionais influenciando as médias.
* Desmarcado: maior flexibilidade, porém com risco de erro se houver uso inadequado de funções de médias em fórmulas adicionais.

**Recalcula dias trabalhados quando dias de direito for maior que o já existente no envelope**

Quando o funcionário tem férias ou afastamento o cálculo dos dias trabalhados ou horas normais são fracionadas na proporção para completar o mês trabalhado, mas nesse período pode ser cancelado tanto férias como afastamento, por exemplo ter sido cadastrado em funcionário indevido, então quando o parâmetro estiver marcado o cálculo retornando o valor de dias de direito será feito no recálculo do movimento.

Quando o parâmetro estiver desmarcado, o cálculo continua não recalculando o evento de dias trabalhados ou horas normais. E caso seja necessário, nesse caso, o recálculo do evento deve-se retirar a referência e horas do evento e recalcular o movimento.

**Considera a dedução de dependente somente até o mês de aniversário**

Se esse parâmetro estiver desmarcado o sistema processará o cálculo do dependente do IRRF de acordo o processo do Governo (DIRF), onde o dependente é considerado o ano inteiro para dedução de IRRF.

* filho(a) ou enteado(a), até 21 anos de idade, ou, em qualquer idade, quando incapacitado física ou mentalmente para o trabalho;
* filho(a) ou enteado(a), se ainda estiverem cursando estabelecimento de ensino superior ou escola técnica de segundo grau, até 24 anos de idade;

Marcando esse parâmetro o sistema desmarca automaticamente o campo incidência 'IRRF' na Liberação de Competência, para o Grau de Parentesco '1-Filho(a) Válido' ou 'D-Enteado(a)' observando:  
a) se o dependente tem mais de 21 anos de idade ou  
b) se o dependente é universitário e tem mais de 25 anos;

Lembrando que, no cálculo do IRRF o sistema sempre verifica o caixa para pagamento, e caso o caixa seja para o próximo mês, e o dependente complete 21 ou 25 anos no próximo mês, este será desconsiderado.

**Exemplo:**

PARÂMETRO MARCADO “Considera a dedução de dependente somente até o mês de aniversário”

02 DEPENDENTES:

TATIANA - 11/11/1999 - 22 ANOS - INC IRRF MARCADO - UNIVERSITÁRIO DESMARCADO

ROGERIO - 04/12/1999 - 21 ANOS - INC IRRF MARCADO - UNIVERSITÁRIO DESMARCADO

Cálculo da folha do mês 11/2021 e caixa 12/2021 – considera apenas um dos dependentes porque o primeiro completa 22 anos na competência atual e o pagamento é no mês caixa que é o próximo mês.

Cálculo de férias data de pagamento 11/11/2021 para o período de gozo 15/11/2021 a 29/11/2021 – considera os dois dependentes porque a competência de pagamento é a atual e o dependente completa 22 anos durante o mês atual.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[<< Retornar para **Folha Normal**](http://tdn.totvs.com.br/display/LRM/Folha+Normal)
