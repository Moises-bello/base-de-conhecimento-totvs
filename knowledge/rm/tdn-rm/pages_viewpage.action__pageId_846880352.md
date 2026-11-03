---
content_hash: 4eef4e80d448aacf979b5a06ec98dc42074ecb98bbc63b4d236026d7f7a60865
fetched_at: '2026-06-29T00:11:50.953842+00:00'
page_id: '846880352'
product: rm
source: tdn-rm
title: Máscara e Expressões Regulares
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=846880352
version: 4
---

**Máscara** define um formato padrão que auxilia a digitação do usuário.

Expressão regular (do inglês **regular expression**, abreviado **regex**) provê uma forma concisa e flexível de identificar cadeias de caracteres de interesse, como caracteres particulares, palavras ou padrões de caracteres. Expressões regulares são escritas numa linguagem formal que pode ser interpretada por um processador de expressão regular, um programa que serve um gerador de analisador sintático ou examina o texto e identifica as partes que casam com a especificação dada. (Wikipédia, 2024).

**Máscaras:**

**0** - Define que será aceito somente 0 (zero) quando definido;

**1** - Define que será aceito somente 0 (zero) ou 1 (um) quando definido;

**2** - Define que será aceito de 0 (zero) a 2 (dois) quando definido;

**3** - Define de 0 a 3;

**4** - Define de 0 a 4;

... (segue a mesma ideia para os demais números);

**9** - Define de 0 a 9;

**@** - Define que pode ser digitado uma letra qualquer maiúscula ou minúscula;

**espaço vazio** - Define um espaço vazio quando definido;

**w** - Define letra ou número maiúsculo ou minúsculo;

**Observação:** os demais símbolos serão replicados na máscara ao serem digitados os valores, como no exemplo de uma máscara de telefone (99) 99999-9999 que o usuário poderá somente ir digitando os números que os demais caracteres serão preenchidos: **(31) 99544-5468**.

**Exemplo de Máscaras:**

**1** - **099 w@ 555**

Digitações válidas:

**012 1a 435**,

**089 aa 545**,

**031 hK 510**

**2** - (**09) 8888@@**

Digitações válidas:

**(01) 7888aB**,

**(08) 8881BA**,

**(03) 0123NM**

**Exemplos de máscaras utilizando Expressão Regular:**  
  
Máscara de exemplo 1: **@99999**(essa máscara define que o primeiro dígito é uma letra qualquer, seguido por cinco números):

Estaria correto: a12345, A12345, ç95456, P87456, etc.

Se quiser garantir que serão aceitos somente três tipos de letras iniciais e que as mesmas devem ser maiúsculas, escreveria a seguinte expressão regular:

**^[ABC]\d{5}$**

Onde,

* **^** indica que irei começar a string;
* **[ABC]**, lista que só casa com A, B ou C maiúsculo,
* **\d{5}$**, indica que terei 5 dígitos numéricos no final da string.

Máscara de exemplo 2: **(99) 9999-9999** (essa máscara define um número de telefone com o seu ddd):

Estaria correto: (31) 3434-5465, (11) 2563-3030, (21) 2345-5645, etc.

Para garantir que temos valores completos igual a indicação da máscara, escrevemos a seguinte expressão regular:

**^\(\d{2}\) \d{4}-\d{4}$**

Onde,

* **^**: indica o início da string;

* `**\(**`: corresponde ao caractere literal '**(**';

* '**\d{2}**': corresponde exatamente a dois dígitos;
* '**\)**': Corresponde ao caractere literal '**)**';
* '' (espaço): corresponde a um espaço;
* '**\d{4}**': corresponde exatamente a quatro dígitos;
* '**-**': corresponde ao caractere literal '**-**';
* '**\d{4}**': corresponde exatamente a quatro dígitos;
* '**$**': indica o final da string.

Máscara de exemplo 3: \*999 (essa máscara define que o primeiro dígito é o \*, seguido por três números):

Exemplos: \*123, \*958, \*456, etc.

Para garantir que temos valores completos igual a indicação da máscara, escrevemos a seguinte expressão regular:

**^\\*\d{3}$**

Onde,

* ^ indica o **início da string**.
* \\* corresponde ao caractere literal \*.
* \d{3} corresponde a **exatamente três dígitos numéricos**.
* $ indica o **final da string**.

Assim, ^\\*\d{3}$ garante que a string **começa com \* e é seguida por três dígitos, sem nenhum outro caractere antes ou depois**.
