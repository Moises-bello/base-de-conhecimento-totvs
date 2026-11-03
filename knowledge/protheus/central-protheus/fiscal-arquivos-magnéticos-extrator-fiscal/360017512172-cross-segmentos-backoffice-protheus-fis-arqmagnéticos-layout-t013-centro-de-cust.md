---
article_id: 360017512172
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: bb9a5b253f5b0141b0e550104354a7d86724e20e765a71b63cbc34b94d4de84a
fetched_at: '2026-06-28T22:42:07.864431+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Centro de Custo C30_CCUSTO Inexistente
type: support-article
updated_at: '2022-08-18T17:39:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017512172-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-Centro-de-Custo-C30-CCUSTO-Inexistente
---

**Dúvida**Erro 1 - Linha: 6 - O valor '21010102' informado na coluna 10 para o campo  **(C30\_CCUSTO)** não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Solução**Este incidente ocorre, pois este centro de custo não foi importado para o TAF.  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o Extrator Fiscal;  
2. Responda a pergunta: **"Deseja Integrar:"**igual a **1-Somente Cadastros**;  
3. Selecione o Layout **T011 - Centro de Custo** e confirme a extração;  
4. Acesse o módulo TOTVS Automação Fiscal -> Miscelanea -> Integração -> Processamentos para processar os dados extraídos;  
5. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do Layout.  
  
**Observação:**  
Ainda no gerenciador de integração, posicione o cursor no registro que referente ao *Layout*T013   
que obteve inconsistência do campo **C30\_CCUSTO** e acione as opções: Outras Ações -> Habilitar Reintegração para que o registro que obteve a inconsistência seja integrado novamente ao TAF.
