---
content_hash: 3f7617729c04855b493b3849b7d14808c1cf61c1ae2b43300e338e7ff4512c94
fetched_at: '2026-06-29T00:09:35.883596+00:00'
page_id: '425459411'
product: rm
source: tdn-rm
title: TOTVS Incorporação x BackOffice Protheus - Cadastro Classe de Valor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459411
version: 2
---

**TOTVS Incorporação x BackOffice Protheus - Cadastro Classe de Valor**

---

A inclusão, alteração e exclusão do cadastro de Classe Valor são realizadas no Protheus, e sincronizadas para o RM. Para realizar o cadastro no Protheus acesse: módulo SIGACTB | Atualizações | Entidades | Custos | Classe de Valor Para visualizar o cadastro sincronizado no RM acesse: TOTVS Educacional  
 Foi criado a entidade de Classe de Valor, sendo que o cadastro será feito pelo Protheus para o TOTVS Educacional. O mesmo cadastro também poderá ser associado a um empreendimento no TOTVS Incorporação através de Cadastros | Empreendimentos | aba Integração. A inclusão, alteração e exclusão do cadastro de Classe de Valor são realizadas no Protheus, e sincronizadas para o RM.  
 O conceito desta entidade contábil não pertence ao BackOffice RM, assim sendo criada uma nova entidade no TOTVS Educacional para armazenar a informação e o relacionamento desta com os eventos contábeis. Para a integração do TOTVS Incorporação será utilizado o mesmo cadastro, efetuando o relacionamento desta entidade ao cadastro do Empreendimento (TIN > Cadastro> Empreendimento-> Aba Integração).

**Dados sincronizados**

* Código da coligada
* Código da filial
* Código da classe de valor
* Descrição
* Analítico/Sintético
* Status do registro

**Observação:**

O BackOffice envia para o TIN, quem pode alterar ou excluir o Classe de Valor será somente o Protheus, o TIN só pode receber o cadastro do Protheus. É possível ver as informações do cadastro de Classe de Valor realizado, através da Mensagem Única **ClassValue**.  
 É possível ver os detalhes da mensagem enviada em Integração / Integração / Mensagem Única / Fila de Mensagens Únicas. Esta tela mostra os campos: Identificador da transação, Uuid mensagem, Versão de Mensagem, Criação da mensagem e Identificador da Integração. Esta tela ainda possui um anexo que mostra as Informações de execução da mensagem.
