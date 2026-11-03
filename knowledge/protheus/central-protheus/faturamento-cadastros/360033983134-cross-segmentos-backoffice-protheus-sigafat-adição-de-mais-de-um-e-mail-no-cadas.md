---
article_id: 360033983134
category: Faturamento - Cadastros
content_hash: 2bbb297c6c395a9009a11c8c2c6db28f2a8ece76cf617d862d70026839a7366c
fetched_at: '2026-06-28T22:38:35.407901+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Adição de mais de um e-mail
  no Cadastro de Cliente
type: support-article
updated_at: '2026-04-13T17:25:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033983134-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Adi%C3%A7%C3%A3o-de-mais-de-um-e-mail-no-Cadastro-de-Cliente
---

**Dúvida**  
É possível cadastrar mais de um e-mail no **"Cadastro de Clientes (CRMA980)"**?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12

**Solução**

É possível informar vários e-mails no campo **A1\_EMAIL** separados por ponto e virgula (;), conforme exemplo:  
  
**Exemplo:** [cliente1@teste.com](mailto:cliente1@teste.com)**;**[cliente2@teste.com.br](mailto:cliente2@teste.com.br)  
  
**OBSERVAÇÃO:** Pode ser necessário aumentar o tamanho do campo para conter os e-mails, pois no padrão do sistema, o campo **A1\_EMAIL** vem configurado com tamanho "**30**".

Caso seja necessário alterar o tamanho do campo, siga as instruções da documentação da Equipe Protheus Framework para aumentar o tamanho do campo **A1\_EMAIL** para um tamanho adequado que comporte os e-mails, sendo o limite do campo **254 caracteres**:

[**Campos - Como alterar o tamanho**](https://tdn.totvs.com/x/JD0tE)
