---
article_id: 360037548193
category: Inspeção de Entradas (SIGAQIE)
content_hash: b912daf93d12c817d96b050ec976bab706e660329fda044abfb8d022bababb45
fetched_at: '2026-06-28T22:42:26.962832+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Falta amarração do Produto x Fornecedor
  cadastrado pela rotina MATA060
type: support-article
updated_at: '2025-09-01T14:32:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037548193-Manufatura-Linha-Protheus-SIGAQIE-Falta-amarra%C3%A7%C3%A3o-do-Produto-x-Fornecedor-cadastrado-pela-rotina-MATA060
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34606885165079) Tempo aproximado para leitura: **00:01:30 min**  
**Ocorrência**No módulo **SIGAQIE - Inspeção de Entradas**, ao incluir um documento de entrada na rotina **MATA103 - Documento de Entrada** ou realizar a importação pelo **QIEA183 - Importação** é exibida a mensagem **Falta amarração do Produto X Fornecedor cadastrado pela rotina MATA060**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**Essa mensagem ocorre quando não existe o cadastro relacionando o produto com o fornecedor na rotina **MATA061 - Produto x Fornecedor**.  
  
**Solução**Para o módulo **SIGAQIE**, além de efetuar o cadastro na rotina **MATA061 - Produto x Fornecedor** é necessário preencher todos os campos obrigatórios e também os campos listados abaixo:

* **Situação - A5\_SITU**
* **Tempo Limite -****A5\_TEMPLIM**
* **Fab/Rev/Perm - A5\_FABREV**
* **Tipo de Atualização -****A5\_TIPATU**

Além disso, quando o campo **Fabricante -****A5\_FABR** estiver preenchido é necessário que o parâmetro **MV\_PRFOFAB - Seleciona índices de qualidade legado** esteja com conteúdo igual à **.T.**.  
Se o campo estiver em branco, o parâmetro **MV\_PRFOFAB** precisa estar desabilitado, ou seja, com conteúdo igual à **.F.**. Caso não exista o parâmetro **MV\_PRFOFAB** ou o seu conteúdo seja falso, é necessário existir relacionamento de produto x fornecedor sem fabricante.  
  
**Importante**  
Os campos citados acima somente estarão disponíveis na rotina **MATA061** quando acessado esta rotina pelo módulo **21 - Inspeção de Entradas**. Isto porque este campos são de uso exclusivo deste módulo.  
  
**Saiba mais**  
Para mais informações referentes ao parâmetro **MV\_PRFOFAB** consulte o [Boletim Técnico do parâmetro MV\_PRFOFAB](http://tdn.totvs.com/pages/viewpage.action?pageId=334336268)

**Observação**  
A partir da release **12.1.2410,** com a **alteração expedida no pacote**[**DMANQUALI-11018**](https://tdn.totvs.com/display/PROT/24372422+DMANQUALI-11018+DT+SigaQIE+-+MV_PRFOFAB)**em 29.08.2025**, o parâmetro **MV\_PRFOFAB** não é mais validado no módulo **SIGAQIE**.
