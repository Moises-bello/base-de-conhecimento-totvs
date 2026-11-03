---
content_hash: ceca63da01050d0eb46608b51ad4d190a823bf01a67aab4295c358b6ea48acf7
fetched_at: '2026-07-02T19:24:26.025140+00:00'
page_id: '519714933'
product: protheus
source: tdn-tec
title: 10.7. Autocompletar (Autocomplete)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519714933
version: 2
---

# Introdução

Para auxiliar os desenvolvedores na escrita de código, dentro dos editores do TDS é possível solicitar que o sistema mostre as possíveis propostas para o contexto em que o cursor se encontra, auxiliando o usuário ao informar quais os possíveis trechos de códigos cadastrados podem ser utilizados onde o cursor se encontra.

# Como Utilizar

 Para utilizar a funcionalidade, por padrão, basta pressionar junto as teclas CTRL + Espaço.

*Observação: Os botões CTRL+Espaço podem ser alterados para qualquer outra tecla de atalho, caso a funcionalidade não apresente o resultado esperado certifique-se de estar utilizando o comando correto.*

```
Figura 1: Editor ao solicitar a apresentação de propostas.
```

Algumas das propostas serão apresentadas somente se o *parser* do IDE estiver ativo, como as funções, métodos, variáveis e propriedades declaradas dentro do arquivo. Para saber mais sobre o *parser* do IDE consulte a página ["Perguntas e Respostas"](http://tdn.totvs.com/x/wICBAg) no tópico 6 ( "Ao editar fontes grandes, apresenta lentidão na digitação" ) .

Caso o usuário esteja conectado a um RPO, ao solicitar novamente o auxílio do autocompletar serão apresentadas as funções disponíveis no RPO.

```
Figura 2: Editor ao solicitar a apresentação de propostas pela segunda vez.
```

Para filtrar as propostas apresentadas basta digitar as iniciais do código desejado logo após ativar a funcionalidade. Também é possível digitar as iniciais antes de ativar a funcionalidade e deverá ser apresentada a janela de propostas já filtrada.

```
Figura 3: Editor ao solicitar a apresentação de propostas filtradas com a cadeia de caracteres "aa".
```

Ao pressionar a tecla Enter ou ao realizar o duplo-clique em cima da proposta desejada será adicionado automaticamente um trecho de código, note que em alguns casos partes do código adicionado terá um quadrado em volta. Este quadrado é um auxiliador que indica quais são as partes que precisam ser customizadas com as peculiaridades de cada programa, por exemplo, uma função que necessita o preenchimento de três argumentos apresentará o quadrado em volta de cada um destes três argumentos.

```
Figura 4: Editor ao selecionar uma proposta que contém trechos customizáveis.
```

Para posicionar o cursor em cima do próximo argumento basta pressionar a tecla TAB do teclado.

# Configuração

A apresentação das propostas pode ser configurada entrando em Janela -> Preferências -> AdvPL / 4GL -> Aparência -> Sequência de Ordenação.

```
Figura 5: Página de preferências "Sequência de Ordenação"
```

Nesta tela é possível selecionar se você deseja que as propostas sejam apresentadas em ordem alfabética ou de forma customizada por tipo.
