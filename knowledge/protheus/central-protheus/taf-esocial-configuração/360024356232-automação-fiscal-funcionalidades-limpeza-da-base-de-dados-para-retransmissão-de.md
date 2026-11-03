---
article_id: 360024356232
category: TAF - eSocial - Configuração
content_hash: 30875e70220d93235325f8a6300964b7f6191fb4a467961b2e559a14e7608750
fetched_at: '2026-06-28T22:45:14.456468+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: Automação Fiscal- Funcionalidades- Limpeza da base de dados para retransmissão
  de eventos ao Governo
type: support-article
updated_at: '2026-06-24T12:07:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024356232-Automa%C3%A7%C3%A3o-Fiscal-Funcionalidades-Limpeza-da-base-de-dados-para-retransmiss%C3%A3o-de-eventos-ao-Governo
---

**Dúvida**O Governo realizou uma limpeza em sua base de dados e preciso fazer o mesmo procedimento no sistema para retransmitir os eventos do eSocial.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - Release 12.1.33 e superiores  
  
**Solução**Para realizar essa limpeza, siga os procedimentos abaixo:

O sistema permite que seja realizada a limpeza da base de dados através da rotina Exclusão Por Período Fiscal, localizado em **Miscelânea → Funcionalidades → Exclusão Por Período Fiscal**.

É fundamental observar as regras abaixo:

* Verificar o **ambiente do Governo** configurado no sistema. Informação localizada em **Atualizações → Configs. TAF → Wizard Config. TSS**:

![](http://tdn.totvs.com/download/attachments/323620412/ambiente.jpg?version=1&modificationDate=1513876110000&api=v2)

* Acesse a rotina **Miscelanea → Funcionalidades → Exclusão por Período Fiscal**:

ATENÇÃO!

![(erro)](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/error.png) No caso do eSocial,**os parâmetros de data são desconsiderados**, apagando desta forma todos os registros localizados na base de dados:

![](http://tdn.totvs.com/download/attachments/323620412/exclu1.JPG?version=1&modificationDate=1513876110000&api=v2)

* Após confirmar o processamento, avalie quais empresas/filiais devem ser consideradas no processo de exclusão:

![](http://tdn.totvs.com/download/attachments/323620412/exclu2.JPG?version=1&modificationDate=1513876110000&api=v2)

* Quando o sistema está configurado para transmitir eventos para o **ambiente de pré-produção** do Governo:

1. 1. Todos os eventos serão excluídos da base de dados independente do status do registro;
   2. O evento S-1000 ( Informações do Empregador ), representado pelo cadastro Complemento de Empresa (TAFA050), não será excluído. Para este evento o conteúdo dos campos STATUS e RECIBO serão deletados, permitindo assim um novo envio do evento ao Governo.

**MENSAGEM DE ALERTA**

![](http://tdn.totvs.com/download/attachments/323620412/exclu3.JPG?version=1&modificationDate=1513876110000&api=v2)

* Quando o sistema está configurado para transmitir eventos para o **ambiente de produção** do Governo:

1. 1. Todos os eventos serão excluídos da base de dados; exceto os registros com status de transmitido, que são:
      1. **Status 2**: Transmitido e aguardando retorno;
      2. **Status 4**: Transmitido e consistente;
      3. **Status 6**: Exclusão transmitida e aguardando retorno;
      4. **Status 7**: Exclusão transmitida e consistente.
   2. O evento S-1000 ( Informações do Empregador ), representado pelo cadastro Complemento de Empresa (TAFA050), não será excluído. Para este evento o conteúdo dos campos STATUS e RECIBO serão deletados, permitindo assim um novo envio do evento ao Governo.

**MENSAGEM DE ALERTA**

![](http://tdn.totvs.com/download/attachments/323620412/exclu4.JPG?version=1&modificationDate=1513876110000&api=v2)

IMPORTANTE!

A funcionalidade de Exclusão por Período Fiscal tem por objetivo eliminar os registros de cadastros referentes a algum layout de obrigação fiscal, seja eSocial, ECF, EFD ICMS/IPI, entre outros. Esta rotina**não elimina registros de cadastros auxiliares** do TAF, pois são informações que não serão geradas em arquivo fiscal ou XML de envio e servem apenas para manter uma integridade entre os cadastros do sistema, portanto, não impedem o correto uso do TAF para entregas fiscais.
