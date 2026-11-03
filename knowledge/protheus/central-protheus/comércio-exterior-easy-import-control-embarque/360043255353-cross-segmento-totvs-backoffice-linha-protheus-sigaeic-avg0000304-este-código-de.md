---
article_id: 360043255353
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: a717538c2b2a6478a4c824d2ce3e78bac67d2db20411d0764ba813171f5ddf80
fetched_at: '2026-06-28T22:39:48.699427+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - AVG0000304 - Este
  Código de Despesa não pode ser incluído
type: support-article
updated_at: '2022-05-02T20:49:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043255353-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-AVG0000304-Este-C%C3%B3digo-de-Despesa-n%C3%A3o-pode-ser-inclu%C3%ADdo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao incluir a despesa da solicitação de numerário apresenta a mensagem: AVG0000304 - Este Código de Despesa não pode ser Incluído.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Import Control – A partir da versão 11.80  
  
**Solução**Ao rotina Numerário (EICNU400) irá apresentar a mensagem , caso esteja incluído as despesas: 101/104/901/902/903, estas não podem ser informadas.   
- Despesa 101 (FOB) gerada com a inclusão da Invoice.   
- Despesa 104 (CIF) .  
- Despesa 901 (Adiantamento a despachante) gerada automaticamente pelo sistema na tabela SWD com o total das despesas adiantadas ao despachante.   
- Despesa 902 (Complemento ao Despachante) utilizada na prestação de contas.  
- Despesa 903 (Devolução do Despachante) utilizada na prestação de contas.  
  
**Saiba mais**  
[MP - SIGAEIC - Solicitação de Numerário - Prestação de Contas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000300267)
