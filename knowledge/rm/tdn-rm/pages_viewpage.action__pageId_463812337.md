---
content_hash: a1885b137f1031a22790f412ad2f164fd69db421acc6be6e3b6ccda0a0c766a3
fetched_at: '2026-06-29T00:10:15.134667+00:00'
page_id: '463812337'
product: rm
source: tdn-rm
title: 05.1 - Seleção de Disciplinas do Ensino Superior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463812337
version: 46
---

**Este Menu está disponível apenas para o contexto ENSINO SUPERIOR.**

Esta step tem como objetivo exibir as disciplinas já selecionadas pela instituição e as que são elegíveis de seleção pelo aluno para realizar sua matrícula, sejam elas, obrigatórias, optativas/eletivas, extras ou equivalentes. Os detalhes da disciplina e turmas disponíveis serão exibidas no canto direito da tela ao clicar na disciplina.

A partir da versão 12.1.2506, foram adicionadas, nos detalhes da turma/disciplina, informações sobre a habilitação, as datas de início e término, além do campus.

Caso a situação de matrícula permita, o aluno pode incluir, mudar de turma ou excluir disciplinas.

Será exibido uma área com o resumo da matrícula, onde o aluno conseguirá visualizar a contagem das disciplinas selecionadas, créditos acadêmicos e financeiros.

Os créditos acadêmicos poderão ser ou não computados no somatório na matrícula, para verificar como é feito este somatório, .

### **1 - Validações de Erros**

Todos os erros encontrados na seleção das disciplinas serão exibidos no canto direito, no painel de validações, ao clicar em algum ícone de erro.

Para mais informações de como o choque de horário é validado .

### **2 - Quadro de Horários**

O quadro de horários será exibido já aberto ao acessar a tela. O aluno tem a opção de minimizar o mesmo, clicando no botão de "Minimizar" a direita do quadro de horários Será possível excluir e adicionar disciplinas no horário específico.

Adicionar disciplinas pelo quadro de horários

A opção de "Adicionar disciplinas" por dentro do quadro de horários, somente irá mostrar as disciplinas que estão na sugestão de disciplinas, que possui aula no horário selecionado.

A partir da versão 12.1.2506, foram adicionadas no quadro de horários as informações sobre o prédio, bloco e sala. Contudo, essas informações só serão exibidas caso o parâmetro "Exibir sala no quadro de horários" esteja habilitado.

### **3 - Disciplinas**

As informações da disciplina para matrícula será exibida em uma área do canto direto, após o aluno selecionar a disciplina desejada.

#### 3.1 - Selecionar uma Sub turma

A opção de selecionar uma sub turma será exibida no portal seguindo o critério definido na parametrização "Matricular em Sub Turmas".

 **TOTVS Gestão Educacional| Configurações| Parâmetros| RM Portal - Matrícula| Geral 5/5**

Segue abaixo as opções existente e suas respectivas situações

* Ao selecionar a opção de "Não permitir" o portal **não** irá exibir a opção para que o aluno possa selecionar uma sub turma.
* Ao selecionar a opção de "Permitido" o portal irá exibir uma lista de sub turma disponíveis para que o aluno possa selecionar o item desejado, porém esta opção **não é obrigatória**.
* Ao selecionar a opção de "Permitido com obrigatoriedade" o portal irá exibir uma lista de sub turma disponíveis para que o aluno possa selecionar o item desejado, porém esta opção **é obrigatória.**

Permitido com obrigatoriedadeMarcado a opção "Permitido com obrigatoriedade", o portal irá exibir uma lista de sub turma sem nenhum item selecionado por padrão, para não induzir o aluno avançar para a próxima etapa sem visualizar, ou selecionar o item desejado. Caso o aluno não selecione nenhum item da lista, o sistema irá exibir uma mensagem de erro no painel de validações  e impedir de avança para a próxima etapa.

#### 3.2 - Disciplina cancelada

Uma disciplina é dita como **cancelada** quando os parâmetros de situação de matrícula **conta como aluno matriculado na turma**e **é uma disciplina em curso** estiverem desmarcados.

Caso o aluno estiver com alguma disciplina **cancelada** conforme a regra acima, a mesma não irá aparecer no quadro de horários e nem nas disciplinas para matrícula, apenas irá aparecer no quadrante de sugestão de disciplinas. Caso o aluno tente matricular nesta disciplina **cancelada** poderá ocorrer dois caminhos, o primeiro é se for a mesma turma que o aluno já estiver com matrícula **cancelada** o sistema irá alterar a situação de matrícula desta disciplina, o segundo é se não for a mesma turma, com isso o aluno o sistema irá fazer uma inclusão de uma nova matrícula para a outra turma que foi selecionada. Em ambos caminhos será registrado no log de movimentação do aluno.

Entretanto se na situação de matrícula na disciplina **cancelada** estiver marcado o parâmetro **não altera a situação de matrícula na disciplina** a disciplina continua a não ser exibida no quadro de horários e nem nas disciplinas para matrícula, porém passa a não ser exibida no quadrante de sugestão de disciplinas, porque neste cenário não se quer que o aluno altere a situação de matrícula, com isso, a mesma não e exibida em nenhum lugar na matrícula do portal.

#### 3.3 - Disciplina trancada

Uma disciplina é dita como **trancada** quando os parâmetros de situação de matrícula **indica trancamento** estiver marcado e os parâmetros **conta como aluno matriculado na turma**e **é uma disciplina em curso** estiverem desmarcados.

Caso o aluno estiver com alguma disciplina **trancada** conforme a regra acima, a mesma não irá aparecer no quadro de horários e nem nas disciplinas para matrícula, apenas irá aparecer no quadrante de sugestão de disciplinas. Caso o aluno tente matricular nesta disciplina **trancada** poderá ocorrer dois caminhos, o primeiro é se for a mesma turma que o aluno já estiver com matrícula **trancada** o sistema irá alterar a situação de matrícula desta disciplina, o segundo é se não for a mesma turma, com isso o aluno o sistema irá fazer uma inclusão de uma nova matrícula para a outra turma que foi selecionada. Em ambos caminhos será registrado no log de movimentação do aluno.

Entretanto se na situação de matrícula na disciplina **trancada** estiver marcado o parâmetro **não altera a situação de matrícula na disciplina** a disciplina continua a não ser exibida no quadro de horários e nem nas disciplinas para matrícula, porém passa a não ser exibida no quadrante de sugestão de disciplinas, porque neste cenário não se quer que o aluno altere a situação de matrícula, com isso, a mesma não e exibida em nenhum lugar na matrícula do portal.

A partir da Versões: 12.1.2306.174, 12.1.2310.108 e 12.1.2402 ,foi incluída opção de realizar o cancelamento da disciplinas durante a matrícula no portal. 

Ao contrário do comportamento de excluir, ao cancelar uma disciplina o sistema não exclui ela do RM ,ele altera a sua [situação de matrícula](https://tdn.totvs.com/display/LRM/Aba+Portal), de acordo com a parametrização configurada na aba portal.

Acesse: Currículo Oferta| Acadêmico | Situação de matrícula| Portal 

As situações de matrícula disponíveis para seleção, são apenas as que estiverem com o parâmetro "É um status na disciplina" habilitado. E os parâmetros: "Conta como aluno matriculado na turma e turma/ disciplina", "É uma disciplina em curso" e "Trancamento da matrícula da disciplina", desabilitados.

A partir das versões: 12.1.2306.174,12.1.2310.108 e 12.12402, foi incluído o parâmetro "Ocultar Quadro de Horários na matrícula através do Portal" na [parametrização por curso](https://tdn.totvs.com/pages/viewpage.action?pageId=425458887).

Ao marcar o parâmetro "Ocultar Quadro de Horários na matrícula através do Portal" , o quadro de horários não será exibido na etapa de seleção de disciplinas durante a realização da matrícula.

Também ao marcar este parâmetro os horários das turmas/disciplinas deixarão de ser exibidos na área de detalhes da turma/disciplina na etapa de seleção de disciplinas na matrícula. Implementação disponível a partir da versões: 12.1.2306.245,12.1.2310.187,12.1.2402.123.

A partir da versão 12.1.2406 se o parâmetro **TOTVS Gestão Educacional| Configurações| Parâmetros| Secretaria| Geral 1/7| Usar grupo de disciplinas Optativas / Eletivas** estiver marcado, as disciplinas optativas e eletivas dentro do Grupo associado ao período (matriz curricular,) aparecerão como opções na matrícula quando houverem Grupos de disciplina Optativa/Eletiva com disciplinas cadastradas associados a matriz curricular do curso.

Note que as disciplinas optativa/Eletivas agora são exibidas dentro do seu Período correspondente.

Com a remoção das Optativas/Eletivas, o grupo foi renomeado para Disc. Equivalentes/Extras

### **4 - Simulação de pagamentos**

Será exibido neste step, o opção de simulação de pagamentos, mediante parametrização de exibição "Exibir a opção para simulação dos valores das parcelas". Ao selecionar a opção de "Simulação" será aberto uma aba, com os planos de pagamento parametrizados pela instituição que podem ser selecionados pelo aluno.

A simulação no Portal do Aluno projeta o valor integral das disciplinas sobre o plano de pagamento selecionado, desconsiderando lançamentos ou baixas prévios. Essa particularidade permite que o aluno visualize o custo real de sua grade acadêmica selecionada no momento da matrícula, demonstrando o cálculo das disciplinas selecionadas como se fossem geradas no momento da consulta.

 **TOTVS Gestão Educacional| Configurações| Parâmetros| RM Portal - Matrícula| Geral 5/5**

Plano de pagamento e bolsa associado ao prospect

Para informações referentes à prospecções, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=702373785).
