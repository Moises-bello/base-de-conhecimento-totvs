---
article_id: 360016522372
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 829306c81770f2932ff2dfeb80346d98a1f0a678577345868c625f1614a7cf2a
fetched_at: '2026-06-28T22:42:07.905477+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T020
  Código de Ajuste C2T_CODAJU inexistente.
type: support-article
updated_at: '2022-08-18T17:44:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016522372-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T020-C%C3%B3digo-de-Ajuste-C2T-CODAJU-inexistente
---

**Ocorrência**O valor ' SP02718 ' informado na coluna 2 para o campo Código do Ajuste (**C2T\_CODAJU**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código de ajuste utilizado não existe na tabela autocontida **C1A (Ajuste da Apuração do ICMS)**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o módulo 84 **- TOTVS Automação Fiscal**;  
2. Clique em Consultas -> Tabelas Dinâmicas;  
3. Filtre a tabela **C1A** **(Ajuste da Apuração do ICMS)** e clique em Abrir Browse e Incluir;  
4. Após, cadastre o código de ajuste e clique em Confirmar;  
5. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
