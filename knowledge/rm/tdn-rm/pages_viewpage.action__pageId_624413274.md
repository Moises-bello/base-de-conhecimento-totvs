---
content_hash: e4843dc9399eddb3d75d3419a8f402e521f6714ec04cfae161b9393f1a992576
fetched_at: '2026-06-29T00:11:03.569384+00:00'
page_id: '624413274'
product: rm
source: tdn-rm
title: Contabilização de Alunos Ativos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624413274
version: 16
---

Esta funcionalidade permite verificar quantos alunos estão ativos no sistema e enviar para o license Server. Os registros são contabilizados na tabela SALUNOSATIVOS.

Para configurar o trace do license server acesse: 

# Regra de Contabilização

Para que um aluno seja considerado ativo é necessário que esteja matriculado em pelo menos uma disciplina que contenha na situação de matrícula um dos parâmetros marcados: **conta como aluno matriculado** ou **é uma disciplina em curso** e não pode ter resultado final nesta matrícula.

Além disso, o **período letivo** deste aluno precisa estar **ativo**, com a **data atual** sendo contemplada entre a **data inicial** e **data final** ou de **previsão de término**.

Matrícula na disciplina.

Comportamento depreciado

Versões inferiores aos patches 12.1.2402.239, 12.1.2406.173 e 12.1.2410.109 não se considerava a data de início do período letivo e não também não era considerado se a matrícula disciplina tinha resultado final.

# Contabilização Manual

Para que seja feita a contabilização de forma manual acesse: Atividades acadêmicas | Assistentes | Contabilização de Alunos Ativos e clique no botão **calcular total de alunos ativos**.

São **seis** contadores disponíveis:

* Total de alunos no curso. Vale ressaltar que se o aluno com mesmo RA estiver em dois cursos distintos, o mesmo será contado duas vezes.
  + Geral: contagem de todos os alunos ativos no curso.
  + Ensino básico: contagem de todos os alunos ativos no curso de nível de ensino com **apresentação** de ensino **básico**.
  + Ensino superior: contagem de todos os alunos ativos no curso de nível de ensino com **apresentação** de ensino **superior**.

* Total de alunos por RA. Vale ressaltar que se o aluno com mesmo RA estiver em dois cursos distintos, o mesmo **não** será contado duas vezes.
  + Geral: contagem de todos os alunos ativos por RA.
  + Ensino básico: contagem de todos os alunos ativos por RA no curso de nível de ensino com **apresentação** de ensino **básico**.
  + Ensino superior: contagem de todos os alunos ativos por RA no curso de nível de ensino com **apresentação** de ensino **superior**.

Comportamento depreciado

Versões inferiores aos patches 12.1.2402.239, 12.1.2406.173 e 12.1.2410.109 contém apenas um único contador.

# Contabilização Automática

Nativamente no Totvs Educacional, esta contabilização é feita de forma automática, por meio da execução de processo.

Por padrão a execução deste fluxo está **habilitada**, não sendo possível **desabilitar**.

Segue abaixo a imagem do fluxo de execução automática.

## Ações

### Carregar menu Educacional

Referente a qualquer carregamento do menu do TOTVS Educacional | Educacional ou troca de contexto dentro do módulo Educacional.

### Excluir agendamentos existentes do processo

Esta ação exclui todos os processos existentes no gerenciamento de jobs **apenas** para a classe deste processo que é a **EduAlunosAtivosProcData**.

### Criar novo agendamento

Nesta ação é criado um novo agendamento para a classe de processo **EduAlunosAtivosProcData**, sendo para iniciar no dia 01 do próximo mês às 01:00 com recorrência mensal.

## Decisões

### Cache de execução de fluxo

Existe um cache de 3 dias (por host) que indica se é para iniciar todo o fluxo do automatismo da métrica, ou seja, toda vez que algum usuário recarrega o menu Educacional é verificado o cache, se ele existir ele retorna se é para iniciar o fluxo ou não, caso ele não exista o fluxo é iniciado. Este cache tem por objetivo deixar o fluxo performático, ou seja, garante que fluxo não execute a todo momento que o usuário troque de contexto.

### Verificação de agendamento válido

Nesta ação é verificado se existe algum agendamento deste processo com recorrência mensal apto para execução ou se o processo está sendo executado neste instante. Se algum dos dois itens mencionados anteriormente forem verdadeiros indica que existe agendamento válido, caso contrário se os dois forem falso, não existe agendamento válido.

### Verificação de três camadas

Esta ação é verificado se o ambiente está configurado em três camadas.

### Existe registro

Nesta ação é verificado se existe ao menos um registro na tabela SALUNOSATIVOS.

### Existe registro no mês atual

Esta ação é verificado se existe ao menos um registro na tabela SALUNOSATIVOS para o **mês atual**.
