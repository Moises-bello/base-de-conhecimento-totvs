---
article_id: 4410700053271
category: Manutenção de Ativos (SIGAMNT)
content_hash: 8839130d9359c8b3775c2e6b39852e4c8d289b1c3765049078337d52837d5fa8
fetched_at: '2026-06-28T22:42:34.035662+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Geração de Documentos a Vencer - MNTA815
type: support-article
updated_at: '2021-10-29T11:46:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410700053271-Manufatura-Linha-Protheus-MNT-Gera%C3%A7%C3%A3o-de-Documentos-a-Vencer-MNTA815
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:15 min** **Dúvida**Para que serve a rotina **Geração de Documentos a Vencer - MNTA815**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**A rotina**MNTA815** permite o gerenciamento dos documentos que irão vencer, possibilitando o controle das datas de vencimento.  
Com o objetivo de gerenciar os documentos que irão vencer e por meio da seleção dos parâmetros, serão definidos os documentos a vencer, conforme projeção e número de parcelas. É importante observar o campo **Valor**, que deverá ser exatamente igual ao valor total dos itens da **Nota Fiscal**. O programa leva em consideração a data atual do Sistema **+ 1 ano** se for optado por anual e **+ 1 mês** se a opção foi mensal. Deve existir um documento gerado para o bem, pois ele irá fazer os cálculos com base no último documento para aquele veículo.   
  
**Importante**

* Observar a **Família**, **Ano** e **Modelo** do veículo, pois os registros de pagamentos futuros serão gerados de acordo com estas informações.
* Antes de rodar o programa para calcular novos vencimentos, altere a frequência de pagamento do documento de 12 meses para 6 meses.

**Saiba mais**Acesse a documentação completa da rotina no *link* [Geração de Documentos a Vencer - MNTA815.](https://tdn.totvs.com/pages/viewpage.action?pageId=640192699)
