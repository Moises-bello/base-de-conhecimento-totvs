---
content_hash: f0bfa52134d1dbdf59400846aaaedf23a92e68ca3e609f7817cf1a9a2f43f706
fetched_at: '2026-06-29T00:08:16.196491+00:00'
page_id: '244928915'
product: rm
source: tdn-rm
title: RMPAT00003 _Desfazer Contabilização de Depreciação/Correção Monetária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244928915
version: 10
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.16 ou superior |
| **Ocorrência:** | Desfazer Contabilização de Depreciação/Correção Monetária |
| **Ambiente:** |  |
| **Passo a passo:** | Este processo permite que a contabilização, integrada ou não ao lote zero do Totvs Gestão Contábil seja excluída. De forma que o processo de [Contabilização de Depreciação/Correção Monetária](https://tdn.totvs.com/pages/viewpage.action?pageId=244926024) seja executado novamente.  Acesse o **Menu Contabilização | Depreciação/Correção | Desfazer Contabilização**.  Deve-se selecionar qual o cenário de cálculo para qual a exclusão será realizada.    Selecionando a opção de **Excluir** os lançamentos contábeis já enviados para o sistema contábil armazenados no lote "N" definido no processo de integração contábil, ou somente gerado o processo de contabilização, mas não integrado, deve se executar o processo de  **Desfazer Contabilização | no Assistente de Exclusão da Contabilidade da Depreciação/Correção deve ser marcado a opção | Excluir |*.*** Caso os lançamentos já tenham sido integrados ao **lote zero da contabilidade** deve ser executado o processo **Desfazer Contabilização**, no Assistente de Exclusão da Contabilidade da Depreciação/Correção deve ser marcada a opção **Excluir via Tarefa**. Essa opção cria uma Tarefa que deve ser executada pelo usuário do TOTVS Gestão Contábil.    Caso seja apresentado algum erro no processo de Exclusão via tarefa, verifique o log.    No TOTVS **Gestão Contábil** deve acessar **Utilitários / Gerenciador,** criar um filtro conforme desejado, selecione a **Tarefa | Processos | Executar Tarefa** para excluir a Contabilização de Depreciação/Correção Monetária.    Caso este erro seja apresentado:    Acesse no Gestão Contábil o **Menu | Utilitários | Permissões | Selecione um item de cada vez | Editar | Incluir | Informe o respectivo usuário |** **Salvar.**    Em seguida execute a Tarefa novamente. Após executar a tarefa verifique o log. |
| **Observações:** |  |
