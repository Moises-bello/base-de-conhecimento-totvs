---
article_id: 360018748731
category: ADVPL - Classe e Função
content_hash: b054306edb58546ce81d2945fb80604d42145e23e46051c1eae3522234409a0a
fetched_at: '2026-06-28T22:40:19.299424+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Executar mile
  em mais de uma filial
type: support-article
updated_at: '2022-01-10T17:54:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018748731-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Executar-mile-em-mais-de-uma-filial
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como executar o mesmo layout do MILE em mais de uma filial sem necessidade de se deslogar do sistema?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
 **Solução**Para executar o layout do MILE em mais de uma filial, será necessário alterar a variável pública cFilAnt.  
Existem duas formas para efetuar esta alteração com base no arquivo de texto:

1. Criando variáveis (aba Variáveis) e utilizando as mesmas em uma condição (condicional ternário) na aba Campos:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014207052/mceclip1.png)  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014207631/mceclip0.png)
2. Criando uma função de usuário que efetue a alteração da propriedade cFilAnt com base nas variáveis memória:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014208491/mceclip0.png)  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014209411/mceclip0.png)  
     
   **Saiba mais**  
   [IIF - Condicional ternário (IF TERNÁRIO)](http://tdn.totvs.com/pages/viewpage.action?pageId=24346937)
