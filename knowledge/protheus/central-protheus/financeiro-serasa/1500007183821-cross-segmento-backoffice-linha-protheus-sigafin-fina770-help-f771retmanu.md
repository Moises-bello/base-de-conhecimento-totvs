---
article_id: 1500007183821
category: Financeiro - Serasa
content_hash: c79a6f71a45f7e03df14c589b35e12cfccc50ba785d1811e62b6d8d54596ded3
fetched_at: '2026-06-28T22:37:28.234585+00:00'
product: protheus
section_id: 35058289522071
source: central-protheus
title: 'Cross segmento - Backoffice Linha Protheus - SIGAFIN - FINA770 - HELP: F771RETMANU'
type: support-article
updated_at: '2026-01-30T12:39:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007183821-Cross-segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA770-HELP-F771RETMANU
---

**Ocorrência**

Ao baixar um arquivo de retorno do Serasa está apresentando a seguinte mensagem:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500010177821)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA770 - Versão 12.0  
  
**Causa**  
Na consulta posição do título pode verificar o Status do titulo do Serasa **(Título não esta no Serasa)**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009908382)  
  
  
**Solução**  
Para retirar do Serasa é preciso que o título esteja como incluído no campo **FWA\_STATUS** (Status Serasa que aparece na consulta posição de título) e o mesmo possa retirar.  
  
**Exemplo**  
É bem parecido como o processo do **CNAB**.   
O mesmo envia para o banco, recebe e retorna com a ocorrência **entrada confirmada**.  
No **Serasa** você manda o título do cliente e retorna o Status incluído que grava no campo **FWA\_STATUS**.  
**0=Sem restrições;**  
**1=Selecionado;**  
**2=Enviado;**  
***3=Incluido***
