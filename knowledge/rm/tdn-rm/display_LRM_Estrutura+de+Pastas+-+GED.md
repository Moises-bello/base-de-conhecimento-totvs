---
content_hash: 1ada9f85f2448fa7837b5c2a661a475592f5ca30bad9c475dcfc0e64293b5414
fetched_at: '2026-06-29T00:10:43.749731+00:00'
page_id: '550331582'
product: rm
source: tdn-rm
title: Estrutura de Pastas - GED
type: documentation
url: https://tdn.totvs.com/display/LRM/Estrutura+de+Pastas+-+GED
version: 5
---

## Padrão para as entidades: SESI e SENAI

| **Processos**  **Módulo: Totvs Educacional** | **Tela do SGE** | **Pasta no GED** | **Nome do Arquivo** |
| --- | --- | --- | --- |
| **Acompanhamento do Aluno**  **Certificação de Competência** | **Aluno** | **Documentos do Aluno** | Será criada uma subpasta com o RA do Aluno. |
| **Matrícula** | **Matrículas no Período Letivo** | **Matrículas** | Será criada uma subpasta com o RA do Aluno. |
| **Bolsas e Descontos** | **Contrato** | **Financeiro do Aluno** | Será criada uma subpasta com o RA do Aluno e Nome do Arquivo conforme o processo:   * Bolsa; * Contrato; * Termo de Compromisso. |
| **Rendimento Escolar**  **Conselho de Classe**  **Plano de Situação de Aprendizagem** | **Turmas/Disciplinas** | **Documentos das Disciplinas da turma** | Será criado uma subpasta com o Código da Turma/Disciplina e o Nome do Arquivo conforme os relatórios:   * Diário de Classe; * Ata de Resultados Finais; * Conteúdo Programático; * Registro de Avaliações; * Registro de Frequência; * Plano de Situação de Aprendizagem.   **Observação:** Cada arquivo deverá ser salvo com o Nome + Sequencial.  Pois poderão haver mais de Diário de Classe para uma mesma Turma/Disciplina.  **Exemplo:** Diário de Classe 01. |
| **Projeto de Curso** | **Matriz Curricular** | **Projeto de Curso** | Código do Curso + Código da Matriz Curricular. |
| **Projeto de Curso** | **Matriz Aplicada** | **Avaliação do Curso** | Código da Turma + Código do Período Letivo. |
| **Planejamento Escolar** | **Calendário** | **Calendário** | Código do Calendário + Código da U.O.\* + Código do Período Letivo.  *\*U.O. - Corresponde ao Código da Filial cadastrado no TOTVS Educacional (SGE).* |
| **Planejamento Escolar** | **Disciplina da Matriz Curricular** | **Plano da Unidade Curricular** | Código da U.O.\* + Código do Período Letivo.  *\*U.O. - Corresponde ao Código da Filial cadastrado no TOTVS Educacional (SGE).* |
