---
article_id: 360057700374
category: Comércio Exterior - Easy Export Control - Relatórios
content_hash: 61bd9260430b54ce57647f65a7080c1527ebeb3a7003829aa660b91ef278a1f7
fetched_at: '2026-06-28T22:36:59.917721+00:00'
product: protheus
section_id: 1500001538161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Erro ao tentar
  imprimir relatório do Crystal
type: support-article
updated_at: '2022-06-14T19:05:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057700374-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Erro-ao-tentar-imprimir-relat%C3%B3rio-do-Crystal
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Qual o procedimento para correção das mensagens durante a utilização dos relatórios do Crystal no módulo de Exportação?

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097855794/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097855934/mceclip2.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Export Control* – A partir da versão 12.1.17  
  
**Solução**Para solução da primeira mensagem será necessário a instalação do arquivo AVGXML2DBF.   
Segue boletim técnico como efetuar a instalação:  
[Como instalar AvgXML2DBF, caso apresente a mensagem Run time error 429?](https://tdn.totvs.com/pages/releaseview.action?pageId=69271844)  
  
Para solução da segunda mensagem será necessário efetuar alteração de um parâmetro. Acesse o módulo SIGACFG em Base de Dados, selecione Dicionário / Base de dados/Parâmetros. Altere o conteúdo do parâmetro **MV\_AVG0053** para ponto (.) conforme é exibido pela imagem abaixo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097866474/mceclip5.png)
