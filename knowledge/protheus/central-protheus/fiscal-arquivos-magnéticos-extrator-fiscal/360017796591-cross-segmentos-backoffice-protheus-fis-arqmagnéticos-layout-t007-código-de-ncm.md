---
article_id: 360017796591
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: b4dc1321c4c79a0cd5885b76c59e83df40b6fd75191be3bb32eb9977b7966c2d
fetched_at: '2026-06-28T22:42:07.836534+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T007
  Código de NCM C1L_CODNCM inexistente
type: support-article
updated_at: '2025-11-13T19:21:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017796591-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T007-C%C3%B3digo-de-NCM-C1L-CODNCM-inexistente
---

**Ocorrência**Erro 1 - Linha: 1 - O valor '84819000' informado na coluna 7 para o campo Cod. Id. NCM (C1L\_CODNCM) somado ao valor '' informado na coluna 8 para o campo Cod. Id. NCM (C1L\_CODNCM) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código de NCM utilizado não existe na tabela autocontida**C0A (Nomenclatura Comum Mercosul)**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **módulo 84 - TOTVS Automação Fiscal**;  
2. Clique em **Consultas**, após na opção Tabelas Dinâmicas;  
3. Filtre a tabela **C0A (Nomenclatura Comum Mercosul)** e clique em Abrir Browse e Incluir;  
4. Depois cadastre o código de ajuste e clique em Confirmar;  
5. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
