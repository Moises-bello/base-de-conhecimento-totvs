---
article_id: 4402117444247
category: SIGAEST - CUSTOS
content_hash: 5fe3e49da57d277c086205d1cd8179efcd5ed3427b3d2362f4cf4797320dbca9
fetched_at: '2026-06-28T22:39:02.253804+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MOD/GGF - Conceito
  e Usabilidade
type: support-article
updated_at: '2025-03-12T11:42:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402117444247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MOD-GGF-Conceito-e-Usabilidade
---

**Dúvida**O que é MOD e GGF? Qual a usabilidade no Protheus?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**O objetivo deste documento de referência é explicar o conceito de Mão de Obra (MOD), sua regra de negócio e como o sistema Protheus trata produtos do tipo Mão de Obra.

## **O que é MOD (Mão de Obra)?**

Mão de obra é o termo utilizado para se referir, geralmente, ao trabalho manual empregado na fabricação de um bem ou serviço. O custo da MOD representa a parcela de custo que o trabalho empregado representa no custo total do produto ou bem gerado.

**Exemplo:**

Na produção de um copo de vidro foi empregada uma mão de obra que é o funcionário que molda o vidro. O custo desse trabalhador deve ser embutido no custo total do copo de vidro para que a venda do mesmo possa custear a mão de obra utilizada na fabricação.

## **O que é GGF (Gastos Gerais de Fabricação)?**

GGF são gastos envolvidos direta ou indiretamente na produção do produto. Mas que não podem ser apropriados diretamente a cada unidade produzida.

**Exemplo:**

Água, energia elétrica, depreciação de máquinas, aluguel do prédio e etc...

## **Produto MOD no Protheus**

O Protheus trata o custo da mão de obra e dos gastos gerais de fabricação em um único tipo de produto, o produto tipo MOD. Logo, podemos entender que no sistema o MOD é:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402376503959/mceclip0.png)

É possível incluir no sistema um produto MOD de duas maneiras:

* Cadastrar o produto com o campo Código (B1\_COD) = MOD + Código do Centro de Custo  
  Importante: Essa forma de cadastrar irá fazer com que todo valor do centro de custo seja alocado no produto.
* Informar o campo CC p/ Custo (B1\_CCCUSTO) = Código do Centro de Custo.  
  Importante: Se for necessário dividir o valor do centro de custo entre mais de um produto, informar o campo Gr Cnt Custo (B1\_GCCUSTO), para utilizar o conceito de Grupo dentro do Centro de Custo.

**Observação importante**: Se a empresa possuir integração contábil e desejar que o custo "venha do lançamento", o código do produto **não pode conter nem iniciar com "MOD"** e deve possuir o campo B1\_CCCUSTO preenchido.

Para melhor entendimento de como configurar e como utilizar MOD e GGF com e sem integração contábil, basta avaliar a nossa documentação abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Processo de configuração de MOD e GGF com e sem integração contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
