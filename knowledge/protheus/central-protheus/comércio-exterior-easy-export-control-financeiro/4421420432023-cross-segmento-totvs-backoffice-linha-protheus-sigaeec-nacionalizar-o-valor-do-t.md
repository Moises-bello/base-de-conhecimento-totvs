---
article_id: 4421420432023
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: 6e37293f3cf6779d9bb3a12f36d868a6b39157a20e751b54935fb4b026132d2d
fetched_at: '2026-06-28T22:36:58.134347+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Nacionalizar o
  valor do título RA criado como movimento exterior
type: support-article
updated_at: '2022-02-03T19:45:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421420432023-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Nacionalizar-o-valor-do-t%C3%ADtulo-RA-criado-como-movimento-exterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**A rotina de Manutenção câmbio (EECAF200) não permite nacionalizar o valor do título RA criado como movimento exterior, como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Export Control - Todas as versões  
  
**Solução**Avaliamos a solicitação e a ocorrência reportada é em decorrência do uso indevido do parâmetro **MV\_AVG0180**.  
Este parâmetro tem como objetivo atender a circular nº 3.436 de 06/02/2009 (RMCCI nº 28): <https://tdn.totvs.com/pages/viewpage.action?pageId=312157433>.   
Com a liberação da funcionalidade de movimento no exterior em 2016 o seu uso passou a ser desnecessário para atender a liquidação de adiantamentos pós embarque.  
Por padrão o parâmetro **MV\_AVG0180** é desabilitado na instalação do produto e sua ativação não é recomendada quando utiliza-se os recursos de movimento no exterior quando integrado ao módulo SIGAFIN.  
Desta forma, orientamos a desativar o parâmetro **MV\_AVG0180** (conteúdo deve ser **.F.** - false).   
  
Realize o procedimento:  
1- Retire a **Dt.Embarque** (EEC\_DTEMBA) na rotina de Embarque (EECAE100), para exclusão dos títulos;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421427204631/mceclip0.png)  
  
2- Acesse o SIGACFG e altere o parâmetro **MV\_AVG0180** para **.F.**.   
3- Acesse a rotina de Embarque (EECAE100), preencha a data de embarque na aba transporte, após na rotina Manutenção cambio (EECAF200) será possível liquidar o título tipo RA.  
  
**Saiba mais**  
[TTRCTC - DT Controle de Cambio com Movimento no Exterior](https://tdn.totvs.com/display/public/PROT/TTRCTC_DT_Controle_de_Cambio_com_Movimento_no_Exterior_BRA)
