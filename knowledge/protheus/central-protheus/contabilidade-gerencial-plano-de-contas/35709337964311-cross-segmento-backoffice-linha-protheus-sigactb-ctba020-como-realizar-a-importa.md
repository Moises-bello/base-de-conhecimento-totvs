---
article_id: 35709337964311
category: Contabilidade Gerencial - Plano de Contas
content_hash: d00dbf3a8e0cdaec2d59be1741572fea68ced2537a91226c3def64276c4ec101
fetched_at: '2026-06-28T22:40:33.348441+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA020 - Como realizar
  a Importação/Exportação do Plano de contas.
type: support-article
updated_at: '2025-10-17T19:29:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35709337964311-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Como-realizar-a-Importa%C3%A7%C3%A3o-Exporta%C3%A7%C3%A3o-do-Plano-de-contas
---

#### 

#### Dúvida Como realizar a amarração das entidades contábeis, considerando uma entidade para diversas.

#### Ambiente Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - Todas Versões

#### 

#### Solução:

Para realizar a Importação/Exportação do plano de contas deve acessar a rotina CTBA020 ao acessar a rotina temos no Botão "Outras Ações", as opções de Importação e Exportação de Plano de contas:

![](https://tdn.totvs.com/download/thumbnails/306850505/image-2025-6-3_11-20-21.png?version=1&modificationDate=1748960421833&api=v2)

### 

### **Exportar:**

Para realizar a Exportação do Plano de Contas, utilize essa opção, escolhendo o caminho do servidor ou local em que o arquivo será gerado.

Para mais detalhes acesse a página: [Exportar](https://tdn.totvs.com/pages/viewpage.action?pageId=306850505#ContaCont%C3%A1bil(CTBA020SIGACTB)-03.1Exportar:)

### 

### **Importar:**

Para realizar a importação do Plano de Contas, utilize esta opção, selecionando o arquivo que será lido para a importação.

Para mais detalhes e layout de importação acesse a página: [Exportar](https://tdn.totvs.com/pages/viewpage.action?pageId=306850505#ContaCont%C3%A1bil(CTBA020SIGACTB)-03.1Exportar:)

### **Importação via MILE:**

Essa opção é disponibilizada pelo Framework do Protheus e que serve para a maioria das rotinas em MVC, salvo algumas exceções. Quando a rotina está configurada para utilizar o **Acelerador MILE**, é possível importar de um arquivo **TXT**o cadastro de contas contábeis, sendo através do Configurador (CFGA600) ou rotina CTBA020, na opção Outras Ações > Outros > Importar:

![](https://tdn.totvs.com/download/thumbnails/306850505/image-2025-7-4_9-47-19.png?version=1&modificationDate=1751633240227&api=v2)

As principais vantagens de utilizar o **MILE**para importação de contas são:

* Não é necessário estar com o Plano de Contas vazio para realizar a importação de uma Conta Contábil.
* A importação é realizada de forma mais flexível, permitindo que o arquivo TXT siga um layout específico para cada cliente. Isso ocorre porque a configuração do MILE é uma customização, adaptada individualmente da forma como cada cliente estrutura seu processo.

Para mais detalhes e layout de importação acesse a página: [Exportar](https://tdn.totvs.com/pages/viewpage.action?pageId=306850505#ContaCont%C3%A1bil(CTBA020SIGACTB)-03.1Exportar:)

## **Saiba mais:**

[Conceito - Plano de Contas](https://tdn.totvs.com/display/PROT/Conceito+-+Plano+de+Contas)

[MILE - Model Integrator Layout Engine](https://tdn.totvs.com/display/public/framework/MILE+-+Model+Integrator+Layout+Engine)
