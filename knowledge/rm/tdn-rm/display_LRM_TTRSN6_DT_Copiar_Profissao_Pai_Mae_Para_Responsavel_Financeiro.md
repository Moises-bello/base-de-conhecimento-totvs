---
content_hash: fd447bcc0c9dea5d0e70a1af0195ecb60dbf32e1f72e81d7c1f4eacf38026cab
fetched_at: '2026-06-29T00:06:19.686888+00:00'
page_id: '221545086'
product: rm
source: tdn-rm
title: TTRSN6_DT_Copiar_Profissao_Pai_Mae_Para_Responsavel_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TTRSN6_DT_Copiar_Profissao_Pai_Mae_Para_Responsavel_Financeiro
version: 1
---

# CADASTRO DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Cadastro do aluno: cadastrar pai ou mãe como responsável financeiro.* |
| **Situação/Requisito:** | *O botão de cópia de pai ou mãe para responsável financeiro não copia a profissão. Isto ocorre porque ao recuperar a pessoa (pai ou mãe) do Gestão de Pessoas*  *para setá-lo(a) como responsável financeiro não é passado o código da profissão para o Financeiro, além de que o Financeiro não está preparado para salvar esta*  *informação passada pelo Educacional.* |
| **Solução/Implementação:** | *Implementar no Financeiro gravação do campo código da profissão (FCFO.CODPROF) passado pelo Educacional, além de implementar no Educacional a*  *passagem do referido campo.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.8.* |
| **Versão Corrigida:** | *12.1.8.* |
| **Versão Expedida:** | *12.1.8.* |

divs
