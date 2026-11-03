---
content_hash: b658cb27ddffcb692fadd01c5da8659073ef0b3119e5079c482bfbc77265463a
fetched_at: '2026-06-29T00:09:34.051348+00:00'
page_id: '425459125'
product: rm
source: tdn-rm
title: Copiar Turmas entre períodos letivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459125
version: 14
---

Este processo copia turmas para outro período letivo, **desde que sejam períodos letivos diferentes**, ou seja, a origem e destino devem ser diferentes, **salvo uma exceção**, se na turma de origem tiver preenchido o **código da próxima turma** e o **período letivo** de **origem** e **destino** for **igual**, para que seja copiado é necessário marcar o parâmetro **utilizar código da próxima turma (origem) para cadastrar turmas de destino****.** Este parâmetro faz com que o código da próxima turma de origem seja o código da turma de destino, mas se caso ocorrer que duas ou mais turmas tenham o mesmo código somente a primeira será copiada.

É usual quando as turmas de um determinado período são semelhantes ao que o usuário necessita cadastrar. O assistente agiliza o trabalho, pois basta copiar as turmas e alterar o que for pertinente ao novo .

Pode ser copiado os seguintes dados:

* Data inicial e final da turma;
* Disciplinas;
* Etapas;
* Professores;
* Horários;
* Professores do horário;
* Campos complementares da Turma;
* Campos complementares da Turma/Disciplina;
* Data inicial e final de matrícula presencial;
* Data inicial e final de matrícula pelo portal;
* Demais dados do cadastro da turma, por exemplo, Campus/Polo.

A condição para que o processo funcione é ter  cadastrada para o período letivo de destino.

Na primeira etapa do processo define-se uma data inicial e final da turma de destino. Esta data será atribuída para a turma/disciplina, professores e Horários, caso marque o checkbox de Disciplinas, Professores e Horários na segunda etapa.

Se todas as datas (início e fim da turma, matrícula presencial e pelo portal) se não forem informadas no processo, serão cadastradas em branco para a turma de destino. Isso implica que mesmo que hajam datas cadastradas na turma e turma/disciplina de origem, essas não serão copiadas para a próxima turma. Somente as datas (inicial e final) dos professores serão copiadas da turma de origem, devido preenchimento da data inicial ser obrigatório. Outro ponto importante é que os professores só serão copiados para turma de destino para aquelas turmas/disciplinas que são semelhantes em ambas as matrizes curriculares.

Fique atendo para as turmas/disciplinas que não estão ativas, ou seja, aquelas que não possuem o chekbox de 'Ativa' marcado em sua identificação. Elas não serão copiadas pelo processo.

Quando é selecionado Disciplinas nos itens associados à turma é habilitado mais uma etapa no processo que permite ao usuário alterar a matriz aplicada da turma e suas disciplinas.

O parâmetro **permitir cadastrar avaliação,** na etapa do tipo notas. Caso a etapa já tenha avaliação cadastrada não será possível desabilitar o parâmetro. Ao optar por desmarcar o parâmetro o anexo avalições será desabilitado, não sendo possível a inclusão de avaliações.

As turmas serão copiadas para o período letivo de destino, mantendo os dados e configurações originais. Dessa forma, não serão realizados autoincrementos durante o processo de cópia, como por exemplo os relacionados aos contadores de turma, e os códigos das turmas copiadas do período letivo de origem serão os mesmos no período letivo de destino.

Informações Complementares

---

[Turma Disciplina](http://tdn.totvs.com/x/C-9bGQ)

[Professores da Turma Disciplina](http://tdn.totvs.com/x/X-tbGQ)

Veja Também

---

[Boletim Técnico cópia de turma entre período letivo](http://tdn.totvs.com/download/attachments/190514371/EDU_BT_Copiar_Turma_PL_PCREQ_3294.pdf?version=1&modificationDate=1434985023000&api=v2)
