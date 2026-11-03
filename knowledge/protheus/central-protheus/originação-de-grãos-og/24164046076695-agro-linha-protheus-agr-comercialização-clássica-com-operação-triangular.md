---
article_id: 24164046076695
category: Originação de Grãos (OG)
content_hash: 4cf0a8366703faaab4ed70f6c0501e8bc4c76b32d28729330434820f641632a7
fetched_at: '2026-06-28T22:45:36.851693+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR -  Comercialização Clássica com Operação Triangular
type: support-article
updated_at: '2026-02-27T17:49:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24164046076695-Agro-Linha-Protheus-AGR-Comercializa%C3%A7%C3%A3o-Cl%C3%A1ssica-com-Opera%C3%A7%C3%A3o-Triangular
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24164046032279) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como incluir uma **Comercialização Clássica com Operação Triangular**?  
  
**Ambiente**  
TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Veja na tabela os **Dados Gerais**;

| Produto: | TOTVS Agro Beneficiamento |
| --- | --- |

| Linha de Produto: | Linha Protheus |
| Segmento: | Agroindústria |
| Módulo: | Gestão de Agronegócio |
| Função: | OGA250 - Romaneio com Pesagem |
| Ticket: | 9516363 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DAGROCCO-3722 |

**2.** Acesse a rotina de **Contrato de Venda - OGA290**;

**3.** Inclua um **Contrato de Venda**.

**4.** Será necessário informar os campos código e loja entidade, código e loja terceiro, safra, produto, tabela, **Op. Triangular=Sim**, **TES de estoque** e **TES financeiro** (gera financeiro, atualiza estoque igual a não) e demais dados necessários;

![PT 5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24164068856727)

**5.** Confirme o contrato.

Acesse a rotina de romaneio com pesagem **OGA250**.

Inclua uma romaneio do tipo **4-(S**) Saída por venda.

Informe o campo contrato com o contrato com tipo de operação triangular, será preenchido alguns campo automaticamente conforme dados do contrato. Informe os demais campos e realize a pesagem. Na aba comercialização terá um item conforme dados do contrato informado no cabeçalho do romaneio, usando a entidade e **TES** financeira do contrato.

![PT 5 1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24165334251159)

Atualize o romaneio. Na atualização do romaneio, na aba comercialização, no primeiro item será setado no campo subtipo o valor **45 (S**) Venda a Ordem e será adicionado mais um item com a entidade de entrega, conforme o código de terceiro informado no contrato e a **TES** de estoque, e será setado com o subtipo **46 (S)** Remessa por venda a Ordem. O campo subtipo é para controle.

![PT 5 2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24165334261911)

Confirme o romaneio. Na confirmação do romaneio será gerado o pedido de venda e as **NF** para os itens na aba comercialização. Primeiro será gerado a **NF** do item com subtipo **46** e em seguida a **NF** com subtipo **45**. Nos itens do pedido de venda do item com subtipo **45** será referenciado a **NF** do item com subtipo **46**, nos campos **C6\_NFORI,C6\_SERIORI,C6\_ITEMORI**.

![PT 5 3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24165350803479)

Caso o parâmetro **MV\_AGRO025**  esteja ativo e esteja configurado a transmissão será aberto o monitor do **Sefaz** para transmissão da **NF**.

No parâmetro **MV\_AGRO026** poderá ser definido o subtipo que não aparecerá no monitor do **Sefaz** para transmissão da **NF** ao confirmar o romaneio. 

Após a transmissão e autorização da **NF** no **Sefaz** do item do romaneio com subtipo **45**, nas opções do menu no romaneio em **Outras Ações → Informar** **Docto Referência**, será possível vincular a **NF** do cliente com a **NF** de remessa da venda a ordem, item do romaneio com subtipo **46**, este vinculo será salvo na tabela **N8J**. Após informar os dados na opção Informar **Docto Referência** será possível transmitir a **NF** de remessa da venda a ordem, subtipo **46** no item do romaneio.
