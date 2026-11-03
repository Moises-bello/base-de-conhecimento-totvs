---
content_hash: 0afa09dce59b03e67dbcdf3730c9d68e93538113c8f714206727de2f07f6af90
fetched_at: '2026-06-29T00:05:56.034626+00:00'
page_id: '149881326'
product: rm
source: tdn-rm
title: Excluir lotes contábeis integrados ao RM Saldus (Delphi)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881326
version: 1
---

| Produto | **RM** |
| --- | --- |
| **Sintoma** | **Excluir lotes contábeis integrados com RM Saldus mas, não estão integrados ao lote zero (Delphi).** |
| Solução | 1. Verifique se lote contábil está no RMLabore e no RMSaldus. 2. Identificado que os lotes estão integrados, é necessário que seja feito a integração com lote “0”. Para realizar a mesma basta selecionar o lote contábil no (SALDUS) ir em “Processos | Integração de lotes” 3. No RMLabore é necessário realizar a solicitação de tarefa. A mesma é executada através do menu “CADASTRO” -> “CONTABILIZAÇÃO” -> “SOLICITAÇÃODATAREFA.NET” 4. Selecione o lote na tela que surgir 5. Após executar a solicitação de tarefa no RMLabore, acessar o RMSaldus. No menu “Utilitários -> Tarefas -> Permissões” é necessário liberar permissão para usuário na “Exclusão Contabilidade Lote Zero” 6. Após adicionar permissão para usuário favor acessar o menu “Utilitários -> Tarefas -> Gerenciador”, a solicitação de tarefa realizada estará localizada, basta selecionar a mesma acessar “Processos -> Executar Tarefa”. |
