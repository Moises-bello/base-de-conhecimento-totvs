---
article_id: 360058926273
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6acf7f4dab6b92003618a469444b419c59e3e094e2c77b758f1aef7e4d11623d
fetched_at: '2026-06-28T22:42:42.124846+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Considerar saldo de um determinado
  armazém para geração das OPs Intermediárias
type: support-article
updated_at: '2023-12-19T17:56:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058926273-Manufatura-Linha-Protheus-SIGAPCP-Considerar-saldo-de-um-determinado-armaz%C3%A9m-para-gera%C3%A7%C3%A3o-das-OPs-Intermedi%C3%A1rias
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como considerar o saldo de um determinado armazém para geração das **OPs Intermediárias**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O Sistema verifica o conteúdo do parâmetro **MV\_CONSEST - Considera estoque na geração de Ordem de produção**, se esse parâmetro tiver o conteúdo igual a **S**, o Sistema valida a disponibilidade de estoque e gera **OP Intermediária** somente se houver necessidade.  
  
Os **armazéns** que o Sistema verifica, neste caso, são os determinados nos parâmetros da função **F12** da rotina **MATA650 - Ordem de Produção**. Caso o parâmetro **Cons. Só Armazém Padrão?** estiver com o conteúdo **Sim**, consulta o saldo somente do **armazém padrão** do item; e se estiver com o conteúdo **Não**, considera o saldo de todos os armazéns definidos nos parâmetros **Considera do Armazém?** e **Até o Armazém?**
