---
content_hash: 9f972d165c16e51a2d031f812e979ac3a8eed7e3b0e3661a0a672f831707a951
fetched_at: '2026-06-29T00:05:53.069626+00:00'
page_id: '1065224596'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Utilitários - RD Station - Configuração
  Integração RD Station Marketing
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1065224596
version: 3
---

A integração entre o módulo **RM TCGI Venda** e o **RD Station Marketing** tem como objetivo automatizar o envio de dados de clientes e contratos para a plataforma de marketing, permitindo ações como automação de campanhas, nutrição de leads e acompanhamento do funil de vendas. Essa integração é realizada por meio de um assistente de configuração dentro do RM, garantindo facilidade na configuração e padronização da comunicação entre os sistemas. A integração é **orientada a eventos**, ou seja, os dados são enviados sempre que ocorre uma ação relevante no sistema e os envios garantem que o RD Station esteja sempre atualizado com o status mais recente do cliente e do contrato.  
  
**Benefícios da Integração:**

* Automação de processos de marketing
* Redução de trabalho manual
* Atualização em tempo real dos dados no RD Station
* Melhor acompanhamento do funil de vendas
* Possibilidade de campanhas mais segmentadas

---

# **Configuração**

A integração é configurada através do processo Assistente de Configuração RD Station Marketing. Esse assistente é responsável por ativar e parametrizar a integração.

Pré-requisito

* Antes de executar o assistente, é necessário que o **SmartLink** esteja devidamente configurado (etapa fora do escopo desta documentação).

### Passo a passo da configuração

1. Acessar o processo **Assistente de Configuração RD Station Marketing**
2. Avançar nas etapas iniciais
3. Selecionar as **coligadas** que participarão da integração
4. Confirmar e executar o processo

Ao final do processo, o sistema exibe uma **mensagem de sucesso ou erro**, indicando o resultado da configuração e são apresentadas **informações adicionais para direcionamento.**

---

# **Funcionamento**

Após a configuração, o RM passa a enviar automaticamente informações para o RD Station conforme eventos específicos do processo de vendas.

**Dados Enviado ao RD Station:**

A integração contempla o envio de dois grupos principais de informações:

Dados de Contato

* Nome
* E-mail
* Telefone
* Data de nascimento
* Profissão
* Estado
* Cidade
* Bairro
* Renda

### Dados de Contrato

* Nome do empreendimento
* ID do contrato de venda
* Situação do contrato
* Data de entrega das chaves
* Motivo do distrato
* Motivo da compra
* Unidade
* Subunidade
* Data de quitação

**Momentos de Envio das Informações:**

O envio dos dados para o RD Station ocorre automaticamente nos seguintes eventos:

* Alteração da **data de entrega das chaves**
* Execução do processo **Efetivar Contrato**
* Execução do processo **Quitar Venda**
* Execução do processo **Efetivar Distrato**
* Execução do processo **Cancelar Contrato**
* Inclusão ou alteração de **comprador** na venda em preparação
