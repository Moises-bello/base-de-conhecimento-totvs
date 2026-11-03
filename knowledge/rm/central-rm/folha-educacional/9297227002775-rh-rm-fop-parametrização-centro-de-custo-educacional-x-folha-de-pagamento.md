---
article_id: 9297227002775
category: Folha Educacional
content_hash: b1cacfa8e0ba71c7740317319a7cac23df9d344cb8895a8c0901a0b0ec30d19a
fetched_at: '2026-06-28T22:46:57.168858+00:00'
product: rm
section_id: 1500000861082
source: central-rm
title: 'RH - RM - FOP - Parametrização Centro de Custo: Educacional x Folha de Pagamento'
type: support-article
updated_at: '2024-10-18T15:54:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9297227002775-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-Centro-de-Custo-Educacional-x-Folha-de-Pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:08:36 min  
  
Dúvida**  
Como realizar parametrização centro de custo Educacional x Folha de Pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Os valores que serão gerados pelo TOTVS Educacional ao TOTVS Folha de pagamento, podem ser destinados a um centro de custo que será parametrizado para cada uma das três atividades de pagamento. O preenchimento dos centros de custos nestas atividades não são obrigatórias, onde esse rateio poderá ser feito posteriormente no TOTVS Folha de pagamento.

* Atividade Extra

Informamos o centro de custo na atividade extra durante o cadastro da atividade extra para o professor. Caso esse campo esteja com um centro de custo preenchido, todo o valor a ser calculado para o professor no TOTVS Folha de pagamento por ministrar esta atividade será gerado para esse centro de custo informado.  
  
Acesse: **Currículo e Oferta / Professores / Anexo: Atividade Extra / Aba: Campos disponíveis.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10110857034519)**

* Atividade Ofertada

O centro de custo na atividade ofertada é buscado do grupo de atividade que é informado na modalidade durante o cadastro da atividade ofertada. Esse grupo de atividade é o mesmo cadastrado para a atividade extra. Todo o valor a ser calculado para o professor no TOTVS Folha de pagamento por ministrar esta atividade ofertada será gerado para este centro de custo. (Vide “Como Fazer - Atividades Ofertadas (Cadastro, Inscrição Presencial e Inscrição Portal)” –Parte de cadastros)  
  
Acesse: **Atividades acadêmicas / Atividades Ofertadas / Edite: Modalidade /Edite: Grupo de Atividade  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9300136624407/mceclip0.png)**

* Turma disciplina

O sistema calcula valores a serem pagos para os professores por ministrar aulas em turmas/disciplinas oferecidas pela instituição. Para que esse valor seja destinado a um centro de custo no TOTVS Folha de

pagamento, é necessário parametrização no TOTVS Educacional.

Temos a possibilidade de buscar o centro de custo vinculado à matriz aplicada da turma disciplina que o professor ministra ou diretamente da turma disciplina.

Marque o parâmetro “Ratear pagamento de professores da turma disciplina por Centro de Custo” e depois selecione a origem desejada “Turma” ou “Matriz Aplicada da turma” para que o processo descrito acima possa ser utilizado.  
  

Acesse: ****Configurações / Parâmetros / Integração / Folha  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9300337235607/mceclip1.png)****

Quando utilizado a origem **Matriz Aplicada a Turma**.

O sistema irá utilizar o centro de custo vinculado a Matriz Aplicada da turma disciplina.

Exemplo: se o professor estiver em 5 turmas/disciplinas distintas de matrizes aplicadas diferentes, o sistema irá ratear o valor de acordo com o centro de custo cadastro na matriz aplicada da turma. Na imagem abaixo, a matriz aplicada da turma recebeu um centro de custo denominado “TI”.

Para cadastrar o centro de custo, verifique no cadastro da turma do professor qual a matriz aplicada correta, acesse o seu cadastro, e informe o centro de custo.

Acesse: ****Currículo e Oferta / Matrizes Curriculares/ Anexo: Matriz Aplicada  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9300583763223/mceclip3.png)****

Quando utilizado a origem da Turma.

O sistema irá utilizar o centro de custo vinculado à turma disciplina que o professor está vinculado.

Exemplo: se o professor estiver em 5 turmas/disciplinas distintas, o sistema irá ratear o valor de acordo com o centro de custo cadastro em cada turma disciplina.   
  
Na imagem abaixo, a turma disciplina recebeu o mesmo centro de custo, denominado “TI”.

Para cadastrar o centro de custo da turma, acesse o seu cadastro e preencha o campo.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9301091251991/mceclip4.png)  
  

Durante a parametrização da integração com o TOVS Folha de pagamento, ainda temos os parâmetros “Turmas livres utilizam o centro de custo da disciplina da turma” que trabalha de forma complementar ao parâmetro “Origem do centro de custo” e o “Associar evento RM Labore à disciplina”.

Como explicado no item anterior temos a possibilidade de poder buscar o centro de custo para fazer o rateio do salário do professor da turma/disciplina ou matriz aplicada da turma/disciplina. Mas quando é uma turma livre - turma que não possui matriz aplicada - e o sistema está marcado para utilizar o centro de custo da matriz, o sistema não sabe de onde utilizar.

Com a utilização do parâmetro “Turmas livres utilizam o centro de custo da disciplina da turma”, o sistema vai utilizar o centro de custo da turma/disciplina quando for turma livre.

Acesse: **Configurações / Parâmetros / Integração / Folha  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9301176993815/mceclip5.png)**

O parâmetro “Associar evento RM Labore à disciplina” quando marcado irá utilizar o evento cadastrado na disciplina, durante o processo de “Associação dos eventos por disciplina” no TOTVS Folha de pagamento. Quando não marcado ela irá obedecer aos eventos cadastrados durante o “Agrupamento Salarial”. Tal parâmetro trabalha em conjunto com outro existente no folha de pagamento “agrupamento salarial por disciplina”.

Acesse: **Configurações / Parâmetros / Integração / Folha  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9301206591127/mceclip6.png)**

**Saiba Mais:**  
[Como fazer EDU](https://tdn.totvs.com/display/LRM/Como+Fazer+-+Edu?preview=%2F4814795%2F73400764%2FIntegra%C3%A7%C3%A3o+TOTVS+Educacional+x+TOTVS+Folha+de+Pagamento+%28Utiliza%C3%A7%C3%A3o+de+Sal%C3%A1rio+composto%29.pdf)
