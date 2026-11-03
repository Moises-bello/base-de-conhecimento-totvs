---
article_id: 360000518668
category: Ferramentas
content_hash: f895f7671a8833c38a85557a7a9d77b438798ec11f580e2706d056a7972c2dc0
fetched_at: '2026-06-28T22:42:18.079197+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework - Linha Protheus - Travamento na tela Preparando Ambiente
type: support-article
updated_at: '2024-05-09T11:17:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000518668-Framework-Linha-Protheus-Travamento-na-tela-Preparando-Ambiente
---

**Ocorrência**Travamento ao tentar acessar o Protheus, a tela trava e permanece a mensagem **Preparando Ambiente**.  
  
**Ambiente**Protheus - Tela Inicial - Versão 12  
  
**Causa**Após migração da base de DBF para Ctree, o binário não consegue fazer a leitura correta desta pasta.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Pare o serviço do Protheus;  
2. Acesse a pasta referente ao **RootPath** do Protheus (por padrão, pasta **Protheus\_Data**);  
3. Renomeie a pasta **HHTRG**;  
4. Reinicie o serviço do Protheus.
