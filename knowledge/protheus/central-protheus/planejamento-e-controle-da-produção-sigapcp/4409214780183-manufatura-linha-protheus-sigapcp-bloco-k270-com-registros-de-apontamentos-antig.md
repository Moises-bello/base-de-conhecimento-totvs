---
article_id: 4409214780183
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7a0d4e22ffa5dbee987abfc007cdc2afcdeb89b9a20dbd5811394f9752fbd49d
fetched_at: '2026-06-28T22:42:40.900671+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Bloco K270 com registros de apontamentos
  antigos
type: support-article
updated_at: '2021-09-23T11:23:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409214780183-Manufatura-Linha-Protheus-SIGAPCP-Bloco-K270-com-registros-de-apontamentos-antigos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Com fazer para ao gerar o arquivo do **SPED** ou o relatório **MATR241 - Relação Bloco K,** não listar no **K270 - Correção de apontamentos** registros antigos de apontamento produção, que estão sendo listados com o campo **Origem** igual a **1**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para inibir a apresentação de registros de apontamentos de produções antigos no **K270**, execute os seguintes passos  
  
1. Na tabela **SD3 - Movimentos Internos**, para todos os registros com **D3\_EMISSAO - Data de emissão** anterior ao primeiro período de obrigatoriedade de entrega do **Bloco K** ou anterior ao primeiro período para o qual se iniciam os testes de geração do arquivo, preencha o campo **D3\_PERBLK - Período Bloco K** com asteriscos, mesmo que já esteja preenchido;  
2. Faça um *backup* das tabelas **T4G - Bloco K Registro K270** e **T4H - Bloco K Registro K275**;  
3. Remova os registros das tabelas **T4G** e **T4H**;  
4. Gere novamente o **SPED** ou o relatório **MATR241.**
