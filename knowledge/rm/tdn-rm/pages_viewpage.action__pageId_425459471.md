---
content_hash: ed524f080e64c03a407e519f4d101e0f4e145679e07590c3e6637f932f4592f9
fetched_at: '2026-06-29T00:09:36.134402+00:00'
page_id: '425459471'
product: rm
source: tdn-rm
title: Secretaria - Geral 1/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459471
version: 5
---

---

**CPF Obrigatório:**

Na tela de cadastro do aluno na aba documentos, existe o campo 'CPF'. Quando este parâmetro esta marcado o sistema não permite salvar um aluno sem preencher o campo

*Links complementares:* *Cadastro de Aluno*  
    
 **Certificado de reservista obrigatório:**

Quando este parâmetro esta marcado o sistema não permite salvar um aluno sem informar na aba documentos, o numero do certificado de reservista.

*Links complementares:* *Cadastro de Aluno*  
    
 **Considerar somente disciplinas autorizadas do professor:**

Este parâmetro quando marcado permite que o professor seja vinculado apenas em disciplinas que esteja autorizado a lecionar. A verificação de quais disciplinas o professor esta autorizado a lecionar pode ser feita no anexo Professor | 'disciplinas autorizadas'

*Links complementares:**Disciplinas Autorizadas*

**Aproveitar código do professor de outra(s) coligada(s):**

O sistema permite que uma mesma 'pessoa' seja vinculada como professor em várias coligadas. Com este parâmetro marcado o sistema vai gerar para todos os cadastro de professor nas diferentes coligadas, o mesmo código.

***Exemplo:***   
 Considere o cenário

Pessoa: Carlos Eduardo   
Coligadas em que leciona: 1-Instituto TOTVS / 2-Faculdade TOTVS

A pessoa Carlos Eduardo é vinculada como professor na coligada 1-Instituto TOTVS. O código do professor é gerado "Prof001"   
Quando a pessoa Carlos Eduardo é cadastrado como professor na coligada 2-Faculdade TOTVS o sistema gera o mesmo código da coligada anterior para o professor "Prof001"

*Links complementares:* *Professor*  
    
 **Percentual mínimo de carga horária entre equivalências:**

Este percentual define o mínimo de horas necessárias para uma disciplina ser aprovada como equivalente.

***Exemplo:***   
 Considere o cenário  
 Disciplina 'Economia I' com valor de horas = 200hrs  
Disciplina 'Introdução a Economia' com valor de horas = 150hrs   
Disciplina "Fundamentos da Economia" com valor de horas = 80hrs

Percentual mínimo de carga horária entre equivalências = 50%  
 A disciplina "Introdução a Economia' pode ser considerada equivalente a disciplina 'Economia I' porque a carga horária da disciplina 'Introdução a Economia' é mais de 50% do valor total de horas da disciplina.  
A disciplina "Fundamentos da Economia" não pode ser considerada equivalente a disciplina 'Economia I' porque a quantidade de horas é inferior a 50% do valor total de horas da disciplina.

*Links complementares:* *Disciplinas* *-* *Equivalência de Disciplinas*  
    
 **Tamanho máximo dos arquivos das ocorrências do aluno (KB):**

Este parâmetro define o tamanho máximo permitido dos arquivos anexados às ocorrências do aluno.

*Links complementares:* Ocorrências do Aluno

**Usar grupo de disciplinas Optativas / Eletivas:**

Com este parâmetro habilitado o sistema permite que grupos de disciplinas optativas e eletivas sejam criados para que os alunos sejam matriculados.

***Exemplo:***   
 Temos 3 disciplinas relacionadas a artes visuais: "Escultura", "Gravura" e "Pintura e Desenho".  
Para facilitar a matricula dos alunos é criado o grupo de optativas "Artes Visuais".

*Links complementares:* *Grupo de Disciplinas**-* *Disciplinas Optativas/Eletivas*  
    
 **Informar disciplinas que não pertencem à matriz curricular no aproveitamento de estudos**

Quando este parâmetro esta marcado o sistema permite que disciplinas que não fazem parte da matriz curricular que o aluno esta matriculado sejam listadas para seleção na tela de aproveitamento de estudos.

*Links complementares:* *Aproveitamento de Estudos*  
    
 **Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, frequência diária e plano de aula:**

Este parâmetro quando marcado permite que o professor faça lançamento de notas e faltas usando as turmas gerenciais.

No processo 'normal' de digitação de notas e faltas o professor seleciona as turmas/disciplinas que o aluno está matriculado e faz o lançamento para cada uma delas.

Com o parâmetro marcado o professor seleciona a turma/disciplina gerencial e a partir dela faz o lançamento para todos os alunos das turmas/disciplinas gerenciadas.

**Exemplo:**  
 Considere três turmas/disciplinas com horários, etapas, tipo de avaliação e tipo de aula (presencial /distancia) iguais.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **DISCIPLINA** | **CURSO** | **ALUNOS** |
| TURMA/DISCIPLINA I | MATEMÁTICA | ADMINISTRAÇÃO | JOÃO / CARLOS |
| TURMA/DISCIPLINA II | CALCULO | SISTEMAS DE INFORMAÇÃO | ANA / MARIA |
| TURMA/DISCIPLINA III | MATEMÁTICA I | ENGENHARIA DE SOFTWARE | JULIANA |

As três turmas/disciplinas são agrupadas em uma turma/disciplina gerencial

|  |  |  |  |
| --- | --- | --- | --- |
|  | **DISCIPLINA** | **CURSO** | **ALUNOS** |
| TURMA GERENCIAL | CALCULO I | ADMINISTRAÇÃO | JOÃO / CARLOS / ANA / MARIA / JULIANA |

O responsável pela secretaria marca o parâmetro no sistema para 'Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, frequência diária  e plano de aula'  
    
 O professor acessa a opção de digitar notas e faltas por etapa e seleciona no campo turma a turma/disciplina gerencial criada.   
    
 A partir da turma/disciplina gerencial o professor lança notas e faltas para todos os alunos matriculados nas turmas/disciplinas gerenciadas: JOÃO / CARLOS / ANA / MARIA / JULIANA

*Links complementares:* *Turmas/Disciplinas* *Turma Disciplina Gerenciada* *Notas e Faltas*  
    
 **Configuração de RA. Calcular RA por:**  
 A geração do RA irá acontecer somente na inclusão de um novo aluno e irá depender da parametrização feita e da máscara de matrícula. Em todos os casos, caso não seja definida uma máscara, o sistema calculará um RA com 10 posições.  
 Os tipos de cálculo de RA são os seguintes:

* **Nenhum**: O sistema irá calcular o RA baseado na máscara de matrícula
  + **Máscara de matricula:** Insira uma máscara padrão para o RA  
    ***Exemplo:*** RA-##### = RA-00001
  + **RA Global**: O número do RA é gerado seguindo a numeração de todos os alunos cadastrados no sistema, independente do contexto
  + **Último RA**: Neste campo aparece o digito final do último RA cadastrado, lembrando que este valor pode ser editado. Caso o usuário altere o valor o próximo aluno cadastrado no sistema terá como digito final um valo posterior ao informado.  
    ***Exemplo:*** O último RA cadastrado tem como último digito '7' (RA-00007); O usuário altera o valor do campo 'último número' para '9'; O próximo aluno é cadastrado no sistema e o RA dele é registrado com final '10' (RA-00010)
* **Por Curso:** Cada curso pode definir sua própria mascara definida no cadastro de cursos. Cada curso terá seu próprio número sequencial; Para visualizar/editar o valor do último RA de cada curso basta clicar no botão 'curso' disponível na tela de parâmetros.
* **Por Nível de Ensino:** Cada nível de ensino pode ter uma máscara de RA distinta. O padrão mais usado é o de numero sequencial (ex: ES-####). Para facilitar a contagem o sistema permite ao usuário visualizar/editar o valor do último RA de cada nível de ensino. Para isto, basta clicar no botão 'nível de ensino' disponível na tela de parâmetros.

*Links complementares:* *Aluno**-**Cursos* *-* *Niveis de ensino*

**Não usar histórico estruturado por grupo de série:**

Este parâmetro somente está disponível para o ensino básico. Quando marcado, o sistema não leva em consideração a posição das disciplinas na parte do histórico, ou seja, as disciplinas podem estar em qualquer posição na parte do histórico.

**Utilizar disciplinas de mesmo grupo de série em partes de histórico diferentes:**

Este parâmetro somente está disponível para o ensino básico a partir da versão 12.1.19. Quando marcado, é possível que disciplinas de mesmo grupo de série possa estar configurada para partes diferentes do histórico.

*Links complementares:* *Histórico Escolar - Ensino Básico - Partes do Histórico*
