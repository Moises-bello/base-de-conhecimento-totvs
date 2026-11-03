---
article_id: 360028592154
category: Inspeção de Processos (SIGAQIP)
content_hash: 1c83bfbe3d607b8abfde8d8a2988d6666d4da863febc97d27b82e856e7844929
fetched_at: '2026-06-28T22:42:25.812034+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Informar cliente na inspeção do processo
type: support-article
updated_at: '2021-10-01T13:12:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028592154-Manufatura-Linha-Protheus-SIGAQIP-Informar-cliente-na-inspe%C3%A7%C3%A3o-do-processo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min**  
**Dúvida**Como informar um **cliente** no laudo de inspeção de processo, na rotina **Resultados - QIPA215**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**Os campos **Cliente - QPK\_CLIENT** e **Loja - QPK\_LOJA** serão preenchidos apenas no momento em que o usuário clicar no botão **Resultados** da rotina de **Resultados - QIPA215.** Neste momento será aberta uma tela para escolha do **cliente** e **loja**. Para que esteja tela seja aberta, realize os seguintes passos:  
  
1. Configure o parâmetro **MV\_QINTPC - Apresenta tela de relacionamento entre Produto x Cliente,** igual a **T**.  
2. Na rotina **Produtos x Clientes - QIPA070**, clique no botão **Incluir** e informe os dados do produto e ensaios do cliente.  
3. Para os próximos laudos preenchidos na rotina de **Resultados**, a tela para seleção de cliente deverá ser apresentada.  
  
**Importante**  
Quando a **Ordem de Produção** que está sendo inspecionada foi gerada com a amarração com um **pedido de venda**, o cliente do mesmo **não** é preenchido automaticamente na rotina de **Resultados**. É necessário realizar o procedimento descrito na solução acima.
