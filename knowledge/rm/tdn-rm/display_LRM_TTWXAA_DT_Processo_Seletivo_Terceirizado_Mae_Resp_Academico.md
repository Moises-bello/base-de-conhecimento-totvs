---
content_hash: e5bd89a1661336176b91cffc1dba8b52dae03e1dec77243f4ac975614956f823
fetched_at: '2026-06-29T00:06:22.361398+00:00'
page_id: '223915492'
product: rm
source: tdn-rm
title: TTWXAA_DT_Processo_Seletivo_Terceirizado_Mae_Resp_Academico
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWXAA_DT_Processo_Seletivo_Terceirizado_Mae_Resp_Academico
version: 120
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Educacional |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Processo Seletivo Terceirizado* |
| **Situação/Requisito:** | *1) Ocorre o seguinte erro ao final do processo: Não foi possível efetuar a matrícula do candidato(a) do processo seletivo.  Candidato(a): [Nome do Candidato]  Motivo: Responsável Acadêmico não é a Mãe do aluno.*  *2) Quando Sistema está configurado para gerar usuário mesmo se aluno não estiver matriculado, ocorre erro informando que o aluno não possui matrícula. Isto não corresponde à realidade porque este processo é responsável por criar o aluno e efetuar a sua matricula.* |
| **Solução/Implementação:** | *Ajustes no processo seletivo terceirizado para criar o responsável acadêmico do aluno corretamente e gerar seu usuário automaticamente conforme parametrização.* |
| **Conversores e Parâmetros:** | *Educacional | Geração de Usuários | Aluno | Gerar usuário automaticamente ao criar aluno.*     *Educacional | Geração de Usuários | Aluno | Parâmetros comuns: Gerar usuários para alunos sem matrícula no período letivo.* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8.115*  *12.1.9* |

divs
