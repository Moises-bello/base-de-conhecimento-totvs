---
article_id: 1500001352161
category: LEGAIS - BLOCO H/MATR460
content_hash: 6a93e438322bfa8894830fa371d6da397e58ba4e8fa70f5a19a6ee0ba49ca114
fetched_at: '2026-06-28T22:42:15.206702+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do Parâmetro
  MV_R460TPC
type: support-article
updated_at: '2021-04-30T12:26:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001352161-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-Par%C3%A2metro-MV-R460TPC
---

**Dúvida**

Qual o objetivo da utilização do parâmetro MV\_R460TPC e o que ele influencia na impressão do relatório MATR460 (P7)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O parâmetro MV\_R460TPC tem uma grande importância quando utilizamos o relatório MATR460, pois ele tem o intuito de configurar o tratamento do Custo de produtos em terceiros sendo M = Custo médio ou R = Custo Remessa)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001356162/mceclip0.png)

**Exemplificando a usabilidade deste parâmetro**

Vamos utilizar o seguinte cenário:

- Entrada de 2 produtos a custo R$100,00;

- Saída para armazém de terceiro de quantidade 1 (MV\_CONTERC e MV\_ALMTERC ativado), com custo médio de R$100,00;

- No próximo período após o fechamento, teremos mais uma entrada com quantidade 1 à custo R$ 120,00 deixando o custo em estoque com R$110,00;

Ao gerar o MATR460: nos dois cenários do parâmetro MV\_R460TPC teremos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102934853/mceclip0.png)

**Saiba mais:**

*[MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901)*

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
