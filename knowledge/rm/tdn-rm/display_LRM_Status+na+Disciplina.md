---
content_hash: c0ec789c1bfa87895cfecdedfd70a53f7edb02dc675b6185e23b907ed8a7a296
fetched_at: '2026-06-29T00:09:33.967586+00:00'
page_id: '425459097'
product: rm
source: tdn-rm
title: Status na Disciplina
type: documentation
url: https://tdn.totvs.com/display/LRM/Status+na+Disciplina
version: 13
---

# Descrição

Antes de efetuar a matrícula de um aluno em uma disciplina, o sistema verifica se a situação de matrícula do aluno no período letivo bloqueia inclusão/exclusão de disciplinas.

#### Conta como créditos cursados ou em curso

Utiliza-se para que a disciplina cursada pelo aluno com esse status de matrícula incremente os créditos em curso. A especificação do valor de créditos de cada disciplina é definida no campo N° de créditos do cadastro da disciplina.

#### Conta créditos financeiros (cobrança por crédito)

Utiliza-se para que o sistema gere os lançamentos de acordo com os créditos definidos da disciplina cadastrada.  
Para que o sistema gere lançamentos é necessário marcar a opção em Opções/Parâmetros/RM Classis/Pasta Integração com Fluxus - Dividir valor de créditos financeiros das disciplinas matriculadas entre as parcelas do contrato.

#### Abater valor da disciplina somente para parcelas com vencimento igual ou posterior a data de alteração da situação de matricula

No cadastro de situação de matrícula com esse parâmetro marcado, a disciplina não será cobrada apenas nas parcelas posteriores àquela data, ou seja, o valor anteriormente gerado não será devolvido ao aluno com desconto nas outras disciplinas.  
Caso o parâmetro esteja desmarcado o valor da disciplina será totalmente desconsiderado em todas as parcelas e o aluno terá direito a um crédito de valores cobrados anteriormente.    
Para mais informações sobre o comportamento desse parâmetro acesso o documento .

#### Bloqueia alteração de situação de matrícula nas disciplinas

Esse parâmetro bloqueia a alteração da situação de matrícula do aluno na disciplina. O sistema possui uma permissão especial localizada nos Parâmetros Educacionais no perfil do usuário. Essa permissão especial permite que o usuário associado a esse perfil altere a situação de matrícula do aluno.

#### Conta como aluno matriculado na turma

Sua função é dizer que o aluno está matriculado na turma e turma/disciplina. Existem diversas validações que olham para este parâmetros como por exemplo: choque de horário e validação de vagas.

A partir das versões 12.1.34.229, 12.1.2205.172, 12.1.2209.114 e 12.1.2302 este parâmetro passa a chamar **Conta como aluno matriculado na turma e turma/disciplina**e ele será marcado e desabilitado automaticamente assim que se marcar o parâmetros **é uma disciplina curso**, pois uma aluno com disciplina em curso é um aluno que conta como matriculado na turma e turma/disciplina.

#### É uma disciplina curso

Tem função de dizer que o aluno de fato está cursando uma determinada disciplina.

A partir das versões 12.1.34.229, 12.1.2205.172, 12.1.2209.114 e 12.1.2302 este parâmetro ao ser marcado irá marcar e desabilitar automaticamente o parâmetro **conta como aluno matriculado na turma e turma/disciplina**.

Para atender as situações de matrícula, de acordo com o layout definido pelo Diploma Digital na versão 1.05. Foi realizado a inclusão dos seguintes campos: Aprovado - Aproveitado, Aprovado - Validado, Aprovado - Cursado, Aprovado - Outra Situação, Pendente, Reprovado, na Situação de matricula - Diploma Digital. Essas alterações estão disponíveis  a partir das versões 12.1.2205.256, 12.1.2209.209, 12.1.2302.135.

A partir da versão 12.1.2306.159, foi alterado o parâmetro Não altera situação de matrícula na disciplina(apenas para matrícula on-line). Agora este parâmetro se aplica também para e matrícula em itinerários formativos no menu exclusivo, do Portal do Aluno.
