---
article_id: 19589572088599
category: Financeiro - Contas a Pagar - Comunicação Bancária Online
content_hash: b91dd5c81f03180e04728107ee0f7cf4eb5c335f310b20c75f15f1ce2fc25b14
fetched_at: '2026-06-28T22:37:49.956920+00:00'
product: protheus
section_id: 26656222001687
source: central-protheus
title: Cross Segmentos - Totvs BackOffice (Linha Protheus) - Financeiro - FINA713
  - Configurar Juros e Multa para o Banco itau
type: support-article
updated_at: '2025-11-27T14:39:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19589572088599-Cross-Segmentos-Totvs-BackOffice-Linha-Protheus-Financeiro-FINA713-Configurar-Juros-e-Multa-para-o-Banco-itau
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19589583821847) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Ao enviar o boleto online do Itaú via API, ocorre a mensagem: **"Data de juros deve ser maior que a data de vencimento".**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19603343830807)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Solução**  
Para ajustar os juros e multa para o banco Itaú, deve acessar a rotina FINA710 - Novo Gestor Financeiro, em **"Configuração de Contas"**, editar o layout do banco Itaú e adicionar nos campos de Juros e Multa a informação abaixo:

**SE1->E1\_VENCREA+1**  
Nessa configuração, os juros irão começar a contar a partir de um dia após o vencimento real do título, conforme o percentual de juros/multa informado.

Exemplo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19589608784919)

Necessário cancelar o borderô e adicionar novamente para transmissão.

Saiba mais  
[**Contas a receber (Comunicação bancária online)**](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)

[**Configuração do layout de configuração de contas FINA713**](https://tdn.totvs.com/pages/releaseview.action?pageId=736963446)
