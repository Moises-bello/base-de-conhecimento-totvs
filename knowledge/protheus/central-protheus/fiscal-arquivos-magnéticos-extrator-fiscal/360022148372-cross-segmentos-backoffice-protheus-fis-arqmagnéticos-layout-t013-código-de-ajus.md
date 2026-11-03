---
article_id: 360022148372
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: ee8706810e0a86641e252e791f0c271ef30927d8f16301b9b123db554e074f73
fetched_at: '2026-06-28T22:42:07.868399+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Código de Ajuste C2D_CODAJ Inexistente
type: support-article
updated_at: '2022-08-18T17:39:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022148372-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-C%C3%B3digo-de-Ajuste-C2D-CODAJ-Inexistente
---

**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código de ajuste não existe na tabela autocontida **C0J - **Ajuste do Documento Fiscal**** do **TAF**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **módulo 84 - TOTVS Automação Fiscal**;  
2. Clique em Consultas, após na opção Tabelas Dinâmicas;  
3. Filtre a tabela **C0J - **Ajuste do Documento Fiscal**** do **TAF**e clique em Abrir Browse e Incluir, cadastre o código de ajuste e clique em Confirmar;  
4. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
