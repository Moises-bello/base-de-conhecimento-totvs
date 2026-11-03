---
content_hash: d2ceb7c12d0029a5bef7f3c9e7d07a1c82727a6c1f82f2ea671455d906d84ea7
fetched_at: '2026-06-29T00:09:53.556989+00:00'
page_id: '440843571'
product: rm
source: tdn-rm
title: EDUCACIONAL01-7434 DT Processo Imprimir Relatório com opção RM Reports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440843571
version: 1
---

# PROCESSO IMPRIMIR RELATÓRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Processo Imprimir Relatório |
| **Situação/Requisito:** | Não habilitava opção para imprimir relatório do RM Reports. |
| **Solução/Implementação:** | Otimização no processo “Imprimir relatório”. Serão listados relatórios do “RM Reports” caso tenha marcado no parâmetro Educacional | Secretaria | Relatórios”, campo “Tipo de relatório” igual a “RM Rports”. O sistema passa a habilitar na tela do processo a lista de parâmetros existentes no relatório selecionado.  Caso esteja configurado para gerar relatório “Gerador de Relatórios (Antigo)”, a tela do processo “Imprimir relatório” listará somente relatórios do antigo gerador.  \*\*Importante: Necessário recriar o arquivo \_Broker.dat.  A alteração foi realizada nos seguintes menu:  Curriculo e oferta | Alunos : Tabela SALUNO, Tipo Relatório = Alunos  Curriculo e oferta | Alunos | Anexos | Cursos/Habilitações : Tabela SHABILITACAOALUNO, Tipo Relatório = Histórico  Curriculo e oferta | Alunos | Anexos | Historico : Tabela SHISTALUNOCOL, Tipo Relatório = Histórico  Curriculo e oferta | Alunos | Anexos | Historico | Anexos | Disicplinas do histórico : Tabela SHISTDISCCOL, Tipo Relatório = Histórico  Curriculo e oferta | Professores : Tabela SPROFESSOR, Tipo Relatório = Professores  Curriculo e oferta | Turmas: Tabela STURMA, Tipo Relatório = Turmas  Curriculo e oferta | Turmas/Disciplinas : Tabela STURMADISC, Tipo Relatório = Turmas  Curriculo e oferta | Turmas/Disciplinas | Anexos | Professores : Tabela SPROFESSORTURMA, Tipo Relatório = Turmas – (Professores da turma/disciplina)  Curriculo e oferta | Turmas/Disciplinas | Anexos | Horários : Tabela SHORARIOTURMA, Tipo Relatório = Turmas – (Horários da turma/disciplina)  Curriculo e oferta | Turmas/Disciplinas | Anexos | Sub turma | Anexos | Horários da subturma: Tabela SHORARIOTURMA, Tipo Relatório = Turmas – Horários da subturmas (campo CODSUBTURMA)  Curriculo e oferta | Turmas/Disciplinas | Anexos | Sub turma | Anexos | Horários da subturma: Tabela SSUBTURMA, Tipo Relatório = Turmas - SubTurma das turmas disciplinas  Financeiro/Contabil | Contratos | Processos | Imprimir Boleto : Tabela FBOLETO, Tipo Relatório = Boleto  Financeiro/Contabil | Contratos | Processos | Imprimir Relatório : Tabela SCONTRATO, Tipo Relatório = Tesouraria |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
