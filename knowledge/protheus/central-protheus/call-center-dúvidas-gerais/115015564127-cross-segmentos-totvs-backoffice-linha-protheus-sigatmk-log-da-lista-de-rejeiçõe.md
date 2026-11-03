---
article_id: 115015564127
category: Call Center - Dúvidas Gerais
content_hash: fbb528766dc02638bd03d553d8d02b5a2d4ecfae5c6de97d1ffed804e32da577
fetched_at: '2026-06-28T22:41:26.840771+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- LOG da Lista de
  Rejeições
type: support-article
updated_at: '2022-06-17T16:32:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015564127-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-LOG-da-Lista-de-Rejei%C3%A7%C3%B5es
---

**Dúvida**  
  
Onde fica Gravado o log da lista de rejeições feitas pelo operador na rotina pre atendimento Call Center?  
  
**Ambiente**  
  
Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- Versão 11 e 12  
  
**Solução**  
  
Quando o operador rejeita um pré-atendimento,se o parâmetro **MV\_TMKDILG** estiver preenchido com um endereço válido dentro da pasta do sistema, o mesmo irá gravar um arquivo .log com todos os clientes que foram rejeitados pelo operador, criando o arquivo com o nome REJ+nome do operador+.cob.log.  
  
Exemplo:  
  
**MV\_TMKREJE** = Permite ou não o operador a rejeitar um pre atendimento (tipo logico, .T. / .F.)  
**MV\_TMKDILG** = endereço onde grava log de processo  
cPathLog + 'REJ' + cOperador + '.COB' // Nome do arquivo com lista de clientes rejeitados pelo operado  
  
  
Obs. O arquivo só e gravado se o parâmetro **MV\_TMKREJE** estiver igual a .T. e o endereço de gravação estiver valido dentro de uma pasta do sistema protheus.

Exemplo: 'System'
