---
article_id: 360022293072
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 4ab5430b1ff03fe41db75e81e3c04cffa8d7c8201affb6da5c33b05eb14ed46b
fetched_at: '2026-06-28T22:42:07.846201+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T007
  Unidade de Medida C1L_UM inexistente
type: support-article
updated_at: '2022-08-18T17:35:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022293072-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T007-Unidade-de-Medida-C1L-UM-inexistente
---

**Ocorrência**Erro 1 - Linha: 1 - O valor 'UN' informado na coluna 5 para o campo Unidade de medida ( C1L\_UM ) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, quando a unidade de medida utilizada, não existe no TAF. **Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o Extrator Fiscal;  
2. Responda a pergunta: **"Deseja Integrar:"**igual a **1-Somente Cdastros**;  
3. Selecione o *Layout* **T005- Identificação das Unidades de Medida** e confirme a extração;  
4. Acesse o módulo **TOTVS Automação Fiscal** -> Miscelânea -> Integração -> Processamentos para processar os dados extraídos;  
5. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do *Layout*;   
6. Efetua re-integração do *Layout* T007 - Identificação do item.
