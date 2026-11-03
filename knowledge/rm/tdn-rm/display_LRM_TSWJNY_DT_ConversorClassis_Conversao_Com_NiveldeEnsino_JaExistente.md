---
content_hash: e1eda2bce5f32050fbb02fe7c1c6d531fd6bb07ab649263ca22d865325eaef53
fetched_at: '2026-06-29T00:06:03.473400+00:00'
page_id: '198954741'
product: rm
source: tdn-rm
title: TSWJNY_DT_ConversorClassis_Conversao_Com_NiveldeEnsino_JaExistente
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWJNY_DT_ConversorClassis_Conversao_Com_NiveldeEnsino_JaExistente
version: 4
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Conversor de Bases RM CLASSIS* |
| **Função:** |  |
| **Situação/Requisito:** | *Ajustar o produto à situações em que o RM Classis é operado em paralelo com o TOTVS Educacional , cada qual atendendo Níeis de Ensino distintos e se deseja migrar os dados do RM Classis para o TOTVS Educacional* |
| **Solução/Implementação:** | [ 1 ] - Instituição:  Passou a considerar os registros já criados diretamente no TOTVS  [ 2 ] - Disciplinas: Passou a verificar apenas a primeira posição da constante de tipo para definir o Tipo de Aula  O processo de criação de sufixos para códigos duplicados executado no ancestral do form  foi sobrescrito. A verificação passou a ser executada diretamente na tabela TEMPDISC e considera tambem os códigos já existentes na SDISCIPLINA.  [ 3 ] Formação Acadêmica:   O conversor de PROFESSORES passou a migrar os dados de Formação Acadêmica  [ 4 ] Pessoa:  Passou a migrar os dados TELEFONE, CELALUNO e CORRACA de EALUNOS para PPESSOA  [ 5 ] Campos Complementares: Corrigido erro na montagem da tabela dinamica na sentença do Conversor  [ 6 ] Etapas da Habilitação:   Passou a considerar como etapa final a de número ZERO  [ 7 ] Horario das Turmas:  Melhoria de performance  [ 8 ] Horarios do Professor: Melhoria de performance  [ 9 ] Matricula: Ajuste no processo em ORACLE para correção de matricula em disciplina equivalente |
| **Conversores e Parâmetros:** | cluMatricula, cluInstituicao, cluDisciplina, cluConversor, cluProfessor,cluPessoa, cluTurmaDiscCompl, cluTurmaCompl, cluAtividadesComplAlunoCompl, cluCursoCompl,cluModEtapaHabilitacao,cluHorarioProfessor, cluHorarioProfessor |
| **Chamados relacionados:** | *TSWJNY* |
| **Requisito (ISSUE):** | *Informe o requisito relacionado.* |
| **Versões/Release:** | *5.0.0.192* |
