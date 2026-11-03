---
content_hash: 4119b75a37f5916088cbb0e417db4580c74ccfe06ae8e4084c802ea7e03ab1ad
fetched_at: '2026-06-29T00:05:58.373334+00:00'
page_id: '185755635'
product: rm
source: tdn-rm
title: Processo de vínculo de tipos de ocorrências customizadas (Código de cálculo
  0043)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185755635
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | Totvs Automação   de Ponto Versão: 12.1.1 ou Superior |
| **Processo** | : | Tipo de   ocorrência |
| **Subprocesso** | : | Uso de ocorrência   customizada com CC 0043 |

Visando maior flexibilidade e melhor usabilidade para o usuário, foi criado um cadastro onde será possível cadastrar tipos de ocorrências customizadas, específicos ao seu escopo de trabalho. Com o auxílio do código de cálculo 0043 será possível realizar cálculos vinculando ocorrências customizadas o que facilitará a criação de controles mais apurados em relação as ocorrências geradas para os funcionários.

Para isso são necessárias algumas parametrizações conforme exemplo a seguir:

Foi cadastrado duas ocorrências de débito, tipo atraso e falta, essas ocorrências customizadas serão consideradas nos cálculos do sistema.

O mesmo conceito pode ser aplicado a qualquer tipo de ocorrência (Débito ou Crédito).

Exemplo:

**1º Passo:** Acessar Configurações | Tipos de ocorrência. Criar as duas ocorrências.

Falta customizada:

Atraso customizado:

Obs.: De acordo com conceito do sistema caso o funcionário tenha um atraso que seja igual o valor da jornada diária está será considerada como Falta. No entanto, é necessário (caso use ocorrências customizadas) informar o evento de falta criado no campo “Transforma em falta” conforme acima.

O campo código das ocorrências customizadas são sempre precedidas de “#”. As ocorrências nativas do sistema são inalteráveis.

**2º Passo:** Associar as ocorrências criadas a eventos para utilização no sistema.

**Débito ou Crédito:** Determina se o código de cálculo do evento é de crédito ou débito. Essa informação é importante para definir a atitude do evento: pagar, descontar ou compensar, para o movimento e para o banco de horas.

Importante: Realizar a associação da ocorrência criada através do menu Anexos| Evento por tipo de ocorrência.

**3º Passo:** Acessar o sindicato do funcionário e realizar a associação dos eventos criados:

**4º Passo**: Associar a ocorrência no horário do funcionário. Nessa etapa, o usuário poderá determinar em que momento o sistema usará a ocorrência customizada verificando através do horário utilizado pelo funcionário. A associação é feita em Cadastro | Horário por Intervalo. Marcar o parâmetro: “Determinar o tipo de ocorrência a ser gerada”. É possível realizar essa parametrização por jornada do funcionário.

Clicar no pequeno quadrado após   para localizar as ocorrências.

Feita essa parametrização é possível verificar que atrasos (e consequentemente faltas) geradas no espelho do funcionário assumirão as ocorrências criadas e parametrizadas. Observe que existe falta e atraso calculados no espelho do funcionário:

Ao verificar as ocorrências percebe-se que essas estão conforme as novas ocorrências criadas:

Observação: O total de horas referente a ocorrências customizadas serão demonstradas também no resumo lateral do espelho de ponto.

Conforme a parametrização realizada na ocorrência será possível tratar as ocorrências da mesma maneira que as demais ocorrências nativas do sistema são manipuladas. Essa parametrização permite que o usuário possa criar de forma personaliza as suas ocorrências e também realizar tratamentos como abonos, compensação, tolerâncias e até mesmo para compensação de banco de horas.

Para maiores informações sobre o lançamento das horas customizadas para o banco de horas acesse.: [Código de cálculo 0043 X Banco de Horas X Alteração Atitude](https://tdn.totvs.com/pages/viewpage.action?pageId=728647367).
