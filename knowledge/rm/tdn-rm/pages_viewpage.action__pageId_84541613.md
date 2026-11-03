---
content_hash: 76df3e3c4bdf574d1061dc2a1cb5ba931912c19d69aaa6ca25e43bc955896e3b
fetched_at: '2026-06-29T00:11:50.745543+00:00'
page_id: '84541613'
product: rm
source: tdn-rm
title: RMFIS00007_Sintegra - Registro Tipo 54/75 sem tipo correspondente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=84541613
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:**11.52 |
| **Processo** | **:** | Processo:  Inconsistência apresentada na validação do arquivo Sintegra |
| **Subprocesso** | **:** | Registro tipo 54 sem registro tipo 75 correspondente |
| **Data da publicação** | **:** | 12/09/2013 |

**Causa**

Mensagens apresentadas na validação do SINTEGRA:

“**Registro tipo 54 sem registro tipo 75 correspondente**” e ou apresentar o erro

“**Registro tipo 75** **sem registro correspondente em pelo menos um dos tipos 54, 57, 60D, 60I, 60R, 74, 77,66**”.

**Solução**

Verificações a serem realizadas para solução aos erros:

* + **Erro 1:**

**Erro 2:**

A mensagem de erro 1 ocorre normalmente em função do **CST** do produto no lançamento (item) estar em branco ou diferente das informações da situação Tributária no cadastro da natureza e referência procedência  no cadastro do produto.

Necessário verificar e ajustar:

**Cadastro | natureza de operação | aba tributação ICMS/IPI** | edita a regra do **ICMS** e vide campo Situação tributária (**2 dígitos**)

  Verifique a procedência : **Cadastro | produto | aba detalhes | aba outros dados |** campo procedência (1 dígito)

Verifique no item do lançamento fiscal se o campo **CST** corresponde a junção da Situação (natureza fiscal) + procedência (produto) (3 dígitos)

**Lançamentos | selecionar o lançamento | aba itens | editar o item | aba identificação | campo CST**

 Verifique os dados cadastrais do **Cliente/Fornecedor**, se contribuinte do ICMS. Cadastro do **Cli./For.** 

**- OBS: Verifique também a informação de CNPJ, IE, endereço, dados  cadastrais do Contador e Representante.**

Verificar no cadastro do produto, se tributado pelo **ICMS**. Cadastro do produto**|anexos dados fiscais do produto**

 Verifica as informações selecionadas no filtro da geração da rotina.  **OBS**: Atenção aos registros selecionados

**Adicional:**

**Informações da Sefaz quanto ao CST**

**Para maiores informações:**

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
