---
article_id: 4434133305879
category: Meu RH - Home
content_hash: e50f02a46e9bfc6cbb68a5a05a787f385d120d63945b354c1cf1f6cec6d3d578
fetched_at: '2026-06-28T22:47:34.603226+00:00'
product: rm
section_id: 1500000861702
source: central-rm
title: RH - RM - Meu RH - O que fazer quando é apresentado o erro, período ativo não
  encontrado
type: support-article
updated_at: '2024-10-15T17:49:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4434133305879-RH-RM-Meu-RH-O-que-fazer-quando-%C3%A9-apresentado-o-erro-per%C3%ADodo-ativo-n%C3%A3o-encontrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22321767005847) Tempo aproximado para leitura: **00:02:20 min** **Ocorrência**Quando o funcionário acessa o Meu RH, é retornado no canto direito o erro: **Período ativo não encontrado. Favor verificar a inconsistência no cadastro de períodos.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**O erro é apresentado, quando o usuário que acessou o Meu RH está vinculado a um Perfil do Automação de Ponto porém, não existem Períodos Ativos cadastrados no Automação de Ponto.  
  
**Solução**Para solucionar o erro, existem **2 opções**:  
  
**1° Opção:**Simplesmente acessar o Produto Automação de Ponto / Configurações / Períodos e cadastrar um período:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27087368637207)  
  
2° Opção:**Acessar Serviços Globais / Usuários, informe no campo Sistema o **Automação de Ponto**, edite o usuário que acessou o Meu RH e remova a associação ao Perfil do Automação de Ponto conforme exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22321883695895)  
  
Após qualquer uma das opções, a mensagem de erro não será mais apresentada via Meu RH.
