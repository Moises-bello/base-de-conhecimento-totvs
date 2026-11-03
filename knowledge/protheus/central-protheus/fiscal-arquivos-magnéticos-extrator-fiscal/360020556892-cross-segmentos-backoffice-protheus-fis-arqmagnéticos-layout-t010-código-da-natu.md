---
article_id: 360020556892
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: f9c4d2909abf144c4f113257ca7cc0c3fc5014d508ea6df2c2eddbe42304942f
fetched_at: '2026-06-28T22:42:07.848751+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T010
  Código da Natureza Cta/Grp C1O_CODNAT inexistente
type: support-article
updated_at: '2022-08-18T17:35:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020556892-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T010-C%C3%B3digo-da-Natureza-Cta-Grp-C1O-CODNAT-inexistente
---

**Ocorrência**Erro 1 - Linha: 1 - O valor '1' informado na coluna 3 para o campo Cod Natureza Cta/Grp ( **C1O\_CODNAT** ) não existe na base de dados.  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o grupo de naturezas informado utilizado no plano de contas não existe na tabela autocontida C2R**- Natureza Conta/Grupo Contab** do **TAF**.    
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o configurador e limpe o conteúdo do parâmetro **MV\_VAUTCON**;2. Execute a Wizard de Configuração em: **TOTVS Automação Fiscal** -> Atualizações -> Configs. TAF -> Wizard Config. TAF;  
3. Verifique se a tabela C2R foi populada com o código faltante;  
4. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
