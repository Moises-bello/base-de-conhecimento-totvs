---
article_id: 34891566024087
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 86a99b4eab9e13c25720ec4109be04cd4f73b321c7457c770be3c7167ad147e8
fetched_at: '2026-06-28T22:38:55.624766+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - InterFunctionCall:
  cannot find function A265ATUSA in AppMap on A100DISTRI(SIGACUSB.PRX)'
type: support-article
updated_at: '2025-09-12T14:30:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34891566024087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-InterFunctionCall-cannot-find-function-A265ATUSA-in-AppMap-on-A100DISTRI-SIGACUSB-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34891566012055) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
InterFunctionCall: cannot find function A265ATUSA in AppMap on A100DISTRI(SIGACUSB.PRX) 01/03/2025 23:40:42 line : 13437  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Na gravação do documento de entrada, o sistema aborta informando a falta da funçao A265ATUSA.  
  
**Solução**  
Implementado tratamento para executar a funcao A265ATUSA quando a mesma constar no repositorio.

**Pacote para aplicação da correção:**  
12.1.2210 <https://suporte.totvs.com/portal/p/10098/download?e=1189877>  
12.1.2310 <https://suporte.totvs.com/portal/p/10098/download?e=1189878>  
12.1.2410 <https://suporte.totvs.com/portal/p/10098/download?e=1189876>

Importante: Execute a aplicação do pacote em ambiente de homologação para validação e somente depois de aprovado coloque em produção. (Antes de qualquer ação realize o backup do ambiente)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações de Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
