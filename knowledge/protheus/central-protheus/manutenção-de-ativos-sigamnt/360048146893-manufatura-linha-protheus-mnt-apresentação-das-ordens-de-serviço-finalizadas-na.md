---
article_id: 360048146893
category: Manutenção de Ativos (SIGAMNT)
content_hash: d83bf9db7ed61da1f380057abb8daed1b0dcf23c29371f28602bb82bbc7efdc1
fetched_at: '2026-06-28T22:42:32.749275+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Apresentação das Ordens de Serviço finalizadas
  na Consulta Padrão
type: support-article
updated_at: '2022-04-26T20:26:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048146893-Manufatura-Linha-Protheus-MNT-Apresenta%C3%A7%C3%A3o-das-Ordens-de-Servi%C3%A7o-finalizadas-na-Consulta-Padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura:**00:00:45 min**  
**Dúvida**Por que não são apresentadas as **O.S. - Ordens de Serviço** finalizadas na consulta padrão?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - A partir da versão 12  
  
**Solução**O tratamento para reporte de produtos em **O.S.** finalizadas é restrito a algumas rotinas, sendo estas: **Baixar Pré-Requisição - MATA185**, **Documento de Entrada - MATA103**, **Movimentação Interna - MATA240**, **Movimentação Múltipla - MATA241**. Portanto, não são todas as consultas padrão que dispõe destas informações.   
Porém quando a consulta padrão nesta rotinas listadas não apresenta o *flag***Incluir as Ordens Finalizadas**, é necessário alterar a consulta utilizada pelos campos **CP\_NUMOS - Ordem de serviço**, **SD1\_ORDEM - Ordem de serviço** e **D3\_ORDEM - Ordem de serviço**, por meio do **Configurador - SIGACFG**, informando o valor **MNTSTJ**, conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017170341/mceclip0.png)
