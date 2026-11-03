---
content_hash: 469079d56eed37c63052e9850317a5e15bd3bfeb6ffdc0333cacb700517bb0a3
fetched_at: '2026-06-29T00:09:33.928614+00:00'
page_id: '425459086'
product: rm
source: tdn-rm
title: Alterar situação de matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459086
version: 11
---

Esta funcionalidade permite alterar a situação atual da matrícula do aluno, possibilitando a mudança do status de matrícula no registro do aluno, conforme necessidade de modificação, como por exemplo, quando um aluno está matriculado mas deseja trancar o curso. Permite ainda alterar a situação de matrículas por disciplina, onde por exemplo, algumas disciplinas podem estar com status cursando, outras dispensadas dentre outras possibilidades.

Para alterar a situação de matrícula do *Período Letivo*, o processo deve ser chamado através do anexo de 'Matrículas no Período Letivo', ou diretamente da listagem de Matrículas, pelo menu 'Matrículas e Avaliações'.  
Para alterar a situação de matrícula nas *Disciplinas* matriculadas, o processo deve ser chamado pela tela de visão ou edição de 'Matrícula em disciplinas'.  
   
Caso a alteração de situação de matrícula seja de *Período Letivo*, serão disponibilizados dois parâmetros na tela do processo:

* "*Propagar informações para todos os alunos*": Este parâmetro permite que, ao selecionar um número grande de alunos para realizar a alteração de situação de matrícula, quando marcado, esta situação de matrícula será automaticamente preenchida para todos os outros alunos selecionados.
* "*Cancelar lançamentos em aberto e não vencidos*": Será realizado o cancelamento de lançamentos conforme descrito no parâmetro, caso contrário o sistema não irá cancelar os lançamentos gerados em aberto.

Quando optamos por cancelar os lançamentos financeiros em abertos e não vencidos, o sistema verificará se os respectivos boletos já foram remetidos e/ou registrados nos bancos, e caso já tenham sido, o cancelamento destes lançamentos não será permitido. Para que o cancelamento de lançamentos como estes, cujos boletos possuem status de remessa igual à ***'Remetido'*** ou ***'Registrado'*** possa ser realizado, é necessário que o parâmetro do sistema '*Cancelar Remessa automaticamente ao cancelar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado*' esteja marcado, assim, ao cancelar os lançamentos, as remessas serão automaticamente canceladas. Ressaltamos que estas remessas ficarão pendentes no módulo *TOTVS Gestão Financeira*, sendo necessário enviar para o banco a remessa de cancelamento dos boletos afetados. Este parâmetro se encontra em *Ambiente |* Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin-Geral 3/4.

Caso a *Situação de Matrícula* escolhida esteja parametrizada para gerar *Contrato,*a data do contrato será a data em que a situação de matricula for alterada.

Plano de pagamento associado ao prospect

Para mais informações referentes à prospecções, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=702373785).

A Situação de Matrícula possui diversos parâmetros que afetam a atualização do período letivo e das disciplinas. Antes de prosseguir, revise essas  para garantir que o comportamento do sistema esteja adequado ao esperado.

# **Ensino Básico**

## **Itinerário formativo**

Ao alterar a situação de matrícula do período letivo o sistema irá validar a quantidade de itinerários matriculados de acordo com o que foi parametrizado na .  
Um Itinerário formativo é dito como matriculado se a sua  atual do aluno, estiver com item "**Aluno ativo"** **marcado** na aba **Período letivo**.

Exemplo:

A Situação de matrícula "**Pré-matrícula"** está com o item **"Aluno ativo"** **desmarcado**.  
A Situação de matrícula "**Matriculado"** está com o item **"Aluno ativo"** **marcado**.  
Na **Parametrização por curso**, o número mínimo e máximo de Itinerário formativo está configurado como 1.  
  
Aluno com matrícula no período letivo com situação de **"Pré-matrícula"** e matriculado no Itinerário formativo também com situação de **"Pré-matrícula"**.  
Ao alterar a situação de matrícula do Período letivo do aluno de **Pré-matrícula** para **Matriculado**, o sistema irá barrar a alteração informando que:   
  - Aluno não possui o número mínimo de matrículas em itinerários formativos  
                      Matrículas: 0 - Mínimo: 1 - Máximo: 1.  
Ou seja, o aluno não está atendendo o mínimo exigido de Itinerário formativo e não realiza a alteração.

# **Atenção**

* O cadastro de '*Situação de matrícula*', disponível dentro do menu *Currículo e Oferta | Acadêmico*, possui vários parâmetros que serão consultados na realização do processo de 'Alteração da situação de matrícula', podendo inclusive, conforme esteja parametrizado, bloquear a mudança de situação para este status. Da mesma forma que nos '*Perfis*' de usuários, no anexo *Parâmetros educacionais | Gera*l, existem parâmetros que possibilitam a determinados usuários realizarem a mudança de situação de matrícula mesmo que através da validação do status a mudança fosse bloqueada.

* A execução deste processo pode estar vinculada à validação de inadimplência dos alunos. Para mais informações [clique aqui](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425459015).
