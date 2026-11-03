---
content_hash: fb94de419850d795787cef7565335bcfe42f5c615dc99e5a5c78be94c8d8e9c3
fetched_at: '2026-06-29T00:09:14.833960+00:00'
page_id: '421385274'
product: rm
source: tdn-rm
title: Máscaras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385274
version: 3
---

---

**Máscara da Tarefa:**

Informe a máscara do código da tarefa. Só é possível alterar a máscara quando não existem tarefas, etapas e obras cadastradas. O código da tarefa será sempre numérico, podendo variar o número de caracteres por nível.

**Atenção**

O código da tarefa pode ser ###.####.##. Nesse caso, os códigos das obras possuem três caracteres, os códigos da etapa possuem quatro caracteres e os códigos dos serviços possuem dois caracteres.

**Máscara de Insumos:**

Informe a máscara do código dos insumos. Se a máscara não for informada o campo de código de insumo poderá ser preenchido com qualquer caracter, utilizando, no máximo, 25. Só é possível alterar a máscara quando não existem insumos cadastrados.Ao alterar a máscara do insumo, os códigos inseridos nos campos de faixa de insumo,na pasta default do grupo de custo serão apagados. O código do insumo pode possuir caracteres numéricos, alfanuméricos, alfas. Esses caracteres são representados pelos seguintes símbolos:

# - Caracteres Numéricos (números de 0 (zero) a 9)

L - Caracteres Alfas (letras de A a Z)

A - Caracteres Alfanuméricos (letras de A a Z e números de 0 (zero) a 9)

/ : - , . ( ) espaço em branco - Caracteres separadores

**Exemplo:** Se a máscara for ##.##, o código do insumo será dois números, o ponto como separador e mais dois números, como 01.33.

Se a máscara for L#.##, o código do insumo será uma letra e um número, o ponto como separador e mais dois números, como A1.33.

Se a máscara for A#.##, o código do insumo será um número ou uma letra para o primeiro caracter, um número para o segundo caracter, o ponto como separador e mais dois números, como A1.33 ou 91.33.  
    
 **Máscara de Composições:**  
 Informe a máscara do código das composições. Se a máscara não for informada o campo de código de composições poderá ser preenchido com qualquer caracter, utilizando, no máximo, 20. Só é possível alterar a máscara quando não existem composições cadastradas. O código da composição pode possuir caracteres numéricos, alfanuméricos, alfas. Esses caracteres são representados pelos seguintes símbolos:

# - Caracteres Numéricos (números de 0 (zero) a 9)

L - Caracteres Alfas (letras de A a Z)

A - Caracteres Alfanuméricos (letras de A a Z e números de 0 (zero) a 9)

/ : - , . ( ) espaço em branco - Caracteres separadores

**Exemplo:** Se a máscara for ##.##, o código da composição será dois números, o ponto como separador e mais dois números, como 01.33.

Se a máscara for L#.##, o código da composição será uma letra e um número, o ponto como separador e mais dois números, como A1.33.

Se a máscara for A#.##, o código da composição será um número ou uma letra para o primeiro caracter, um número para o segundo caracter, o ponto como separador e mais dois números, como A1.33 ou 91.33.   
  
**Máscara de Requisição de Materiais:**

Informe a máscara do código das requisições de materiais.

Não é possível efetuar uma requisição de materiais sem que sua máscara esteja definida.

A máscara deve ser composta por, no mínimo, cinco números, ou seja, deve possuir ao menos cinco vezes o caracter #. Caso deseje incluir letras à máscara, elas devem ser posicionadas no início, sempre antes dos números. A máscara devem conter, no máximo, quinze caracteres.

**Máscara de Requisição de Materiais Extras:**

Informe a máscara do código das requisições de materiais.

Não é possível efetuar uma requisição de materiais extras sem que sua máscara esteja definida.

A máscara deve ser composta por, no mínimo, cinco números, ou seja, deve possuir ao menos cinco vezes o caracter #. Caso deseje incluir letras à máscara, elas devem ser posicionadas no início, sempre antes dos números. A máscara devem conter, no máximo, quinze caracteres.

**Usar auto-incremento**

Caso esta opção esteja habilitada, ao incluir uma composição no projeto, o campo Código será gerado automaticamente dependendo do valor inicial informado.

**Valor inicial**

Informe o valor inicial que será gerado o cógido da composição. Este valor inicial reflete também na renumeração das composições do projeto, é verificado qual será o primeiro código a ser gerado.

---
