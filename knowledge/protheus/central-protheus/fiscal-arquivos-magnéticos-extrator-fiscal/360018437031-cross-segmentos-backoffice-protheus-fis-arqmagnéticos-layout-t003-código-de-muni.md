---
article_id: 360018437031
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: ee74730d9a6ff437eb8c260213bee75049824e4e7ee248fd55863b7bb35d6cb6
fetched_at: '2026-06-28T22:42:07.830361+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T003
  Código de Município C1H_CODMUN inexistente
type: support-article
updated_at: '2022-08-18T17:34:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018437031-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T003-C%C3%B3digo-de-Munic%C3%ADpio-C1H-CODMUN-inexistente
---

**Ocorrência**Erro 1 - Linha: 1 - O valor 'SP' informado na coluna 16 para o campo Cod. Id. UF (**C1H\_UF**) somado ao valor '10153' informado na coluna 8 para o campo Cod. Ident.Municipio (**C1H\_CODMUN**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código de município informado para o cadastro de cliente/fornecedor não existe na tabela autocontida **C07 - Municípios do IBGE** do TAF.    
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse APSDU, abra a tabela **T2U** e apague o conteúdo do campo **T2U\_VERSAO** referente a tabela C07;2. Execute a Wizard de Configuração em: **TOTVS Automação Fiscal** -> Atualizações -> Configs. TAF -> Wizard Config. TAF;  
3.  Verifique se a tabela C07 foi populada com o município faltante;  
4. Efetue a extração e processamento do *Layout*T003 novamente.   
  
**Observação:**  
  
Verifique se o município é válido, conforme Tabela do IBGE.
