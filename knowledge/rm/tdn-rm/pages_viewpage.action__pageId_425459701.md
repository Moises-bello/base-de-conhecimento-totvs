---
content_hash: 425dc5fa0a452701755a5181fe97994a57d716039b4593ae170964e5bc9075d9
fetched_at: '2026-06-29T00:09:38.065656+00:00'
page_id: '425459701'
product: rm
source: tdn-rm
title: Parâmetros - Matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459701
version: 16
---

---

Itens responsáveis por configurar os parâmetros dos processos de Matrícula do aluno no curso, Período letivo e Disciplinas. Composto por 9 etapas de configuração.

## **Geral 1/2**

Etapa 1 – Parâmetros gerais da matrícula;

## **Geral 2/2**

Etapa 2 – Parâmetros gerais da matrícula;

## **Movimento 1/4**

Etapa 3 – Movimentação de matrícula;

## **Movimento 2/4**

Etapa 4 – Movimentação de matrícula;

## **Movimento 3/4**

Etapa responsável por algumas configurações da matrícula em lista de espera e prioridade.

### Matricular em lista de espera caso as vagas estejam esgotas

Disponível apenas para o **Ensino Superior**, este parâmetro é responsável por dizer ao sistema se esgotar as vagas na turma/disciplina o aluno irá para lista de espera. A lista de espera consiste em uma situação de matrícula que é atribuído ao aluno caso não haja mais vagas para a turma/disciplina. Somente será possível habilitar este parâmetro se informar uma situação de matrícula que indica lista de espera.

Importante

A lista de espera apenas poderá ser utilizada no esgotamento de vagas da **turma/disciplina** e nunca para a **turma**, ou seja, o controle de lista de espera dos alunos é feita apenas quando a matriz curricular do aluno estiver parametrizada com o controle de vagas por disciplina da turma.

### Bloquear matrícula em lista de espera para disciplinas com Correquisito não cumprido

A partir das versões **12.1.31.264, 12.1.32.209, 12.1.33.133 e 12.1.34** o parâmetro Boquear matrícula em lista de espera para disciplinas com Correquisito **não concluído** passa a chamar Bloquear matrícula em lista de espera para disciplina com correquisito **não cumprido**.

Somente será habilitado para seleção caso o parâmetro: **Matricular em lista de espera caso as vagas estejam esgotadas** estiver habilitado, então se a matrícula em lista de espera estiver **ativa**, a disciplina em questão possua correquisito não cumprido e não possua vagas na turma/disciplina, o sistema bloqueia a execução do processo de matrícula informando que não há vagas e que a disciplina possui correquisito, caso o parâmetro esteja **marcado**.

Se a turma/disciplina selecionada não pertencer a matriz do aluno, será verificado se possui uma equivalência, caso possua, o sistema irá verificar os requisitos da disciplina equivalente da matriz do aluno, e caso tenha um requisito do tipo correquisito a matricula será bloqueada.

Vale ressaltar que mesmo não tendo cumprido o correquisito a matrícula em lista de espera será efetuada, porém ao tentar alterar a situação de matrícula deste aluno para uma que indica que é uma disciplina em curso, o sistema irá bloquear por não ter cumprido o correquisito. Por outro lado, se ele estiver **desmarcado**o sistema irá permitir a matrícula da disciplina em lista de espera.

**Validações para utilização deste parâmetro**

* + Caso o sistema esteja parametrizado para considerar a matriz do aluno para requisitos, o sistema verifica se a disciplina vinculada a turma/disciplina selecionada durante o processo de matricula possui requisitos e que a mesma seja do tipo correquisito.
  + É verificado também se a disciplina em questão possui requisitos no currículo individual do aluno do tipo correquisito.
  + Se a turma/disciplina selecionada não pertencer a matriz do aluno, é verificado se possui uma equivalência, caso possua, o sistema verifica os requisitos da disciplina equivalente da matriz do aluno, e caso tenha um requisito do tipo correquisito a matricula é bloqueada.
  + Se o sistema não estiver parametrizado para considerar a matriz do aluno, será considerada a parametrização dos requisitos de acordo com a grade da matriz vinculada a turma/disciplina.
  + Independente dos cenários citados, a disciplina possuindo requisito do tipo correquisito a matricula é bloqueada e apresentada a mensagem de "Não há vagas na turma informada. Disciplina com correquisito".

O parâmetro: "Desconsiderar pré-co-requisito na montagem da sugestão de turmas/disciplinas" deverá estar habilitado, para que o sistema carregue as disciplinas com pré-requisitos.

## **Movimento 4/4**

Etapa 6 – Movimentação de matrícula.

### **Trancamento do curso**

* **Trancar o curso no 1º período:** permite que o aluno possa trancar o curso no primeiro período.
* **Nº de períodos trancados:** número de períodos seguidos que o aluno pode ficar com o curso trancado.
* **Nº de trancamentos:** número de vezes que o aluno pode trancar o curso.

Para que o cálculo de número de períodos trancados seja feito corretamente é necessário que a sequência de períodos letivos cursados pelo aluno esteja correta. Essa sequência é montada através do campo de período letivo anterior no cadastro de período letivo. Também é necessário que o período letivo corrente esteja parametrizado corretamente.

## **Sugestão de Disciplinas 1/2**

Etapa 7 – Sugestão de disciplinas

## **Sugestão de Disciplinas 2/2**

Etapa 8 – Sugestão de disciplinas

## **Fórmulas Visuais**

Etapa 9 – Fórmulas visuais

**[Fórmulas Visuais](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425458554)**
