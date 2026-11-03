---
content_hash: c7193722017482707c9189ba072a36030aad10d58ecee9c149687a289239c368
fetched_at: '2026-06-29T00:10:10.702526+00:00'
page_id: '452719911'
product: rm
source: tdn-rm
title: Retificação da Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719911
version: 13
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Retificação da Folha de Pagamento**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizada**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2306.212
* 12.1.2310.143
* 12.1.2402 e Superiores

## **02. VISÃO GERAL**

Através deste processo é possível realizar a retificação de meses anteriores à folha de pagamento. A retificação será através da digitação de evento(s) que se deseja acrescentar, alterar valor, e/ou quando houver um aumento salarial que não seja por dissídio.

**Observações:**

* O processo de retificação fará o cálculo dos valores de INSS conforme tabela da época.
* Os valores do líquido da diferença calculada serão lançados no período e competência atual para cálculo de IRRF.
* Para funcionários demitidos será calculada a retificação do período anterior a demissão quando ainda estava A - Ativo, para calcular retificação do mês da demissão e de valores pagos após o mês da demissão será necessário usar o módulo de rescisão complementar marcando o parâmetro de retificação.
* Os períodos de lançamento da retificação serão criados sempre na competência a ser retificada e seu cadastro será a partir do número 10000 ou conforme parametrizado no campo "Período Inicial" existente em : Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/6. Caso tenha mais de um período a ser retificado, será necessária a realização do processo novamente, assim como a mudança do número de período de  lançamento da retificação (Exemplo:10001) .
* O período processado fará a retificação para funcionários que estão na seleção e tem esse período na ficha financeira, para os funcionários que não tem o período na ficha financeira não serão selecionados para a retificação.

**Atenção:**

**01 -** Caso o evento já exista no envelope de pagamento, este entrará com o comportamento de "Adicionar" valor.

**Exemplo:**No envelope de pagamento do mês de fevereiro de 2018 consta o evento "0344 - HORA EXTRA 80%" com a quantidade de 10:00 horas. Porém será necessário retificar este evento, pois a quantidade de horas corretas são 15:00 horas. Neste caso deverá digitar a quantidade de 05:00 horas, ou seja, somente o complemento, assim após o cálculo da retificação a quantidade de horas no evento "0344 - HORA EXTRA 80%"será de 15:00 horas. 

**02 -** Os eventos informados na pasta Eventos para Retificação serão calculados para todos os funcionários da seleção de funcionários, ou seja, se o funcionário não tem aquele determinado evento no mês da retificação o mesmo será lançado para o funcionário em questão se existir na pasta Eventos para Retificação.

**Exemplo:**

Funcionários professores recebem os eventos

0253  hora aula - administração

0254  hora aula - direito

0255  hora aula - sistema de informação

Funcionários administrativos recebem o evento

0002   dias trabalhados

Selecionando todos os eventos acima e todos os funcionários da coligada, significa que serão lançados eventos de hora aula para o funcionário administrativo e como esses eventos podem ter o código de cálculo 1 – horas normais significa que o valor a ser lançado nos mesmos será do salário normal do funcionário.

Outro detalhe é que o evento 0082 – hora extra com o valor selecionado de 10 horas também será lançado caso não exista no envelope por ser considerado como soma conforme orientado no **Atenção:** Caso o evento já exista no envelope de pagamento, este entrará com o comportamento de "Adicionar" valor.

**03 -** Caso o sistema esteja parametrizado para pagar o valor do atestado médico sem discriminar, ou seja pago com dias trabalhados e depois de algum tempo o parametrizador foi alterado para discriminar o evento de CC145 - ATESTADO MÉDICO, o sistema não conseguirá fazer a retificação de alteração do envelope original para o CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS devido a alteração de parâmetro do parametrizador. Nesse caso somente será feito se o parametrizador estiver sem o evento de CC145 - ATESTADO MÉDICO.

## **03. EXEMPLO DE UTILIZAÇÃO**

**[Como gerar a retificação da folha de pagamento de meses anteriores?](https://tdn.totvs.com/pages/releaseview.action?pageId=438289252#1-1)**

Outros Links Úteis

eSocial leiaute [S-1200 - Remuneração do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719412)

[DT - S-1200 e S-1210 - Unificação de períodos mediante retificação](https://tdn.totvs.com/pages/releaseview.action?pageId=811714715)

## **04.** **TELA Retificação da Folha de Pagamento**

**Principais Campos e Parâmetros**

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Quebra de Seção | Informar a quebra de seção |
| Seleção de Funcionários | Informar a seleção de funcionários |
| Competência a ser retificada | Informar mês, ano e período que será retificado |
| Período lancto.Retificação | Informar o período que será incluído na ficha financeira para a retificação. Deve ser a partir do período 10000 e que esteja informado no parametrizador / eSocial / Configurações Gerais 5/7 |
| Retificar eventos de afastamento (CC’s 145 e 445) pelo processo automático | Marcar esse parâmetro para que o cálculo da retificação alterando os´códigos de cálculo automaticamente de acordo com a nova marcação do parâmetro “Afastamento pela previdência social” no histórico de afastamento **(DISPONÍVEL A PARTIR DA VERSÃO 12.1.2402)** |

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Incluir / Excluir | Incluir ou excluir linhas na grid para serem retificados de acordo com a seleção. |
| Linha da grid | Informar a seleção de um ou vários eventos para serem retificados. Atenção para informar hora / ref / valor de acordo com o evento selecionado. |

## **05. TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
* PFRETIFICACAOPERIODO
