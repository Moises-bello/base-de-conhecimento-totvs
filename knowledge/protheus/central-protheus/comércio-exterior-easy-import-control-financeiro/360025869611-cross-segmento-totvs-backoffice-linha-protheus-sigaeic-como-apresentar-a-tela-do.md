---
article_id: 360025869611
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: a59dc9802b67b8ccc298e4bfcfc91934f5ce7a5fca989e1c75298c70c35b8f2d
fetched_at: '2026-06-28T22:39:44.296586+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - SIGAEIC - Como apresentar
  a tela do contas a pagar do SIGAFIN na geração dos títulos
type: support-article
updated_at: '2021-09-27T14:26:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025869611-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-apresentar-a-tela-do-contas-a-pagar-do-SIGAFIN-na-gera%C3%A7%C3%A3o-dos-t%C3%ADtulos
---

**Dúvida**Como apresentar título em tela na rotina de Desembaraço ou no Controle de Cambio?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**1 . Na rotina do Desembaraço/ Manutenção (EICDI502) ou no Financeiro/ Controle de Cambio (EICAP100).

2. Selecione F11, nos Parâmetros configure o Gerar Títulos Autom. no Fin, como "2-Não".   
![](https://totvssuporte.zendesk.com/attachments/token/gdSchGz6nuSOVLqVwwSkRbYes/?name=inline1250870198.png)  
  
3. Ao confirmar a inclusão do título, será apresentado o título em tela para confirmação e gravação no financeiro.![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024692091/mceclip0.png)

**Observação**Caso a natureza do título esteja informada no **cadastro do fornecedor** campo Natureza (**A2\_NATUREZ**), essa será gravada no campo **E2\_NATUREZ** . Não tendo a natureza informada no cadastro do fornecedor campo **A2\_NATUREZ**, será verificado a natureza informada no **F11** do **câmbio,** para a geração do título. Sem o preenchimento da natureza em nenhum cadastro não será possível gravação do título no SIGAFIN, pois o campo **E2\_NATUREZ** é obrigatório.
