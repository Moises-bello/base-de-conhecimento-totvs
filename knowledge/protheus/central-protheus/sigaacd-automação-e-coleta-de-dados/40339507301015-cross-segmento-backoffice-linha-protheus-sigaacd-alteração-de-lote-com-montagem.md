---
article_id: 40339507301015
category: SIGAACD - Automação e Coleta de Dados
content_hash: 23edec04cffd51c9ef0bd7b2f40ce749a0325b50f6d769e5d0a0a7f2fa321f4c
fetched_at: '2026-06-28T22:39:11.360782+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Alteração de lote
  com montagem de carga
type: support-article
updated_at: '2026-05-08T22:46:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40339507301015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Altera%C3%A7%C3%A3o-de-lote-com-montagem-de-carga
---

Foi implementado um parâmetro chamado MV\_ACDELCG no sistema TOTVS Protheus para controlar a exclusão dos dados de montagem de carga ao alterar o lote na ordem de separação. Se configurado como .F., mantém os dados; se .T., exclui-os. Isso resolve o problema de perda de dados ao informar um lote diferente do sugerido.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40339472142103) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao realizar uma ordem de separação de um determinado produto que contém rastreabilidade e montagem de carga, ao informar um lote diferente do sugerido, os dados da montagem de carga estão sendo apagados.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Foi efetuado um tratamento no sistema para que os dados da montagem de carga sejam mantidos ao ser informado um lote diferente do sugerido na ordem de separação. Para que esse comportamento seja aplicado, foi criado o parâmetro MV\_ACDELCG. Quando este parâmetro estiver configurado como .F., os dados da montagem de carga são mantidos. Caso esteja configurado como .T., os dados são excluídos.

**Passos**

1. Acesse o ambiente e verifique se o parâmetro **MV\_ACDELCG** está criado.
2. Certifique-se de que o parâmetro possui o Tipo configurado como Lógico.
3. Valide se a Descrição está definida como "Define se a montagem da carga será excluída no estorno da liberação do pedido de venda.".
4. Ajuste o Conteúdo do parâmetro para .F. (**Não exclui**) para manter os dados, ou mantenha como .T.

    (**Exclui - Default**) caso deseje apagá-los.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[DTEXPRO-318 DT Alteração de lote com montagem de carga](https://tdn.totvs.com/pages/releaseview.action?pageId=751518835)
