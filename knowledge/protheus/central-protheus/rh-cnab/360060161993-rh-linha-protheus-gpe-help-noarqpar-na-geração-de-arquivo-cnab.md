---
article_id: 360060161993
category: RH - CNAB
content_hash: ea34e3a3486ea377280f7bdabdce170ed67cc1fdc3f460cd8342d5f3721dd4dd
fetched_at: '2026-06-28T22:43:39.282391+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - HELP NOARQPAR na Geração de arquivo CNAB
type: support-article
updated_at: '2025-06-16T14:30:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060161993-RH-Linha-Protheus-GPE-HELP-NOARQPAR-na-Gera%C3%A7%C3%A3o-de-arquivo-CNAB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23939126727063)**Tempo aproximado para leitura**: 00:02:00** min

**Ocorrência**No módulo Gestão de Pessoal, ao tentar realizar a geração de arquivo CNAB o sistema apresenta *HELP*: NOARQPAR.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Este *HELP* é apresentado por que o nome do *layout* de configuração no servidor pode estar em letras maiúsculas, ou o arquivo de configuração do CNAB não está configurado corretamente.  
  
**Solução**Erro apresentado:

**![noarqpar.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100964953)**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse Miscelânea / Líquido / Geração Arquivo de Líquidos (GPEM080), clique em Perguntas e confirme se a pergunta "Arquivo de Configuração?" está preenchida com o caminho correto do arquivo *layout* de configuração.  
![Gerar CNAB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/23939078450455)

2. Confirme se o nome do arquivo *layout* de configuração CNAB do Protheus esta com letras minúsculas, como no exemplo abaixo:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23939078465559)

3. O erro também pode ser apresentado quando arquivo de configuração não estiver na pasta do diretório informado na pergunta "Arquivo de Configuração?". Neste caso, será necessário adicionar um novo arquivo de configuração na pasta indicada para resolução do erro.

**Saiba Mais:**  
[RH - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
