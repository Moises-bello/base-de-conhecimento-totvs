---
article_id: 25990532645015
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 88b75a045984d67579290120008425284fd9f135d5d88892d45202d0bfad5108
fetched_at: '2026-06-28T22:42:44.417264+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A712NOSMQ ao executar a rotina
  PCPA712
type: support-article
updated_at: '2024-08-29T19:32:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25990532645015-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A712NOSMQ-ao-executar-a-rotina-PCPA712
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25990576543639) Tempo aproximado para leitura: **00:01:14 min****Ocorrência**Ao tentar executar o **PCPA712** é apresentada a mensagem **A712NOSMQ**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem ocorre quando a filial na qual o usuário está logado não está cadastrada numa tabela que faz a gestão das filiais para o processamento do **PCPA712**.  
  
**Solução**Siga os passos abaixo para solucionar esta situação  
1. Acesse a rotina **PCPA139** para que essa filial seja carregada no quadro **Filiais para integração com o MRP**;  
2. Se for listada com a cor verde, execute novamente o **PCPA712**;  
3. Se for listada com a cor vermelha, através da rotina **PCPA106** localize qual a filial centralizadora que tem essa filial como centralizada, e execute o **PCPA712** a partir dessa filial centralizadora.  
  
**Glossário**  
**PCPA712** - **MRP** Memória  
**A712NOSMQ** - A execução do **MRP** está bloqueada nesta filial  
**PCPA139** - Parâmetros de integração do **MRP**  
**PCPA106** - Empresa centralizadora  
**MRP** - Manufacturing Resource Planning
