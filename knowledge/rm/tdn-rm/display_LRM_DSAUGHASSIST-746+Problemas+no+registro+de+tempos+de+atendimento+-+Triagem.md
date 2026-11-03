---
content_hash: 9aca997dc373b2b157360f472823a569e81f8894b15f21a7ad01685b10ac8d78
fetched_at: '2026-06-29T00:09:01.869693+00:00'
page_id: '378285406'
product: rm
source: tdn-rm
title: DSAUGHASSIST-746 Problemas no registro de tempos de atendimento - Triagem
type: documentation
url: https://tdn.totvs.com/display/LRM/DSAUGHASSIST-746+Problemas+no+registro+de+tempos+de+atendimento+-+Triagem
version: 1
---

# DSAUGHASSIST-746 Problemas no registro de tempos de atendimento - Triagem

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Totvs Gestão Hospitalar |
| **Função:** | Logs de triagem do atendimento |
| **Situação/Requisito:** | 1. Datas de registro nulas, principalmente para processo de geração de senha; coluna RECCREATEDON da tabela SZLOGATENDIMENTO; Paciente gerou nova senha de Atendimento  2.Falta de etapa de início de alguns processos Ex. Possui ”Término da Triagem” e não possui o “Início da Triagem” no atendimento;  3.Status de processos duplicados ,Tela possibilita erros de duplicação de status. Se abrir e fechar uma triagem, o registro “Início de Triagem” fica salvo no banco, porém a triagem ainda não foi feita. Quando for aberta novamente, irá ficar duplicado na tabela. Terá dois “Inícios” e um “Término”.  4. Diferença entre os status “Paciente gerou senha de Atendimento” e “Paciente gerou nova senha de Atendimento”.  5. Não existe uma lógica entre o código sequencial da tabela SZLOGATENDIMENTO (coluna “CODIGO”) e a data de inserção na tabela (coluna “RECCREATEDON). Qual a informação que precisamos considerar para ordenar os status cronologicamente? |
| **Solução/Implementação:** | 1: Correção do bug que não preenchia as devidas colunas quando a data do atendimento estava vazia ao invés de nula  2: Modificação para que sempre gere o inicio de atendimento no momento de criar um novo atendimento pelo painel de class. de risco.  3: Sempre que abria a tela gerava um novo inicio de triagem, agora só irá gerar log da primeira vez que for aberta.  4: Não se tratava de um bug, um dos status é gerado pelo totem quando o paciente pega senha e outro pelo registro de atendimento caso a senha seja alterada.  5: As datas estavam gravando em ordem errada por alguns lugares não possuírem os segundos nos horários, fazendo gravar sempre 00. |
| **Requisito:** | DSAUGHASSIST-746 |
