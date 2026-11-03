---
content_hash: cbd90a552cf9f28e6bacb7ead256de618c7e6625881ed935d4269e902b005e82
fetched_at: '2026-06-29T00:09:32.469745+00:00'
page_id: '425458856'
product: rm
source: tdn-rm
title: Processo de Correção de Gabaritos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458856
version: 2
---

O processo de correção de gabaritos consiste em ler um arquivo texto contendo as respostas dos alunos para um determinado gabarito e atualizar a nota de avaliação do aluno em um período letivo. Para executar o processo de correção de gabaritos, o usuário deverá seguir alguns passos descritos nos tópicos abaixo.

**Informações de período letivo e gabarito.** O usuário deverá informar um período letivo e um gabarito previamente cadastrado. Somente gabaritos do período letivo selecionado serão listados.   
 O usuário informa o arquivo texto que contém as respostas dos alunos.  
 **Conteúdo do arquivo de respostas.** O conteúdo do arquivo de respostas é um arquivo texto separado por ponto-e-vírgula contendo: a> Registro acadêmico do aluno; b> Tipo de prova; c> Respostas;  
 **Exemplo de arquivo de respostas:** EB-00123;A;BBCDACEDD EB-00567;A;ACC EABBC EB-00467;B;BBCDACEED Nota: o espaço em branco na segunda linha do exemplo indica que o aluno não informou a resposta da questão 4. Assim, o aluno irá "errar" a questão.  
 **Filtro de matriz aplicada e turma.** O sistema usará os filtros de matriz aplicada e turma para selecionar a matrícula dos alunos contidos no arquivo de respostas.   
 **Exemplo:**   
 Período letivo selecionado = 2013  
 Curso = ADM  
  
 Ao ler o arquivo de respostas, o sistema irá, para cada registro acadêmico, verificar se o aluno possui matrícula no período letivo de 2013, no curso ADM. ***Importante:***  
 *Caso o aluno tenha duas matrículas no curso ADM em 2009, o sistema tentará atualizar as duas.*   
 Somente matrículas de Turmas / Disciplinas que tenham avaliação cadastrada conforme prova do gabarito serão listadas.  
  
 **Análise das respostas e atualização da nota da avaliação**  
  
 **Validação de dados do arquivo de respostas:**  
 O sistema carrega os dados do gabarito, questões e valores de cada questão, em seguida valida a quantidade de colunas do arquivo e monta uma lista com as respostas de cada aluno  
 **Exemplo:** EB-00123;A;BBCDACEDD EB-00567;ACC EABBC EB-00467;B;BBCDACEED Neste caso, o sistema não irá processar a linha 2, pois contém apenas 2 colunas. Demais linhas serão processadas normalmente.  
 Após validar as colunas o sistema valida os tipos de prova.   
 **Exemplo:** EB-00123;A;BBCDACEDD EB-00567;F;ACC EABBC EB-00467;B;BBCDACEED Neste caso, o sistema não irá processar a linha 2, pois contém tipo de prova F (O sistema permite apenas tipos de prova A, B, C, D e E). Demais linhas serão processadas normalmente.  
 Por último o sistema valida a quantidade de respostas por tipo de prova.   
 **Exemplo:**  
 Prova A = 5 questões EB-00123;A;BBCDA EB-00567;A;ACC EA EB-00467;A;B Neste caso, o sistema só irá processar a linha 1, pois contém 5 respostas  
 **Correção das respostas do aluno.** Para cada resposta do aluno, o sistema irá verificar se ele acertou ou não a questão baseado no tipo de prova do aluno e o tipo de prova cadastrada no gabarito. O aluno irá "acertar" a questão se sua resposta for a mesma cadastrada no gabarito ou se a questão for anulada.  
 **Cálculo dos pontos** Para cada questão, o sistema irá contar os pontos obtidos - aluno por aluno - e atualizar as notas de cada um. ***Importante:*** *Caso o parâmetro de "Descontar questões certas a cada errada" esteja marcado, o sistema irá deduzir da nota total do aluno na disciplina as questões que ele errou.*   
 **Exemplo:** Questão 1, peso 10 em matemática: aluno acertou; Questão 2, peso 10 em matemática: aluno acertou; Questão 3, peso 05 em matemática: aluno errou; Neste caso, a nota do aluno será 15 em matemática.  
 Ao final do processo o sistema atualiza todas as notas e informa ao usuário a quantidade de provas cadastradas/atualizadas.
