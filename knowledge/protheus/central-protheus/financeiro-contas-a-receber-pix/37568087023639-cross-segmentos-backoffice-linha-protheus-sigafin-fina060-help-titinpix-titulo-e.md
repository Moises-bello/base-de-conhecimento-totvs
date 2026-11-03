---
article_id: 37568087023639
category: Financeiro - Contas a Receber - PIX
content_hash: f905761b57c0128b68c32779038ec1230623b854a0014143164a7dec0f5325fc
fetched_at: '2026-06-28T22:38:16.465455+00:00'
product: protheus
section_id: 1500001539301
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA060 - HELP: TITINPIX
  - Titulo em carteira PIX'
type: support-article
updated_at: '2026-01-09T19:14:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37568087023639-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA060-HELP-TITINPIX-Titulo-em-carteira-PIX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37568115566359) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
HELP: TITINPIX - Titulo em carteira PIX

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37568115567127)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Causa**  
Este cenário ocorre pois antes de realizar a transferência é preciso cancelar o título PIX.  
  
**Solução**  
Para realizar transferência entre carteiras, necessário cancelar o título PIX através da rotina Monitor PIX (FINA890).  
  
Por favor, siga o passo a passo abaixo:  
1 - Após cancelar o borderô, acessar a rotina **FINA890 (Monitor PIX)**  
2 - Ao acessar a rotina, posicionar-se no título e clicar em **Outras Ações > Cancelar.**  
3 - Validar o título a ser cancelado na rotina **Monitor PIX e Confirmar.**  
4 - Acessar a rotina **Funções Contas a Receber ou Transferências 'FINA060'** , posicionar-se no título e seguir com a transferência **(exemplo: carteira 0).**

**Saiba mais:** [**Pagamentos instantâneos - PIX**](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
