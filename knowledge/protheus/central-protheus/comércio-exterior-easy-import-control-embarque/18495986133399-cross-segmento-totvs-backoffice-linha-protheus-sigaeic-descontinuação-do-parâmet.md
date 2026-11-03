---
article_id: 18495986133399
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: ef6631155558f573c2de103c9397bde5522ac4dbf96aa8d7322ca7c19579eadd
fetched_at: '2026-06-28T22:39:48.836980+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Descontinuação
  do parâmetro "MV_EIC0062".
type: support-article
updated_at: '2023-10-23T16:10:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18495986133399-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Descontinua%C3%A7%C3%A3o-do-par%C3%A2metro-MV-EIC0062
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18495976794519)Tempo aproximado para leitura: **02:00 min****Dúvida**Descontinuação do parâmetro "**MV\_EIC0062"**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– A partir da versão 12.1.33.  
  
**Solução**Foi descontinuado o parâmetro "**MV\_EIC0062"**, assim o sistema irá validar somente o parâmetro "**MV\_EIC0063"** que lista os Estados dos Importadores, possibilitando que ao processo de importação seja gerado um movimento interno através da rotina "**Complemento de Valor"**.  
  
Ao gerar uma Nota Fiscal Complementar, caso o Estado do importador esteja configurado com o Parâmetro "**MV\_EIC0063"** e possua despesa base de custo, será apresentado a pergunta: “Foram identificadas despesas base de custo para o processo e o Estado do Importador está configurado para a geração do Complemento de Valor. Deseja prosseguir utilizando as despesas base de custo na geração da Nota Fiscal Complementar?”, possibilitando desta forma a geração da Nota Fiscal Complementar com despesa base de custo.  
  
**Saiba mais:****[Configuração de uso da rotina de complemento de valor](https://tdn.totvs.com/pages/releaseview.action?pageId=782312469)**
