---
article_id: 360021431171
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: a53cfaf2b834d35f013a63927014290040191a58b3bfe0ccf2e6524f7bf4b4ce
fetched_at: '2026-06-28T22:42:07.924089+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T082
  Conta Contábil C5M_CODCTA inexistente
type: support-article
updated_at: '2022-08-18T17:45:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021431171-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T082-Conta-Cont%C3%A1bil-C5M-CODCTA-inexistente
---

**Ocorrência**O valor '2101010000' informado na coluna 11 para o campo ( **C5M\_CODCTA**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre quando a conta contábil não foi importada para o TAF.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o desbloqueio das contas;  
2. Acesse a rotina do **Extrator Fiscal**;  
3. Responda a pergunta: **"Verifica movimento para os layouts cadastrais?"**igual a 1-Não;  
4. Selecione o *Layout***T010 - Plano de Contas**;  
5. Confirme a extração;  
6. Acesse o módulo **TOTVS Automação Fiscal** -> **Miscelanea -> Integração -> Processamentos** para processar os dados extraídos;  
7. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do *Layout*;  
8. Após isso, efetue a extração e processamento do registro **T082** novamente.
