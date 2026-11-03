---
article_id: 360020264271
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 5dc5f7bf9a01d5613fc45a2215d0bc60f3bba23d1139847f06878c07a7c01e5f
fetched_at: '2026-06-28T22:42:07.917284+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T021
  Identificador do Subitem C3K_IDSUBI Inexistente
type: support-article
updated_at: '2022-08-18T17:45:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020264271-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T021-Identificador-do-Subitem-C3K-IDSUBI-Inexistente
---

**Ocorrência**Erro 1 - Linha: 2 - O valor '90101' informado na coluna 5 para o campo(**C3K\_IDSUBI**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código de ajuste não existe na tabela autocontida **CHY-****Código de Subitem** do **TAF,**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **módulo 84 - TOTVS Automação Fiscal**;  
2. Clique em Consultas e depois, na opção Tabelas Dinâmicas;  
3. Filtre a tabela **CHY-****Código de Subitem**e clique em **Abrir Browse** e **Incluir**;  
4. Depois cadastre o código de ajuste e clique em Confirmar;  
5. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
