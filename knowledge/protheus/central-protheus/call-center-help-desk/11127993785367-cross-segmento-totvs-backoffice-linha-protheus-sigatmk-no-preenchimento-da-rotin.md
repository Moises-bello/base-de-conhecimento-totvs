---
article_id: 11127993785367
category: Call Center - Help Desk
content_hash: f30f0c2a8501e456d8504988e8d367e8d1fa13906da162b63d0da7380e0b4715
fetched_at: '2026-06-28T22:41:27.674711+00:00'
product: protheus
section_id: 1500001537181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - No preenchimento
  da rotina TMKA503A o código de categoria (ADE_CODCAT) não é apresentado
type: support-article
updated_at: '2025-01-10T19:41:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11127993785367-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-No-preenchimento-da-rotina-TMKA503A-o-c%C3%B3digo-de-categoria-ADE-CODCAT-n%C3%A3o-%C3%A9-apresentado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No preenchimento da rotina TMKA503A o código de categoria não é apresentado , após a inclusão do assunto.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Todas as versões  
  
**Causa**Isso pode ocorrer de acordo com a configuração efetuada na rotina **TMKA510J** realiza a seleção das informações cadastradas na rotina **QNCA010** (responsável pelos dados do campo de código de categoria).     
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Valide o cadastro existente ou cadastre o código de categoria na rotina **QNCA010**, preenchendo o campo "Tipo Tabela" (QI0\_TIPO) = 4 Categoria Problema  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11126772063511)  
2- Entre na rotina **TMKA510J** e selecione a opção alterar. (Utilize o mesmo assunto selecionado que foi informado anteriormente no campo ADE\_ASSUNT).  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11126872980631)

3-  Selecione a aba Causa  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11127642213143)

4- Adicione o código informado na rotina QNCA010

OBS: Caso a seleção desse campo estiver vazia , todos os registros da rotina **QNCA010** estarão disponíveis na seleção do campo (ADE\_CODCAT). Contudo se algum campo for atribuído para o assunto , o mesmo trará as informações adicionadas na linha AG8.  
  
Saiba mais :

[(QNCA010 - SIGATMK)](https://tdn.totvs.com/pages/viewpage.action?pageId=425451715)

[Assuntos x Informações de Chamados (TMKA510J - SIGATMK)](https://tdn.totvs.com/pages/viewpage.action?pageId=341226796)

[Teleatendimento (TMKA503A - SIGATMK)](https://tdn.totvs.com/pages/viewpage.action?pageId=341227190)
