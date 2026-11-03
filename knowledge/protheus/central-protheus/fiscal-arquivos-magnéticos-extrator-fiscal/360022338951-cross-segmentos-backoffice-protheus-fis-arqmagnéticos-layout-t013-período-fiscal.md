---
article_id: 360022338951
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: deb8b796f1edc5f6ee5d365ea88c7b2fcfc4955c1130fb4609dd5b513b2a23ca
fetched_at: '2026-06-28T22:42:07.898974+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Período Fiscal C2G_PERFIS Não Informado
type: support-article
updated_at: '2022-08-18T17:44:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022338951-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-Per%C3%ADodo-Fiscal-C2G-PERFIS-N%C3%A3o-Informado
---

**Ocorrência**Erro 1 - Linha: 6 - Coluna: 5 Campo obrigatório não informado: Per. Fiscal Pr ( **C2G\_PERFIS** )  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o complemento de **Comunicação/Telecomunicação** não foi informado no cadastro de origem do dado.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse a rotina **Nota fiscal manual de saída**, posicione o cursor sobre a nota e acione as opções **Outras Ações -> Complemento -> Comunicação/Telecomunicação**e preencha oo campo **Per. Fiscal** **(FX\_PERFIS)**;  
2. Acesse o Extrator Fiscal;  
3. Responda a pergunta: **"Deseja integrar:"**igual a **1-Somente Cadastros**;  
4. Selecione o *Layout***T013- Documento Fiscal** e confirme a extração;  
5. Acesse o módulo **TOTVS****Automação Fiscal -> Miscelânea -> Integração -> Processamentos** para processar os dados extraídos;  
6. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do *Layout.  
7. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.*
