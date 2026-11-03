---
content_hash: a73cc9ea6d9e25c3bcbc0f6cd7b784bc53eb52744f378a0a21e6e6570d387e4e
fetched_at: '2026-06-29T00:06:23.922347+00:00'
page_id: '224108196'
product: rm
source: tdn-rm
title: TUAJSL_Atributo_Segurança_TBC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224108196
version: 124
---

# Atributo de Segurança nos DataServers

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS EDUCACIONAL* |
| **Função:** | *Segurança* |
| **Situação/Requisito:** | *Segurança de acesso aos DataServers através do WebService (TBC)* |
| **Solução/Implementação:** | *A partir da versão 12.1.8 foi realizado pela Framework da linha RM a verificação de atributos de segurança existentes nos DataServers para validar a permissão do usuário através do acesso pelo TBC.*  *Na versão 12.1.8 alguns dataServers ainda não possuem a tag de segurança, causando a seguinte mensagem de erro para o usuário:*     Ocorreu um erro ao efetuar a leitura do registro: Não foi encontrado o atributo de segurança no NomeDataServer.  **A partir da versão 12.1.9, todos os dataservers possuem os atributos de segurança definidos.** **Já na versão 12.1.8, foi realizado apenas para os principais DataServers.**  **Alguns DataServers adicionais também receberam as definições de segurança, solucionando o problema acima.**  EduHistoricoFinanceiroData.cs EduCursoHistoricoData.cs EduDisciplinaHistData.cs EduGrupoHistData.cs EduHistAlunoColData.cs EduHistDiscFacData.cs EduHistoricoEBData.cs EduHistoricoEnsSupData.cs EduComplDiscData.cs edit EduFrequenciaDiariaData.cs EduNotaAvaliacaoAlunoData.cs EduNotaAvaliacaoData.cs EduNotaEtapaAlunoData.cs EduNotaEtapaData.cs EduNotasData.cs EduHorarioProfessorData.cs EduHorarioTurmaData.cs EduLogProfessorTurmaData.cs EduProfessorTurmaData.cs EduFuncaoProfessorData.cs EduOcorrenciaProfessorData.cs EduProfessorData.cs EduProfessorFilialData.cs EduTurmaProfessorData.cs EduDocumentoData.cs EduHorarioData.cs EduTipoMatriculaData.cs EduTurnoData.cs EduDOCALUNOData.cs EduIrmaosData.cs EduResponsavelAlunoData.cs EduTipoAlunoData.cs EduTipoResponsavelData.cs EduAtividadeAlunoData.cs EduAtividadeData.cs EduBoletoData.cs EduParcPlanoData.cs EduPlanoPgtoData.cs EduResponsavelContratoData.cs EduResponsavelData.cs EduServicoPlanoPgtoData.cs EduTipoIngressoData.cs EduEtapasData.cs EduSubTurmaData.cs EduHoraAulaData.cs EduQuadroHorarioProfData.cs EduAtendimentoData.cs |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.8.120* |
| **Versão Expedida:** | *12.1.8.120* |

divs
