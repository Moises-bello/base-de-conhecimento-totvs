---
article_id: 360028768452
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 43b3de9ddc8a337b2aadd14ad19c07d6ec40a77be86afb6226fd715694f21d55
fetched_at: '2026-06-28T22:42:42.017507+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como informar o Opcional Default no
  cadastro de Produtos
type: support-article
updated_at: '2022-06-14T13:23:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028768452-Manufatura-Linha-Protheus-SIGAPCP-Como-informar-o-Opcional-Default-no-cadastro-de-Produtos
---

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:01:00 min****Dúvida**No cadastro de **Produtos - MATA010** o campo **Opcional Default - B1\_OPC** fica desabilitado. Como proceder para informar o **Opcional Default**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para preencher o campo **Opcional Default** é necessário acessar a rotina **MATA010**, selecionar o registro referente ao produto pai da estrutura, em modo de alteração, e por meio das **Outras Ações** selecionar a opção **Opcionais**.  
Caso o produto não possua opcionais na estrutura, a opção **Opcionais** das **Outras Ações**não estará disponível. Ou seja, é necessário associar os itens opcionais nos componentes da **Estrutura** - **MATA200** para que seja habilitada essa função.  
Quando assinalada uma opção para o produto pai, sempre que abrir uma **Ordem de Produção - MATA650** essa opção virá selecionada como *default*.
