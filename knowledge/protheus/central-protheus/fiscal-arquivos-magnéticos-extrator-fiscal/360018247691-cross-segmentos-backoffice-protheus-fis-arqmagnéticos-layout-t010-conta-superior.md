---
article_id: 360018247691
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 16ea83f5d8367604f7c21956d58bfcb7218a8c45b96d31f1c52e22633553d84f
fetched_at: '2026-06-28T22:42:07.851659+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T010
  Conta Superior C1O_CTASUP inexistente
type: support-article
updated_at: '2022-08-18T17:35:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018247691-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T010-Conta-Superior-C1O-CTASUP-inexistente
---

**Ocorrência**O valor '2101010000' informado na coluna 10 para o campo Conta Superior ( **C1O\_CTASUP** ) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, quando existem contas superiores bloqueadas ao efetuar a extração do Layout T010.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Efetue o desbloqueio das contas;

Verifique também o cadastro do planos de contas se está com status bloqueado na "CT1 CT1\_BLOQ = 2 - Não bloqueado"  
**2.** Acesse o Extrator Fiscal;  
**3.** Responda a pergunta: **"Deseja Integrar:"**igual a **1-Somente Cadastros, data de integração 1970 até hoje**;  
**4.** Selecione o *Layout***T010 - Plano de Contas**; e confirme a extração;  
**5.** Acesse o módulo TOTVS Automação Fiscal -> Miscelânea -> Integração -> Processamentos para processar os dados extraídos;  
**6.** Confirme na tela do gerenciador de integração se houveram inconsistências na importação do Layout.
