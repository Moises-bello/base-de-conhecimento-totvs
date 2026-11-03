---
article_id: 28442210102551
category: Materiais - Compras (SIGACOM)
content_hash: b5a33d768b1b9573d9995312e0de31b061f2dc5170e9df2e02544227b8d8a4b9
fetched_at: '2026-06-28T22:41:17.378145+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de entrada
  com integração com RH não mostra dados na aba de Duplicatas
type: support-article
updated_at: '2024-12-11T13:24:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28442210102551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-entrada-com-integra%C3%A7%C3%A3o-com-RH-n%C3%A3o-mostra-dados-na-aba-de-Duplicatas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28442210074903) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Ao incluir um documento de entrada com integração com RH (utilizando um fornecedor com o campo A2\_NUMRA vinculado a um número de matrícula de pessoa cadastrada no módulo de RH) o sistema exibe os dados na aba de Duplicatas, porém, após incluir o documento e visualizar o mesmo, os dados de natureza financeira e valores de título não são mais exibidos.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Versão 12

**Solução**

Ao incluir um documento de entrada com integração com módulo de RH todos os valores que seriam gerados no módulo Financeiro passam a ser gerados no módulo de RH, que compreende a gravação da tabela SRK - Movimento de Valores Futuros. Neste caso, nenhum valor será gravado no módulo Financeiro, sejam valores de títulos ou natureza financeira.  
Os valores mostrados no momento da inclusão da nota são apenas uma prévia dos valores que serão gerados para o módulo de RH.  
Após a inclusão da nota, todos os valores deverão ser verificados no módulo de Gestão de Pessoal.

***Saiba Mais :***

[MP - SIGACOM - Pontos de Entrada - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000169747-MP-SIGACOM-Pontos-de-Entrada-Compras?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
