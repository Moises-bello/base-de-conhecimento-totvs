---
content_hash: b44788075bda86092b4c93598e76683354cfcd20b1e8bf5d0b24327a511f30e9
fetched_at: '2026-06-29T00:09:32.650320+00:00'
page_id: '425458896'
product: rm
source: tdn-rm
title: Importar candidatos a partir de arquivos texto
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+candidatos+a+partir+de+arquivos+texto
version: 6
---

Por este processo, os usuários do Totvs Avaliação e Pesquisa podem importar candidatos de um arquivo texto e realizar sua inscrição na prova. Para tal, é necessário que o usuário crie um arquivo texto (encoding UTF-8).

**Importante**

Os candidatos que serão inscrito nas provas deverão estar cadastros no sistema como pessoa (PPESSOA).  
Para realizar a importação é necessário que os arquivos de texto utilizados respeitem o seguinte layout:  
   
CODPROVA; CODGRUPO; CODPERIODO; NOME; DATA DE NASCIMENTO; CPF; IDENTIDADE; EMAIL; NRND

|  |  |  |
| --- | --- | --- |
| **Campo** | **Obrigatório?** | **Tipo de valor** |
| CODPROVA | Sim | Alfanumérico |
| CODGRUPO | Não | Alfanumérico |
| CODPERIODO | Não | Alfanumérico |
| NOME | Sim | Alfabético |
| DATA DE NASCIMENTO | Sim | DD/MM/AAAA |
| CPF | Não | Alfanumérico |
| IDENTIDADE | Não | Alfanumérico |
| EMAIL | Não | Alfanumérico |
| NRND | Não | Numérico (0 a 5) |

**Observações**

* Os campos **CODGRUPO**e **CODPERIODO** são opcionais, devendo ser preenchidos somente se a prova possuir o grupo e/ou o período informado cadastrado, caso contrário, o candidato não será importado. O sistema verifica se o registro de pessoa já existe cadastrado na base através das colunas **DATA DE NASCIMENTO**  e **NOME**.
* As colunas: **CPF**, **IDENTIDADE** e **EMAIL** são campos que complementam a busca. Não são obrigatórios, no entanto, se preenchidos o importador verificará se o registro já existe cadastrado na base também através destas colunas.
  + **Observação:**como o campo**IDENTIDADE**é um campo sem formatação definida no cadastro da pessoa (PPESSOA), ou seja, não possui um formato único como atualmente é o campo CPF, este campo deve ser informado exatamente como está no cadastro da pessoa, considerando todos os caracteres (números, letras, pontos e traços) no arquivo.
* O campo **NRND** se refere ao tipo de gabarito definido na prova. Esta informação é do tipo numérico. Os tipos possíveis de gabaritos: 0 = original, 1 a 4 = alternativos, 5 = aleatório. Como é um valor opcional, se não existir será inserido um valor default = 0.

**Importar inscrições de candidatos de outras provas**

Habilitando este parâmetro, no momento de importar o arquivo, para todas as linhas cujo campo **CODPROVA** possua um valor diferente do código da prova a realizar a importação, o sistema irá importar os candidatos referentes a essas linhas para as provas correspondentes, de acordo com o que for informado no campo **CODPROVA**.
