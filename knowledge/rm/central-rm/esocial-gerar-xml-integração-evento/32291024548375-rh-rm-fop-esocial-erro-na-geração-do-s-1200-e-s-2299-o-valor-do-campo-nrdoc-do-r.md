---
article_id: 32291024548375
category: eSocial - Gerar XML/ Integração Evento
content_hash: c78458cad44d7e781aded89e0ba9984787d4464ccf2967c093303e93828d41b6
fetched_at: '2026-06-28T22:47:12.953744+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na geração do S-1200 e S-2299: O valor do campo
  ''nrDoc'' do registro ''descFolha'' excedeu o tamanho do campo e foi truncado'
type: support-article
updated_at: '2026-05-27T20:30:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32291024548375-RH-RM-FOP-eSocial-Erro-na-gera%C3%A7%C3%A3o-do-S-1200-e-S-2299-O-valor-do-campo-nrDoc-do-registro-descFolha-excedeu-o-tamanho-do-campo-e-foi-truncado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32290963528343) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao gerar os eventos S-1200/S-2299 é apresentada a mensagem: O valor do campo 'nrDoc' do registro 'descFolha' excedeu o tamanho do campo e foi truncado

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões   
  
**Causa**  
O erro ocorre devido não possuir uma versão ou patch que contempla as novas validações da tag nrDoc que permite de 1 a 15 dígitos informados no campo, número do contrato referente ao empréstimo.

Sendo assim, como não atualizou para um versão vigente ou patch, o sistema ainda fica mantendo a antiga validação que era 8 dígitos.  
  
Segue Manual de Orientação do eSocial:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32290963529495)

**Solução**  
1. Para corrigir o erro mencionado na geração do XML, é necessário atualizar para as versões e patches a seguir:  
  
12.1.2406.277, 12.1.2410.229, 12.1.2502.145, 12.1.2506 ou superiores.

2. É necessário atualizar o campo abaixo com a nova Nota Técnica, a fim de atender às validações exigidas no layout vigente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32291527659671)

Link Central de Downloads: [Downloads e Atualizações](https://suporte.totvs.com/portal/p/10098/download#company/)

Saiba mais  
Para mais informações, acesse:   
[TOTVS RH Informa](https://informa.totvs.com/rh/)
