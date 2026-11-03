---
article_id: 35936416876951
category: Materiais - Compras (SIGACOM)
content_hash: 6dddc875c41a2adbebbca68fc004c6d54449f51ee9878228ecdd2670e352c6a7
fetched_at: '2026-06-28T22:41:21.895493+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Qual é a funcionalidade
  do campo C1_NFCWF ?
type: support-article
updated_at: '2026-01-27T14:58:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35936416876951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Qual-%C3%A9-a-funcionalidade-do-campo-C1-NFCWF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35936416851095) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual é a funcionalidade do campo C1\_NFCWF no Novo Fluxo de Compra?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310

**Solução**  
Sua função é enviar notificação para o solicitante que criou a Solicitação de Compra quando a análise da cotação no Novo Fluxo de Compras gerar um pedido de compra. Para que o solicitante receba o e-mail de quando a SC virar um Pedido de Compra, deve seguir as etapas abaixo:

Na tela de **Solicitação de Compras** (**MATA110**), informar no campo **Notifica WF (NFC)** - **C1\_NFCWF**- a opção **1-Sim**, para que fique registrado no sistema que deseja receber o e-mail quando a SC virar um Pedido de Compra.

***Atenção***

***Para que o solicitante seja devidamente comunicado via e-mail, seu e-mail deve estar cadastrado no perfil de usuário no Protheus, pois caso contrário, não receberá as notificação via e-mail.***

![](https://tdn.totvs.com.br/download/attachments/680260500/WF_MATA110.gif?version=1&modificationDate=1742393836443&api=v2)

Segue abaixo Exemplo do e-mail que o solicitante irá receber.  
*![](https://tdn.totvs.com.br/download/attachments/680260500/image-2025-4-11_9-1-10.png?version=1&modificationDate=1744372871007&api=v2)*

***Obs1:***

Por padrão p campo **Notifica WF (NFC)** - **C1\_NFCWF** possui em seu cadastro no Configurador o Inicializador Padrão como "2", referente a opção "Não", conforme imagem abaixo do cadstro do padrão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37964865124631)

Caso se deseje que o campo se inicie com o "Sim", pode-se alterar o Inicilizador Padrão do campo em seu cadastro no no SIGACFG para "1" que é a opção referente ao "Sim".

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
