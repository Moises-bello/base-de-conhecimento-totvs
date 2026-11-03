---
article_id: 115013880628
category: Call Center - Televendas
content_hash: 5e9d700075bc92bd2576a970ddc2305ab079e6393da71d4f77a9ad18d0a75b3d
fetched_at: '2026-06-28T22:41:30.321897+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK-Como configurar para
  não emitir o tmkr03 e tmkr3a
type: support-article
updated_at: '2022-12-27T21:47:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013880628-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Como-configurar-para-n%C3%A3o-emitir-o-tmkr03-e-tmkr3a
---

**Dúvida**  
  
Como configurar para não emitir o tmkr03 e tmkr3a?  
  
**Ambiente**  
  
Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - versão 11 e versão 12  
  
**Solução**  
  
O relatório de Orçamento (tmkr3A) e Pedido (tmkr03) não é acionado por parâmetro.   
Trata-se de um Rdmake de Sugestão de impressão, disponibilizado nas pastas internas do ERP -  \my projects\samples\source\call center.  
Para retirá-lo da aplicação, poderá acessar o Totvs Development Studio - Abrir Arquivo - localizar a pasta \my projects\samples\source\call center, selecionar o relatório TMKR3A.PRX ou TMKR03.  
Adicioná-lo a um projeto e deletar, serão apresentados os ambientes de onde deseja deletar,e confirmar a deleção.  
Ao realizar esse procedimento o relatório não será mais apresentado na confirmação do Orçamento.  
  
Obs: Este procedimento deve ser efetuado por analista programador que detenha o conhecimento de compilação de fontes.
