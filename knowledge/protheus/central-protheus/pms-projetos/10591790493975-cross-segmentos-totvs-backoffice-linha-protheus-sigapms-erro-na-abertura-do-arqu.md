---
article_id: 10591790493975
category: PMS - Projetos
content_hash: e8cf1bf318c97937ae6099e6773c3a3e4241f756d67f8727519af979a2c82e74
fetched_at: '2026-06-28T22:37:15.980951+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Erro na abertura
  do arquivo. Verifique a existência do arquivo selecionado
type: support-article
updated_at: '2022-11-30T12:32:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10591790493975-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-Erro-na-abertura-do-arquivo-Verifique-a-exist%C3%AAncia-do-arquivo-selecionado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Na rotina de Gerenciamento de Projetos (PMSA200) ao tentar realizar ações na EDT/Tarefa o sistema apresenta a mensagem: "Falha na abertura. Erro na abertura do arquivo. Verifique a existência do arquivo selecionado"  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Todas as versões  
  
**Causa**A mensagem é gerada quando o sistema tenta localizar o arquivo "PMSA200.pln" dentro da pasta "Profile" do sistema, porém não consegue localizá-lo.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se existe a pasta "Profile" dentro da "Protheus Data", no diretório de instalação do Protheus;  
2. Caso a pasta "Profile" não exista, basta cria-la;  
3. Com a pasta criada, ao acessar a rotina Gerenciamento de Projetos (PMSA200) e realizar o processo novamente, o sistema criará o arquivo "PMSA200.pln" automaticamente.
