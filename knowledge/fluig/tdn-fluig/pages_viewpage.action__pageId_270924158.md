---
content_hash: b76f37f290d711cb176771cdcc27f690b5b5075b9f745c1bb64d3721505bed1b
fetched_at: '2026-06-28T21:35:24.594456+00:00'
page_id: '270924158'
product: fluig
source: tdn-fluig
title: Eventos de Formulário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270924158
version: 42
---

## Índice

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é descrever os eventos de formulários avançados no fluig, abordando criar validações e manipulações do seu formulário.

# Pré-requisitos

---

Antes de iniciar, é importante que leia a documentação sobre  e, durante a leitura você vai sentir a necessidade de entender um pouco mais sobre o parâmetro *form* ()

# Como criar eventos de formulário

---

Após a criação de uma definição de formulário é possível realizar a criação de scripts para customização. O eventos para formulários são criados conforme passos a seguir:

0.5falsesamplesfadetrue1Passo1

* Para a criação de um script de formulário no fluig, na visão *Explorador de pacotes* *(Package Explorer)* deve-se acessar a pasta *forms* do projeto fluig, clicar com o botão direito e no menu acessar *Novo (New) > Outras (Other).*

**Figura 5 - Criação de script evento da definição de formulário.**

2Passo 2

* Abra a pasta Fluig e selecione a opção *Script Fluig* e clique no botão *Avançar* *(Next > )*.

**Figura 6 - Criação de script evento da definição de formulário.**

3Passo 3

* Selecione o tipo e clique em *Avançar (Next >)*.

4Passo 4

* Nesta tela é necessário informar os campos pertinentes ao evento que se deseja adicionar e clicar no botão**Concluir**.

#f2f2f2#f2f2f2

Após a criação de uma definição de formulário é possível realizar a criação de scripts para customização. O eventos para formulários são criados conforme os passos abaixo.

* Para a criação de um script de formulário no Fluig, na visão **Explorador de pacotes (Package Explorer)** deve-se acessar a pasta forms do projeto fluig, clicar com o botão direito e no menu acessar **Novo (New) > Outras (Other)**.
* Abra a pasta Fluig, selecione a opção **Script Fluig** e clique no botão **Avançar (Next >)**.
* Selecione o tipo e clique em **Avançar (Next >)**.

**Figura 7 - Criação de script evento da definição de formulário.**

5Passo 5

* No exemplo selecionamos o evento *validateForm*, e o relacionamos a definição de formulário *form\_exemplo\_fluig*.

**Figura 8 - Criação de script evento da definição de formulário.**

6Passo 6

* Ao concluir a estrutura principal do método estará disponível no editor.

**Figura 9 - Criação de script evento da definição de formulário.**

7Passo 7

* Configure seu script. Para entender mais sobre os eventos e algumas dicas continue lendo essa documentação

**Figura 10 - Criação de script evento da definição de formulário.**

# LOGs

---

Uma das funções mais importantes para entender o que está acontecendo no código e rastreamento futuro é o log. Tanto em eventos de formulário, eventos de processo, datasets, o fluig permite fazer log em quatro níveis:

## log.info

Usado para apresentar alguma mensagem de rastreamento do código ou dos campos

jsjs

## log.warn

---

Usado para indicar algum ponto de atenção ou problema eminente no código

js

## log.debug

---

Os logs, se não usados com moderação, podem mais atrapalhar do que ajudar. Por isso, caso necessário, algumas informações podem ser utilizadas como debug, que são ativas somente quando o usuário realmente ver elas

js

## log.error

---

Usado para imprimir um log de erro

js

## log.dir

---

Este log não é um tipo diferente, na verdade é um log.info turbinado. Serve para fazer o log de objetos mais complexos que simples strings

js

# Eventos

---

Os eventos de formulários são um conjunto de scripts carregados pela API de Formulários, os quais são desenvolvidos utilizando Javascript e são chamados durante a execução de ação em formulários ou em momentos específicos de interação em formulários.

## beforeProcessing

---

Esse evento é o primeiro a ser disparado. Ocorre antes de qualquer outro evento da definição de formulário. O evento recebe como parâmetro um objeto do tipo .

Neste contexto, o FormControler deve ser usado apenas para consulta de dados, alterações nos dados não serão persistidas.

js

No contexto deste evento a variável *form* pode ser usada somente para consulta aos campos da definição de formulário, seus valores e estado de apresentação.

## displayFields

---

Esse evento é disparado no momento em que os objetos do formulário são apresentados. O evento recebe como parâmetro um objeto do tipo  e um parâmetro *customHTML* que serve para personalizar e inserir dados diretamente do servidor no formulário.

Esse evento pode ser utilizado para alterar os valores a serem apresentados no campo do formulário e é o único que permite a alteração antes da renderização. Para isto basta usar o seguinte procedimento:

jsAo modificar um registro, preenche o campo com o valor 1true

Você pode também ocultar campos pelo nome ou pelo id:

js

Outras funções interessantes que podem ser usados neste evento são:

* Para visualizar o formulário no formato original com os campos desabilitados, deve-se utilizar o método *setShowDisabledFields*.

* Para habilitar ou desabilitar o botão de excluir nas linhas do formulário filho, que por padrão é habilitado, deve-se utilizar o método *setHideDeleteButton*.

* Para ocultar o os botões*Imprimir*e *Imprimir em nova Janela*,deve-se utilizar o método *setHidePrintLink*.

| Sem customizações | Com customização |
| --- | --- |
|  | js |
|  | js |

Formulário funcional com exemplos de utilização de***setVisible*,***setVisibleById***, setHideDeleteButton e setHidePrintLink****:****

xmlFormulário - Clique para expandirtruetrue


# Ao Salvar escolha o que ocultar ao salvar o formulário

Ocultar toda tabela

Ocultar campo A

Ocultar campo N da primeira linha

Ocultar campo M da segunda linha

Ocultar linha 1

Ocultar botão de excluir

Ocultar botão de imprimir

Ocultar Lorem Ipsum

## Tabela de registros

| N | M |
| --- | --- |
|  |  |

Lorem Ipsum: Proin eget purus non mauris vehicula aliquam vitae sed est
