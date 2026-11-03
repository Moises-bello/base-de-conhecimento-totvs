---
article_id: 360045160814
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 79123909075ecd72d3e626cf06aaf67bdf5363dead7d1fac34bd68fa3b1fb4e6
fetched_at: '2026-06-28T22:38:31.208101+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-Exclusão de cliente com movimentação '
type: support-article
updated_at: '2021-04-28T15:53:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045160814-MP-FAT-Exclus%C3%A3o-de-cliente-com-movimenta%C3%A7%C3%A3o
---

**Dúvida**

Foi habilitado o parâmetro **MV\_VALCNPJ** para impedir que ocorra inclusão de cliente (**MATA030**) e gere registros  duplicados.

Porém, em base, já há vários cadastros em duplicidade com movimentação de pedidos de vendas e títulos no financeiro, neste caso, qual seria o melhor procedimento para excluir os cadastros duplicados sem que perca a rastreabilidade dos pedidos, títulos e demais movimentações.  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 11.  
  
**Solução**

Não é possível a exclusão do cadastro com movimentação, o sistema nem irá permitir e exibirá a mensagem que o cliente não poderá ser excluído , pois a permissão de exclusão desses registros quebrará todo vínculo de movimentações podendo causar inconsistência de informações no banco de dados.  
  
Uma saída paliativa seria ativar o **bloqueio do registro** (**a1\_msblql**), assim, se algum usuário tentar incluir esses registro para novas movimentações, como um orçamento ou um pedido por exemplo, o sistema alertará que o registro está bloqueado.  
  
Observação: o bloqueio somente funcionará se houver foco no campo, tipo no momento que selecionar o registro bloqueado, se já estiver gravado e não tiver foco no registro, o sistema não validará o bloqueio.

Mais informações sobre bloqueio de registro pode ser acessado em: **[MP-FAT-Bloqueio-de-Registro-Cadastro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021216391-MP-FAT-Bloqueio-de-Registro-Cadastro)**
