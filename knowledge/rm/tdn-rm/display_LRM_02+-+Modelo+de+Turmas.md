---
content_hash: 01654fc88db7a7305c625d829898788b1165cb725f7f404a673a5de1fd29c8ee
fetched_at: '2026-06-29T00:11:28.194512+00:00'
page_id: '730534356'
product: rm
source: tdn-rm
title: 02 - Modelo de Turmas
type: documentation
url: https://tdn.totvs.com/display/LRM/02+-+Modelo+de+Turmas
version: 24
---

O Modelo de Turmas define a forma como as turmas serão criadas quanto ao seus tipos, datas de início e fim, nome da turma e a seus limites de vagas. Os modelos de turmas serão utilizados na etapa de criação de turmas.

A permissão para ter acesso este menu no portal está no caminho abaixo.

**Acessar RM.exe I Menu | Serviços Globais | Perfil | Educacional | Acesso ao Menus | Educacional | Educacional (Portal) | Gestão Educacional | Gestão de ofertas | Modelo de turmas**

No modelo de turma é definida qual máscara de turma deve ser usada na geração do código da turma: a máscara informada no cadastro do curso ou a máscara informada no modelo de turmas. Ao passar o mouse sobre o ícone de informações na frente do campo da máscara, serão exibidas as instruções do padrão a ser utilizado para informar a máscara de turma, caso o modelo seja configurado para não utilizar a máscara do cadastro de curso.

Para Turma livre não se utiliza máscara do curso, visto que esse modelo de turma não possui matriz curricular, então a informação sobre a máscara da turma é obrigatória. 

As opções de informações para compor o código da turma livre são diferentes da turma com matriz curricular.

A partir da versão 12.1.2510.127, houve uma alteração na máscara do curso**:** o número sequencial passou a ser iniciado pela combinação *Período Letivo/Curso. Além da* inclusão de uma nova *tag* [O], que corresponde à descrição do tipo de turno.

Para os modelos de turma que não utilizam a máscara definida no cadastro do curso e que não são configurados como turma livre, foi criado o tipo sequencial de máscara por turma, composto pela combinação Período Letivo/Curso ou Período Letivo/Curso/Período.

Para o tipo sequencial Período Letivo/Curso/Período, a utilização da tag [p], correspondente ao período, torna-se obrigatória na definição da máscara.

Disponível a partir da versão 12.1.2510.139.

Foi disponibilizado um parâmetro que permite definir se o valor sequencial é **numérico** ou **alfabético**.

### Comportamento do sequencial

* **Numérico**:  
  Quando houver mais de uma tag `#` consecutiva, o valor deve ser preenchido com zeros à esquerda, respeitando a quantidade de caracteres definida, e incrementado de forma sequencial.  
  *Exemplo:* `##` → `01`, `02`, `03`, ...
* **Alfabético**:  
  Não há preenchimento com caracteres adicionais. Tanto a utilização de `#` quanto de `##` gera inicialmente o valor `A`, seguido de `B`, `C`, e assim sucessivamente.

Funcionalidade disponível a partir da versão 12.1.2510.157.

**Proporcionalidade**

O modelo de turma adota o conceito de proporcionalidade entre o máximo de alunos e os demais campos (mínimo de alunos, vagas para calouros, máximo de alunos de outros cursos e máximo de alunos de outras matrizes aplicadas).

No exemplo acima, está sendo informado o valor máximo de 80 alunos, e o valor mínimo de 20 alunos, o que gera uma proporcionalidade de 25%.

O sistema armazena o valor máximo de alunos (80) mas para os demais campos, é armazenado a proporcionalidade do valor informado na tela em relação ao máximo de alunos, assim sendo:

| Campo | Valor informado | Valor armazenado |
| --- | --- | --- |
| Máx. alunos | 80 | 80 |
| Mín. alunos | 20 | 25% |
| Vagas para calouros | 10 | 12,5% |
| Máx. alunos outros cursos | 10 | 12,5% |
| Máx. alunos outras matrizes aplicadas | 10 | 12,5% |

Todos os campos armazenados são uma proporção em relação ao máximo de alunos e o sistema consegue fazer a conversão/recuperação do valor nominal, a partir do cálculo dessa proporcionalidade, caso o usuário realize alterações, ou inclua um novo registro.

Essa proporcionalidade armazenada é importante para garantir que os ajustes feitos em demandas, capacidades, agrupamentos e realocações de turmas, na etapa de Gestão de Turmas, usem sempre a mesma regra que foi definida no modelo de turma, mantendo assim, a proporção correta para definir se uma turma está acima, abaixo ou conforme a capacidade.

Exemplo:

Se uma turma for gerada utilizando o modelo da tabela acima, e possuir demanda de 30 alunos, na etapa de Gestão de turmas, ela terá uma demanda esperada com status CONFORME, pois 30 alunos é mais que 25% do total de 80 (capacidade).

Se mudarmos a capacidade dessa turma para 200 alunos, a proporção a ser adotada continua sendo a definida no modelo de turma, ou seja, 25%. Nesse caso, 30 alunos é inferior aos 25% do novo total de 200 (capacidade), e essa turma terá uma demanda esperada com status ABAIXO.

**Visualização**

A tela exibirá inicialmente até 500 modelos de turma cadastrados. Caso haja mais modelos disponíveis, será possível visualizá-los clicando no botão "Carregar mais resultados".
