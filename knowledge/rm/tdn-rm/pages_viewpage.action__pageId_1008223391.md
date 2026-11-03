---
content_hash: aa90cf79217f913588a6b97c5992d44ab0e77d7227a5fede98cc6bc1741a0d55
fetched_at: '2026-06-29T00:05:47.158835+00:00'
page_id: '1008223391'
product: rm
source: tdn-rm
title: Acelerador de Implantação PDC - Dados Bancários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1008223391
version: 2
---

# Dados Bancários do Empreendimento (Boleto com Registro Online)

Esta etapa tem como objetivo **cadastrar as informações bancárias do empreendimento**, utilizadas para a emissão de boletos com registro online.

## Exibição da Etapa

A tela **Dados Bancários do Empreendimento** será exibida somente quando, na etapa **Situação Financeira**, estiver configurado o parâmetro:

* **Permite gerar novo boleto para parcela vencida e do mês**
* E a opção selecionada no campo **Opções de pagamento das parcelas** for:
  + **"Registro online"** ou **"Registro online/Pix TPD"**.

Caso essas condições não sejam atendidas, a tela não será exibida durante o fluxo de parametrização do empreendimento.

## Campos de Preenchimento

* **Empreendimento**

**Descrição:** Identifica o empreendimento ao qual os dados bancários serão vinculados.  
**Como preencher:** Selecione o empreendimento desejado na lista apresentada pelo sistema.  
**Exemplo:** 2008 - EMPREENDIMENTO AUTOMAÇÃO  
**Obrigatoriedade:** Sim.

* **Convênio**

**Descrição:** Indica o tipo de convênio bancário utilizado para emissão dos boletos.  
**Comportamento:**

* + Nesta etapa, o tipo de convênio será sempre **Online**, pois a emissão é realizada via registro online.
  + O campo não requer seleção manual, sendo definido automaticamente pelo sistema.  
    **Obrigatoriedade:** Automático.

* **Filial (Dados Bancários)**

**Descrição:** Indica a filial responsável pelos dados bancários (agência, conta, carteira, entre outros) utilizados para emissão dos boletos.  
**Comportamento:**

* + O campo é preenchido automaticamente após a seleção do convênio.
  + O sistema utiliza os dados bancários da filial vinculada ao convênio online do empreendimento.  
    **Obrigatoriedade:** Automático.

## Regras e Comportamentos

* A tela é exibida apenas se a configuração financeira permitir emissão de boletos com registro online.
* O convênio é sempre definido como **Online**.
* O campo **Filial (dados bancários)** é preenchido automaticamente com base no convênio online.
* O campo **Empreendimento** deve ser informado manualmente.
* Caso o empreendimento não possua dados bancários cadastrados, o sistema exibirá mensagem de alerta solicitando o preenchimento.
