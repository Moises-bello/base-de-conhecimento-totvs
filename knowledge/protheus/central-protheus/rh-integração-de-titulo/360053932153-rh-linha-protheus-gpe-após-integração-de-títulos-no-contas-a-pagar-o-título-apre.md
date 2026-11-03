---
article_id: 360053932153
category: RH - Integração de Titulo
content_hash: 13a70f5f4f22894770d52cf0d41e785c69c5d87baa609d4d30d20095aaa62796
fetched_at: '2026-06-28T22:43:36.147681+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Após Integração de títulos no contas a pagar, o
  título apresenta natureza diferente do titulo gerado no GPE
type: support-article
updated_at: '2025-07-23T20:02:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053932153-RH-Linha-Protheus-GPE-Ap%C3%B3s-Integra%C3%A7%C3%A3o-de-t%C3%ADtulos-no-contas-a-pagar-o-t%C3%ADtulo-apresenta-natureza-diferente-do-titulo-gerado-no-GPE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33657601606295)** Tempo aproximado para leitura: 00:02:00 min

**Ocorrência**Após Integração de títulos no contas a pagar, o título apresenta natureza diferente do titulo gerado no GPE.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**1) Verifique se a tabela SE2 possui alguma validação customizada, para receber e alterar a natureza amarrada no fornecedor. Instruções para verificação podem ser encontradas na documentação relacionado no tópico **Saiba Mais** deste documento

2) Verifique se existe natureza cadastrada para fornecedor e se a ordem dos campos no Contas a Pagar foi alterado para Fornecedor - Natureza.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Será necessário ajustar a validação de modo que a natureza informada no GPE, seja preponderante a natureza cadastrada no fornecedor ou retornar o campo da tabela SE2 para o padrão:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089234993)  
  
2. Caso tenha ocorrido alteração na sequência dos campos na tabela SE2 (de E2\_NATUREZ/E2\_FORNECE para E2\_FORNECE/E2\_NATUREZ), o fornecedor cadastrado com natureza fará o gatilho e preencherá automaticamente o campo natureza.

Será necessário ajustar os campos no padrão ou verificar junto ao Departamento Financeiro, se a natureza amarrada ao fornecedor, pode ser alterada ou excluída. ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089235233)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Na integração de títulos é apresentada a mensagem: Um ou mais campos obrigatórios não foram preenchidos Natureza](https://totvssuporte.zendesk.com/knowledge/articles/4403032076183/pt-br?brand_id=1509248)
