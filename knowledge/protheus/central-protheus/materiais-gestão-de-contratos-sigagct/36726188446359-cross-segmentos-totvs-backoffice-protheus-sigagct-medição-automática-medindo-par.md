---
article_id: 36726188446359
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 9f77f58beb98111d85b0e0e47d4e71cb3010c188876c286cc57851f54d4032e1
fetched_at: '2026-06-28T22:37:23.850297+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Medição Automática
  medindo parcela do Cronograma parcialmente, ficando centavos em aberto
type: support-article
updated_at: '2025-12-02T19:47:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36726188446359-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-medindo-parcela-do-Cronograma-parcialmente-ficando-centavos-em-aberto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36726220718103) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Medição Automática fazendo medição parcial da parcela do Cronograma, ficando centavos de valor em aberto

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Referente a questão de uma medição realizada totalmente, em que ao realizar medição, ela não é baixada totalmente ficando centavos de valor em aberto, em casos ja verificados no atendimento do suporte, a situação pode estar relacionados a divergencia de tamanho de campo e decimais nos campos relacionados a quantidade de valor dos processo realizado.

Dessa forma orienta-se, referente uso de casas decimais nos processos do Gestão de Contratos, para o correto funcionamento deve ser realizada a análise e verificação no ambiente em questão de todos os campos envolvidos de quantidade e valor, se estão condizentes com o mesmo tamanho e número de casas decimais, no dicionário e banco de dados tanto campos referentes a quantidade quanto campos referentes a valor.

E também serem verificados da mesma forma os campos dos documentos dos outros módulos que são gerados pelo GCT, como Pedido de Compras e/ou Venda e Títulos, por exemplo.  
  
Abaixo segue artigo que contêm as informações disponíveis sobre casas decimais do Gestão de Contratos e também artigo do FAT, que contem informações de campos de demais módulos a serem conferidos no ambiente, e após ajuste estando condizentes a realização de teste com novo contrato cadastrado.

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os campos a serem considerados no ajuste de casas decimais das tabelas do Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022576132-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-campos-a-serem-considerados-no-ajuste-de-casas-decimais-das-tabelas-do-Gest%C3%A3o-de-Contratos-?source=search)  
  
[FAT0068 Aumento de Casas Decimais no ambiente Faturamento (SIGAFAT)](https://tdn.totvs.com/x/twEmDg)  
  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Casas decimais no Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001427308-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Casas-decimais-no-Faturamento?source=search)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
