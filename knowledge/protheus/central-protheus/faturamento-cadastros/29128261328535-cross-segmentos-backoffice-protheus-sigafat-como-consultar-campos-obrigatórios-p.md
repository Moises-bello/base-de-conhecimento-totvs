---
article_id: 29128261328535
category: Faturamento - Cadastros
content_hash: e4cd2944a53c6cf5c7b1a46f76ce43bb2c8cdb26f522f836efae13d79a94035f
fetched_at: '2026-06-28T22:38:35.486441+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT -Como consultar campos obrigatórios
  pela APSDU
type: support-article
updated_at: '2026-06-22T19:58:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29128261328535-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Como-consultar-campos-obrigat%C3%B3rios-pela-APSDU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29128261296279) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como faço para consultar quais campos eu possuo obrigatório em uma rotina/tabela?  
  
**Ambiente**Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Você pode consultar os campos obrigatórios acessando a **APSDU** e entrando na tabela SX3. Em seguida, selecione a opção "Útil" e clique em "Copiar Para". No campo "Para", informe a seguinte expressão:  
  
**(Subs(X3Reserv(X3\_RESERV),7,1)=="x" .or. Subs(X3\_OBRIGAT,1,1)== "x")**  
  
Feito isso ficará conforme a imagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29128234187927)  
  
**Observação:** Caso não tenha acesso à **APSDU**, será necessário realizar a consulta diretamente pelo "configurador"(**SIGACFG**), acessando as tabelas e consultando campo por campo. Não existe outro processo além do descrito neste artigo.
