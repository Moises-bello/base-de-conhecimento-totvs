---
article_id: 15033302118679
category: Financeiro - Contas a Pagar
content_hash: 46149d7fed2e6947bb452efc9901169e363cd5a37606fc221d5538fd05c9779f
fetched_at: '2026-06-28T22:38:08.513484+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - ExecAuto FINA050 -
  Error log JOB threads doesn''t support remote/visual components '
type: support-article
updated_at: '2023-06-07T12:22:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15033302118679-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-ExecAuto-FINA050-Error-log-JOB-threads-doesn-t-support-remote-visual-components
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**  
Ao tentar utilizar o ExecAuto da rotina FINA050 com rateio de múltiplas naturezas utilizando a Function StartJob (função que executa uma rotina em uma segunda thread sem interface) ou via JOB é apresentado o erro JOB threads doesn't support remote/visual components  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o parâmetro MV\_RATAUTO está com o conteúdo .T. (Permite exibir ou não a tela de rateios quando é realizado a inclusão de Contas a Pagar via rotina automática)  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **Configurador** (**SIGACFG**);  
2. No menu, acesse **Ambiente** -> **Cadastros** -> **Parâmetros;**  
3. Na lupa de pesquisa do canto superior da tela, procure por **MV\_RATAUTO**;  
4. Clique em "**Editar**" posicionando no parâmetro;  
5. Altere o conteúdo para **.F.**  
  
**Saiba mais**[FINA050 Contas a Pagar - Rotina Automática](https://tdn.totvs.com/pages/releaseview.action?pageId=6070752)  
[Function StartJob](https://tdn.totvs.com/display/tec/StartJob)
