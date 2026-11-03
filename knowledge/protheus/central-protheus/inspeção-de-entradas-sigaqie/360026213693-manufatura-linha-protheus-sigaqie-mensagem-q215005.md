---
article_id: 360026213693
category: Inspeção de Entradas (SIGAQIE)
content_hash: a794695350a76b000cb837ed09669b43f5cb87fedfa99696a0e15f610767bd2f
fetched_at: '2026-06-28T22:42:27.070169+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Mensagem Q215005
type: support-article
updated_at: '2021-09-08T12:58:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026213693-Manufatura-Linha-Protheus-SIGAQIE-Mensagem-Q215005
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min****Ocorrência**Ao preencher um laudo na rotina de **Resultados - QIEA215**, é apresentada a mensagem **Q215005**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**A mensagem **Q215005** indica que o ensaiador não possui o nível exigido no ensaio.  
  
**Solução**  
Caso deseje conceder o acesso para que o usuário em questão faça o preenchimento do laudo, realizando os seguintes passos:  
1. Na rotina de **Cadastro de Ensaios - QIEA020**, localize o ensaio em questão, clique em **Alterar** e verifique o conteúdo do campo **Nivel Ensaiador - QE1\_NIENSR**.  
2. Acesse a rotina **Usuários - QIEA050**, localize o usuário que deverá preencher o laudo, altere o conteúdo do campo **Nivel Usr - QAA\_NIVEL** para o nível informado no **QIEA020** e clique em **Salvar**.
