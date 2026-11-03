---
article_id: 37074826747543
category: Contabilidade gerencial - Reforma Tributária
content_hash: 092b9d1ff7a9e7b1af57116820a9dc578c886817072f4567eebccb4d914b4b39
fetched_at: '2026-06-28T22:40:29.740796+00:00'
product: protheus
section_id: 37095816599831
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - Adequação do
  Plano de Contas e Lançamentos à Reforma Tributária
type: support-article
updated_at: '2025-12-19T20:07:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37074826747543-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-Adequa%C3%A7%C3%A3o-do-Plano-de-Contas-e-Lan%C3%A7amentos-%C3%A0-Reforma-Tribut%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37153005462935) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Como adequar a Contabilidade Gerencial (SIGACTB) para atender às exigências da reforma tributária, novos tributos (IBS, CBS e IS) ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - A partir da Versão 12.1.2410

**Solução** 

A Reforma Tributária estabelece um sistema de impostos sobre consumo que exige maior transparência contábil. Os tributos deixam de estar embutidos nos valores brutos, demandando que a contabilização seja realizada de forma segregada (valor líquido versus tributo) em cada operação.

Para garantir a conformidade fiscal, a rastreabilidade dos valores e a correta previsibilidade de caixa, é necessário realizar ajustes cadastrais e de processos no módulo Contabilidade Gerencial (SIGACTB).

**Siga os passos abaixo para realizar as adequações:**

**1. Diagnóstico Inicial** Antes de alterar o sistema, mapeie os fluxos de receitas e tributos impactados. Identifique quais impostos terão contabilização automática (**IBS**, **CBS**) e revise os processos de faturamento para entender o tratamento atual dos valores brutos e líquidos.

**2. Revisão do Plano de Contas (Rotina CTBA020)** É necessário adaptar o Plano de Contas (tabela CT1) para refletir a nova sistemática.

* **Receita Bruta:** Inclua contas específicas para registrar valores antes da dedução de tributos.
* **Receita Líquida:** Crie contas para valores após retenções, permitindo a visão real da receita disponível.
* **Tributos a Recolher:** Crie contas passivas transitórias, segregando cada imposto (**IBS**, **CBS**, etc.) individualmente.
* **Diferenças e Ajustes:** Crie contas de controle para conciliar divergências entre registros contábeis e fiscais.

**3. Configuração de Lançamentos Padrão (Rotina CTBA080)** Ajuste ou crie novos Lançamentos Padrão (tabela CT5) para garantir a segregação.

* Evite contas genéricas; cada categoria tributária deve possuir conta específica.
* Certifique-se de que o histórico padrão facilite o rastreamento das partidas dobradas.
* Valide em ambiente de teste se os lançamentos automáticos estão classificando corretamente os valores líquidos e os tributos destacados.

**4. Revisão de Demonstrativos Contábeis** Ajuste as visões gerenciais que compõem os relatórios oficiais:

* **DRE (Demonstração do Resultado):** Deve apresentar a receita já líquida dos tributos retidos, separando Receita Bruta, Tributos Retidos e Receita Líquida.
* **Balanço Patrimonial:** Detalhe no Passivo as contas de "Tributos a Recolher" (**IBS**, **CBS**, **ISS**) e contas de conciliação de diferenças.
* **DFC (Fluxo de Caixa):** Separe o pagamento de tributos do recebimento bruto de vendas, pois os tributos destacados impactam diretamente o fluxo operacional.

**5. Exemplo de Contabilização (Compra de Mercadoria)** Considerando uma mercadoria de R$ 10.000,00 com **IBS** (12%) e **CBS** (9%) destacados, totalizando uma Nota Fiscal de R$ 12.100,00, a estrutura sugerida é:

| **Conta Contábil** | **Natureza** | **Valor (R$)** | **Observação** |
| --- | --- | --- | --- |
| Estoques (Ativo) | Débito | 10.000,00 | Valor líquido da mercadoria |
| Tributos a Recolher – IBS (Passivo) | Débito | 1.200,00 | Imposto destacado separado |
| Tributos a Recolher – CBS (Passivo) | Débito | 900,00 | Imposto destacado separado |
| Fornecedor a Pagar (Passivo) | Crédito | 12.100,00 | Valor total da NF |

**Exemplo de Plano de Contas com 3 (Três) níveis:**

![gif_plano.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37153710013463)

**Saiba mais:**  
[Adequando a Contabilidade à Reforma Tributária](https://tdn.totvs.com/pages/releaseview.action?pageId=975771867)
