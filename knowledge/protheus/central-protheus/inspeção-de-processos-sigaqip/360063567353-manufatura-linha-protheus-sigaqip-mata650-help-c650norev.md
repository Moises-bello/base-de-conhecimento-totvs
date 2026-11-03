---
article_id: 360063567353
category: Inspeção de Processos (SIGAQIP)
content_hash: 4a0fff61aecc492b693363e779e940d5aad898ee969768700127cc1231b48d22
fetched_at: '2026-06-28T22:42:25.834409+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - MATA650 - Help C650NOREV
type: support-article
updated_at: '2023-09-08T18:17:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063567353-Manufatura-Linha-Protheus-SIGAQIP-MATA650-Help-C650NOREV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17381447592599)**Tempo aproximado para leitura: **00:02:15 min**  
**Ocorrência**Ao incluir uma ordem de produção na rotina **MATA650 - Ordens de Produção** é apresentado *help* **C650NOREV - Não existe especificação para este Produto/Roteiro**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**O *help* **C650NOREV** ocorre quando o parâmetro **MV\_QIPMAT - Indica se o módulo de Insp.de Processos está integrado com materiais** está como **S - Sim**. Este *help* alerta que quando há integração entre **PCP - Planejamento e Controle da Produção** com o **QIP - Inspeção de Processos**, é necessário que exista uma especificação cadastrada para o produto da ordem. E quando não há especificação cadastrada para o referido produto na rotina **QIPA010 - Especificação de Produtos**, este *help* é exibido.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Se o produto for inspecionado no **SIGAQIP - Inspeção de Processos**, deve cadastrar uma especificação para o mesmo na rotina **QIPA010**;
2. Se o produto não for inspecionado no **SIGAQIP**, o *help* **C650NOREV** deverá ser ignorado, pois este alerta não é um impeditivo para a conclusão da **OP - Ordem de Produção**.

**Importante**

1. Quando o parâmetro **MV\_QBLOESP - Define se será permitida a inclusão de OP's no SIGAQIP, para produtos criado pelo SIGAPCP, e que não tenha especificação cadastrado** estiver como **2**, a mensagem será apenas um alerta permitindo a inclusão da **OP** sem que o produto tenha uma especificação cadastrada. Porém, caso o parâmetro esteja como **1**, será exibida a mesma mensagem mas, não será permitida a inclusão da **OP** caso o produto não possua especificação cadastrada, ou seja, o parâmetro como **1** irá bloquear a inclusão da **OP** para produto sem especificação cadastrada.
2. Para utilizar um roteiro secundário na abertura da **OP**, o parâmetro **MV\_QIPFROT - Indica se deve utilizar o roteiro de operações primário, da especificação do produto, na abertura de Ordens de Produção** deve ter conteúdo igual a **F - False**, mas também será consistido se o roteiro informado na **OP**, tem a especificação cadastrada no **QIPA010**. Se não possuir este cadastro, será apresentado o *help* **C650NOREV**, mas não irá impedir a abertura da **OP** e a integração com o **SIGAQIP - Inspeção de Processos** não será realizada.

**Saiba Mais**  
Existe a possibilidade de não exibir do *help* **C650NOREV** utilizando o ponto de entrada [MT650QIP - Valida integração com o módulo SIGAQIP em Ordens de Produção](https://tdn.totvs.com/pages/releaseview.action?pageId=325848051).
