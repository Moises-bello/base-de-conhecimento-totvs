---
content_hash: 866ab84e66dd0f0db0e875b2be342b6213e44beab818c07f7263177631fe8b88
fetched_at: '2026-06-29T00:09:46.547309+00:00'
page_id: '435104830'
product: rm
source: tdn-rm
title: Evento Financeiro - Processo - Excluir lançamento financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104830
version: 2
---

**Excluir lançamento financeiro**    
 O processo de Excluir lançamentos financeiros permite a exclusão de lançamentos associados ao parcelamento do evento financeiro e que estejam integrados ao módulo de gestão financeira da RM ou Protheus.   
 Assim é possível remover todos os lançamentos financeiros relacionados a distribuição do parcelamento do evento financeiro desejado.  
 O processo de exclusão de lançamentos financeiros faz a leitura da distribuição do parcelamento do evento financeiro localizando os respectivos lançamentos financeiros associados e remove todos os lançamentos financeiros relacionados a distribuição do parcelamento do evento financeiro.  
 No processo usuário seleciona as parcelas que terão os lançamentos excluídos.  
 Só serão excluídos lançamentos financeiros para parcelas do evento financeiro que possuam a situação igual a "Integrada" ou "Cancelada". Só serão excluídos lançamentos financeiros que não estejam baixados, parcialmente baixados ou em cobrança (remitidos a banco ou com boleto gerado), podem ser cancelados.  
 Após a realização deste processo a parcela estará da seguinte forma:

* Os lançamentos financeiros associados a distribuição do parcelamento do evento financeiro serão excluídos. - A distribuição das respectivas parcelas do evento financeiro selecionadas será excluída. - A situação da parcela passará de "Cancelada" ou "Integrada" para "Não integrada". - A situação de um evento financeiro passará de "Integrado" ou "Parcialmente integrado" para "Não integrado" ou continuará como "Parcialmente integrado". - O evento financeiro fica disponível novamente para alteração, caso não existam parcelas em Situação "Integrada" ou "Cancelada".
