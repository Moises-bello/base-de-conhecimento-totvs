---
article_id: 5452451527191
category: Materiais - Compras (SIGACOM)
content_hash: 9aa3ddec7e86385bec62d9991e81d9618e991cc9d5fb0781eeb95be86c33b0d7
fetched_at: '2026-06-28T22:41:18.810645+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP A100CQ no Documento
  de Entrada
type: support-article
updated_at: '2026-04-23T15:53:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5452451527191-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-A100CQ-no-Documento-de-Entrada
---

**Ocorrência**

HELP A100CQ ao tentar excluir um documento de entrada:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5452414571031/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões.  
  
**Causa**O help A100CQ ocorre quando o produto relacionado a NF possui integração com o módulo Inspeção de Entradas. Neste caso ao entrar com a NF o sistema encaminha a mesma para o armazém de CQ e após a realização da inspeção é realizada a baixa de CQ para que o saldo do produto seja enviado para o armazém de produção.  
   
Sendo assim é necessário estornar a baixa de CQ através da rotina QIEA215 para que o saldo do produto retorne ao armazém de CQ. Assim o sistema permitirá excluir a NF.  
   
Quando o Controle de Qualidade (CQ) do produto é realizado, ao realizar a entrada do produto automaticamente o produto irá para a rotina de "BAIXAS do CQ" para liberação ou rejeição. A mensagem apresentada ocorre em duas situações:  
   
• Quando o produto foi rejeitado pelo CQ.  
• Quando o produto foi liberado pelo CQ.  
   
Não duas situações a legenda do produto na rotina de Baixas do CQ ficará "vermelha". Para conseguir realizar a exclusão da nota deve-se realizar o estorno: selecionar o registro no Baixas do CQ e clicar em estornar; Na ultima linha dos dados apresentados, preencher o campo "Estorno" com "X" e confirmar; A movimentação deverá ficar com legenda "verde".

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar Baixa do C.Q. (MATA175)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011962151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-Baixa-do-C-Q-MATA175-)
