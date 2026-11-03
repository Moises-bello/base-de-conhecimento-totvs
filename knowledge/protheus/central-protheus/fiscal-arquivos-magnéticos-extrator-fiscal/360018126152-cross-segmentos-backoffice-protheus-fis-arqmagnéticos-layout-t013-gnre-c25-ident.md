---
article_id: 360018126152
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 2caba9446930c86f520d746db500e9408c86939214d607818e60207f01e45d34
fetched_at: '2026-06-28T22:42:07.883710+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  GNRE C25_IDENTI inexistente
type: support-article
updated_at: '2022-08-18T17:40:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018126152-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-GNRE-C25-IDENTI-inexistente
---

**Ocorrência**Erro 1 - Linha: 2 - O valor '1' informado na coluna 2 para o campo (**C25\_IDENTI**) somado ao valor '**ICM000035674**' informado na coluna 3 para o campo (**C25\_IDENTI**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois a **GNRE (Guia Nacional de Recolhimento)** não foi importado para o TAF. Este dado populará a tabela **C0R** - **Documento de Arrecadação**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o Extrator Fiscal;  
2. Responda a pergunta: **"Deseja integrar:"**igual a **1-Somente Cadastros**;  
3. Selecione o Layout **T001AE- Documento de Arrecadação**e confirme a extração;  
4. Acesse o módulo **TOTVS Automação Fisca**l -> Miscelânea -> Integração -> Processamentos para processar os dados extraídos;  
5. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do *Layout*;  
6. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
