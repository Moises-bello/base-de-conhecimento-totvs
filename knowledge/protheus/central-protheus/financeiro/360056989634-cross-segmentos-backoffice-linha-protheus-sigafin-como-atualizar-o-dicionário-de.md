---
article_id: 360056989634
category: Financeiro
content_hash: f573db0526ea17e86e02cab6da08c50699eb1922e2ba04484bb51158556d4a21
fetched_at: '2026-06-28T22:38:01.248333+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como atualizar o dicionário
  de dados (arquivo SXSBRA.TXT) do Protheus 12
type: support-article
updated_at: '2024-04-18T21:15:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056989634-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-atualizar-o-dicion%C3%A1rio-de-dados-arquivo-SXSBRA-TXT-do-Protheus-12
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**MP - SIGAFIN - Como atualizar o dicionário de dados  (arquivo SXSBRA.TXT) do Protheus 12

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Para atualizar o dicionário de dados do Protheus 12, siga o procedimento abaixo:

- Acesse o Portal do Cliente: [http://suporte.totvs.com](http://suporte.totvs.com/)

- Menu Downloads e Atualizações

- Linha Protheus

- Microsiga Protheus Versão 12.1.XX (onde XX é a versão da Release do P12 que você vai utilizar)

- Todos

- Categoria: Dicionário de dados

- Baixe o DICIONÁRIO DE DADOS COMPLETO - BRASIL se estiver fazendo uma migração de versão anterior do           Protheus para Protheus 12;

- Baixe tanto o DICIONÁRIO DE DADOS COMPLETO - BRASIL quanto o DICIONÁRIO DE DADOS DIFERENCIAL - BRASIL se estiver fazendo uma migração de release do Protheus 12

Obs.: se não estiverem aparecendo as versões, em "Filtros de pacotes" selecione "Todos pacotes disponíveis" e selecione a categoria novamente.  
Após baixar, descompacte o arquivo SXSBRA.TXT na pasta Systemload do Protheus.

Se estiver fazendo migração de versão anterior do Protheus para Protheus 12, o migrador de versão irá utilizar o dicionário completo como base.

Se estiver fazendo migração de release do Protheus 12, após atualizar os arquivos, deve executar o [UPDDISTR](http://tdn.totvs.com/pages/viewpage.action?pageId=181965468).

Aviso:

SOMENTE execute o UPDDISTR se estiver migrando de release do Protheus 12, de uma release antiga para uma release nova. Se estiver fazendo migração de uma versão anterior do Protheus para Protheus 12, NÃO É NECESSÁRIO executar o UPDDISTR.
