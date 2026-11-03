---
content_hash: a3f8965102161a116061acd8e034cc8f74f7eadd5682cef5d0e41638fe0ae55c
fetched_at: '2026-06-29T00:09:34.135739+00:00'
page_id: '425459151'
product: rm
source: tdn-rm
title: Gabaritos
type: documentation
url: https://tdn.totvs.com/display/LRM/Gabaritos
version: 15
---

O menu de Gabaritos é responsável por armazenar as respostas de uma determinada avaliação e atualizar as notas das avaliações dos alunos. 

Configuração

A funcionalidade está disponível em **Educacional |** **Matrícula e Avaliação | Gabaritos | Configuração**

Para que o cadastro seja feito é obrigatório informar os seguintes campos:

* **Período letivo**
* **Cód. Gabarito**
* **Descrição**
* **Cód. Etapa**
* **Cód. Prova**

Caso o parâmetro "Descontar questões certas a cada errada" estiver **marcado** o comportamento do sistema será:

Cenário: 

Questão 1: Valor 5 ✅

Questão 2: Valor 5 ✅

Questão 3: Valor 3 ❌

Nesse cenário, o aluno ficara com a nota 7 no total da avaliação.

A etapa e a prova informada não tem relacionamento direto com as etapas e provas vinculadas a períodos letivos e turmas/disciplinas.

Para realizar a inclusão das respostas do gabarito, deve-se acessar a tela disponível em **Anexos | Respostas do gabarito**.

Para que o cadastro das respostas do gabarito seja feito é obrigatório informar os seguintes campos:

* **Tipo de prova**
* **N° Questão**
* **Resposta**

Existem 5 **Tipos de prova**: A, B, C, D e E; estes tipos de provas são internos do sistema e não podem ser alterados. 

O campo **Resposta** aceita apenas valores de um único digito, como A, B, C, D ou  1, 2, 3, 4.

Só é possível ter uma resposta para cada Tipo de Prova/Questão. Caso seja necessário indicar que determinada questão foi anulada e seu ponto será atribuído a todos os alunos, deve-se informar \* (asterisco) como resposta.

Para definir o valor de cada resposta, deve-se acessar a tela disponível em **Anexos | Valor das respostas do gabarito**.

Para realizar o cadastro do valor das respostas do gabarito, deve-se selecionar o **código da disciplina** e o **valor da questão** para aquela disciplina.

Processo de Correção das Respostas do Gabaritos:

A funcionalidade está disponível em **Educacional |** **Matrícula e Avaliação | Gabaritos | Importação**

O processo de correção de gabaritos consiste em ler um arquivo .txt contendo as respostas dos alunos para um determinado gabarito e atualizar a nota de avaliação do aluno em um período letivo.

O conteúdo do arquivo de respostas é um arquivo texto separado por ponto-e-vírgula contendo: Registro acadêmico do aluno; Tipo de prova; Respostas;  
Ao ler o arquivo de respostas, o sistema irá, para cada registro acadêmico, verificar se o aluno possui matrícula no período letivo e no curso.

Exemplos:

* RA\_ALUNO;A;ABCD
* RA\_ALUNO2;A;A CD (o espaço em branco indica que o aluno não informou a resposta da questão 4, sendo assim, ele não irá pontuar.)

Exemplo do arquivo txt:

Bloquear alteração de notas e faltas

Serão listadas somente matrículas de Turmas / Disciplinas que tenham avaliação cadastrada conforme prova do gabarito.  
Caso o aluno tenha duas matrículas no curso selecionado, o sistema irá atualizar as duas. 

O sistema irá **bloquear** as alterações das notas e faltas caso a opção "**Bloquear alterações de notas e faltas**" esteja **marcada** no cadastro da **situação de matrícula na disciplina.**

Informação

Caso o parâmetro educacional "Alterar notas e faltas bloqueadas por situação de matrícula" esteja marcado, será desconsiderado o parâmetro da situação de matrícula "Bloquear alterações de notas e faltas".
