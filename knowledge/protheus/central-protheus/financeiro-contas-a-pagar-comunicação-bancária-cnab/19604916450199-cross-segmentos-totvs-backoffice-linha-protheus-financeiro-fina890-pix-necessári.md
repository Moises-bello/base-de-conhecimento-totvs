---
article_id: 19604916450199
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 92368a9431e97b6c4639711adf6a91d56f9558dfb7b70991ad99aa15003d6a2d
fetched_at: '2026-06-28T22:37:56.526385+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Totvs BackOffice (Linha Protheus) - Financeiro - FINA890
  - PIX - Necessário informar o nome do arquivo de configuração no Banco XXX
type: support-article
updated_at: '2025-11-12T12:32:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19604916450199-Cross-Segmentos-Totvs-BackOffice-Linha-Protheus-Financeiro-FINA890-PIX-Necess%C3%A1rio-informar-o-nome-do-arquivo-de-configura%C3%A7%C3%A3o-no-Banco-XXX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19604871184407) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar a geração do arquivo de remessa em PIX, ocorre a mensagem**" Necessário informar o nome do arquivo de configuração no Banco XXX"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19604909640343)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois o arquivo de remessa não foi informado nos parâmetros da rotina **FINA890 - Monitor PIX**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19604887075607)  
  
**Solução**  
1. Adicionar o arquivo na pasta Protheus\_data da aplicação  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19604916407703)  
2. Informar o nome do arquivo iniciando com "\"   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19604909647383)  
3. Avançar a opção de seleção de bancos que irá permitir a próxima etapa de seleção de títulos para geração do arquivo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19604887084183)  
  
**Saiba mais**  
[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
