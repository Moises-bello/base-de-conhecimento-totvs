---
article_id: 39154724662295
category: Escrita Fiscal - Configurador de Tributos
content_hash: 061f50159e265b34d5b318b284d57f3bcc51837db3d77a5c756f9e495a918105
fetched_at: '2026-06-28T22:39:17.614514+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  FIS - Como gerar GNRE pelo Fisa170?
type: support-article
updated_at: '2026-03-19T18:56:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39154724662295-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-gerar-GNRE-pelo-Fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39154724645143) Tempo aproximado para leitura: 00:05**min**  
  
**Dúvida**  
Como gerar GNRE pelo Fisa170?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Segue a  configuração para Gerar GNRE pelo fisa170, exemplo ICMS ST

MV\_estado = SP

MV\_SUBTRIB = SP120120120120

Cliente = BA

TES

CFOP = 6401

Valor da mercadoria = 1000,00

Base do icms = 1000,00\*7% = 70,00

Base do icms st = 1000,00\*39,73% = 1379,30\*20,5% = 282,76

282,76-70,00= 212,76

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39154733791383)

Configurações para Gerar a GNRE

Guia de escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39154733793559)

Codigo de receita

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39154733796503)

Vincular no Cadastro de regra de calculo ICMSST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39154733797271)

No pedido de Vendas

Gera GNRE = sim

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39154733802135)

obs: Para gerar a Guia de recolhimento SE2 precisa configurar o financeiro

<https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras>

Boletim

https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos
