---
article_id: 8130646811159
category: Integrações Outros BackOffice
content_hash: 1656898697f8ce7f51c2cf1ea3ba0b73e1c6577357f1493fbc535853e0a6f099
fetched_at: '2026-06-28T22:46:42.126402+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RM - FOP - Integração RM Labore x BackOffice Protheus - Não encontrado no DE/PARA
type: support-article
updated_at: '2025-02-03T19:24:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8130646811159-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-N%C3%A3o-encontrado-no-DE-PARA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:30 min****Dúvida**Como ajustar o erro entidade XXXX não encontrada no DE/PARA quando há integração entre o **RM Labore x BackOffice Protheus?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Utilizando como exemplo o **Cliente/Fornecedor**, é retornado o erro ao realizar alguma integração entre o RM Labore x BackOffice Protheus podendo ser envio de Lançamento Financeiro, Contábil, Funcionários e outros.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8130502172183/mceclip1.png)

2. Provavelmente o item mencionado no erro (no exemplo é o fornecedor) teve a chave alterada de algum modo, é necessário validar novamente o DE/PARA do Protheus nesse caso em **SIGACFG>AMBIENTE>Schedule> De/para mensagem única**

![](https://totvssuporte.zendesk.com/attachments/token/jn9OCRLRA3BuPeGl6t2vt6VIW/?name=image.png)

3. Verifique se o DE/PARA existe corretamente na tabela do item retornado no erro, no caso de fornecedores é realizado na tabela **SA2** campo **A2\_COD**  
   
![](https://totvssuporte.zendesk.com/attachments/token/mo3mMKn8DxW5MC8VB3IK0OdP8/?name=image.png)  
   
Caso preferir, o cliente poderá também recriar o DE/PARA automaticamente:

1. Excluir o DE/PARA do item que retornou o erro no **RM** e também no **Protheus**;
2. Caso o Protheus envie naturalmente na integração o item que retornou erro, deve-se acessar o Protheus e editar alguma informação, como no exemplo foi o fornecedor, edite esse fornecedor e altere algum campo qualquer como nome: FORNECEDOR TESTE ficaria FORNECEDOR TESTEXXXX  por exemplo.
3. Caso o RM envie naturalmente na integração o item que retornou erro, poderá realizar o mesmo passo da dica 2 para criar o DE/PARA também.
4. Essa alteração no nome envia novamente o Fornecedor (ou o item que retornou o erro) do **Protheus** ao **RM criando um novo registro de DE/PARA correto ou do RM ao Protheus.**

   
![](https://totvssuporte.zendesk.com/attachments/token/YkZ0QngSocrta59acTXTxs5Q6/?name=image.png)
