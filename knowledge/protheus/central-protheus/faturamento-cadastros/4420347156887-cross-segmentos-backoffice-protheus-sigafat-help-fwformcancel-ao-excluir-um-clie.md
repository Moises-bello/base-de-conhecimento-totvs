---
article_id: 4420347156887
category: Faturamento - Cadastros
content_hash: 951afb159efa113bf00529ba39860ec84e18323867eb4a28cf10d50dec74cd47
fetched_at: '2026-06-28T22:38:35.460903+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help FWFORMCANCEL ao excluir
  um Cliente
type: support-article
updated_at: '2026-04-02T11:32:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420347156887-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-FWFORMCANCEL-ao-excluir-um-Cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39468754080151) Tempo aproximado para leitura: **00:03:30min**  
  
**Dúvida**  
Ao excluir o cliente apresentou o help FWFORMCANCEL, como resolver?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**  
O help ocorre porque o cadastro do cliente está vinculado em outra rotina/tabela do sistema, para solucionar:

- Identifique a rotina/tabela que apresenta no help;  
- Verifique se é possível desvincular o cadastro do cliente da rotina da tabela que apresentou no help.

Exemplo:   
  
Caso o cliente já tenha faturado um pedido, terá que excluir as notas e pedidos, do contrário não será possível excluir o cliente, para manter a integridade dos dados.

Como contorno, existe o campo "**Status**" no cadastro do cliente, que permite alternar entre **ativo** e **inativo**, impedindo o uso em rotinas quando o status for inativo.

**Saiba mais:**  
[LGPD - Exclusão de Dados do Cliente Armazenados em Banco de Dados](https://tdn.totvs.com/pages/viewpage.action?pageId=637760248)
