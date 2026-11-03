---
content_hash: 211b18e470c286280998e4a7da4c53ecd52a5fa48c8662efb22db528b40734a1
fetched_at: '2026-06-29T00:09:34.093139+00:00'
page_id: '425459139'
product: rm
source: tdn-rm
title: Integração da Prova de Etapa da Turma/Disciplina com a Prova do Totvs Avaliação
  e Pesquisa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459139
version: 2
---

Para que seja realizado a Integração do Totvs Educacional com o Totvs Avaliação e Pesquisa(Testis) com relação às avaliações das etapas deve-se seguir os passos descritos abaixo:

* Possuir uma prova de avaliação de conhecimento cadastrada no Testis
* Entre no cadastro da etapa da turma disciplina onde o aluno está matriculado e crie uma avaliação.
* No registro da avaliação existe um campo para informar qual será a prova do Testis a ser utilizada.
* Depois de vincular a prova, na Turmas/Disciplinas execute o processo descrito como 'Associar Prova do Avaliação e  Pesquisa aos alunos'.
* Para que seja possível listar os alunos no processo de 'Associar prova do Avaliação e Pesquisa aos alunos' o status de matrícula do aluno em disciplinas deve possuir os parâmetros 'Conta como aluno matriculado na turma', 'Conta como créditos cursados ou em curso', 'É uma disciplina em curso' marcados no cadastro de situação de matrícula, Aba Status na disciplina.
* Depois que este processo tiver sido executado, ao entrar no cadastro da Prova em Anexos>>Candidatos verá que o aluno já se encontra vinculado.
* O aluno deve entrar no Portal e proceder com a execução da prova utilizando o menu EXECUTOR WEB presente na parte inferior da tela de Login e Senha.
* Após o aluno ter executado e terminado a prova, deve-se entrar no Testis no cadastro de provas e executar o processo de 'Corrigir questões fechadas da prova'.
* Depois da correção, deve-se criar um arquivo de texto(.txt) contendo os candidatos e as questões da prova.

O conteúdo do arquivo deverá ser **separado por ponto-e-vírgula** e deverá conter (nesta ordem): RA do aluno, código da prova do Testis, ID interno (identificador presente na **BHISTÓRICO**) da prova no Testis e respostas.  
  
 As respostas poderão conter:

* **Letras:** a resposta informada pelo candidato;
* **Espaço em branco:** o candidato não marcou opção, ou seja, anulou a questão;
* **Asterisco:** o candidato marcou mais de uma alternativa para a questão, ou seja, anulou a questão;

Segue exemplo de arquivo: **ES-00001;16;429;D A****DB**  
    
 A importação do arquivo deve ser feita primeiramente em Matrícula e Avaliação>>Gabaritos>>Importação Avaliação e Pesquisa.  
    
 Selecione o arquivo de texto, avance e execute.  
    
 Depois da execução, entre novamente no mesmo processo de importação, selecione o arquivo de texto, selecione a opção 'Arquivo já importado', marque 'Importar a nota para o Classis', informe o Período Letivo, avance e execute o processo.  
    
 Ao proceder com este, a nota será encaminha ao aluno em notas de avaliações.
