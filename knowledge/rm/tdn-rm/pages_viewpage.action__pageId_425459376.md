---
content_hash: 93715b30186deb0046d48ccb7dc4a4482c205e7ed16a372a03e720e921b24917
fetched_at: '2026-06-29T00:09:35.512348+00:00'
page_id: '425459376'
product: rm
source: tdn-rm
title: TOTVS Incorporação x BackOffice Protheus - Cadastro Plano de Contas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459376
version: 4
---

**TOTVS Incorporação x BackOffice Protheus - Cadastro Plano de Contas**

---

A inclusão, alteração e exclusão do cadastro de Plano de Contas são realizadas no Protheus, e sincronizadas para o RM. Para realizar o cadastro no Protheus acesse: módulo SIGACTB | Atualizações | Entidades | Plano de Contas Para visualizar o cadastro sincronizado no RM acesse: BackOffice | Gestão Contábil | Cadastros | Plano de Contas Contábil

**Máscara do código do Plano de Contas**

A máscara parametrizada da conta contábil no RM é validada no processo de inclusão. Visto que o Protheus não permite inserção de caracteres de ponto ( "." ) no código, o parametrizador da integração "TOTVS Incorporação x BackOffice Protheus" alterará automaticamente o parâmetro "Não usa Máscaras" para valor verdadeiro. Caso sistema de origem faça tratamento de máscara no seu código (Ex.: 1.011.001) o parâmetro "Não utiliza máscara nas contas" deverá ser alterado e a máscara corretamente configurada.

**Caminho da parametrização**:

Menu BackOffice >> Gestão Contábil >> Ambiente >> Parâmetros >> TOTVS Gestão Contábil >> Plano de Contas >> Plano de Contas Contábil

**Parâmetros default**

Visto que o cadastro do Plano de Contas Contábil será feito no Protheus, ao ativar a integração (execução do configurador) do TOTVS Incorporação com BackOffice Protheus os parâmetros abaixo serão automaticamente alterados para os respectivos valores . Usa Código Reduzido: Desmarcado Edita Código Reduzido: Marcado Não utiliza máscara nas contas: Marcado  
 Foi criado a entidade de Plano de Contas, sendo que o cadastro será feito pelo Protheus para o TOTVS Gestão Contábil. No Gestão Contábil estes cadastros são visualizados em Menu BackOffice | Gestão Contábil | Plano de Contas Contábil. A inclusão, alteração e exclusão do cadastro de Plano de Contas são realizadas no Protheus, e sincronizadas para o RM.

**Dados sincronizados**

* Código da coligada
* Código da conta
* Código reduzido da conta
* Descrição da conta
* Natureza da conta
* Se é Analítica ou Sintética
* Ativa ou inativa
* Permissão de informação Gerencial

**Observação:**

O BackOffice envia para o Gestão Contábil, quem pode alterar ou excluir o Plano de Contas será somente o Protheus, o Gestão Contábil só pode receber o cadastro do Protheus. É possível ver as informações do cadastro de Plano de Contas realizado, através da Mensagem Única **AccountantAccount**.  
 É possível ver os detalhes da mensagem enviada em Integração / Integração / Mensagem Única / Fila de Mensagens Únicas. Esta tela mostra os campos: Identificador da transação, Uuid mensagem, Versão de Mensagem, Criação da mensagem e Identificador da Integração. Esta tela ainda possui um anexo que mostra as Informações de execução da mensagem.
