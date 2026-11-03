---
content_hash: 966fc65f4544da4df41474f1eadb36c98cdb96a730c0b51fea50111101a8e447
fetched_at: '2026-06-29T00:08:57.037293+00:00'
page_id: '353272349'
product: rm
source: tdn-rm
title: Como_Fazer_Aluguel_Reajuste
type: documentation
url: https://tdn.totvs.com/display/LRM/Como_Fazer_Aluguel_Reajuste
version: 1
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Incorporação |
| **Versões:** | 12.1.20 |
| **Módulo** | Aluguel |
| **Ambiente:** | RM |
| **Recurso** | Reajuste |
| **Observações:** | N/A |

# Objetivo

Este documento apresentará de forma simples como realizar o reajuste do módulo de Aluguel

# Definição da Regra de Negócio

Para que seja possível reajustar um contrato de aluguel de um imovel se faz necessário a parametrização do Módulo Totvs Incorporação.

**Pré-condições:**

 1- Ter Parametrizado o Módulo de Aluguel.

2- Ter um Imovel com um contrato de Aluguel atrelado efetivado e com titulos financeiros a vencer.

3- Ter a aba “dados do reajuste” configurado de acordo com o que foi acordado na clausula de reajuste do imovel alugado.

4- Ter incluido os indices da cotação utilizada (IGPM).

5- Efetuar o reajuste e validar o cálculo.

**Passo 1**- Acesse: TOTVS RM/ Projetos/ Incorporação(SGI)/ Aluguel / Contrato de Locação

**Passo 2**- Dentro do Contrato de Locação verifique a data de inicio e termino da vigência do contrato, e a aba dados do reajuste com configuração feita.

**Passo 3**- Verifique o cadastro de cotações e indices e alimente os mesmos de acordo com os indices divulgados mês a mês, no caso iremos trabalhar com o IGPM.

**Passo 4**- Ao chegar no momento adequado proximo ao reajuste do contrato execute a rotina de reajuste, podendo ser a mesma para um ou mais contratos e podendo ser agendada num determinado horário caso o processamento leve muitas horas.

 **Outras formas de aplicação do reajuste**

Na lista de Contratos de Locação selecione 1 ou mais contratos e vá em processos → Aplicar Reajuste

Mesmo que as "datas de proximo reajuste" não sejam a mesma nos contratos selecionados o sistema irá aplicar o reajuste conforme sua respectivas competencias.

**Agendamento de Reajuste**

Para evitar esquecimentos ou falhas, é possivel agendar os reajustes acessando o menu Agendar Reajuste

O agendamento permite selecionar multi Coligadas e ainda informar se o reajuste agendado considera:

* "Mes Atual da Data do Agendamento": reajusta os contratos com "data do proximo reajuste" igual ao mes de execução do agendamento;
* "Mês Proximo a Data do Agendamento":  reajusta os contratos com "data do proximo reajuste" um mes a mais da execução do agendamento;
* "Mês Anterior a Data do Agendamento":  reajusta os contratos com "data do proximo reajuste" um mes a menos da execução do agendamento;

**Passo 5**- Após efetuar o reajuste com sucesso validar o cálculo e concluir que o valor das parcelas foram ajustadas.

O sistema salva uma memória de cálculo utilizada para chegar ao valor da parcela atualizada conforme abaixo:

Data de Reajuste: 01/01/2018

Valor Total Antes do Reajuste: R$ 759,08

Valor Final Antes do Reajuste: R$ 750,00

Índice: IGPM

A cotação cadastrada é o [índice mensal].

Meses de defasagem: 0

Periodicidade (em meses): 12

Variação do período: 1,210916%

Correção Capitalizada: Sim

(1 + 0,0800 / 100)

\* (1 + 0,0100 / 100)

\* (1 + -1,1000 / 100)

\* (1 + -0,9300 / 100)

\* (1 + -0,6700 / 100)

\* (1 + -0,7200 / 100)

\* (1 + 0,1000 / 100)

\* (1 + 0,4700 / 100)

\* (1 + 1,0000 / 100)

\* (1 + 1,0000 / 100)

\* (1 + 1,0000 / 100)

\* (1 + 1,0000 / 100)

Variação Acumulada = 0,0121091645816118256233487508

 Cálculo do Reajuste:

 Imóvel: 1

Valor Mensal Reajustado = (1 + 1,210916%) \* R$ 750,00 = R$ 759,08

 Valor Total Após Reajuste = R$ 759,08

Obs.: Se o contrato tiver mais de um imóvel é a soma do novo valor de aluguel de cada item

Valor Final Após Reajuste = R$ 759,08

Obs.: Se o contrato tiver valor de desconto temos um valor final a ser cobrado

Não posui fórmula associada. Para alterar o cálculo, utilize o parametrizador.

Calculo (Valor total - desconto):

Valor final = 759,0800 - 0,0000

Verificando os titulos financeiros:

**Considerações**

* O reajuste so altera o valor de parcelas já geradas ou não seja, não cria parcelas automaticamente;
* Se alguma parcela que deveria ser reajusta estiver paga ou remetida a banco/ registrada, o sistema não fará a alteração nela. O sistema calculará a diferença (ex: (Valor do Aluguel DEPOIS do reajuste) -Valor do Aluguel ANTES do reajuste → R$10.500,00 -R$10.000,00 = R$ 500,00) e lançará a diferença (500,00) como valor de integração na proxima parcela que estiver em aberto. Este processo é chamado como calculo de resídio e para funcionar deve ter sido parametrizado (parametros da coligada) um valor de integração para residuo.

Mais informações acesse

<http://wikihelp.totvs.com.br/WikiHelp/IMB/IMB.AplicarReajustAlg.aspx>

<http://wikihelp.totvs.com.br/WikiHelp/IMB/IMB.DesfazerReajuste.aspx>
