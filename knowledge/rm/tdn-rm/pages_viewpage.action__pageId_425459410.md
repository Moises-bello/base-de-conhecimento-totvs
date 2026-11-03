---
content_hash: b12cf976ad64b6a97bbf1ca95fdfaf4d5af71587da04acf6b16f5641d4734dcb
fetched_at: '2026-06-29T00:09:35.881458+00:00'
page_id: '425459410'
product: rm
source: tdn-rm
title: TOTVS Incorporação x BackOffice Protheus - Cadastro Item Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459410
version: 2
---

**TOTVS Incorporação x BackOffice Protheus - Cadastro Item Contábil**

---

A inclusão, alteração e exclusão do cadastro de Item Contábil são realizadas no Protheus, e sincronizadas para o RM. Para realizar o cadastro no Protheus acesse: módulo SIGACTB | Atualizações | Entidades | Custos | Item Contábil Para visualizar o cadastro sincronizado no RM acesse: TOTVS Educacional  
 Foi criado a entidade de Item Contábil, sendo que o cadastro será feito pelo Protheus para o TOTVS Educacional. O mesmo cadastro também poderá ser associado a um empreendimento no TOTVS Incorporação através de Cadastros | Empreendimentos | aba Integração. A inclusão, alteração e exclusão do cadastro de Item Contábil são realizadas no Protheus, e sincronizadas para o RM.  
 O conceito desta entidade contábil não pertence ao BackOffice RM, assim sendo criada uma nova entidade no TOTVS Educacional para armazenar a informação e o relacionamento desta com os eventos contábeis. Para a integração do TOTVS Incorporação será utilizado o mesmo cadastro, efetuando o relacionamento desta entidade ao cadastro do Empreendimento (TIN > Cadastro> Empreendimento-> Aba Integração).

**Dados sincronizados**

* Código da coligada
* Código do item contábil
* Descrição

**Observação:**

O BackOffice envia para o TIN, quem pode alterar ou excluir o Item Contábil será somente o Protheus, o TIN só pode receber o cadastro do Protheus. É possível ver as informações do cadastro de Item Contábil realizado, através da Mensagem Única **AccountingItem**.  
 É possível ver os detalhes da mensagem enviada em Integração / Integração / Mensagem Única / Fila de Mensagens Únicas. Esta tela mostra os campos: Identificador da transação, Uuid mensagem, Versão de Mensagem, Criação da mensagem e Identificador da Integração. Esta tela ainda possui um anexo que mostra as Informações de execução da mensagem.
