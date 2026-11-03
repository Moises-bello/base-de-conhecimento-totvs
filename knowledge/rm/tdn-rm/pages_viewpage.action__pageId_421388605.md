---
content_hash: 01259a4300294484dfbe3ffc5920780c00f0586f1018086be4e5e2ab57fc8f6d
fetched_at: '2026-06-29T00:09:17.460799+00:00'
page_id: '421388605'
product: rm
source: tdn-rm
title: Histórico de Alteração do Boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388605
version: 4
---

O Histórico de alteração de Boleto tem por objetivo gravar registros no histórico e na tabela FBOLETOHISTORICO para cada processo executado e alterações realizadas em Boleto (s) e seu lançamento (s).

A tabela FBOLETOHISTORICO contém todos os campos existentes na tabela de boleto (FBOLETO) além do campo, de nome Origem da Gravação, que indica qual processo chamou a alteração, podendo ser:

* Efetivação Desconto Duplicata
* Alteração do boleto via interface
* Alteração Conta Caixa e Convênio do boleto
* Alteração Lançamento financeiro
* Alteração Vencimento do boleto
* Cancelamento Acordo de lançamentos do Educacional
* Baixa e cancelamento
* Baixa Cancelamento Remessa de boleto
* Cancelamento Boleto
* Impressão de boleto
* Exclusão Lançamento do Boleto
* Geração Código de Barras via fórmula (função de fórmula CODBARRABOLETO ou CODBARRABOLETODATA)
* Geração IPTE via fórmula (função de fórmula , IPTEBOLETO ou IPTEBOLETODATA)
* Inclusão Baixa
* Inclusão de lançamento em Boleto
* Parametrização Financeiro: ocorre ao alterar o parâmetro "Usar dados bancários global do Cli/For" no parametrizador do Financeiro.
* Processo Alteração Cli/For Lançamento (chamado pelo Totvs Processo Seletivo)
* Registro Online
* Remessa de boleto
* Retorno Bancário
* Portal TIN.

**Observação:**  
Essa funcionalidade precisa ser configurada nos  do sistema, o usuário irá definir através de parametrização se o recurso será ou não utilizado no sistema.
