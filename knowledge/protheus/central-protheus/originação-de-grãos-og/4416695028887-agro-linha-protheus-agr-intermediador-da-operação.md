---
article_id: 4416695028887
category: Originação de Grãos (OG)
content_hash: 4185544b8d98499cc7bc5a2c09d7533f888a7851b86d88de2677de7219cf38b2
fetched_at: '2026-06-28T22:45:40.941024+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Intermediador da Operação
type: support-article
updated_at: '2025-01-03T19:38:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416695028887-Agro-Linha-Protheus-AGR-Intermediador-da-Opera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20412739416215) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Como informar o intermediador da operação no modulo SIGAAGR?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Beneficiamento de Sementes - UBS** Ao gerar um pedido de venda através da rotina **Ordem de Carregamento - AGRA900;** Será atualizada a informação da tabela **SC5 - Pedido de Venda** **C5\_INDPRES - Presença Comprador** com o valor **zero** não se aplica.  
**Beneficiamento de Algodão - UBA;** Ao gerar um pedido de venda através da rotina **Romaneio de Saída - AGRA750;** Será atualizada a informação **C5\_INDPRES** com o valor **zero** não se aplica.  
**Comercialização de commodities;** No **Contrato de Venda - OGA290**, **Compra e Armazenagem - OGA270, OGA280 e OGA260;** Será possível informar a **presença do comprador** e o **código do intermediador**.  
No romaneio, no **cabeçalho** e na aba **comercialização** será possível **informar** a presença do comprador e o código do intermediador, por padrão será preenchido com o mesmo **valor do contrato**.
