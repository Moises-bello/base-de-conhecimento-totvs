---
article_id: 40671276763927
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b1839d481c4310825f6fb8c2fba3c2ee20c87d0d94d7e34b6bbf6c877ee21f80
fetched_at: '2026-06-28T22:38:55.496121+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro de chave duplicada
  na tabela NNS ao realizar solicitação de transferência
type: support-article
updated_at: '2026-05-22T18:18:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40671276763927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-de-chave-duplicada-na-tabela-NNS-ao-realizar-solicita%C3%A7%C3%A3o-de-transfer%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40671266770711) Tempo aproximado para leitura: 00**:**01:00 **min**  
  
**Dúvida**  
Ao realizar uma solicitação de transferência entre filiais por meio da rotina MATA311, o sistema apresenta a seguinte mensagem de erro no banco de dados: "Cannot insert duplicate key row in object 'dbo.NNS010' with unique index 'NNS010\_UNQ'."  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
O incidente ocorre devido a uma duplicidade ou inconsistência no controle de numeração do License Server para a tabela NNS (Solicitações de Transferência), fazendo com que o sistema tente inserir um registro utilizando um código que já existe no banco de dados. Para corrigir esse cenário, realize os seguintes passos:

* Reinicie os serviços do sistema (Appserver) e o License Server para garantir a correta sincronização e atualização dos contadores.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-?source=search)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Como definir o Preço de Venda do Pedido de Venda derivado do processo de Transferência entre Filiais ?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021390332-MP-SIGAEST-Custo-do-produto-derivado-do-processo-de-transfer%C3%AAncia-via-MATA311-)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
