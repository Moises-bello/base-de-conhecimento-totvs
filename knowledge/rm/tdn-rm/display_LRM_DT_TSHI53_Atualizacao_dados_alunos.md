---
content_hash: 8055ea1b5b552c7fdb9f987991c4eaa385803bf464a31d8f368cfe508be97600
fetched_at: '2026-06-29T00:08:11.520342+00:00'
page_id: '243011570'
product: rm
source: tdn-rm
title: DT_TSHI53_Atualizacao_dados_alunos
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_TSHI53_Atualizacao_dados_alunos
version: 112
---

# Atualização dos dados do cadastro de alunos através do WebService (TBC)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Classis.NET* |
| **Função:** | *Atualização dos dados de alunos* |
| **Situação/Requisito:** | *Atualização dos dados do cadastro de alunos através do WebService (TBC)* |
| **Solução/Implementação:** | *Está disponível o dataserver EduAlunoData onde é possível realizar a consulta de alunos, cadastro de novos alunos e edição de dados cadastrais de alunos através do WebService wsDataServer do TBC.*  *Segue abaixo um exemplo básico para utilização do DataServer EduAlunoData através da ferramenta SoapUI:*  ***ReadView***  *Irá retornar uma lista de alunos levando em consideração também um filtro personalizado pelo usuário, passado por parâmetro para o WebService.*  ***Descrição dos parâmetros:***  ***DataServerName:** Deve ser indicado o dataserver EduAlunoData*  ***Filtro:** Um filtro personalizado do usuário que limitará o retorno dos dados pelo WebService.*  ******Contexto***:*** **Deve ser informado ao DataServer as informações do contexto que será realizado as alterações. Este contexto é importante inclusive, para que o DataServer recupere as informações dos parâmetros do sistema no contexto informado.**  *Segue abaixo um exemplo de utilização:*      ******ReadRecord******  *Retorna todas as informações manipuláveis de um único aluno, filtrado basicamente pela chave primária da tabela SALUNO. (CODCOLIGADA e RA)*  ***Descrição dos parâmetros:***     ***DataServerName:** Deve ser indicado o dataserver EduAlunoData*     ***PrimaryKey:** Valores da chave-primária separados por ponto e vírgula.*     ******Contexto***:*** **Deve ser informado ao DataServer as informações do contexto que será realizado as alterações. Este contexto é importante inclusive, para que o DataServer recupere as informações dos parâmetros do sistema no contexto informado.**  **Segue abaixo um exemplo de utilização:**      *******SaveRecord:*******  *Realiza o cadastro ou alteração das informações do aluno, baseadas no XML passado como parâmetro. Para facilitar montagem da estrutura do XML é recomendável utilizar o mesmo XML de retorno do método ReadRecord.*  ***Descrição dos parâmetros:***  ***DataServerName:** Deve ser indicado o dataserver EduAlunoData*  ***PrimaryKey:** Valores da chave-primária separados por ponto e vírgula.*  ******Contexto***:*** **Deve ser informado ao DataServer as informações do contexto que será realizado as alterações. Este contexto é importante inclusive, para que o DataServer recupere as informações dos parâmetros do sistema no contexto informado.**  **Exemplo de edição de aluno:**        *Após a execução:*      ***Exemplo de cadastro de um novo aluno:***  *Para cadastrar um novo aluno através do WebService TBC, devera ser passado o RA como valor 0.*  *Desta forma, será cadastrado um novo aluno. Se for passado o código de uma pessoa existente, será reutilizado, caso contrário será cadastrado uma nova pessoa para este novo aluno.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
