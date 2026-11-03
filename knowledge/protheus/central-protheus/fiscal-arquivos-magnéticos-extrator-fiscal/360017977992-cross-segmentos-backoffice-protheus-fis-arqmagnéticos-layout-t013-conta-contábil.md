---
article_id: 360017977992
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: b352b178f41763fc89d5fc93dc9b19069dac06fedc0f73d823af0b7a01e7852c
fetched_at: '2026-06-28T22:42:07.880820+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Conta Contábil e Centro de Custo C30_CTACTB, C30_CCUSTO inexistente
type: support-article
updated_at: '2022-08-18T17:40:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017977992-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-Conta-Cont%C3%A1bil-e-Centro-de-Custo-C30-CTACTB-C30-CCUSTO-inexistente
---

**Ocorrência**O valor '6101030200' informado na coluna 9 para o campo Conta Contábil (**C30\_CTACTB**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, quando a conta contábil utilizada não existe na tabela **C1O - Plano de Contas** do TAF. Este item é levado para o TAF, através da extração do *Layout* **T010 - Plano de Contas.****Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o Extrator Fiscal;  
2. Responda as perguntas:

* **Deseja integrar:"**igual a **1-Somente Cadastros**;;
* **Data de: "**01/01/**1979"** **data até "Informar data de hoje"**
* **Apenas Reinf: NÃO**

3. Selecione o Layout **T010 - Plano de Contas, T011 - Centro de custo**e confirme a extração;  
4. Acesse o módulo **TOTVS Automação Fiscal** -> Miscelânea -> Integração -> Processamentos para processar os dados extraídos;  
5. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do *Layout*;   
6. . Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
