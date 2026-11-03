---
article_id: 360018492531
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 7739de0189ecaf5937363ecc0011f690a5f8798b50ea989a56db47d26e533ce1
fetched_at: '2026-06-28T22:42:07.911514+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T020
  Identificador do Subitem C2T_IDSUBI Inexistente
type: support-article
updated_at: '2022-08-18T17:44:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018492531-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T020-Identificador-do-Subitem-C2T-IDSUBI-Inexistente
---

**Ocorrência**Erro 2 - Linha: 4 - O valor '00285' informado na coluna 5 para o campo Identificador do Subitem (**C2T\_IDSUBI**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código de ajuste não existe na tabela autocontida **CHY-** **Código de Subitem** do **TAF**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **módulo 84 - TOTVS Automação Fiscal**;  
2. Clique em Consultas, após na opção Tabelas Dinâmicas;  
3. Filtre a tabela **CHY-** **Código de Subitem**e clique em Abrir Browse e Incluir;  
4. Depois cadastre o código de ajuste e clique em Confirmar;  
5. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
