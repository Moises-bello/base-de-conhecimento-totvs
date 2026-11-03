---
article_id: 360017981752
category: TAF - GIA
content_hash: bbb8e5c4ad18c8da78ec5350a72779fdf399ca0f745c6a48734c9bb69a1e842e
fetched_at: '2026-06-28T22:41:32.411964+00:00'
product: protheus
section_id: 1500001547982
source: central-protheus
title: MP - TAF - Error.log type mismatch on + on XFUNRELAC(TAFXFUN.PRW)
type: support-article
updated_at: '2021-04-28T15:22:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017981752-MP-TAF-Error-log-type-mismatch-on-on-XFUNRELAC-TAFXFUN-PRW
---

**Ocorrência**No módulo **TAF**, ao acionar a opção **Incluir** ou **Visualizar** é apresentado **error.log:   
  
type mismatch on + on XFUNRELAC(TAFXFUN.PRW) 27/09/2018**

**Ambiente**Protheus - TOTVS Automação Fiscal - A partir da versão 12.1.17  
   
 **Causa**Esta situação ocorre, pois o inicializador padrão do campo **C20\_DCODMO** está incorreto.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o módulo **Configurador**-> Base de Dados -> Dicionário -> Base de Dados;  
2. Posicione o cursor sobre a opção **Dicionário de Dados**, localizada no painel a esquerda;  
3. Clique em **Pesquisar**e busque pela tabela **C20**, após clique em **Editar**;  
4. Posicione o cursor sobre a opção **Campos**, localizada no painel a esquerda;  
5. Clique em **Pesquisar**e busque pelo campo **C20\_DCODMO**;   
6. Clique em **Editar**, selecione a pasta **Opções**, altere o conteúdo do campo **Inic. Padrão** para **XFUNRELAC(44,"C20\_CODMOD")**;   
7. Clique em **Salvar**, após em **Confirmar** e para finalizar acione a opção **Atualizar Base de Dados**para que as alterações realizadas sejam efetivadas.
