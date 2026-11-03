---
article_id: 37033344190231
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f1c088aae05d08d22f9f000aab91fe368bbbc7cef7fe3598ca0a1148ad9ea6cc
fetched_at: '2026-06-28T22:38:57.047590+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA261 Erro transferência
  endereços dentro do armazém 98
type: support-article
updated_at: '2025-12-17T12:26:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37033344190231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-Erro-transfer%C3%AAncia-endere%C3%A7os-dentro-do-armaz%C3%A9m-98
---

O problema de não permitir transferir produtos entre endereços no processo de CQ no TOTVS Protheus.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37033349387543) Tempo aproximado para leitura: **01:00:00 min**  
  
**Dúvida**  
Não Permite fazer a  transferir de endereço produtos no  processo de CQ, como corrigir?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Ajuste na validação de transferência entre armazém, para o armazém de CQ. Para correção do incidente aplicar o pacote de correção abaixo, na sua base de homologação realizar o backup do seu ambiente.

12.1.2210:<https://r.totvs.io/p/1221453>

12.1.2310:<https://r.totvs.io/p/1221452>

12.1.2410:<https://r.totvs.io/p/1221451>

12.1.2510:<https://r.totvs.io/p/1221454>

**Issue TDN:** DMANMAT01-46512

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
