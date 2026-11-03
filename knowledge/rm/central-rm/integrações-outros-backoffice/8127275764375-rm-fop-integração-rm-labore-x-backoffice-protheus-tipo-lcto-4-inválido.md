---
article_id: 8127275764375
category: Integrações Outros BackOffice
content_hash: 94d69bfb5ff8880d86b213db7ae66975d89300a357d06a39defd8ae34bf1b3ee
fetched_at: '2026-06-28T22:46:42.130725+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RM - FOP - Integração RM Labore x BackOffice Protheus - Tipo Lcto 4 - Inválido
type: support-article
updated_at: '2025-02-03T19:25:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8127275764375-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Tipo-Lcto-4-Inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:38 min****Ocorrência**Quando se utiliza a integração entre o **RM x Backoffice Protheus**, ao realizar a integração de algum lançamento contábil, é retornado o erro na tabela **CT2** e ao acessar o **XML**, informa que o tipo de lançamento 4 é inválido.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema **Protheus** aceita 40 caracteres para o campo de histórico e o **RM** envia um valor maior que este.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Obtenha o XML do erro utilizando o artigo [RH - RM - FOP - Integração RM Labore x BackOffice Protheus: Obtenção o XML mensagem de Resposta e Transformada no RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036176914)  
2. Identifique a linha do lançamento que retornará o erro, exemplo:

* O erro foi apresentado informando no item 112, está informando que o tipo de lançamento enviado é o 4, o sistema acusa este como inválido.
* A integração acontece somente com tipo 1,2 e 3, quando retornado o tipo 4 é pelo motivo do **histórico do evento** que foi contabilizado ser muito grande.

![](https://totvssuporte.zendesk.com/attachments/token/Uq48yoeRcZwlUGTQwsCMJkJDH/?name=image.png)

   
Observe na imagem acima que o campo **Hist Lanc** preencheu somente **FÉRIAS**, já no evento item 111 (no xml temos que observar 1 valor a menos) o histórico é preenchido como **4438 - ESTORNO DE PENSAO ALIMENTICIA S/ FERIAS.**

O erro acusou somente **FÉRIAS** que foi os caracteres que ultrapassaram o limite de 40 da tabela do **Protheus**.  
   
   
![](https://totvssuporte.zendesk.com/attachments/token/Ov5jT3nznMG2XjYad52Pz55t1/?name=image.png)  
3. Deverá acessar o cadastro do evento que possui esse histórico e ajustar para valores menores que 40 caracteres para que a integração ocorra normalmente.

![](https://totvssuporte.zendesk.com/attachments/token/46HdP9T1h8qnFochUfCmfNZtp/?name=image.png)
