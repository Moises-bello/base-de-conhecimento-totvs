---
article_id: 6329188593047
category: PMS - Integrações
content_hash: 42b3371fe08a0bb017da3566396969a851c54df3aa5b4dfb529c81b79f022e7e
fetched_at: '2026-06-28T22:37:16.724002+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Integração Parâmetro MV_PMSITMU
type: support-article
updated_at: '2024-02-26T18:10:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6329188593047-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Integra%C3%A7%C3%A3o-Par%C3%A2metro-MV-PMSITMU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21627663451799) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Integração RM x Protheus apresentando mensagem App: [PROTHEUS] - [RM]':Parâmetro MV\_PMSITMU desativado  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as Versões  
  
**Solução**  
1) Verifique se os fontes PMSI200 , PMSI200A e PMSXSOLUM estão atualizados  
2) Normalmente esta mensagem ocorre com contratos antigos onde não estavam gravando os registros na tabela ANE. Procure criar um novo contrato para integração  
3) Na integração o parâmetro deve estar como 1, impedindo incluir, alterar e excluir dados de todas as rotinas do Gestão de Projetos, servindo apenas para consultas
