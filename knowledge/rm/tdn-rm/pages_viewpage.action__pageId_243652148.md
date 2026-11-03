---
content_hash: 3dcf7f11171f482f237092789d3df081c0cc19e3477d0aa9594ac50ea4fad22b
fetched_at: '2026-06-29T00:08:12.862734+00:00'
page_id: '243652148'
product: rm
source: tdn-rm
title: Formatação (Passo a Passo)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243652148
version: 27
---

# Índice:

---

.\*ndice:

# Como Funciona:

---

Como exemplo usaremos o **Relatório TesteFormatação .** Existem 3 campos nesse relatório:

* **CHAPA**
* **NOME**
* **SALÁRIO**

Iremos utilizar o campo **SALÁRIO** como base para a explicação sobre a formatação. Observe a imagem abaixo e perceba que o campo **SALÁRIO** está sem formatação.

**Imagem 1 - Relatório TesteFormatação** com campo **SALÁRIO** sem formatação.

# Configurando a Formatação

---

Clicando na **SmartTag** do controle a ser formatado a tela **"Texto Tarefas"** será apresentada.

**Imagem 2 -** Tela **"Texto Tarefas"**.

Clicando em **[...]** na Propriedade Formato do Texto a Tela **"Editor de Formatar Caracter"** será apresentada.

**Imagem 3 -** Tela **"Editor de Formatar Caracter"**.

# Diferentes Categorias de Formatação

---

Fonte de Dados1DataHora

|  |
| --- |
| Formata diferentes valores transformando-os em data (System.DateTime). |

2Número

|  |
| --- |
| Formata diferentes valores transformando-os em numéricos. |

Ao utilizar uma máscara numérica contendo com '#' significa que o dígito é opcional, o que irá representar um vazio quando não houver valores. Para tornar a representação do dígito obrigatória basta utilizar o carácter '0'. Com isso, a posição do dígito sempre será informada.

Abaixo seguem alguns exemplos para simplificar o entendimento.

**Exemplos:**

O número \*012\* com uma das máscaras ('#', '##', '###', '####', '#0', '#00', ... ) resultará em \*12\* (perceba que não é obrigatório exibir o número insignificante '0')

Os números \*012\* ou mesmo o número \*12\* com máscara '000' resultará em \*012\* (perceba que mesmo o número insignificante '0' será exibido pois essa máscara obriga a exibição de 3 dígitos)

3Porcento

|  |
| --- |
| Formata os valores numéricos transformando-os em valores percentuais. |

4Moeda

|  |
| --- |
| Formata os valores numéricos transformando-os em valores monetários (acompanhados ou não, dos símbolos monetários). |

5Especial

|  |
| --- |
| Tipos especiais de Formatação, como telefone, cpf, cnpj, entre outros. |

6Geral

Utiliza prefixos e sufixos para gerar a máscara de formatação à ser utilizada.

falseLinks Auxiliares

Links que podem auxiliar no entendimento da funcionalidade:

* [Microsoft - Propriedade máscara](https://msdn.microsoft.com/library/system.windows.forms.maskedtextbox.mask(v=vs.110).aspx).
* [Tipos de Formatação](https://documentation.devexpress.com/#CoreLibraries/DevExpressUtilsFormatTypeEnumtopic)
* [Especificadores de Formato](https://documentation.devexpress.com/#WindowsForms/CustomDocument2141)

# Aplicando a Formatação

---

]]>

Ao escolher o tipo de Formatação, por exemplo, **Formato Monetário {0:c2}**, ao gerar o relatório o mesmo será devidamente aplicado.

]]>

**Imagem 10 -** Escolhendo o formato que será aplicado no controle.

**Imagem 11 - Relatório TesteFormatação** com campo **SALÁRIO** devidamente formatado.

# Restrições da Funcionalidade e Usos Inadequados

---

* **Não existe** implementação, hoje, no Reports **que possibilite, a formatação de vários controles ao mesmo tempo**.
* Existe uma funcionalidade chamada **SUMÁRIO,** disponibilizada ao escolher mais de um controle, onde uma de suas propriedades também é **"Formato de texto",** porém ela é **utilizada internamente nos cálculos** à ser realizado pelo **SUMÁRIO,** ela **não tem ligação direta** com a propriedade de mesmo nome disponibilizada individualmente em cada controle, explicada acima, no passo a passo.

**Imagem 12 -** Propriedade **"Formato do Texto"** do Sumário.

* A formatação de texto deverá ocorrer individualmente para cada controle.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Formatação

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**

<http://tdn.totvs.com/x/kIcpE>
