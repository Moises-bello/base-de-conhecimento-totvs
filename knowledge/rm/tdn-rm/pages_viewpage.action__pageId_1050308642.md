---
content_hash: ae6ed191afb2d6a205d936b140c73e291bb751dde8d65dd37b9db24b1b6ef44d
fetched_at: '2026-06-29T00:05:51.485623+00:00'
page_id: '1050308642'
product: rm
source: tdn-rm
title: Reforma Tributária - Compras Governamentais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1050308642
version: 21
---

# Conteúdo

2Conteúdononenone

# 1. Sobre

A Reforma Tributária introduziu regras específicas para **operações envolvendo entes governamentais**, incluindo:

* identificação do **tipo de operação com entes governamentais**;
* aplicação de **percentual redutor de alíquota** em compras governamentais;
* geração de **informações específicas na NFS-e Modelo Nacional**.

Para atender a essas exigências, a **Linha RM** recebeu evoluções em:

* Cadastro de Clientes/Fornecedores
* Cadastro de Vigência de Alíquotas
* Movimentação Fiscal
* Tributação do Movimento/Item
* Emissão dos documentos fiscais eletrônicos

Este documento descreve **as entregas realizadas, em desenvolvimento e planejadas**, bem como as **ações necessárias por parte do cliente**.

# 2. Cadastro de Cliente/Fornecedor

Foi incluída a opção **“Distrito Federal”** no campo **Órgão Público**, disponível no cadastro de Cliente/Fornecedor.

**Status:** Liberado 

**Ação do cliente:**

Revisar os cadastros de clientes classificados como **Órgão Público** e garantir que o **ente governamental esteja corretamente informado**.

Essa informação é utilizada pelo sistema para a geração das informações fiscais exigidas nas operações com o setor público.

# 3. Cadastro de Vigência de Alíquotas

Foi criado o campo "**Percentual de Redução para Compras Governamentais**". Esse campo permite informar o **percentual redutor aplicado às alíquotas de IBS e CBS** nas operações com entes governamentais.

**Status:** Liberado

**Ação do cliente:**

Para **o ano de 2026**, o percentual redutor definido pela legislação é: **0% (zero)**

Portanto, **nenhuma parametrização é necessária neste ano**.

A partir de **2027**, o cliente deverá:

* informar no cadastro o **percentual redutor divulgado pelos órgãos competentes**.

Para mais detalhes acesse nossa documentação:

# 4. Movimentação (Faturamento)

## 4.1 Campo Tipo de Operação com Entes Governamentais

Foi criado no **Movimento**, aba (**Fical / Documentos Fiscais Eletrônicos)**, o campo "**Tipo de Operação com Entes Governamentais ou serviços sobre bens imóveis**" com as seguintes opções:

| Código | Descrição |
| --- | --- |
| 0 | Nenhum |
| 1 | Fornecimento com pagamento posterior |
| 2 | Recebimento do pagamento com fornecimento já realizado |
| 3 | Fornecimento com pagamento já realizado |
| 4 | Recebimento do pagamento com fornecimento posterior |
| 5 | Fornecimento e recebimento do pagamento concomitantes |

**Status:** Liberado

**Ação do cliente:**

Durante a **inclusão do Movimento**, o usuário deverá **informar manualmente** o tipo de operação aplicável.

Essa informação será utilizada para:

* geração das **tags fiscais da NFS-e Modelo Nacional**
* definição de **regras específicas da operação com ente governamental**.

Para mais detalhes acesse nossa documentação: 

## 4.2 Tributação do Movimento/Item

## 4.2.1 Percentual Redutor

Campo "**% Redutor".**

Comportamento:

* + preenchido **automaticamente pelo sistema**
  + utiliza o valor configurado no **Cadastro de Vigência de Alíquotas**

Ao buscar as **alíquotas de IBS e CBS aplicáveis à operação**, o serviço também retornará o **percentual redutor**.

## 4.2.2 Alíquota Efetiva Original

Campo **Alíquota Efetiva Original**

Comportamento:

* + calculado automaticamente pelo sistema
  + representa a **alíquota efetiva antes da redistribuição do IBS e CBS para o ente adquirente**

⚠ **Importante**

Esse comportamento **só se aplica a partir de 2027**.

**Status:** Em desenvolvimento

**Previsão:**

**Ação do cliente:** Nenhuma

# 5. Configuração Recomendada de Tipos de Movimento

Para facilitar a utilização das operações com entes governamentais, recomenda-se a criação de **Tipos de Movimento específicos para cada cenário**:

* Fornecimento com pagamento posterior
* Recebimento do pagamento com fornecimento já realizado
* Fornecimento com pagamento já realizado
* Recebimento do pagamento com fornecimento posterior
* Fornecimento e recebimento do pagamento concomitantes

## 5.1 Parametrização de Referência de Documento Fiscal

Nos **Tipos de Movimento utilizados para emitir notas fiscais** nas seguintes operações:

* **Recebimento do pagamento com fornecimento já realizado (tpOper = 2)**
* **Fornecimento com pagamento já realizado (tpOper = 3)**
* **Movimento de retorno da autorização da prefeitura**

deve ser habilitado o parâmetro "**Referência Documento Fiscal"**

Caminho:

Parâmetros  
→ Tipo de Movimento  
→ Fis  
→ NF-e

## 5.2 Associação de Documentos Referenciados

Durante a inclusão das movimentações referentes a:

* **Recebimento do pagamento com fornecimento já realizado (tpOper = 2)**
* **Fornecimento com pagamento já realizado (tpOper = 3)**

o usuário deverá:

1. acessar a aba **Referência DOC**
2. associar os **documentos fiscais correspondentes**

Essa associação permitirá que o sistema **gere corretamente o grupo gRefNFSe na NFS-e**.

Atenções Importantes de Parametrização

Ao criar novos **Tipos de Movimento**, recomenda-se avaliar as seguintes configurações conforme a necessidade do processo do cliente:

* Se o movimento **vai contabilizar**
* Se **vai gerar financeiro**
* Se **vai afetar estoque**

Também é necessário revisar a **parametrização dos tributos atuais**, quando aplicável:

* ICMS
* IPI
* ISS
* PIS
* COFINS

# 6. NFS-e Modelo Nacional

A emissão da **NFS-e Modelo Nacional** passa a considerar as informações configuradas para operações com entes governamentais.

## 6.1 Geração da Tag tpOper (Tipo de Operação)

Durante a emissão da NFS-e, a tag **tpOper** será gerada quando:

* o campo **Tipo de Operação com Entes Governamentais** do movimento estiver **diferente de "0 - Nenhum"**.

**Status:** (informar)  
**Ação do cliente:** Nenhuma

## 6.2 Geração da tag tpEnteGov (Tipo de Ente Governamental)

A tag será gerada quando:

* o **Cliente/Fornecedor estiver classificado como Órgão Público**, e
* o campo **Tipo de Operação com Entes Governamentais** estiver **diferente de "0 - Nenhum"**.

**Status:** (informar)  
**Ação do cliente:** Nenhuma

## 6.3 Geração da tag pRedutor (Percentual de redução de alíquota em compra governamental)

A tag será gerada quando o campo **% Redutor** estiver informado na **Tributação do Movimento/Item**.

**Status:** Em desenvolvimento  
**Ação do cliente:** Nenhuma

## 6.4 Geração do grupo gRefNFSe – NFS-e Referenciadas

O grupo **gRefNFSe** será gerado quando:

* o campo **Tipo de Operação com Entes Governamentais** estiver configurado como:

  + **2 – Recebimento do pagamento com fornecimento já realizado**, ou
  + **3 – Fornecimento com pagamento já realizado**

**E**

* existir **NFS-e associada ao movimento**.

**Status:** Em backlog  
**Previsão:** (informar)

# 7. NF-e / NFC-e

A emissão da **NF-e** passa a considerar novas informações em operações com entes governamentais para os Impostos IBS e CBS.

Os novos grupos gTribCompraGov e gCompraGov serão gerados automaticamente sempre que:

* Cliente/Fornecedor estiver classificado como **Órgão Público**,
* Para evitar rejeições, é necessário que o campo **Tipo de Operação com Entes Governamentais** seja preenchido com valor **diferente** de **"0 - Nenhum"**.

Além disso, o grupo gREd passará a ser gerado mesmo para CSTs que normalmente não permitem seu preenchimento (como, por exemplo, o CST 000), porém apenas nos casos em que a venda for realizada para um Cliente/Fornecedor classificado como Órgão Público.

Importante destacar que esses grupos não serão gerados para notas fiscais do tipo **NFC-e**.

Para mais detalhes acesse nossa documentação:

* gCompraGov

* gTribCompraGov

**Status:** Liberado

# 8. CT-e / CT-e OS

A emissão da  **(CT-e / CT-e OS) Modelo Nacional** passa a considerar as informações configuradas para operações com entes governamentais.

## 8.1 Geração da tag tpEnteGov (Tipo de Ente Governamental)

A tag será gerada quando:

* **Cliente/Fornecedor estiver classificado como Órgão Público**, e o campo **Tipo de Operação com Entes Governamentais** estiver **diferente de "0 - Nenhum"**.
* Ao habilitar o **Tipo de Operação com Entes Governamentais** é gerado os grupos **gCompraGov e** **gTribCompraGov** sendo respectivamente dependentes. Estes grupos deverão ser gerados sempre que o cliente/fornecedor for um Órgão Público e  a tag **tpEnteGov** estiver em preenchida.

Para mais detalhes acesse nossa documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=982929067>

**Status:** Liberado

# 9. NFCom

A emissão da **NFCom** passa a considerar as informações configuradas para operações com entes governamentais.

Os novos grupos **gTribCompraGov** e **gCompraGov** serão gerados automaticamente sempre que:

* Cliente/Fornecedor estiver classificado como **Órgão Público.**
* Para evitar rejeições, é necessário que o campo **Tipo de Operação com Entes Governamentais** seja preenchido com valor **diferente** de **"0 - Nenhum"**.

Para mais detalhes acesse nossa documentação:

* gCompraGov**:**
* gTribCompraGov:

**Status:** Em desenvolvimento (Aguardando TSS)
