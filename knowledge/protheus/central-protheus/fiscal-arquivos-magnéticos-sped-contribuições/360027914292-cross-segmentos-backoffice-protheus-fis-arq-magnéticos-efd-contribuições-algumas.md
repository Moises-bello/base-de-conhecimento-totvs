---
article_id: 360027914292
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: f58644c8fc96014f5edfccb7831d5d3106db501a30cda0077befd58230e308c7
fetched_at: '2026-06-28T22:42:04.853436+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - EFD Contribuições
  - Algumas Rotinas não estão disponíveis na FISA001
type: support-article
updated_at: '2025-02-26T13:05:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027914292-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Algumas-Rotinas-n%C3%A3o-est%C3%A3o-dispon%C3%ADveis-na-FISA001
---

**Ocorrência**Mesmo o ambiente estando adequado para atender o **Layout 005** do **EFD Contribuições**, algumas rotinas não estão disponíveis na **FISA001**.  
  
"**Ajuste Base de Cálculo de PIS e COFINS**"   
"**Recibos de Transmissão do SPED**"   
  
Algumas perguntas não estão disponíveis na *Wizard*.  
"**Decisão Judicial Ex. ICMS ?**"  
"**Exclusão ICMS a Recolher ?**"   
 "**Dev./ Canc. período anterior**"   
   
 **Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**Esse erro ocorre, pois o dicionário de dados não foi executado e com isso as tabelas **F2Z** e **F3N** não foram criadas, segue validação:

*IF FindFunction("FISA210") .AND. AliasIndic("F2Z")*  
*oTree:AddItem(STR0116 ,"008","PMSEDT3","",,,2) //"Ajustes da Base de Cálculo de PIS e COFINS"*  
*EndIF*  
  
  
*IF FindFunction("FISA211") .AND. AliasIndic("F3N")*  
*oTree:AddItem(STR0117 ,"019","PMSEDT3","",,,2) //"Recibos de Transmissão do SPED"*  
*EndIF*  
  
**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Para habilitar as opções desejadas precisa possuir os fontes **FISA210**/ **FISA211** - Tabelas **F2Z**/ **F3N**.  
2. Aplique o patch (link abaixo) e utilize a opção "**Somente os fontes atualizados**";  
3. Fazer o *Download* do **Dicionário de Dados** que está em anexo;  
4. Copiar os arquivos **sdfbra.txt** e **sx2.unq** para a pasta *SYSTEMLOAD* do **Protheus** e Executar o **UPDDISTR**;  
5. Executar a rotina novamente.

Link Patchs:   
12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=732303> ;   
12.1.16:<https://suporte.totvs.com/portal/p/10098/download?e=732301> ;   
11.80:<https://suporte.totvs.com/portal/p/10098/download?e=732302> ;

Para acessar a documentação da solicitação acesse o link:   
[http://t](http://tdn.totvs.com/x/TKTUGg)<http://tdn.totvs.com/pages/releaseview.action?pageId=450143308>

![](https://totvssuporte.zendesk.com/attachments/token/9aq6PeBShrvyydzT1MRBvxOlq/?name=image002.png)
