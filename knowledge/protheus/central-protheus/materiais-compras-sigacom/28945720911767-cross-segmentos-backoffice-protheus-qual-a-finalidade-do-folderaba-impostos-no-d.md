---
article_id: 28945720911767
category: Materiais - Compras (SIGACOM)
content_hash: cdc1ee6337fb8b57f8ba6d984a96005b7f315addf7fd4eb80e4989a4f46b456d
fetched_at: '2026-06-28T22:41:11.873012+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Qual a finalidade do Folder/Aba Impostos
  no Documento de Entrada?
type: support-article
updated_at: '2025-01-03T18:16:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28945720911767-Cross-Segmentos-Backoffice-Protheus-Qual-a-finalidade-do-Folder-Aba-Impostos-no-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28945739503255) Tempo aproximado para leitura: **00:02:00 min****Dúvida**

Qual a finalidade do Folder / Aba "Impostos" no Documento de Entrada?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as Versões

**Solução**

Este folder apresenta as informações relacionadas aos tributos que incidem sobre o Documento de Entrada e está dividido em três partes: **Dados de Cobrança do ISS**, **DIRF** e **Informações referentes aos impostos.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28945720889623)

***1- Dados de Cobrança do ISS:*** Contém as informações referentes a cobrança do ISS, tais como o fornecedor para qual será gerado o título de ISS do documento e a data de vencimento do título.  
Dica: Utilize o parâmetro ***MV\_AUTOISS*** para preencher automaticamente as informações de cobrança de ISS e DIRF.   
Através do parâmetro é possível informar o código e a loja do fornecedor para qual será gerado o título de ISS, se o título do documento deverá se usado para geração de DIRF e o código de retenção.

***2- DIRF:*** Contém informações relacionadas a DIRF e ao ISS, tais como se o título vinculado ao documento deve gerar DIRF, código de retenção e se a responsabilidade do pagamento do ISS é do tomador do serviço. Obs.: Para visualizar os dados referente a DIRF é necessário habilitar o parâmetro ***MV\_VISDIRF***.  
Dica: Utilize o parâmetro ***MV\_AUTOISS*** para preencher automaticamente as informações de cobrança de ISS e DIRF.   
Através do parâmetro é possível informar o código e a loja do fornecedor para qual será gerado o título de ISS, se o título do documento deverá se usado para geração de DIRF e o código de retenção.

***3- Informações referentes ao impostos:*** Contém as informações referentes aos tributos que incidem sobre o documento.

**Obs:**

* Para ativar a pasta Dirf, altere o valor do parâmetro ***MV\_VISDIRF*** para 1.
* Em caso de dúvidas sobre o cálculo dos impostos, entre em contato com a equipe do suporte ao módulo Fiscal.

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
