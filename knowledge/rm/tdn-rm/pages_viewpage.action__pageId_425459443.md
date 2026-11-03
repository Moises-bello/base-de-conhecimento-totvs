---
content_hash: e7fb4924e3cd3ceb4183abd91e264aeb8d0010171e0fc1b01c4e5d6f05f11157
fetched_at: '2026-06-29T00:09:35.941391+00:00'
page_id: '425459443'
product: rm
source: tdn-rm
title: TOTVS Incorporação x BackOffice Protheus - Cadastro Centro de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459443
version: 2
---

**TOTVS Incorporação x BackOffice Protheus - Cadastro Centro de Custo**

---

A inclusão, alteração e exclusão do cadastro de Centro de Custo são realizadas no Protheus, e sincronizadas para o RM.

Para realizar o cadastro no Protheus acesse: módulo SIGACTB | Atualizações | Entidades | Custos

Para visualizar o cadastro sincronizado no RM acesse: BackOffice | Gestão Contábil | Cadastro | Centros de Custos

**Dados sincronizados**

* Código da coligada
* Código do centro de custo
* Situação do registro (ativo ou inativo)
* Nome
* Código reduzido
* SPED Contábil (não ultilizado pelo Protheus)

Obs: O BackOffice envia para o TIN, quem pode alterar ou excluir o Centro de Custo será somente o Protheus, o TIN só pode receber o cadastro do Protheus. É possível ver as informações do cadastro de Centro de Custo realizado, através da Mensagem Única **CostCenter**.  
    
 É possível ver os detalhes da mensagem enviada em Integração / Integração / Mensagem Única / Fila de Mensagens Únicas. Esta tela mostra os campos: Identificador da transação, Uuid mensagem, Versão de Mensagem, Criação da mensagem e Identificador da Integração. Esta tela ainda possui um anexo que mostra as Informações de execução da mensagem.
