---
article_id: 360052085214
category: RH - Ponto Eletrônico
content_hash: af0cf69ab179456406cfd4a1514405838f9ae33a93b9203ec4535c34ffbb1684
fetched_at: '2026-06-28T22:44:58.331369+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Parâmetro que define se ocorrerá integração do
  Ponto Eletrônico com o TSA ou Suricato
type: support-article
updated_at: '2022-07-19T19:21:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052085214-RH-Linha-Protheus-PON-Par%C3%A2metro-que-define-se-ocorrer%C3%A1-integra%C3%A7%C3%A3o-do-Ponto-Eletr%C3%B4nico-com-o-TSA-ou-Suricato
---

**Dúvida**Qual parâmetro define se ocorrerá integração do Ponto Eletrônico com o TSA ou Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Recentemente foi criado um novo parâmetro que determina no Ponto Eletrônico se ocorrerá integração com o TSA ou Suricato, que é o **MV\_TSAINT.**Se o parâmetro estiver com .T., o sistema entenderá que a integração será com o TSA, se estiver com .F. será com o Suricato.Para criar o parâmetro, será necessário utilizar o UPDDISTR, aplicando o pacote de expedição a partir do dia 14/08/2020 ou criar o parâmetro manualmente, para a versão 12.1.27 e anteriores  
Segue abaixo dados para criação manual:  
Tipo: 1 - Lógico  
Descrição: Identifica se a integração será realizada com    
Cont. Descr.: o TSA ou Suricato. .T. = TSA, .F. = Suricato  
  
**Informações complementares**  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
