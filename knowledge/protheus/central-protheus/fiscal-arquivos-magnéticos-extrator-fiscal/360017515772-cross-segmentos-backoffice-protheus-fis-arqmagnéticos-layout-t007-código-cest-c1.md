---
article_id: 360017515772
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 5ce4e3375e982fdad7ada35fe2f7063342f8d93b2c84bde21b34cc0f560c965a
fetched_at: '2026-06-28T22:42:07.833316+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T007
  Código CEST C1L_IDCEST inexistente
type: support-article
updated_at: '2022-08-18T17:34:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017515772-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T007-C%C3%B3digo-CEST-C1L-IDCEST-inexistente
---

**Ocorrência**Erro 1 - Linha 1 - O valor '0000000' informado na coluna 28 para o campo identificador do Registro (C1L\_IDCEST) não existe na base de dados.   
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código CEST utilizado não existe na tabela autocontida**T71 (Cod. Especificador ST)**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **módulo 84 - TOTVS Automação Fiscal**;  
2. Clique em Consultas, após na opção Tabelas Dinâmicas;  
3. Filtre a tabela **T71 (Cod. Especificador ST)** e clique em Abrir Browse e Incluir;  
4. Após, cadastre o código CEST e clique em Confirmar;  
5. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
