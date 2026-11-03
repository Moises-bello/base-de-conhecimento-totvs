---
article_id: 20461832854423
category: Faturamento - Cenários de Venda
content_hash: 5e56490fbfcb828c405340915652fba8f94cbafec52fe265f6710cd70f1627ae
fetched_at: '2026-06-28T22:38:34.096530+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT -  OMSA010 - Tabela
  de preço permitindo incluir o mesmo item diversas vezes
type: support-article
updated_at: '2025-01-10T19:39:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20461832854423-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-OMSA010-Tabela-de-pre%C3%A7o-permitindo-incluir-o-mesmo-item-diversas-vezes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20461832837399) Tempo aproximado para leitura: **00:05:00 min** **Dúvida:**Tabela de preço permitindo incluir o mesmo item diversas vezes - OMSA010  
  
**Ambiente:**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução:**

Trata-se de um conceito, é possível ter dois ou mais produtos iguais na mesma tabela, desde que os campos de **DA1\_QTDLOT** (Faixa), **DA1\_ESTADO** (Estado) ou **DA1\_DATVIG** (Vigência) estejam diferentes.  
 

**Exemplos:**

1 - Tenho um produto PROD01, cadastro esse produto a partir de 09/01/2024 Vigência **(DA1\_DATVIG)** vai custar R$ 300,00, mas em 01/03/2024 o produto vai mudar o preço para R$ 350,00, então pode-se incluir esse produto duas vezes, mas com vigências diferentes.  
   
2 - Outro cenário de exemplo, em SP aplica-se um preço, mas no RJ aplica-se outro, então é possível cadastrar o produto duas vezes, desde que o estado **(DA1\_ESTADO)**, não seja o mesmo.  
   
3 - Suponhamos que, até a quantidade (faixa) **(DA1\_QTDLOT)** de 100 itens do produto na tabela é um preço, de 100 itens até 200 é outro preço e acima de 200 é outro preço diferente, então, pode-se cadastrar esse mesmo produto diversas vezes, desde que em faixas diferentes.  
   
Então é necessário verificar se os campos citados estão iguais nesse produto que está sendo incluído duas ou mais vezes na tabela de preço, vale ressaltar que, se um ou dois campos citados estiverem iguais, o sistema vai permitir a inclusão, só não vai permitir, caso os 3 campos citados estiverem exatamente iguais, gerando a mensagem do exemplo abaixo.

![uniqueline.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20461827302167)

**Veja também:**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como converter a tabela de preço para outra moeda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047416534-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-converter-a-tabela-de-pre%C3%A7o-para-outra-moeda?source=search)**
