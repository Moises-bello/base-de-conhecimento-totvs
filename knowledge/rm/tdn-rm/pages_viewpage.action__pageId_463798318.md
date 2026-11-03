---
content_hash: f6bcf647b0fa20f5c59341359022672775a4e49de03600de762ff460773e89b6
fetched_at: '2026-06-29T00:10:15.010996+00:00'
page_id: '463798318'
product: rm
source: tdn-rm
title: Formula de Envia E-mail Automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463798318
version: 5
---

Formula de Envia E-mail Automático

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Gestão de Relacionamento com Cliente |
| **Módulo:** | Totvs Gestão de Relacionamento com Cliente |
| **Rotina:** | Tipo de Atendimento |
| **Parâmetro(s):** | Não se Aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | TOPEXECONTROL01-2371 |
| **Tabelas Utilizadas:** | HTIPOATENDIMENTO |

## Objetivo

Permitir que seja possível realizar o envio de e-mail de forma imediata após a execução da formula em determinada ação.

### Procedimentos

10Cadastro

Para realizar o cadastro da formula é necessário acessar o modulo de Serviços Globais | Administração | Cadastros | Fórmulas.

* Selecione o sistema: Gestão do Relacionamento com cliente;
* Incluir | Editor de fórmulas | Selecione a formula "ENVIAEMAILIMEDIATAMENTE".

A formula envia um e-mail imediatamente, caso o e-mail for do tipo HTML e tiver a palavra chave [ACOESDOATENDIMENTO] em seu corpo, serão incluídos links ao corpo do e-mail para cada uma das possíveis ações do atendimento do contexto para sua tarefa atual.

* Endereço de e-mail do remetente [string]
* Endereço de e-mail do destinatário [string]
* Endereço de e-mail ao qual será enviada uma cópia do e-mail [string]
* Assunto do e-mail [string]
* Corpo do e-mail [string]
* Formato do e-mail (true caso for HTML e false caso for texto) [bool]

Exemplo:

ENVIAEMAILIMEDIATAMENTE('totvs@[totvs.com.br](http://totvs.com.br)', 'corpore@[totvs.com.br](http://totvs.com.br)', 'agilis@[totvs.com.br](http://totvs.com.br)', 'Assunto', 'Mensagem', true);

1Parâmetros Gerais

Para que o envio de e-mail funcione corretamente é necessário que nos Parâmetros Gerias de envio de e-mail estejam parametrizados corretamente.

Para isso, acesse de qualquer modulo o menu Ambiente | Configuração | Parâmetros | Parâmetros Globais | aba Envio de E-mails, deve ser preenchidos os campos de Servidor SMTP, Usuário, Senha, domínio e porta.

Exemplo:
