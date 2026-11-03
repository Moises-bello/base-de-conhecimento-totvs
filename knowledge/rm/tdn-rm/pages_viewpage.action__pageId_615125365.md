---
content_hash: caaf826cd0d31773442920973e818c2e5a27b2a909787b3e608fcd2d84e23833
fetched_at: '2026-06-29T00:10:59.649030+00:00'
page_id: '615125365'
product: rm
source: tdn-rm
title: WebService - Inscrição de Candidatos - Novo Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=615125365
version: 5
---

Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | 12.1.17 |
| **Nome do dataserver** | EduPSInscricaoUsuarioAreaData |
| **Pre-****requisitos** | Utilizar um processo seletivo do novo portal |

**Objetivos**

Este dataserver EduPSInscricaoUsuarioAreaData diferentemente do EduPSInscricaoAreaOfertadaData não necessita que o usuário (pessoa) esteja cadastrado no cadastro de usuários do processo seletivo, o dataserver faz o cadastro dos usuários (candidato e responsáveis) envolvidos no processo e a inscrição além de preencher corretamente os dados referente ao termos de aceite da inscrição.

Importante

Este dataserver é exclusivo para utilização em processos seletivos que utilizem o novo portal de inscrições.

Como configura o WebService e Obter as chaves primarias.

[Como Expor os Web Services do RM através do Host (recomendado)](http://tdn.totvs.com/pages/viewpage.action?pageId=89620766)

[Utilizando o TOTVS WS Client - Ferramenta para auxiliar a utilização dos Web Services providos pelo TBC](http://tdn.totvs.com/pages/viewpage.action?pageId=189307798)

**Informações de criação do Projeto e Autenticação no link abaixo.**

[Criação do Projeto e Autenticação.](http://tdn.totvs.com/pages/viewpage.action?pageId=322149560)

**XML completo base para a cadastro e inscrição de candidatos e****responsáveis**

xmlXmltrue

1
117
0
1
2021-04-29T19:25:35.099
0
F
06200
MG
0
F
T
T
F
F
F
1
F
F
F
F

F
F
F
F
F

1
117
0
13
1
0

1
117
0
13
1

1
117
0

0
Candidato de teste
Apelido
2010-10-10T00:00:00
S
M
10
7
Rua
1
Comp
Bairro
MG
Belo Horizonte
31720430
1
123456
52785177436
31333333
99999999
123456
MG
SSP
2010-10-10T03:00:00
123456
123
123
123456
12345
MG
2010-10-10T03:00:00
0
123456
123
2010-10-10T03:00:00
123456
123456
Belo Horizonte
MG
2010-10-10T03:00:00
123456
0
1
1
1
123456
3216
2010-10-10T03:00:00
2010-10-10T03:00:00
Definidito
email@email.com
10
88888888
77777777
126
123456
0
Espanha
2010-10-10T03:00:00
2020-10-10T03:00:00
06200
123456
2010-10-10T03:00:00
EB
Brasil
Reservista
2010-10-10T03:00:00
MG
A+
1
1
06200
Nome social
F
1
117
T
F
F
F
F
F

0
Pai de teste
Apelido
1950-10-10T00:00:00
C
M
10
9
Rua
1
Comp
Bairro
MG
Belo Horizonte
31720430
1
123456
19633776643
33333333
99999999
12345
MG
SSP
2010-10-10T03:00:00
123456
123456
123456
123456
12345
MG
2010-10-10T03:00:00
0
123456
12345
2010-10-10T03:00:00
123456
123456
Belo Horizonte
MG
2010-10-10T03:00:00
123456
0
0
1
1
123456
123456
2010-10-10T03:00:00
2010-10-10T03:00:00
Fixo
email@teste.com.br
2
88888888
77777777
923
123456
0
Espanha
2010-10-10T03:00:00
2010-10-10T03:00:00
06200
123456
2010-10-10T03:00:00
EB
123456
Reservista
2010-10-10T03:00:00
MG
A-
1
1
06200
Nome social
F
1
117
F
T
F
F
T
F

0
Mão de teste
Apelido
1960-10-10T00:00:00
C
F
10
123456
77660008730
123
MG
SSP
2010-10-10T03:00:00
123456
123456
123456
123456
12345
MG
2010-10-10T03:00:00
0
123456
12345
2010-10-10T03:00:00


Belo Horizonte
MG
0
0
email@teste.com.br
0



2010-10-10T03:00:00
MG
06200
Nome social
F
1
117
F
F
T
F
F
F

0
Responsável financeiro
1980-10-10T00:00:00
M
25633646711
0
Belo Horizonte
MG
0
0
0
06200
F
1
117
T
F

1
117
-1
8

1
117
-1
12
]]>

**Descrição das tabelas:**

* SPSINSCRICAOAREAOFERTADA (obrigatória)
  + Grava dados básicos da  inscrição do candidato como por exemplo local de prova, deficiências, cotas e se é treineiro.
* SPSOPCAOINSCRITO (obrigatória)
  + Grava uma ou mais áreas de interesse que o candidato está se inscrevendo, caso possua uma segunda área de interesse deve ser respeitado o campo <NUMEROOPCAO>.
* SPSIDIOMAINSCRITO  (não obrigatória)  
  + Caso a área interesse possua idioma, deve ser informado nesta tabela qual idioma ou quais idiomas o candidato está se inscrevendo.
* SPSINSCAREAOFERTACOMPL  (obrigatória)
  + Grava os campos complementares caso sejam definidos para inscrição do candidato. Esta tabela deve ser informada mesmo sem possuir um campo complementar definido para a inscrição.
* SPSUSUARIO (obrigatória)
  + Grava os dados dos usuários envolvidos na inscrição, esta tabela é obrigatória para o candidato, para os responsáveis deve ser observado os parâmetros do processo seletivo. Os campos de dados pessoais e endereço devem ser informados conforme a definição de visibilidade e obrigatoriedade de campos do processo seletivo.
  + Para os dados dos responsáveis deve ser observado os campos da tabela (valores aceitos - T para verdadeiro ou F para falso):   
    - <EHCANDIDATO> - Define se é o candidato
    - <EHPAI> - Define se o usuário em questão é o pai do candidato
    - <EHMAE> - Define se o usuário em questão é a mãe do candidato
    - <EHRESPFIN> - Define se o usuário em questão é o responsável financeiro, pode ser o próprio candidato dependendo da definição do processo seletivo.
    - <EHRESPACAD> - Define se o usuário em questão é o responsável acadêmico, pode ser o próprio candidato dependendo da definição do processo seletivo.
    - <EHRESPINSC> - Define se o usuário em questão é o responsável pela inscrição.
* SPSINSCRICAOAREAOFERTADASUBDEF (não obrigatória)
  + Grava as subdeficiências do candidato caso seja informado alguma deficiência na tabela SPSINSCRICAOAREAOFERTADA .
