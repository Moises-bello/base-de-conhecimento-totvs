---
article_id: 36882064512535
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7be99b9ccb226abd67ebe5173a0e1cb0e9f59043d7f5942f83ccd8f0b5d7f815
fetched_at: '2026-06-28T22:42:46.998774+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Seleção do contrato de parceria para
  geração de autorização de entrega pelo MRP
type: support-article
updated_at: '2025-12-09T17:46:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36882064512535-Manufatura-Linha-Protheus-SIGAPCP-Sele%C3%A7%C3%A3o-do-contrato-de-parceria-para-gera%C3%A7%C3%A3o-de-autoriza%C3%A7%C3%A3o-de-entrega-pelo-MRP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36882064499863) Tempo aproximado para leitura: **00:00:55 min**  
  
**Dúvida**  
Na geração de documentos pelo **MRP**, como é feita a seleção do contrato de parceira para gerar a autorização de entrega?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Nos casos em que há mais de um contrato de parceria , pode-se definir a matriz de fornecimento que será utilizada quando o parâmetro **MV\_MATRIZF** tiver o conteúdo **.T.**.  
Caso o parâmetro tenha conteúdo **.F.** , deve-se observar o preenchimento do parâmetro **MV\_PESQCTP**, com esse parâmetro com o conteúdo **F**, no cadastro do produto, através do preenchimento dos campos **B1\_PROC** e **B1\_LOJPROC** deve ser informado o fornecedor e a loja que atende a demanda, caso o parâmetro **MV\_PESQCTP** tenha o conteúdo **P** o Sistema ordenará os contratos por ordem crescente de código de fornecedor e loja e aquele que tiver disponibilidade para realizar a entrega será selecionado automaticamente

**Saiba mais**  
Para mais informações sobre matriz de fornecimento no link [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Matriz de Fornecimento (MATA128)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412998824215-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Matriz-de-Fornecimento-MATA128)

**Glossário**  
**MRP** - Material Requirement Planning  
**MV\_MATRIZF** - Indica se utiliza matriz de fornecimento para contrato de parceria  
**MV\_PESQCTP** - Indica se a pesquisa do contrato de parceria será por produto+fornecedor+loja (F) ou somente por produto (P)  
**B1\_PROC** - Fornecedor padrão  
**B1\_LOJPROC** - Loja padrão
