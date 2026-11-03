---
content_hash: 73c1f8a6e15c7be1ded88a446775b57dfd9f5be903cf1ffa8561d6ea80baa30f
fetched_at: '2026-06-29T00:09:50.762630+00:00'
page_id: '435110514'
product: rm
source: tdn-rm
title: Como processar a distribuição para tomadores de serviços em retificações?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435110514
version: 8
---

# Objetivo:

---

       O objetivo deste documento informar como será a distribuição para tomadores de serviços de retificação da rescisão e folha de pagamento em meses anteriores.

---

1true1Regras geraisRegras gerais

Será distribuída a retificação conforme regras abaixo:

1. Competência atual – distribuição conforme rateio de tomadores cadastrados no anexo do funcionário.
2. Competências anteriores – distribuição referente ao período da retificação que deverá ser entre 10000 e 30000.
3. Histórico de Tomador – distribuição conforme histórico do rateio de tomadores cadastrados no anexo do funcionário. Neste caso existe a possibilidade de geração deste histórico com o processo “Conversor Histórico Rateio Tomador” em Configurações.

O parâmetro “Distribuição de Retificação de Folha” habilitará o Rateio por tomador quando a competência for anterior ao mês atual. Neste caso poderá ser utilizado o rateio para períodos que não sejam de retificação com o parâmetro desmarcado e para períodos que sejam de retificação com o parâmetro marcado.

Caso já exista distribuição para o período, o sistema não irá distribuir e apresentará mensagem no log.

Na competência atual, quando selecionado o período 10000 não habilitará as informações:

* Distribuição de Retificação de Folha
* Rateio tomador por

Na competência anterior, quando selecionado o período 10000 habilitará as informações “Distribuição de Retificação de Folha”, “Rateio tomador por” e “Histórico de Tomador” com a opção de distribuir pelo rateio de tomadores cadastrados no anexo do funcionário rateio de tomador atual ou seguindo o rateio de eventos ou pelo rateio de tomadores cadastrados no histórico de rateio de tomador no anexo do funcionário:

Selecionando “Tomadores da Competência Atual”, o rateio de tomador que a distribuição do período da retificação de rescisão seguirá será o mesmo que estiver cadastrado no anexo “Rateio Tomador” do funcionário.

Selecionando “Rateio de eventos” deverá ter cadastrado em “Rateio de Eventos” o rateio de tomador que a distribuição do período da retificação de rescisão seguirá.

Selecionando “Histórico de Tomador”, o rateio de tomador que a distribuição do período da retificação seguirá será o mesmo que estiver cadastrado no anexo “Histórico de Rateio por Tomador” do funcionário.

2Exemplo 1 - Retificação de rescisãoExemplo 1 - Retificação de rescisão

Supondo que havia um evento a ser pago de Reembolso de vale transporte. A rescisão deverá ser retificada e este valor será rateado entre os tomadores de serviço após o cálculo da rescisão complementar de retificação.

Na rescisão original foi calculado um evento de dias trabalhados de código ‘0002’, que foi distribuído para três tomadores cadastrados na época da distribuição da rescisão.

Será utilizado este mesmo rateio para a distribuição do período da retificação da rescisão. Para isso acesse:

Cadastre:

Feito o cadastro acesse a distribuição do Sefip:

Será feito o rateio na mesma proporção do rateio do evento ‘0002’ sendo que os valores ficarão da seguinte forma:

C00001 = 25% de 600,00 = 150,00

C00001 = 50% de 600,00 = 300,00

C00001 = 25% de 600,00 = 150,00

**Observações:**

01 - Para o parâmetro Tomadores da Competência atual, a distribuição será processada conforme rateio de tomadores cadastrados no anexo do funcionário. Ou seja, a distribuição será processada com o cadastro atual do funcionário em dias.

02 – Quando não houver tomador discriminado será considerado o tomador empresa cadastrado no parametrizador.

3Exemplo 2 - Retificação de folhaExemplo 2 - Retificação de folha

Feito a retificação do envelope de pagamento do mês de setembro de 2017, para realizar o lançamento de um valor de vinte horas de horas extras.

No envelope original foi calculado um evento de Hora aula - sistema de informação de código ‘0255’, que foi distribuído para dois tomadores cadastrados no período. 

Será utilizado este mesmo rateio para a distribuição do período da retificação da rescisão. Para isso acesse:

Cadastre:

Feito o cadastro acesse a distribuição do Sefip:

Será feito o rateio na mesma proporção do rateio do evento ‘0255’ sendo que os valores ficarão da seguinte forma:

C00003 = 16,66% de 583,00 = 97,24

RM = 83,33% de 583,00= 486,09

**Observações:**

01 - Para o parâmetro Tomadores da Competência atual, a distribuição será processada conforme rateio de tomadores cadastrados no anexo do funcionário. Ou seja, a distribuição será processada com o cadastro atual do funcionário em dias.

02 – Quando não houver tomador discriminado será considerado o tomador empresa cadastrado no parametrizador.

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.23 |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |

falsefalse

**Status: Finalizado**

false

**Data:**

false

**Autor: Andreia Barbosa**
