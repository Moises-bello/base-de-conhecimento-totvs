---
article_id: 29368795248919
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 8c5fd9195530d308e3afc402ca474bf1aa3e617cca3f4b450cd181d5036e173b
fetched_at: '2026-06-28T22:38:45.342418+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Funcionamento do parâmetro
  "Filtra já Emitida?" na Rotina Documento de Saída (MATA460A)
type: support-article
updated_at: '2025-01-20T21:15:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29368795248919-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-Filtra-j%C3%A1-Emitida-na-Rotina-Documento-de-Sa%C3%ADda-MATA460A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29368795234583) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual é o funcionamento do parâmetro "**Filtra já Emitida?**" na Rotina Documento de Saída (**MATA460A**)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**O parâmetro "**Filtra já emitidas**?" define se os pedidos que já possuem notas fiscais emitidas (ou seja, já foram faturados) serão considerados na consulta.  
  
1. Quando o parâmetro é configurado como "**Sim**":  
O sistema irá **filtrar** e excluir os pedidos que já foram faturados (com nota emitida).  
Assim, serão exibidos apenas os pedidos que ainda estão pendentes de emissão de nota fiscal.  
  
2. Quando o parâmetro é configurado como "**Não**":  
O sistema **não aplica o filtro** e inclui todos os pedidos na consulta, sejam eles faturados ou não.  
Isso permite visualizar tanto os pedidos pendentes quanto os que já possuem nota emitida.  
  
Resumindo:  
Filtra já emitidos? = Sim → **Filtra** e exibe apenas pedidos pendentes.  
Filtra já emitidos? = Não → Mostra todos os pedidos, inclusive os já faturados.

**Saiba mais:  
[Documentos de Saída (MATA460A - SIGAFAT)](https://tdn.totvs.com/x/M5PjFQ)**
