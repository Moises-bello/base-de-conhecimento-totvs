---
article_id: 360021047172
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: fb444058e8ce3d99d3fbc94b1e014f3e63783e0afb4c1cc1dcfc09cac020c0a3
fetched_at: '2026-06-28T22:37:19.946048+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como é tratada a Norma
  IFRS 15 (CPC47) no módulo de Gestão de Contratos ?
type: support-article
updated_at: '2022-10-10T18:32:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021047172-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-%C3%A9-tratada-a-Norma-IFRS-15-CPC47-no-m%C3%B3dulo-de-Gest%C3%A3o-de-Contratos
---

**Dúvida**Como é tratada a Norma IFRS 15 (CPC47) no módulo de Gestão de Contratos ?  
  
**Ambiente**Microsiga Protheus - a partir da versão 12.1.17  
  
  
**Solução**

A **IFRS 15** - Receitas de Contratos com Clientes substituirá praticamente todas as regras para reconhecimento de receitas. Esse modelo único busca trazer maior consistência e comparabilidade das práticas para reconhecimento de receitas entre setores, jurisdições e mercados de capitais.

Todos os contratos de vendas precisarão ser atendidos para a nova norma contábil **IFRS 15**, exceto para os contratos de:

* Arrendamento mercantil;
* Seguros
* Instrumentos financeiros
* Trocas de ativos monetários entre linhas de negócios

A identificação do contrato no Gestão de Contrato ocorrerá na relação de **Planilhas** x **Clientes** após assinatura do contrato, ou seja, ao mudar a situação do contrato para vigente.

As obrigações de desempenho são promessas em um contrato para transferir para um cliente bens ou serviços que são distintos:

* Bens
* Serviços

A identificação das obrigações de desempenho do contrato, ocorrerão ao longo de um período através das rotinas de medição (CNTA121), além disso, as obrigações de desempenho serão identificados através do campo tipo de produto (**B1\_TIPO**).

O preço de transação será alocado para cada **obrigação de desempenho** com base nos preços de venda relativos a cada bem ou serviço distinto prometido no contrato.

Subtende-se que o preço alocado será realizado para cada medição, pois a o cumprimento de uma obrigação de desempenho pode ocorrer em um determinado período ou ao longo de um período.

Quando uma obrigação de desempenho é satisfeita através da transferência de um bem ou serviço prometido para um cliente (quando o cliente obtém o controle desse bem ou serviço). Uma obrigação de desempenho pode ser reconhecida. Sendo assim, o reconhecimento da receita ocorrerá para cada encerramento da medição.

***Exemplo:***  
Será disponibilizado no módulo Contábil SIGACTB dois números de lançamento padrão (LP) para atender a norma IFRS 15 (bens e serviços).

* **LP 69H - Encerramento da Medição por Item - Norma IFRS 15**
* **LP 69I - Estorno da medição por Item - Norma IFRS 15**

**• Atualizações de RPO e Dicionários mais atuais disponíveis:**

[Pacotes de Atualização - Gestão de Contratos](https://tdn.totvs.com/pages/releaseview.action?pageId=679961416)

**• Documentações:**

[Documentação Técnica](http://tdn.totvs.com.br/pages/viewpage.action?pageId=315887811) 

**• Conceito da norma IFRS 15 (Norma Internacional de Relato Financeiro)**

[Parecer da Consultoria Tributária](http://tdn.totvs.com.br/pages/releaseview.action?pageId=286735028%20)

***Saiba Mais:***

[MP - SIGAGCT - Lançamentos Padronizados do módulo Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015864572-MP-SIGAGCT-Lan%C3%A7amentos-Padronizados-do-m%C3%B3dulo-Gest%C3%A3o-de-Contratos)

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
