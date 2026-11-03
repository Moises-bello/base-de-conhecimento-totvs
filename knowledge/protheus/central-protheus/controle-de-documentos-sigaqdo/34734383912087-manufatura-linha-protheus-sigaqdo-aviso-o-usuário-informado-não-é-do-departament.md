---
article_id: 34734383912087
category: Controle de Documentos (SIGAQDO)
content_hash: 0d3a45a2aaf065d90014276743ff51fc7dc41ee8c52991d595b51a007cd66478
fetched_at: '2026-06-28T22:42:28.936108+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Aviso - O usuário informado não é do
  departamento indicado!
type: support-article
updated_at: '2025-09-05T19:14:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34734383912087-Manufatura-Linha-Protheus-SIGAQDO-Aviso-O-usu%C3%A1rio-informado-n%C3%A3o-%C3%A9-do-departamento-indicado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34734359125527) Tempo aproximado para leitura: **00:00:56 min**  
  
**Ocorrência**  
Na rotina **QDOA050 - Cadastro de Documentos**, ao finalizar um documento, ocorre a mensagem **Aviso - O usuário informado não é do departamento indicado!**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**  
A mensagem **Aviso - O usuário informado não é do departamento indicado!** ocorre quando o **departamento do usuário distribuidor** incluído em Distribuidores **não está igual ao departamento no cadastro de usuário QAXA010 - Usuários**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar opção **Distribuidores** e **excluir o usuário**.  
2. Caso seja um **usuário ativo**, há possibilidade de incluí-lo novamente. Nesta ação o Sistema trará a informação de origem (**QAXA010 - Usuários**).
