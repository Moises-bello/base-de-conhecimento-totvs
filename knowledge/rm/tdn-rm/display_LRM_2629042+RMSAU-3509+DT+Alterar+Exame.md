---
content_hash: ef6deca168402232ba4cbb2e139590b882eda252d980e27efd94b684492efd23
fetched_at: '2026-06-29T00:08:57.169980+00:00'
page_id: '353277762'
product: rm
source: tdn-rm
title: 2629042 RMSAU-3509 DT Alterar Exame
type: documentation
url: https://tdn.totvs.com/display/LRM/2629042+RMSAU-3509+DT+Alterar+Exame
version: 3
---

# INSERIR EXAME EM ATENDIMENTO EXTERNO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar. |
| **Função:** | Inserir exames no Registro de Atendimento Externo |
| **Situação/Requisito:** | Ao inserir mais de 20 exames para o mesmo atendimento e clicar em Registrar, o sistema apresentava um erro referente ao campo MNEMONICOS da tabela SZAMOSTRAS, informando que o limite de caracteres para o mesmo era de 100. |
| **Solução/Implementação:** | Realizado solicitação de script de alteração no banco de dados para alterar o tamanho do campo MNEMONICOS da tabela SZAMOSTRAS de 100 para 250 caracteres. |
| **Requisito:** | RMSAU-3509 |
| **Tickets relacionados:** | [2629042](https://totvssuporte.zendesk.com/agent/tickets/2629042 "Open ticket in Zendesk Support") |
