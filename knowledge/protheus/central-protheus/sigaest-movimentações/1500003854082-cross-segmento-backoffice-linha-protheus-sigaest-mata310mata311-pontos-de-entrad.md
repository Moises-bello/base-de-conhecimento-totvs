---
article_id: 1500003854082
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 9d260fda31e56c67c24d910fe171189660e11564b0971a00a55d92d4fa615ea2
fetched_at: '2026-06-28T22:38:57.136736+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 -
  Pontos de entrada da rotina Transferência entre Filiais
type: support-article
updated_at: '2025-12-10T14:03:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003854082-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Pontos-de-entrada-da-rotina-Transfer%C3%AAncia-entre-Filiais
---

**Dúvida**  
Quais os Pontos de Entrada envolvidos nas rotinas MATA310/MATA311 - Transferência entre Filiais?  
  
**Ambiente**  
Microsiga Protheus – Estoque/Custos – A partir da versão 12.1.17  
  
**Solução**  
Veja abaixo os Pontos de Entradas relacionados às rotina MATA310/MATA311 - Transferência entre Filiais:

|  |  |  |
| --- | --- | --- |
| **Nome:** | **Título:** | **Descrição:** |
| [**M310BUT**](https://tdn.totvs.com/x/VIDbJg) | Adiciona botões na Enchoicebar | Localização.: Function MATA310 - Transferência de saldos entre filiais  Finalidade: Permite adicionar botões na enchoicebar da rotina |
| [**M310FILIAL**](https://tdn.totvs.com/x/YP-XJg) | Permite definição de filiais de origem e destino na transferência | LOCALIZAÇÃO : Function A310TreeCM() - Função utilizada para montar os objetos TREE executados pela rotina de transferência de filiais MATA310. |
| [**M310FILTROb**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087582) | Manipulação do critério de seleção dos produtos | O ponto de entrada permite ao usuário a manipulação do critério de seleção dos produtos, retornando os filtros necessários para a rotina. |
| [**M310QTD**](https://tdn.totvs.com/x/NIBNAQ) | Define sugestão de quantidade a ser transferida da origem ao destino | Ponto de entrada que ativa/desativa sugestão da quantidade a ser transferida da origem para o destino |
| [**M310TUDOK**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087890) | Recebimento de Validações Customizadas | Ponto de Entrada que recebe as validações customizadas durante a confirmação da transferência entre filiais. Está localizado na função de validação A310TOk(). |
| [**MTA310OK**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087903) | Transferência entre Filiais | LOCALIZAÇÃO: Ponto de entrada localizado na função "A310ValOK()" da rotina de transferência entre filiais. Esta função é a responsável por realizar as validações do botão "OK" da janela principal da rotina. EM QUE PONTO: Será executado antes que sejam obtidos |
| [**M310PERG**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087871) | Exibe grupo de perguntas em transferência de Materiais | O ponto de entrada M310PERG é utilizado para definir se o usuário deseja que na rotina de transferência de materiais ("MATA310") seja exibido ou, não o grupo de perguntas MT460A. |
| [**M310CABEC**](https://tdn.totvs.com/pages/releaseview.action?pageId=236603630) | Manutenção do array aCabec | É utilizado para permitir que o usuário manipule o array aCabec que contém os itens do cabeçalho do pedido de vendas, documento de entrada ou fatura de entrada. |
| [**M310ITENS**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087583) | Permite manipulação do array altens | É utilizado para permitir que o usuário manipule o array aItens que contém os itens do cabeçalho do pedido de vendas, documento de entrada ou fatura de entrada. É passado um parâmetro para identificar a rotina a ser executada após o ponto de entrada.  Eventos |
| [**M310PPED**](https://tdn.totvs.com/pages/releaseview.action?pageId=268583455) | Permite fazer tratamentos após a inclusão do pedido de vendas da transferência de filiais | O Ponto de Entrada M310PPED, permite fazer tratamentos após a inclusão do pedido de vendas da transferência de filiais. |
| [**M310ESTO**](https://tdn.totvs.com/pages/releaseview.action?pageId=516225226) | Ponto de Entrada na confirmação do estorno do relacionamento entre origem e destino | Function A310EstRel() - Função utilizada para estornar relacionamento entre origem e destino executados pela rotina de  transferência de filiais MATA310. |
| [**MT311ROT**](https://tdn.totvs.com/display/public/PROT/PEST07671_PONTO_DE_ENTRADA_MT311ROT) | Manipula botões existentes na Solicitação de Transferência | P.E que possibilita o usuário manipular os botões existentes e adicionar novos botões na rotina Solicitação de Transferência. |
| [**MT311LEG**](https://tdn.totvs.com/display/public/PROT/PEST07666_MT311LEG_ADICIONA_LEGENDA) | Adiciona legenda na browser | LOCALIZAÇÃO: Localizado na função MATA311() responsável por montagem de legenda na browser  EM QUE PONTO: No inicio da função para criação do objeto da legenda. |

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Transferência entre Filiais*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
