---
article_id: 8661171970071
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 60794044489543c411c6d7832a40b9c859a3e5100b2abbcaa5ddbf31d4f4bbc6
fetched_at: '2026-06-28T22:39:47.840559+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Erro ao fechar
  a tela de atualização dos NCM's via TOTVS COMEX Conteúdo
type: support-article
updated_at: '2022-09-05T16:41:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8661171970071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Erro-ao-fechar-a-tela-de-atualiza%C3%A7%C3%A3o-dos-NCM-s-via-TOTVS-COMEX-Conte%C3%BAdo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao fechar a tela de integração de NCM via TOTVS Comex Conteúdo, é exibido um Error Log.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8660567437591/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8660569710231/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– Todas versões  
  
**Solução**

Ao fechar a janela de seleção de NCM, era retornado um campo vazio, dando prosseguimento a rotina, gerando portanto, o erro. Sendo assim, foi feita uma validação para prosseguir apenas se um dos botões forem selecionados.

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1079377>; 12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1079375>; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1079376>;

**Saiba mais**

<https://tdn.totvs.com/pages/releaseview.action?pageId=706922787>
