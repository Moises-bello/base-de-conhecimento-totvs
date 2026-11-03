---
article_id: 360019124371
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 8e24cfc257558e48520ae2b13954f23bd05ea042a6b2f3861726fbc47c2f6185
fetched_at: '2026-06-28T22:42:07.887814+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Identificação do Modelo C20_CODMOD inexistente
type: support-article
updated_at: '2022-08-18T17:43:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019124371-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-Identifica%C3%A7%C3%A3o-do-Modelo-C20-CODMOD-inexistente
---

**Ocorrência**Erro 1 - Linha: 1 - O valor '01' informado na coluna 15 para o campo  **(C20\_CODMOD)** não existe na base de dados.  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código de identificação do modelo não existe na tabela **C01 (Modelos dos Documentos Fiscais)** do **TAF**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o módulo **Configurador**e limpe o conteúdo do parâmetro **MV\_VAUTCON**;2. Acesse o módulo **TOTVS Automação Fiscal** -> **Atualizações** -> **Configs. TAF** -> **Wizard Config. TAF**;  
3. Marque a caixa de seleção ao lado da coluna **Status Autocontidas**e clique em **Avançar**;  
4. Selecione a opção ***Layout* TOTVS ou Tabela Compartilhada no SGDB** e clique em **Avançar**;  
5. Informe os parâmetros para conexão com o banco de dados e clique em **Avançar**;  
6. Clique em **Processar as configurações realizadas neste assistente**e aguarde o término da atualização;   
7. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
