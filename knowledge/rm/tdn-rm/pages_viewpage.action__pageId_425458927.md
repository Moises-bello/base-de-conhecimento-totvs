---
content_hash: bb4a517d247f222c61969eff6862498b334e54fb56d7a2d0854a686604ed44ce
fetched_at: '2026-06-29T00:09:33.134414+00:00'
page_id: '425458927'
product: rm
source: tdn-rm
title: Questões
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458927
version: 21
---

Por este menu é possível cadastrar as questões que serão utilizadas na confecção das "Avaliações de conhecimento" ou "Pesquisa de Opinião". Todas as questões estão vinculadas a matérias e áreas.

Assim o banco de questões poderá ser atualizado de acordo com as necessidades organizacionais e as questões cadastradas poderão ser utilizadas em inúmeras provas.

O cadastro de questões está dividido em:

**Identificação**

Nesta etapa, são informadas a **área e a matéria** o código da questão, a pontuação, se a questão está ativa e o seu nível de dificuldade. Além disso, define-se o tipo de prova da questão: se é uma prova de conhecimento ou uma pesquisa de opinião.

Outra informação importante é Tipo de Questão, que poderá ser:

* Exclusiva: questão de múltipla escolha que possui apenas uma opção de resposta como correta.
* Múltipla: questão de múltipla escolha que pode conter mais de uma opção de resposta para serem consideradas como corretas.

* Múltipla - compensação: Indica se para cada resposta correta haverá um percentual de acerto para a questão. Recurso disponível para questões com tipo de prova Conhecimento.

* Aberta: questão que não possui opções como resposta. As questões abertas exigem que os participantes digitem suas respostas em uma caixa de comentários, não oferecendo opções específicas pré-definidas de respostas.

**A partir da versão: 12.1.2606**

Passam a existir mais dois tipos de opções de resposta válidos para o novo Executor Web: **NPS e CSAT**

CSAT possui 5 alternativas, fixadas em uma sequência numérica de 1 a 5 já NPS possui 11 alternativas fixadas na sequência de 0 a 10.

Todos os textos das opções de resposta (**CSAT** e **NPS**) são editáveis. Para o NPS, apenas as opções 0 e 10 são utilizadas e exibidas no portal. Recomenda-se bom senso no preenchimento desses valores.

OBS: As opções de resposta só ficarão visíveis caso o usuário selecione o tipo de prova como **Pesquisa**.

Alternativas **NPS**:  
  
  
Alternativas **CSAT**:

**Altura em linhas**: este campo estará visível somente quando a questão for do tipo "Aberta". O valor deste campo poderá variar de 1 a 100 e, é responsável, por definir a altura em linhas que o campo "TextoBox" da resposta aberta.

**Exemplo:**

Nos parâmetros da questão, definimos a atura em linhas tamanho 2, ao acessar o antigo executor web, o tamanho da "caixa" para informar o texto da questão do tipo aberta, será na altura de duas linhas.

Este parâmetro será aplicado apenas nas execuções de provas via ***Antigo Executor Web***.

false

Para o Novo Executor Web, essa parametrização não é levado em consideração.

Utilizado somente para o tamanho do campo na interface do **antigo executor** e não para quantidade de caracteres.

Está sendo descontinuado, aproveite para utilizar o novo executor, para mais informações, clique [aqui](https://tdn.totvs.com/x/z0JZIQ)!!

**Área de transferência:** Ao incluir uma questão é possível utilizar a opção **Colar área de trabalho** que permite copiar dados da área de trabalho e preencher o enunciado e as opções da questão. Para isto é preciso utilizar um padrão de texto. O usuário poderá escolher colar um texto com a linha em branco como separador do enunciado e das opções ou sem separador.

Neste caso, o sistema irá considerar a quebra de linha como separador. Para realização desta cópia, você deverá respeitar um padrão para este procedimento, no exemplo abaixo é utilizado a linha em branco como separador:

AQUI DEVERÁ CONSTAR O ENUNCIADO DA QUESTÃO. (linha em branco) OPÇÃO A (linha em branco) OPÇÃO B (linha em branco) \*OPÇÃO C (linha em branco) OPÇÃO D (linha em branco)

**Observação**

* O asterisco representa a opção correta.
* Para utilizar a opção sem separador basta remover as linhas em branco.

**Enunciado/opções**

Etapa onde é cadastrado o Enunciado da questão e as opções de respostas para as questões do tipo exclusiva e/ou múltipla e nas questões abertas a resposta. O preenchimento das opções estará diretamente ligado ao tipo de questão definido.

falseTags personalizadas

O sistema permite o uso de tags personalizadas para formatação de caracteres especiais, como sobrescrito e subscrito. Um ícone informativo ao lado do enunciado exibe, via *tooltip*, as instruções de uso.

## Opções de resposta Exclusiva / Múltipla:

**Tipo de Prova Conhecimento:** Deverá ser preenchido o código e marcado qual(is) a(s) opção(ões) "Correta(s)" da questão.

**Tipo de Prova Pesquisa:** Deverá ser preenchido o código da opção e o percentual de importância desta (destas) resposta(s) para a pesquisa efetuada.

**Observação**

Quando o tipo de prova for definido como **Pesquisa**, não existirá o campo **Correta** para ser preenchido nas opções cadastradas.

## Múltipla por Compensação:

**Tipo de Prova Conhecimento:** Deverá ser preenchido o código e marcado quais as opções "corretas" da questão. O percentual de importância destas respostas para a pesquisa efetuada, também deverá ser definido. Será possível definir o percentual aplicado a acertos e erros em cada opção. (Totalizando: 100% para Acertos e 100% para erros).

**Exemplo**

A questão cadastrada terá 4 opções, sendo apenas 2 delas corretas.

· Opção por compensação marcada, validando apenas 2 opções corretas da questão, o percentual de pontos de cada questão correta será 50%.   
· Opção por compensação marcada, validando acertos e erros com pontuação em percentuais fechando em 100% para cada tipo de resposta, ou seja, 2 opções corretas da questão, sendo 50% para cada resposta correta marcada na prova, podendo utilizar 2 opções erradas da questão, sendo 50% para cada resposta incorreta marcada.

## Resposta Aberta:

Não possui opções como resposta. É possível colocar a resposta correta para as provas de avaliação de conhecimento, ou comentário para as provas de pesquisa de opinião. Após a execução da prova que contenha a questão aberta, é possível validar a resposta dada pelo candidato através do ranking.

**Classificações**

Permite identificar a qual grupo de classificações as questões estão associadas. O usuário poderá inserir 0 ou quantas classificações desejar para uma questão.

E somente conseguirá incluir uma classificação na questão se caso tiver permissão no perfil do usuário. Importante: O usuário só poderá visualizar as questões quando as mesmas não possuírem classificações vinculadas ou se tiverem classificações que possuem permissões de perfil de usuário.

**Figura**

É possível incluir figuras para serem usadas nas questões.

**Estatísticas**

Visualiza as informações sobre a o uso da questão como: Primeira vez aplicada, última vez aplicada, total de acertos e total de erros.

 Informações complementares

---

[Provas que utilizam a questão](http://tdn.totvs.com/x/DQBjGQ)

[Anexos e Processos da Questão](https://tdn.totvs.com/x/7f9bGQ)

 Como fazer

---

[Provas que utilizam a questão](http://tdn.totvs.com/x/DQBjGQ)
