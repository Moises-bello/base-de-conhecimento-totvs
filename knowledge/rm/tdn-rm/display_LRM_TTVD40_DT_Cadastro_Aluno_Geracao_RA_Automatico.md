---
content_hash: 1b3dd3ff3d3c37442d6abfa6c719059cbe1412109a14bc3fce770f9f584b448e
fetched_at: '2026-06-29T00:06:22.719508+00:00'
page_id: '223925945'
product: rm
source: tdn-rm
title: TTVD40_DT_Cadastro_Aluno_Geracao_RA_Automatico
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVD40_DT_Cadastro_Aluno_Geracao_RA_Automatico
version: 119
---

# CADASTRO DE ALUNO COM GERAÇÃO DE RA AUTOMÁTICO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Cadastro de aluno com geração de RA automático* |
| **Situação/Requisito:** | *Ao tentar criar um novo aluno, o ocorre o seguinte erro: "Período letivo corrente deve ser parametrizado".* |
| **Solução/Implementação:** | *Foram realizados testes sistêmicos onde foi identificado que, o ajuste no método que gera RA, para que exiba o erro, informando que é necessário o preenchimento do período letivo corrente na parametrização, ocorra somente se na máscara do RA existir um "&". A mensagem informativa para o usuário será: "Foi configurado uma máscara para geração automática do RA que necessita do preenchimento do período letivo corrente na parametrização (Configuração | Parâmetros | Secretaria | Período Letivo).". Caso contrário não será feita nenhuma validação ao cadastrar o aluno.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TU0572 |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.83.55*  *12.1.10* |
| **Versão Corrigida:** | *11.83.55*  *12.1.10* |
| **Versão Expedida:** | *11.83.55.201*  *12.1.10* |

divs
