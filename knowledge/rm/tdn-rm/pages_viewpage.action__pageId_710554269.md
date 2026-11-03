---
content_hash: 33f7a8d66174f740c1de649e11e480f0d8d1b1fa2139ce66d7a8ee3825670fd3
fetched_at: '2026-06-29T00:11:25.530707+00:00'
page_id: '710554269'
product: rm
source: tdn-rm
title: 01 - Período letivo de Planejamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=710554269
version: 46
---

O período letivo de planejamento é o início do processo para criar um nova oferta, nele será possível vincular o novo .

A permissão para ter acesso a este menu no portal pode ser encontrada no caminho abaixo.

**Acessar RM.exe I Menu | Serviços Globais | Perfil | Educacional | Acesso ao Menus | Educacional | Educacional (Portal) | Gestão Educacional | Gestão de ofertas | Período letivo de planejamento**

O cadastro no portal possibilitará o vinculo de apenas um período letivo acadêmico, que será o período letivo base para a criação da oferta. Este período letivo não poderá estar encerrado e deverá ter o campo "período letivo anterior" informado.

Não será possível ter dois períodos letivos de planejamento com o mesmo código. Além disso, um período letivo acadêmico somente poderá estar vinculado a um período letivo de planejamento.

O  campo ***"Demanda de alunos do 1º período"***, tem como finalidade gerar a demanda regular para as disciplinas do 1º período no passo de . Ao salvar o cadastro se este campo for deixado vazio, o mesmo será automaticamente preenchido com zero.

O campo ***"Mínimo de disciplinas demandadas pelo aluno"***, define o número mínimo de disciplinas que o aluno deve ter na sugestão antes que o sistema inclua disciplinas do próximo período, além do inicialmente recomendado.

* **Exemplo:** O aluno está no 3º período e possui uma disciplina pendente do 1º período. O sistema gera demanda para a disciplina do 1º período e para as disciplinas do 4º período. Supondo que o aluno já tenha concluído, eliminado, todas as disciplinas do 4º período, a demanda é gerada apenas para a disciplina que ele deve no 1º período.

           No contexto acima, se a nova parametrização estiver configurada como 2, e como no 4º período o aluno não possui disciplinas pendentes, o sistema irá gerar demanda do aluno para as disciplinas do 5º período.

           Caso o aluno não tenha mais períodos à frente ou número de disciplinas pendentes suficientes, pois está prestes a concluir o curso, a demanda das disciplinas será gerada até o máximo de disciplinas encontradas que atendam à regra.

           Por default este campo está configurado com 1.

**Atenção:** Ao informar o valor deste campo, não informar valor superior à quantidade média de disciplinas por período da grade para que o sistema não gere demandas de disciplinas de um período a mais do que realmente seria a demanda do aluno.

O campo ***"Validar pré-requisitos"*** marcado faz com que o sistema verifique se existe pré-requisito em alguma disciplina do próximo período, e existindo só irá gerar a [demanda](https://tdn.totvs.com/display/LRM/01+-+Executar+demanda) caso o aluno esteja cumprindo os critérios.

Os pré-requisitos são cadastrados nas disciplinas da matriz curricular.

Os tipos de pré-requisitos são:

* Número mínimo de créditos acadêmicos
* Número mínimo de disciplinas
* Carga horaria da disciplina
* Requisitos, no anexo da disciplina da grade
* Por formula de pré-requisitos

Observação: Para alunos em disciplinas que ainda não estejam aprovados (resultado final), porém que estejam em curso (situação de matrícula que indica **É uma disciplina em curso**), serão contabilizados para a validação do pré-requisito cumprido.

O agrupamento ***"Permite atualização e regeração da oferta"*** é utilizado para possibilitar que o usuário, faça alterações em uma oferta que já foi gerada (dentro dos critérios de cada combo-seleção) e posteriormente faça o reprocessamento dessa oferta gerando uma nova oferta com as edições feitas.

Para mais informações a respeito do professor da turma/disciplina com folha de pagamento aprovada, ver: .

O campo ***Situação*** refere-se ao status de período letivo de planejamento, que pode ser: Em planejamento; Inativo ou Finalizado. Por default o status "Em planejamento", já está informado.

**Observação:** Apenas os períodos letivos que estão com status "Em planejamento" ficam disponíveis para seleção no lockup, em planejamento de ofertas, para ser planejado.

Ao acessar a visão do cadastro do período letivo no TOTVS educacional é possível visualizar o status do período letivo.

Após realizar o preenchimento das datas nas etapas do planejamento a aba "Planejamento de oferta" ficará visível no cadastro do período letivo do TOTVS Educacional exibindo as informações somente para visualização.
