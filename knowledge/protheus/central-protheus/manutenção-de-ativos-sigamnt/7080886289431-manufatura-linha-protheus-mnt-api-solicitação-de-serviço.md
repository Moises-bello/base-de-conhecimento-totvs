---
article_id: 7080886289431
category: Manutenção de Ativos (SIGAMNT)
content_hash: cbc3b604e1a463da2b0f47be3a5e22e6e0da4a258fa1c991dce7ca6d00c83f61
fetched_at: '2026-06-28T22:42:32.733774+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - API Solicitação de Serviço
type: support-article
updated_at: '2025-04-10T12:06:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7080886289431-Manufatura-Linha-Protheus-MNT-API-Solicita%C3%A7%C3%A3o-de-Servi%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31311317842711)*** Tempo aproximado para leitura: **00:01:05 min** **Dúvida**Como utilizar a **API** para **Solicitação de Serviço - S.S**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Para funcionamento da **API**, os requisitos para funcionamento são:

* Ter configurado o **Rest** no ambiente, conforme a documentação disponível em [Configuração do REST Protheus para uso com os aplicativos Mobile](https://tdn.totvs.com/x/nhHvGQ);
* A chave **Security** deverá estar habilitada **Security=1**, no **appserver.ini** do ambiente.

Ao executar a chamada do *Webservice*, deverá ser configurado para **Basic Auth** utilizando usuário e senha do **Protheus**.  
**Username** <username>  
**Password** <password>  
  
**Header**Campos que deverão ser adicionados no **Header** para possibilitar a inclusão de uma **S.S.**

| Variável | Descrição | Obrigatório | Exemplo |
| --- | --- | --- | --- |
| tenantId | Código da empresa + Código da Filial | Sim | T3,M RJ 01 |

**Importante**  
O valor inserido na variável **tenantId** não deverá possuir espaço entre a vírgula;  
No exemplo apresentado na tabela acima, **T3** corresponde a uma empresa e **M RJ 01** a uma filial.  
  
**Saiba mais**Para informações complementares e exemplos, verifique o *link*  
[API SIGAMNT/SIGAGFR - Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=683181217)
