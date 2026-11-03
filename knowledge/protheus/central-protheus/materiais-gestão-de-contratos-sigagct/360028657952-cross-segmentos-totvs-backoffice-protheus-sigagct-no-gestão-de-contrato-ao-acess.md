---
article_id: 360028657952
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: c5a5abf9a1bd0b122f64e043dc6bdf82099581b3b3606f5484ee47231b90f907
fetched_at: '2026-06-28T22:37:20.293842+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT -  No Gestão de Contrato
  ao acessar no Menu programa CNTA200 na versão 12 apresenta o error log: InterFunctionCall:
  cannot find function CNTA200 in AppMap on __EXECUTE(APLIB090.PRW)'
type: support-article
updated_at: '2022-05-19T21:05:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028657952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-No-Gest%C3%A3o-de-Contrato-ao-acessar-no-Menu-programa-CNTA200-na-vers%C3%A3o-12-apresenta-o-error-log-InterFunctionCall-cannot-find-function-CNTA200-in-AppMap-on-EXECUTE-APLIB090-PRW
---

**Ocorrência**  
No Gestão de Contrato ao acessar no Menu programa CNTA200 na versão 12 apresenta o error log: InterFunctionCall: cannot find function CNTA200 in AppMap on \_\_EXECUTE(APLIB090.PRW)  
  
**Ambiente**  
Microsiga Protheus – Gestão de contratos – A partir da versão 12  
  
**Causa**

Esse incidente ocorre, pois, na versão 11 os acessos das rotinas de Contrato, Planilha, Cronograma e Revisão são em fontes separados (CNTA100 / CNTA200 / CNTA210 / CNTA140) e já na versão 12 foi realizada a junção das rotinas em único fonte (CNTA300) e Revisão fontes CNTA300R, mas a chamada é através da rotina de Contratos (CNTA300).  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Baixe do portal do cliente o menu da versão 12 e atualize, assim o problema deixará de ser apresentado, segue orientação abaixo para atualizar o menu e como fazer o download no portal do cliente.

DOWNLOAD MENU DE MÓDULO-P12:

Entre no Portal do Cliente ( http://suporte.totvs.com.br )

Entre no menu Downloads e Atualizações

Outras linhas de Produto: Protheus

MICROSIGA PROTHEUS VERSÃO 12.1.X (onde X é a versão da sua release)

Software:MENUS

Nas abas acima tem a a opção Filtro de pacotes, clique em Todos pacotes disponíveis

Baixe o arquivo **XX-XX-XX-BRA-MENUS\_12\_1\_XX.ZIP**

Renomeie o arquivo do módulo que ocorre o erro na pasta system (Exemplo **SIGAGCT.XNU**)

Copie somente o arquivo do módulo que ocorre o erro e cole na pasta system

Acesse o servidor e teste o menu.

2. Após realizar a atualização do menu relatado no passo 1 , acesse a rotina Manutenção CNTA300 para que possa efetuar a inclusão do contrato, da planilha e se o contrato tiver cronograma financeiro.

***Saiba Mais:***

[GCT\_P11 x P12 - Alterações entre Versões - Módulo de Gestão de Contratos](http://tdn.totvs.com/pages/releaseview.action?pageId=317309270)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
