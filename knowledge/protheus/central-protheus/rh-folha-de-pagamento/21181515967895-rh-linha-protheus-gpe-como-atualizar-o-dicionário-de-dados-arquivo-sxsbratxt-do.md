---
article_id: 21181515967895
category: RH - Folha de Pagamento
content_hash: 85db031852e9de22fb43839c033324324ba32130335d274940da3e1fadfe5c90
fetched_at: '2026-06-28T22:44:12.163013+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como atualizar o dicionário de dados (arquivo SXSBRA.TXT)
  do Protheus 12
type: support-article
updated_at: '2025-04-16T11:38:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21181515967895-RH-Linha-Protheus-GPE-Como-atualizar-o-dicion%C3%A1rio-de-dados-arquivo-SXSBRA-TXT-do-Protheus-12
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21181502264599) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como atualizar o dicionário de dados (arquivo SXSBRA.TXT)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
   
**Solução**

Para atualizar o dicionário de dados do Protheus 12, siga o procedimento abaixo:

- Acesse o Portal do Cliente: <http://suporte.totvs.com>

- Menu Downloads e Atualizações

- Linha Protheus

- Microsiga Protheus Versão 12.1.XX (onde XX é a versão da Release do P12 que você vai utilizar)

- Todos

- Categoria: Dicionário de dados

- Baixe o DICIONÁRIO DE DADOS COMPLETO - BRASIL se estiver fazendo uma migração de versão anterior do Protheus para Protheus 12;

- Baixe tanto o DICIONÁRIO DE DADOS COMPLETO - BRASIL quanto o DICIONÁRIO DE DADOS DIFERENCIAL - BRASIL se estiver fazendo uma migração de release do Protheus 12

Obs.: se não estiverem aparecendo as versões, em "Filtros de pacotes" selecione "Todos pacotes disponíveis" e selecione a categoria novamente.  
Após baixar, descompacte o arquivo SXSBRA.TXT na pasta Systemload do Protheus.

Se estiver fazendo migração de versão anterior do Protheus para Protheus 12, o migrador de versão irá utilizar o dicionário completo como base.

Se estiver fazendo migração de release do Protheus 12, após atualizar os arquivos, deve executar o UPDDISTR.

Aviso:

SOMENTE execute o UPDDISTR se estiver migrando de release do Protheus 12, de uma release antiga para uma release nova. Se estiver fazendo migração de uma versão anterior do Protheus para Protheus 12, NÃO É NECESSÁRIO executar o UPDDISTR.

**Saiba Mais:**

[MP - FIS - Procedimento UPDDISTR – Central de Atendimento TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042296533-MP-FIS-Procedimento-UPDDISTR)
