---
content_hash: f44cf70a18291d85d82b781e79b122ff7287b82cca8db757017cd968cb5686fe
fetched_at: '2026-06-29T00:09:46.528292+00:00'
page_id: '435104825'
product: rm
source: tdn-rm
title: Conta Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Conta+Caixa
version: 1
---

**Conta Caixa**   
Esta funcionalidade foi criada para atender a necessidade de informar para qual conta bancária ou conta caixa irá o lançamento financeiro do contrato de locação, através de parâmetros na tela de "Parâmetros de Integração para Aluguel".  
As seguintes alterações foram realizadas para atender tal necessidade no módulo de Aluguel:

* Criação do campo "Código Conta Caixa".  
  Foi criado um campo denominado Código conta caixa na tela de Parâmetros de integração para Aluguel onde é possível informar a conta utilizada nos lançamentos financeiros referenciados por este grupo de parâmetros. O processo Gerar Lançamentos Financeiros envia a informação do código da conta caixa para o Módulo Financeiro. O campo de coligada da conta caixa não é apresentado em tela e o sistema atribuí ao campo o valor da coligada correspondente ao código da conta caixa selecionada.  
  O usuário acessa o sistema, seleciona o módulo de Incorporação, acessa a funcionalidade de Aluguel , aciona o botão Casdastro e seleciona o Parâmetros de Integração para Aluguel. No cadastro que se abre fornece as informações necessárias.   O campo "Id parâmetro" é de preenchimento obrigatório.
