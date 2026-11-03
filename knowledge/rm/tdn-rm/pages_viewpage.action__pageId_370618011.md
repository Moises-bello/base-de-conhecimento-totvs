---
content_hash: 77fbc9246d759554252850b0c654bc6bb4cae7515af0e79a199c6035ed0bb625
fetched_at: '2026-06-29T00:09:01.002568+00:00'
page_id: '370618011'
product: rm
source: tdn-rm
title: Como funciona a vinculação do índice de horário no S-2200 e S-2206?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370618011
version: 11
---

---

Iremos demonstrar nessa FAQ como o sistema faz a montagem do grupo <horario> no XML, além de detalhar a vinculação da tag <dia> com os índices cadastrados no horário.

A vinculação do índice de horário no S-2200 e S-2206 se comportará de formas diferentes de acordo com o parâmetro "Considerar o Cadastro de Jornada na geração dos eventos (S-2200 e S-2206)" existente na etapa "Configurações Gerais 3/5" do parametrizador do eSocial.

1true1Parâmetro marcadoParâmetro habilitado

O grupo "horario" será criado com base no cadastro de jornada do horário, ou seja, será feita a vinculação das colunas Índice → Dia, conforme exemplo abaixo:

No eSocial, quando for gerar o XML, a Segunda-Feira corresponde a 1, ou seja:

|  |  |
| --- | --- |
| 1 | Segunda-Feira |
| 2 | Terça-Feira |
| 3 | Quarta-Feira |
| 4 | Quinta-Feira |
| 5 | Sexta-Feira |
| 6 | Sábado |
| 7 | Domingo |

Já que o XML não leva dias de descanso (índice 6 e 7), a geração ficaria da seguinte forma:

* A criação se inicia do primeiro Índice do horário.
* A tag preenchida com I (Horário por Intervalo) | 0005 (Código do Horário) | 1 (Índice)

| Dia (<dia>) | Índice (<codHorContrat>) |
| --- | --- |
| 6 | I|0005|1 |
| 7 | I|0005|2 |
| 1 | I|0005|3 |
| 2 | I|0005|4 |
| 3 | I|0005|5 |

**Observação:** O comportamento explicado acima será feito para os eventos S-2200 (Carga Inicial/Admissão) e S-2206.

2Parâmetro desmarcadoParâmetro desabilitado3true1S-2200 - Carga InicialS-2200 - Carga Inicial

Caso a data de admissão seja inferior a data de inicio da obrigatoriedade dos eventos não periódicos, o sistema irá considerar o registro que possua a data anterior mais próxima do inicio da obrigatoriedade dos eventos não periódicos.

**Exemplo:** Data de admissão do funcionário é   e o inicio de obrigatoriedade dos eventos não periódicos parametrizada no sistema é . Ao buscar no histórico, será considerado que possui a data .

O grupo referente a tag "<horario>" será criado com base na data de mudança do histórico, ou seja, será feita a vinculação do Índice → Dia da Data Mudança do Horário.

Após a verificação acima, sabemos que no dia da admissão do funcionário **a jornada que se refere a uma segunda-feira é a de Índice 1**.

No eSocial, quando for gerar o XML, a Segunda-Feira corresponde a 1, ou seja:

|  |  |
| --- | --- |
| 1 | Segunda-Feira |
| 2 | Terça-Feira |
| 3 | Quarta-Feira |
| 4 | Quinta-Feira |
| 5 | Sexta-Feira |
| 6 | Sábado |
| 7 | Domingo |

Já que o XML não leva dias de descanso (Índice 6 e 7), a geração ficará da seguinte forma:

* + A criação se inicia do primeiro Índice do horário.
  + A tag preenchida com I (Horário por Intervalo) | 0002 (Código do Horário) | 1 (Índice)

| Dia (<dia>) | Índice (<codHorContrat>) |
| --- | --- |
| 1 | I|0005|1 |
| 2 | I|0005|2 |
| 3 | I|0005|3 |
| 4 | I|0005|4 |
| 5 | I|0005|5 |

No XML:

2S-2200 - AdmissãoS-2200 - Admissão

O grupo referente a tag "<horario>" será criado com base na data de admissão do funcionário, ou seja, será feita a vinculação do Índice → Dia da Data de Admissão, conforme exemplo abaixo:

Podemos notar que a data de admissão do funcionário é  – Segunda-Feira.

O índice que será utilizado como base para a vinculação "Índice → Dia Data de Admissão" será recuperado no histórico de horário do funcionário, **onde será utilizado o registro referente a data de admissão**.

Após a verificação acima, sabemos que no dia da admissão do funcionário **a jornada que se refere a uma segunda-feira é a de Índice 1**.

No eSocial, quando for gerar o XML, a Segunda-Feira corresponde a 1, ou seja:

|  |  |
| --- | --- |
| 1 | Segunda-Feira |
| 2 | Terça-Feira |
| 3 | Quarta-Feira |
| 4 | Quinta-Feira |
| 5 | Sexta-Feira |
| 6 | Sábado |
| 7 | Domingo |

Já que o XML não leva dias de descanso (Índice 6 e 7), a geração ficará da seguinte forma:

* A criação se inicia do primeiro Índice do horário.
* A tag preenchida com I (Horário por Intervalo) | 0002 (Código do Horário) | 1 (Índice)

| Dia (<dia>) | Índice (<codHorContrat>) |
| --- | --- |
| 1 | I|0002|1 |
| 2 | I|0002|2 |
| 3 | I|0002|3 |
| 4 | I|0002|4 |
| 5 | I|0002|5 |

No XML:

Caso **não exista** histórico de horário referente a data de admissão o sistema irá considerar o horário/índice vinculado no cadastro do funcionário.

Sendo assim, o Índice (Letra) será relacionada ao dia da semana que o funcionário foi admitido.

Já que o XML não leva dias de descanso (Índice 6 e 7), a geração ficará da seguinte forma:

* A criação se inicia do primeiro Índice do horário.
* A tag preenchida com I (Horário por Intervalo) | 0007 (Código do Horário) | 1 (Índice)

| Dia (<dia>) | Índice (<codHorContrat>) |
| --- | --- |
| 1 | I|0007|1 |
| 2 | I|0007|2 |
| 3 | I|0007|3 |
| 4 | I|0007|4 |
| 5 | I|0007|5 |

3S-2206Carga Inicial

Para os casos em que ocorrer a mudança de horário após o inicio da obrigatoriedade dos eventos não periódicos, o arquivo XML S-2206 será gerado com base na data de mudança, onde é feita a vinculação do Índice → Dia da Data Mudança do Horário.

**Exemplo:**

Foi feita a mudança do horário na data de mudança.

Ao buscar no histórico, será considerado que possui a data .

Após a verificação acima, sabemos que no dia da admissão do funcionário **a jornada que se refere a uma segunda-feira é a de Índice 1**.

No eSocial, quando for gerar o XML, a Segunda-Feira corresponde a 1, ou seja:

|  |  |
| --- | --- |
| 1 | Segunda-Feira |
| 2 | Terça-Feira |
| 3 | Quarta-Feira |
| 4 | Quinta-Feira |
| 5 | Sexta-Feira |
| 6 | Sábado |
| 7 | Domingo |

Já que o XML não leva dias de descanso (Índice 6 e 7), a geração ficará da seguinte forma:

* + A criação se inicia do primeiro Índice do horário.
  + A tag preenchida com I (Horário por Intervalo) | 0002 (Código do Horário) | 1 (Índice)

| Dia (<dia>) | Índice (<codHorContrat>) |
| --- | --- |
| 1 | I|0003|1 |
| 2 | I|0003|2 |
| 3 | I|0003|3 |
| 4 | I|0003|4 |
| 5 | I|0003|5 |

No XML:

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |
| 12.1.19 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autor:**
