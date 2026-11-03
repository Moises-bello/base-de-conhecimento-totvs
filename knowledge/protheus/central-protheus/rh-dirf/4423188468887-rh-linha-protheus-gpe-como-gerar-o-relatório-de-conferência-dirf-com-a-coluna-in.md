---
article_id: 4423188468887
category: RH – DIRF
content_hash: b31a4cf8aa33aa07d62f3fab1888da84593f421be2ccb17deafca2f2b609494b
fetched_at: '2026-06-28T22:44:06.888568+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar o Relatório de Conferência DIRF com
  a coluna INSS e Dependentes separadas
type: support-article
updated_at: '2025-08-19T13:13:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4423188468887-RH-Linha-Protheus-GPE-Como-gerar-o-Relat%C3%B3rio-de-Confer%C3%AAncia-DIRF-com-a-coluna-INSS-e-Dependentes-separadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34286855151127)** Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como gerar o Relatório de Conferência DIRF (GPEM570) com a coluna INSS e Dependentes separadas?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**No Configurador-SIGACFG pelo caminho **>Base de Dados >Dicionário >Base de Dados**, selecione Perguntas:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4423575352471)  
  
Pesquise pelo grupo de perguntas GPM570 e inclua a nova pergunta conforme abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4423568463895)  
Ou execute a atualização de dicionário (UPDDISTR) com a ultima expedição contínua disponibilizado no portal para criar esse novo grupo.

Após criar, entre na rotina **Relatório Conferência** pelo caminho **>Miscelânea >Dirf >Relatório Conferência**, e nos parâmetros de geração, na pergunta **Imprimir De. Separadamente?** deixe com SIM:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4423176345367)  
  
O relatório será impresso com as deduções de INSS e Dependentes em colunas separadas:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4423176542359)  
  
  
**Expedição Contínua:** <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO>.

**Saiba Mais:**[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF?page=2#articles)
