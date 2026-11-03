---
content_hash: e007bc7fefd7fd03f4b265e7338a0ecd30ad4907eabcb6e6ef62de6742c3d425
fetched_at: '2026-06-29T00:08:57.352544+00:00'
page_id: '354456763'
product: rm
source: tdn-rm
title: Criação de Filtro por perfil com consulta sql
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354456763
version: 3
---

# Exemplo de criação de filtro por perfil com consulta sql

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1 |
| **Ocorrência:** | Criação de filtro por perfil |
| **Ambiente:** | Framework - Todas as versões do Sistema |
| **Passo a passo:** | 1. Acesse o perfil do usuário que deseja cadastrar o filtro com consulta sql; 2. Selecione o menu Filtro por Perfil: 3. Clique no Menu Incluir: 4. Selecione a tabela que deseja criar o filtro, neste exemplo, XEMPREENDIMENTO: 5. Clique em novo: 6. Adicione novo filtro, selecione o campo codigo do empreendimento, selecione o operador IN (SQL) e clique nas reticências para adicionar a consulta sql: 7. Crie uma consulta sql, conforme desejado, por exemplo:    SELECT CODEMPREENDIMENTO FROM XEMPREENDIMENTO WHERE COD\_PESS\_EMPR=100  **Importante:** A tela de filtro precisa que apenas um campo seja retornado, pois o sistema montará a grid com as informações. Neste exemplo, a consulta sql retorna apenas o código do empreendimento. Não se deve utilizar uma consulta retornando todos os campos, por exemplo: SELECT \* FROM XEMPREENDIMENTO, pois dessa forma será apresentado erro ao selecionar a visão. 8. Clique em ok para selecionar a consulta sql: 9. Clique em adicionar para aplicar a condição do filtro: 10. Informe o nome para o filtro: 11. Salve as configurações: 12. Será apresentado um aviso: 13. Salve as configurações do filtro: 14. Ao acessar o RM com o usuário que possui o filtro por perfil configurado, mesmo aplicando à visão a condição para retornar todos os empreendimentos, apenas o empreendimento do filtro será apresentado: |
| **Observações:** |  |
