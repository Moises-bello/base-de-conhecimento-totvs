---
content_hash: 47e043392487633465a45e957974f1391f51de46c15f57efa660064dbce4b35a
fetched_at: '2026-06-29T00:09:10.851824+00:00'
page_id: '403049516'
product: rm
source: tdn-rm
title: 3561981 FINANCEIRO01-8537 DT Cli/For estrangeiro persiste parâmetro de permitir
  CPF/CNPJ global repetido em coligada distinta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403049516
version: 1
---

# Cliente/Fornecedor

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | C&P |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Cliente/Fornecedor |
| **Situação/Requisito:** | O sistema exibe a mensagem de erro a seguir, ao incluir um cliente/fornecedor global, com nacionalidade estrangeira, quando o campo CPF/CNPJ está em branco: "O Cliente/Fornecedor com CPF/CNPJ '''' já está incluído em outra coligada. Devido a parametrização do sistema, o mesmo não poderá ser cadastrado.". O sistema não deveria validar o campo CPF/CNPJ uma vez que o mesmo não será utilizado pelo cliente/fornecedor estrangeiro. |
| **Solução/Implementação:** | Otimização no processo de inclusão de cliente/fornecedor. Agora o sistema só valida o parâmetro 'Permite CPF/CNPJ de Cli/For Global repetido em coligada distinta' quando a nacionalidade for brasileira. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000060 |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
