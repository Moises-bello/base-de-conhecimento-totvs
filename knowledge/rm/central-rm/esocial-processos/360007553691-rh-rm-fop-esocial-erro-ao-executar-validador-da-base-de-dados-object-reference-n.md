---
article_id: 360007553691
category: esocial - Processos
content_hash: 871af4b887d67b86a34dae61ea3be514670be0b026169f634bcbd94f39faf302
fetched_at: '2026-06-28T22:47:08.349198+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao executar validador da base de dados: Object
  reference not set to an instance of an object'
type: support-article
updated_at: '2024-06-14T13:44:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007553691-RH-RM-FOP-eSocial-Erro-ao-executar-validador-da-base-de-dados-Object-reference-not-set-to-an-instance-of-an-object
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao executar a rotina de validação da base de dados do eSocial, é apresentado o erro **Object reference not set to an instance of an object*****.***

**![erro8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045181633/erro8.png)**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Conforme mensagem apresentada, o erro ocorre quando o perfil de parâmetros foi salvo com preenchimento em algum campo ou tabela que, após ajustes para atender os novos Leiautes do eSocial foram deletados.  
  
**Solução**Para correção da ocorrência favor realizar as validações abaixo:  
1. Acesse **eSocial | Saneamento de Dados | Validador da Base de Dados,** na tela inicial exclua todos os perfis de parâmetros cadastrados; 

![ree.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045181093/ree.png)

2. Após exclusão, feche a janela de execução da rotina;  
3. Em seguida, acesse a rotina novamente, crie um novo perfil de parâmetros e avance até finalizar o processo.
