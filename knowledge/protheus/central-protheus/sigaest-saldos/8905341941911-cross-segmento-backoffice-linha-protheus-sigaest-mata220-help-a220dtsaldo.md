---
article_id: 8905341941911
category: SIGAEST - SALDOS
content_hash: b2625380d80f6b7a866a41c5edd8469bce6757d290907421a8411734899b2e86
fetched_at: '2026-06-28T22:39:14.886206+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA220 HELP A220DTSALDO
type: support-article
updated_at: '2024-03-07T11:21:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8905341941911-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA220-HELP-A220DTSALDO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21869935267223) Tempo aproximado para leitura: **00:04:15 min****Dúvida**

Ao incluir Saldo Inicial (MATA220) esta exibindo o **HELP A220DTSALDO**. Como devo proceder?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21870165585943)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Para inclusão de Saldos Iniciais pela rotina MATA220 ***não é permitido** **digitar*** a data de inclusão (B9\_DATA), caso tenha habilitado o campo ou por execauto o help A22ODTSALDO é apresentado.

O **HELP A220DTSALDO** passou a ser apresentado na ISSUE [DMANMAT01-36374](https://tdn.totvs.com/pages/releaseview.action?pageId=704083860) é necessário efetuar os passos abaixo para atualizar o arquivos de helps:

*"Criado a validação para não ser informada a data do saldo seja via execauto seja via habilitação do campo.*

*Atenção : A Validação se dará através de um help e ate que seja atualizado os helps padrões com este novo help, poderá ser criado provisoriamente um help no dicionário :*

*Com um Administrador entrar no SIGACFG em Dicionário → Manutenção e help, Digitar A220DTSALDO no código do help e clicar em avançar*

*Uma tela irá perguntar se é um help novo , responda SIM e no Box Help de variável digite o texto "O saldo inicial não deve ser informado a data do saldo." e no box help da solução digite o texto "Não informe a data do saldo." , clique em confirmar e salvar."*

![](https://tdn.totvs.com/download/attachments/704083860/image2022-8-15_15-44-4.png?version=1&modificationDate=1660589045193&api=v2)

|  |
| --- |
| ***Importante*:** Caso, mesmo assim persistir a apresentação do HELP A220DTSALDO, revise nas Configurações do Campo B9\_DATA se utiliza algum **Inicializador Padrão (X3\_RELACAO)** ou **Validação de Usuário (X3\_VLDUSER)** que estejam inputando dados no campo na Inclusão manual. |

**Saiba Mais:**  
[*Clique aqui e veja mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)
