---
article_id: 360016688871
category: Materiais - Compras (SIGACOM)
content_hash: ef88050f130e8d88ec326b8a8f9b14449b15b9cea6b8824faa15dfae48204eb2
fetched_at: '2026-06-28T22:41:08.939233+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help CNPJ/CPF - Modo
  edição não respeitado. Valor não pode ser atribuído. (CNPJ/CPF)
type: support-article
updated_at: '2023-01-09T14:35:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016688871-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-CNPJ-CPF-Modo-edi%C3%A7%C3%A3o-n%C3%A3o-respeitado-Valor-n%C3%A3o-pode-ser-atribu%C3%ADdo-CNPJ-CPF
---

**Ocorrência**

Help CNPJ/CPF - Modo edição não respeitado. Valor não pode ser atribuído. (CNPJ/CPF)

No **módulo Compras** ao tentar finalizar inclusão de um fornecedor pela rotina **Fornecedor** o sistema apresenta a mensagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012694711/mceclip0.png)

**Ambiente**Protheus – Compras – A partir da versão 12.1.17.  
  
**Causa**Validação incorreta do campo.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o sistema via APSDU/Arquivo/Abrir - Localizar a tabela -SX3;  
2. Após, filtre pela tabela SA2;  
3. Altere o campo X3\_VALID;  
4. Segue o print da validação abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/M7hXZf2fIevmhWhwmnRcd0MvM/?name=inline1807360285.png)

​
