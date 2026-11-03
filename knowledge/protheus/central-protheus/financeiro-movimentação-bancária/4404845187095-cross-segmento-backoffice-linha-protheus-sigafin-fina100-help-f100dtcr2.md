---
article_id: 4404845187095
category: Financeiro - Movimentação Bancária
content_hash: 6e9b57a2f5a78c0e3b3947386b90c3b6a7b65a6f5a161f46fc621e04f688c885
fetched_at: '2026-06-28T22:38:19.412370+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -SIGAFIN -  FINA100 - Help: F100DTCR2'
type: support-article
updated_at: '2026-05-13T18:09:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404845187095-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Help-F100DTCR2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40447448923927) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

O sistema não está permitindo realizar  transferências  (FINA100) em um dia não útil (final de semana ou feriados) .

É exibida mensagem "*F100DTCR2*

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404844965655)

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Financeiro – Todas as versões  
  
**Solução**  
A rotina de Movimentação Bancária (FINA100), para movimentações com data igual ou superior a 24/07/2020, passou a validar se a data de crédito da transferência bancária corresponde a um dia útil, respeitando as regras da função `DataValida`.

Entretanto, essa validação inicialmente não considerava transferências entre caixas financeiros, operações que podem ocorrer independentemente de finais de semana ou feriados. Dessa forma, foi implementado um ajuste permitindo transferências entre bancos caixa, desde que os bancos de origem e destino atendam a pelo menos uma das seguintes condições:

* O código do banco cadastrado (`A6_COD`) possua os dois primeiros caracteres “CX”;
* O banco esteja configurado para operar em carteira, conforme parâmetro `MV_CARTEIR` (exemplo: `CX1/CX2/CX3`);
* O banco esteja configurado como caixa geral financeiro no parâmetro `MV_CXFIN` (exemplo: `CX1/00001/0000000001`);
* O parâmetro `MV_CXLJFIN` esteja habilitado (indicando que os caixas do SIGALOJA também são considerados caixas financeiros) e o banco esteja configurado na Tabela 23 (Tabelas Genéricas - SX5).

Informações adicionais:

* Caso o parâmetro `MV_DIASCRD` esteja configurado, ele não terá efeito sobre transferências entre contas caixa, seguindo a mesma regra mencionada acima.

Assuntos relacionados:

Mesmo com a implementação do PIX, que permite movimentações em finais de semana e feriados, o BACEN não alterou as regras contábeis. Assim, a data contábil da operação continua sendo considerada como o próximo dia útil após a movimentação.

Essa regra pode ser observada nos próprios extratos bancários em operações realizadas via PIX.

Dessa forma, este pacote de correção não contempla movimentações realizadas por PIX.
