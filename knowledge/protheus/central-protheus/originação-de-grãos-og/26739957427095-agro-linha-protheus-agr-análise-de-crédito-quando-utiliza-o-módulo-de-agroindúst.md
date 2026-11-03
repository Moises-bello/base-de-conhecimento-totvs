---
article_id: 26739957427095
category: Originação de Grãos (OG)
content_hash: a54ded66e282f696c60245897c49637670749f77718eae1ccbb8f7dd7fb77fcb
fetched_at: '2026-06-28T22:45:36.981685+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Análise de Crédito quando utiliza o Módulo de
  Agroindústria
type: support-article
updated_at: '2025-06-13T21:16:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26739957427095-Agro-Linha-Protheus-AGR-An%C3%A1lise-de-Cr%C3%A9dito-quando-utiliza-o-M%C3%B3dulo-de-Agroind%C3%BAstria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26739924888983) Tempo aproximado para leitura: **00:02:20 min** **Dúvida**Como é realizado a **Análise de Crédito quando utiliza o Módulo de Agroindústria**?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12.1.17  
  
**Solução****Assunto:**

A **análise de crédito** tem como objetivo avaliar a possibilidade de conceder **crédito** a uma pessoa física ou jurídica, analisando a veracidade das informações prestadas e suas condições de honrar os compromissos financeiros. Também serve para minimizar os riscos da operação financeira e maximizar os resultados esperados.

Para definir as regras de limite de crédito do cliente é necessário analisar os campos:

**• Risco**  
**• Limite de Crédito**  
**• Limite de Crédito Secundário**  
**• Vencimento do Limite de Crédito**  
**• Classe de Crédito**  
**• Moeda do Limite de Crédito**  
**• Parâmetros Utilizados**

O **Sistema Protheus** em seu produto padrão já possui mecanismos de **análise de créditos** a serem aplicados em operações de vendas ou saída, garantindo o momento no qual o agente cedente irá avaliar o potencial de retorno do tomador do crédito, bem como, os riscos inerentes à concessão.  
  
**Regra de Análise de Crédito quando utiliza o Módulo de Agroindústria:**

Quando é utilizado o módulo de Agroindústria e o parâmetro **MV\_AGRB003 - Mercado que terá análise de crédito** estiver ativo, será considerado a seguinte regra **1=Mercado Interno; 2=Mercado Externo; 3=Ambos ou 4=Nenhum**, o Sistema passará a avaliar além dos pontos acima descritos, mais o **Romaneio Corrente**, **Agendamento** e **Contrato em Andamento**, conforme regra abaixo detalhada.

Fluxo do processo

![](https://tdn.totvs.com/download/attachments/396372038/modelo.png?version=1&modificationDate=1535650954000&api=v2)
