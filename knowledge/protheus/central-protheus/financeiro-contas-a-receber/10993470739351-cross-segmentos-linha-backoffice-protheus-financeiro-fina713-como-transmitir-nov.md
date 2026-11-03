---
article_id: 10993470739351
category: Financeiro - Contas a Receber
content_hash: f9b9eb7e3327da0504c4e2320336b7aab1355318868a5281b3006902ffac7516
fetched_at: '2026-06-28T22:38:14.205213+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Linha BackOffice Protheus - Financeiro - FINA713 - Como transmitir
  novamente o Borderô via Boleto Online
type: support-article
updated_at: '2022-12-16T19:32:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10993470739351-Cross-Segmentos-Linha-BackOffice-Protheus-Financeiro-FINA713-Como-transmitir-novamente-o-Border%C3%B4-via-Boleto-Online
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Como transmitir novamente o Bordero com erro via Boleto Online?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
**1 - Caso onde possua 1 titulo dentro do Bordero**  
Cancelar o Bordero via FINA060, após correção, colocar em Bordero novamente  
  
**2 - Caso onde possua mais de 1 titulo dentro do Bordero**  
Utilizar a rotina **FINA590 - Manutenção de Bordero**, para retirar o titulo do Bordero, após a correção da incosistencia, incluir o titulo dentro do Bordero pela mesma rotina ( FINA590 ) e realizar novamente a transmissão  
  
**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Configuração e Funcionalidade do Novo Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7019775569047)  
[Boletos (Comunicação Bancária via API) - FINA710](https://tdn.totvs.com/pages/viewpage.action?pageId=612548392)
