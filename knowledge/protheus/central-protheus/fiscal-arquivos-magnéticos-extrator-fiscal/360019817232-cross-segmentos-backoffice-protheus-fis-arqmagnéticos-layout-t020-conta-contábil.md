---
article_id: 360019817232
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 04de2696f1bc2c1034c13852bb0a6f6f064fddd948bced57747a53844a0fe7f3
fetched_at: '2026-06-28T22:42:07.908624+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T020
  Conta Contábil C6Z_CODCTA inexistente
type: support-article
updated_at: '2022-08-18T17:44:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019817232-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T020-Conta-Cont%C3%A1bil-C6Z-CODCTA-inexistente
---

**Ocorrência**Erro 1 - Linha: 17 - O valor '11602' informado na coluna 2 para o campo (**C6Z\_CODCTA**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois a conta contábil não foi importado para o **TAF**. Este dado populará a tabela **C1O**- **Plano de Contas**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o Extrator Fiscal;  
2. Responda a pergunta: **"Deseja integrar:"**igual a **1-Somente Cadastros**;  
3. Selecione o Layout **T010 - Plano de Contas**e confirme a extração;  
4. Acesse o módulo **TOTVS Automação Fisca**l -> **Miscelânea** -> **Integração** -> **Processamentos** para processar os dados extraídos;  
5. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do *Layout*;  
6. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
