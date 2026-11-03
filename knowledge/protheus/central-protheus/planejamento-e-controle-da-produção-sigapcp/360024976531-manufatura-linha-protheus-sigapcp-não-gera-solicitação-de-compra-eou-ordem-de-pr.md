---
article_id: 360024976531
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 341b097ea7f3a927c74bd5d7b5e8c252fadb1d0e0cd9515c5e9834b324940f4d
fetched_at: '2026-06-28T22:42:44.595379+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Não gera solicitação de compra  e/ou
  ordem de produção intermediária automaticamente ao abrir uma ordem de produção
type: support-article
updated_at: '2025-12-18T20:37:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024976531-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-gera-solicita%C3%A7%C3%A3o-de-compra-e-ou-ordem-de-produ%C3%A7%C3%A3o-intermedi%C3%A1ria-automaticamente-ao-abrir-uma-ordem-de-produ%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18535993202967)** Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Por que não gera **SC -** **Solicitação de Compra** e/ou **Ordem de Produção Intermediária** automaticamente ao abrir uma **OP -** **Ordem de Produção**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Primeiramente é necessário verificar se os parâmetros **MV\_GERASC - Gera Solicitação de Compras a partir da inclusão da ordem de produção** para a geração de **SCs** e o parâmetro **MV\_GERAOPI - Gera OP do produto Intermediário a partir de OP do produto principal** para a geração de **OPs** intermediárias estão ativados.  
  
Caso os parâmetros acima estejam ativados, é necessário verificar a faixa de armazéns para verificação dos estoques disponíveis na lista de parâmetros do **MATA650 - Ordens de produção**. Por meio do parâmetro **Cons So. Armazém Padrão?** é possível indicar se deve considerar somente o armazém padrão. Se o conteúdo deste parâmetro for **Não** o Sistema analisará o saldo disponível conforme os parâmetros **Considera do Armazém?** e **Até o Armazém?**  
  
Ou seja, ao gerar os empenhos o Sistema verificará se há saldo para empenhar os produtos considerando as faixas de armazéns informados no filtro. Se mesmo analisando a faixa de armazéns informados no filtro não for encontrado saldo disponível o Sistema gerará as **OPs** e **SCs**. Porém essa verificação na faixa de armazéns apenas ocorrerá se o parâmetro **MV\_CONSEST - Considera Estoque na Geração de Ordem de Produção?** for igual a **S**.  
  
**Importante**  
Os parâmetros **MV\_GERASC** e **MV\_GERAOPI** não vão impactar na geração das **Solicitações de Compra** e das **OPs Intermediárias** geradas pelo **MRP - Material Requiriments Planning**
