---
article_id: 360018491891
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 0562876131b98099dd6f38ea96a2e859dc9f767ecdc9924e5e6826b3f8a77809
fetched_at: '2026-06-28T22:42:07.902073+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T020
  Código de Ajuste C2T_CODAJU Inexistente
type: support-article
updated_at: '2022-08-18T17:44:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018491891-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T020-C%C3%B3digo-de-Ajuste-C2T-CODAJU-Inexistente
---

**Ocorrência**Erro 1 - Linha: 4 - O valor 'SP000002' informado na coluna 2 para o campo Código do Ajuste (**C2T\_CODAJU**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código de ajuste não existe na tabela autocontida **C1A - **Ajuste da Apuração do ICMS**** do **TAF**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **módulo 84 - TOTVS Automação Fiscal**;  
2. Clique em Consultas, após na opção Tabelas Dinâmicas;  
3. Filtre a tabela **C1A - Ajuste da Apuração do ICMS**  e clique em Abrir Browse e Incluir;  
4. Depois cadastre o código de ajuste e clique em Confirmar;  
5. Efetue novamente a extração e processamento do**Layout T020**.
