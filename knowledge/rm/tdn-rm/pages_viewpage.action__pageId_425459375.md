---
content_hash: d64a6e6a6592886090f48b9ff384e2786f18767a6885b1193555e6dace7c2ea4
fetched_at: '2026-06-29T00:09:35.509940+00:00'
page_id: '425459375'
product: rm
source: tdn-rm
title: TOTVS Incorporação x BackOffice Protheus - Cadastro Plano de Contas Gerencial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459375
version: 2
---

**TOTVS Incorporação x BackOffice Protheus - Cadastro Plano de Contas****Gerencial**

---

A inclusão, alteração e exclusão do cadastro de Plano de Contas Gerencial são realizadas no RM TOTVS Gestão Contábil, e sincronizadas para o Protheus. Para realizar o cadastro sincronizado no RM acesse: BackOffice | Gestão Contábil | Cadastros | Plano de Contas Gerencial Para visualizar o cadastro no Protheus acesse: Contabilidade Gerencial | Configurações | Entidades Contábeis.

Esta entidade é utilizada na Integração TIN POC X Protheus.

**Máscara da Conta Gerencial para execução do Processo**

Conforme documentado no requisito de desenvolvimento do processo "Gerar e Associar Contas Gerenciais", para que o mesmo seja executado corretamente é necessário que a máscara "9" do Plano de Contas Gerencial  seja "#.###.###.####", mas devido a restrições do Protheus o parâmetro "Não Utiliza Mascara" será automaticamente marcado como verdadeiro no RM ao executar o configurador, assim sendo cadastradas as Contas Gerenciais seguindo a mesma máscara somente removendo os caracteres de ponto. Em resumo, ao ativar a integração (execução do configurador) do TOTVS Incorporação com BackOffice Protheus a mascara será alterada para o valor citado acima, o parâmetro "Não utiliza máscara nas contas" marcado como verdadeiro e os códigos gerados sem o caractere de ponto.

**Dados sincronizados**

* Código da coligada
* Código da conta gerencial
* Código reduzido da conta
* Descrição da conta
* Natureza da conta
* Se é Analítica ou Sintética
* Ativa ou inativa

Obs:

O TOTVS Gestão Contábil envia para o BackOffice Protheus, quem pode alterar ou excluir o Plano de Contas Gerencial será somente o TOTVS Gestão Contábil, o Protheus só pode receber o cadastro do Protheus. É possível também ver as informações do cadastro de Plano de Contas Gerencial realizado, através da Mensagem Única **ListOfManagerialAccountingEntity**. A seguir apresentamos outra forma de gerar as Contas Gerenciais.

**Processo de geração de Contas Gerenciais por Sub-Unidade**

O processo "Gerar e Associar Contas Gerenciais", responsável por gerar Contas Gerenciais para Sub-Unidades, também disparará mensagem de integração com a lista de registros inseridos. Este processo está localizado em: TOTVS Incorporação | Apuração de Resultado Contábil pelo POC | Regras de Apuração | Gerar e Associar Contas Gerenciais.  
 É possível ver os detalhes da mensagem enviada em Integração / Integração / Mensagem Única / Fila de Mensagens Únicas. Esta tela mostra os campos: Identificador da transação, Uuid mensagem, Versão de Mensagem, Criação da mensagem e Identificador da Integração. Esta tela ainda possui um anexo que mostra as Informações de execução da mensagem.
