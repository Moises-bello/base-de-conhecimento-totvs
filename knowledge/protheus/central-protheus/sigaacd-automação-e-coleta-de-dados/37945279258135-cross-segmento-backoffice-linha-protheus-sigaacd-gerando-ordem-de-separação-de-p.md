---
article_id: 37945279258135
category: SIGAACD - Automação e Coleta de Dados
content_hash: aba385f050929db881e6dec2eb994276502e014db3c0f92e1f148e755428d33c
fetched_at: '2026-06-28T22:39:11.014784+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Gerando ordem de separação
  de produtos com apropriação indireta
type: support-article
updated_at: '2026-01-26T20:11:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37945279258135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Gerando-ordem-de-separa%C3%A7%C3%A3o-de-produtos-com-apropria%C3%A7%C3%A3o-indireta
---

A rotina Ordem de Separação (ACDA100) está gerando Ordem de Separação por Ordem de Produção com apropriação indireta.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37945295024791) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
A rotina **Ordem de Separação (ACDA100)** está gerando OS por ordem de produção para produtos indiretos, mesmo com o parâmetro MV\_PAPRIND configurado como 'T'.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Foram realizados ajustes para evitar a geração de OS para produtos indiretos quando o parâmetro estiver habilitado.

**Issue TDN:**DMANMAT01-44012

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1187288> ; 12.1.2310:<https://suporte.totvs.com/portal/p/10098/download?e=1187290> ; 12.1.2410:<https://suporte.totvs.com/portal/p/10098/download?e=1187289> ;

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[PACD0007 - Parâmetros - Automação e Coleta de Dados (ACD)](https://tdn.totvs.com/pages/viewpage.action?pageId=235596091)

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
