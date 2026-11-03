---
article_id: 4415797504279
category: Gestão de Armazenagem (WMS)
content_hash: 60dc594e154114632c15909864d398cbf80488cb52bfefdf000da3f83b7c915b
fetched_at: '2026-06-28T22:45:48.072169+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Parametrizar o relatório WMSR280 - Desempenho
type: support-article
updated_at: '2021-12-14T12:51:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415797504279-Log%C3%ADstica-Linha-Protheus-WMS-Parametrizar-o-relat%C3%B3rio-WMSR280-Desempenho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20min** **Dúvida**Como parametrizar o relatório WMSR280 - Desempenho?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (SIGAWMS) -  A partir da versão 12  
  
**Solução**No filtro ou pergunte**Recurso ?** deve ser optado por **Humano, Físico ou Unitizador**, sendo que o recurso humano tem como referência o cadastro **Funções - GPEA030**, o recurso físico é referenciado pelo cadastro **Recursos Físicos - WMSA430** e o unitizador pelo **Monitor de Serviço - WMSA332**.  
  
Além disto, informar no último filtro ou pergunte uma referência para a realização da cobrança, a fim de que o relatório não apresente a quantidade zerada.  
  
**Importante**Como o total de horas é apresentado em minutos, caso uma atividade seja executada em menos de um minuto, esse campo permanecerá zerado.  
  
**Saiba mais**Veja mais detalhes nas documentações abaixo:

[Opções do campo "Recurso" da tela Parâmetros do relatório de Desempenho (WMSR280);](https://tdn.totvs.com/pages/viewpage.action?pageId=655437889)  
[Campos "Quantidade" e "Total de Horas" do relatório de Desempenho (WMSR280) aparecem zerados.](https://tdn.totvs.com/x/hDcRJw)
