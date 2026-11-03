---
content_hash: b11753a515daba3708e8c9c3da76d599d2c7d8343313d8d1ac5a091ae1c6996e
fetched_at: '2026-06-29T00:05:55.341871+00:00'
page_id: '134153344'
product: rm
source: tdn-rm
title: Parametrização de múltiplos vínculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=134153344
version: 2
---

# Múltiplos Vínculos

FAQ: **Parametrização de múltiplos vínculos**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.5x e superiores |

Este processo tem o objetivo de tratar o cálculo de IRRF para as pessoas que tiverem mais de um vínculo na mesma coligada e o cálculo de INSS para as pessoas que tiverem mais de um vínculo considerando todas as coligadas.

Sempre que se tratar de funcionário com múltiplos vínculos, é possível informar a chapa centralizadora para desconto do IRRF/INSS, e a coligada centralizadora para desconto do INSS, onde somente os funcionários centralizadores sofreram os devidos descontos.

É possível também parametrizar para que no cálculo de um funcionário o sistema verifique as bases das demais chapas, porém cada chapa terá seu desconto de INSS e IRRF.

Para isso é necessário marcar o parâmetro ‘Calcula IRRF/INSS de múltiplos vínculos sem chapa centralizadora’ existente em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros II.

Somente é permitido definir uma única coligada como centralizadora de INSS, e apenas uma chapa por coligada poderá ser definida como centralizadora de IRRF e/ou INSS.

Uma vez que uma das chapas é marcada para uma ‘Pessoa’, a alteração é realizada em todas as coligadas.

Caso nenhuma chapa seja marcada, não será caracterizado múltiplos vínculos e o cálculo será realizado normalmente.

Uma vez que marcar uma chapa para uma ‘Pessoa’ o usuário deverá obrigatoriamente preencher todas as informações para todas as coligadas, conforme regras abaixo:

**1) INSS**

* Quando na coligada centralizadora existir mais de uma chapa, será obrigatório definir a chapa centralizadora de INSS/IRRF.

* Quando na coligada centralizadora existir apenas uma chapa, ao marcar a coligada o sistema automaticamente irá marcar a chapa, e se o usuário desmarcar a chapa, automaticamente o sistema irá desmarcar a coligada;

* Quando existir mais de uma coligada e o usuário marcar mais de uma chapa sem selecionar a coligada centralizadora, o sistema irá exigir que o usuário selecione a coligada centralizadora de INSS.

**Observação I:**

No processo “Definição da(s) chapa(s) e coligada centralizadora(s) de IRRF/INSS” serão apresentadas apenas as chapas do funcionário com situação <>D-demitido.

**Observação II:**

Quando a coligada estiver parametrizada para utilizar chapa centralizadora, ou seja, o parâmetro ‘Calcula IRRF/INSS de múltiplos vínculos sem chapa centralizadora’ existente em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros II estiver desmarcado, o sistema irá verificar os dependentes de IRRF da chapa centralizadora, onde será realizado o desconto.

Porém quando o parâmetro estiver marcado, mesmo o sistema verificando a base de todas as chapas da mesma pessoa, na verificação dos dependentes de IRRF o sistema sempre irá buscar os dependentes da chapa corrente, ou seja, a chapa onde esta sendo realizado o cálculo.

**Observação III:**

Este processo somente estará disponível quando o parâmetro parâmetro ‘Calcula IRRF/INSS de múltiplos vínculos sem chapa centralizadora’ existente em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros II estiver desmarcado.

*Exemplo:*

No exemplo acima, o desconto de INSS da pessoa FUNCIONARIO será realizado apenas na coligada 6, chapa 006002000327.

**2) IRRF**

Já o desconto de IRRF, por ser separado por coligada, será realizado nas chapas 006002000327 e 007002000127.

Para utilizar o cálculo de INSS e IRRF múltiplos vínculos, é necessário fazer o cadastro de eventos do com os seguintes códigos de cálculos:

**305** - IRRF FOLHA BASE PENSÃO

**306** - IRRF FÉRIAS RECIBO BASE PENSÃO

**307** - IRRF 13º SALÁRIO BASE PENSÃO

**308** - IRRF PARTICIPAÇÃO NOS LUCROS BASE PENSÃO

**316** - IRRF FÉRIAS ENVELOPE BASE PENSÃO

**Atenção!**Estes novos códigos de cálculos serão utilizados no cálculo da pensão alimentícia. Deverão ser cadastrados com o tipo ‘Base de cálculo’ e com as mesmas incidências dos eventos de desconto correspondes (4 - IRRF, 30 - IRRF Férias, 49 - IRRF 13º Salário, 127 - IRRF Partic. nos Lucros, 61 - IRRF Férias Envelope).

**Observação I:**Estes eventos somente serão lançados quando o evento de pensão alimentícia for lançado e seu valor for diferente de zero.

**Observação II:**Quando existir fórmula no evento que contém o código de cálculo 4, o sistema não irá lançar automaticamente estes códigos de cálculos.

**302** - Base de IRRF Folha Outros Vínculos

**303** - Base de IRRF 13º Salário Outros Vínculos

**304** - Base de IRRF Participação Lucros Outros Vínculos

**317** - Base de IRRF Férias Recibo Outros Vínculos

**318** - Base de IRRF Férias Envelope Outros Vínculos

**Atenção!**Estes novos códigos de cálculos deverão ser cadastrados com o tipo ‘Base de cálculo’. No vínculo centralizador de IRRF, serão lançados os eventos com os códigos de cálculo acima com a base de IRRF dos outros vínculos para auxiliar na conferência do cálculo do IR descontado.

---

**Pensão Alimentícia**

Apesar de existir uma chapa única escolhida para o desconto do IRRF/INSS, entende-se que para efeito do cálculo de pensão alimentícia esta regra não é válida, pois podem ocorrer situações onde seja determinado judicialmente que o recolhimento de pensão seja realizado somente em um vínculo da pessoa.

Sendo assim, os valores dos rendimentos sujeitos ao recolhimento de pensão, os valores de IRRF a serem utilizados como deduções e o desconto final da pensão devem ser específicos para cada chapa.

Para tratar esta situação, mesmo que uma determinada chapa não seja centralizadora de desconto de IRRF, serão lançados eventos do tipo base de cálculo com o valor do IRRF que deveria ser descontado na chapa.

Quando o parâmetro ‘Calcula IRRF/INSS de múltiplos vínculos sem chapa centralizadora’ estiver desmarcado, na chapa centralizadora, serão lançados os eventos do tipo base e os eventos de desconto de IRRF, caso contrário estes eventos não serão lançados.

Os dependentes de pensão, da mesma forma que já funciona hoje, poderão ser cadastrados tanto na chapa centralizadora, quanto nas demais chapas para o calculo do “IRRF Dedução Pensão”.

**INSS**

Para atender a legislação previdenciária (IN 03/2005), onde ordena que se o empregado tem mais de um vínculo, os pagamentos das suas contribuições devem obedecer ao teto do salário de contribuição, serão disponibilizadas duas maneiras para o sistema calcular o INSS quando existir mais de uma chapa vinculada a mesma ‘Pessoa’. Sendo elas:

a)    Considerar automaticamente todas as chapas da ‘Pessoa’ em todas as coligadas, e o desconto será realizado apenas na coligada e chapa definida como centralizadora.

b)    Considerar automaticamente todas as chapas da ‘Pessoa’ em todas as coligadas, e o desconto será realizado individualmente, cada chapa terá o seu desconto.

**IRRF**

Quando a ‘Pessoa’ tiver mais de uma chapa na mesma coligada, o IRRF será calculado considerando todas as bases de IRRF na coligada corrente, devido se tratar da mesma fonte pagadora, e o desconto será realizado apenas na chapa definida como centralizadora.

**Atenção!**Os eventos de desconto de IRRF irão considerar apenas os dependentes cadastrados na chapa centralizadora.

**Cálculo de Rescisão e Diferenças**

Ao calcular rescisão ou diferenças para funcionários com múltiplos vínculos, o sistema deverá fazer o lançamento de INSS e IRRF apenas na chapa centralizadora.

**Observação!**Para que o INSS por dissídio seja lançado corretamente, é necessário sempre processar a diferença por dissídio para a chapa centralizadora de INSS, independente de ter aumento salarial.

**Cálculo de Férias**

Para cálculo das férias, é regra que todas as chapas (vinculadas e centralizadora) tenham férias cadastradas no mesmo período de gozo.

Quando houver vínculos em outras coligadas, o cálculo das férias deverá ser realizado por último na coligada centralizadora.

---

**Novos códigos de cálculo**

**Cód. Cálculo 305 - IRRF FOLHA BASE PENSÃO**

Base de Cálculo do tipo valor, com as mesmas incidências do evento com cód. de cálculo 4 – IRRF.

O sistema irá fazer o cálculo do IRRF somente com a base do funcionário corrente, da mesma forma que o código de cálculo 4 quando não se utiliza múltiplos vínculos.

Este código de cálculo será utilizado no cálculo da pensão alimentícia quando o funcionário utilizar múltiplos vínculos.

**Cód. Cálculo 306 - IRRF FÉRIAS RECIBO BASE PENSÃO**

Base de Cálculo do tipo valor, com as mesmas incidências do evento com cód. de cálculo 30 - IRRF Férias.

O sistema irá fazer o cálculo do IRRF Férias somente com a base do funcionário corrente, da mesma forma que o código de cálculo 30 quando não se utiliza múltiplos vínculos.

Este código de cálculo será utilizado no cálculo da pensão alimentícia de férias quando o funcionário utilizar múltiplos vínculos.

**Cód. Cálculo 307 - IRRF 13º SALÁRIO BASE PENSÃO**

Base de Cálculo do tipo valor, com as mesmas incidências do evento com cód. de cálculo 49 - IRRF 13º Salário.

O sistema irá fazer o cálculo do IRRF 13º somente com a base do funcionário corrente, da mesma forma que o código de cálculo 49 quando não se utiliza múltiplos vínculos.

Este código de cálculo será utilizado no cálculo da pensão alimentícia de 13º quando o funcionário utilizar múltiplos vínculos.

**Cód. Cálculo 308 - IRRF PARTICIPAÇÃO NOS LUCROS BASE PENSÃO**

Base de Cálculo do tipo valor, com as mesmas incidências do evento com cód. de cálculo 127 - IRRF Partic. nos Lucros.

O sistema irá fazer o cálculo do IRRF PLR somente com a base do funcionário corrente, da mesma forma que o código de cálculo 127 quando não se utiliza múltiplos vínculos.

Este código de cálculo será utilizado no cálculo da pensão alimentícia de PLR quando o funcionário utilizar múltiplos vínculos.

**Cód. Cálculo 316 - IRRF FÉRIAS ENVELOPE BASE PENSÃO**

Base de Cálculo do tipo valor, com as mesmas incidências do evento com cód. de cálculo 61 - IRRF Férias Envelope.

O sistema irá fazer o cálculo do IRRF Férias somente com a base do funcionário corrente, da mesma forma que o código de cálculo 61 quando não se utiliza múltiplos vínculos.

Este código de cálculo será utilizado no cálculo da pensão alimentícia de férias quando o funcionário utilizar múltiplos vínculos.

**Cód. Cálculo 302 - BASE DE IRRF FOLHA OUTROS VÍNCULOS**

Base de Cálculo do tipo valor.

Este código de cálculo será lançado no vínculo centralizador de IRRF com a base de IRRF dos outros vínculos para auxiliar na conferência do cálculo do IR descontado.

**Atenção!**A base será lançada subtraindo os eventos que estornam e deduzem IRRF.

**Cód. Cálculo 303 - BASE DE IRRF 13º SALÁRIO OUTROS VÍNCULOS**

Base de Cálculo do tipo valor.

Este código de cálculo será lançado no vínculo centralizador de IRRF com a base de IRRF 13º dos outros vínculos para auxiliar na conferência do cálculo do IR descontado.

**Atenção!**A base será lançada subtraindo os eventos que estornam e deduzem IRRF 13º.

**Cód. Cálculo 304 - BASE DE IRRF PARTICIPAÇÃO LUCROS OUTROS VÍNCULOS**

Base de Cálculo do tipo valor.

Este código de cálculo será lançado no vínculo centralizador de IRRF com a base de IRRF PLR dos outros vínculos para auxiliar na conferência do cálculo do IR descontado.

**Atenção!**A base será lançada subtraindo os eventos que deduzem IRRF PLR (cód. de cálculo 143).

**Cód. Cálculo 317 - BASE DE IRRF FÉRIAS RECIBO OUTROS VÍNCULOS**

Base de Cálculo do tipo valor.

Este código de cálculo será lançado no vínculo centralizador de IRRF com a base de IRRF Férias dos outros vínculos para auxiliar na conferência do cálculo do IR descontado.

**Atenção!**A base será lançada subtraindo os eventos que estornam e deduzem IRRF Férias.

**Cód. Cálculo 318 - BASE DE IRRF FÉRIAS ENVELOPE OUTROS VÍNCULOS**

Base de Cálculo do tipo valor.

Este código de cálculo será lançado no vínculo centralizador de IRRF com a base de IRRF Férias dos outros vínculos para auxiliar na conferência do cálculo do IR descontado.

**Atenção!**A base será lançada subtraindo os eventos que estornam e deduzem IRRF Férias.
