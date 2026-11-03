---
article_id: 360018588311
category: SIGAACD - Automação e Coleta de Dados
content_hash: ce758dc1045e91106188bd7a9b6d3ddbc94def0b769114250e39870f56adc6b3
fetched_at: '2026-06-28T22:39:11.048082+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como mapear a porta
  e imprimir Etiquetas no ACD?
type: support-article
updated_at: '2021-11-18T18:55:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018588311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-mapear-a-porta-e-imprimir-Etiquetas-no-ACD
---

**Dúvida**  
Como mapear a porta LPT1/CUPs e imprimir no ACD?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Por padrão o SIGAACD utiliza a porta LPT1. Para utilizar a porta USB será necessário um programa que possa emular a porta USB em **LPT1.**

Sugerimos o uso do programa ***DosPrint***. O uso deste fica de livre escolha. Porém é imprescindível que a Impressora esteja mapeada na porta LPT1 para conseguir efetuar as impressões das etiquetas.

Com a impressora devidamente mapeada como LPT1, ao imprimir as etiquetas, as mesmas são enviadas ao *Spool* da mesma.

**Como emular porta quando utilizado o Sistema Operacional Linux?**

Usuários do Sistema Operacional Linux precisam mapear a porta LPT via CUPS (“Common Unix Printing System"). Se trata de um sistema de impressão para sistemas baseados em Unix.

Veja abaixo exemplo de mapeamento:

```
LPT<x>=<nome da impressora no spool>LPT1=hp640c
```

Neste exemplo, toda impressão direcionada para a porta **LPT1**, será redirecionada para a impressora CUPS nomeada hp640c.

<x> será o número da porta para a impressora configurada no *spool*.

**Observação Importante:**

**É importante que o cliente avalie a linguagem da impressora com o fabricante**, pois existem cenários onde algumas Empresas fabricantes foram compradas e o nome do fabricante pode divergir da linguagem.

Exemplo: Impressora da marca Zebra podem utilizar a linguagem Eltron.

**Linguagens homologadas e RDMakes para aplicação e uso da impressão**

rVeja abaixo a lista de linguagens homologadas e ao final do artigo, o arquivo anexo com os RDMakes para cada uma delas:

 

* ZPL (ou EPL em alguns casos) - Linguagem de programação do fornecedor Zebra
* EPL – Linguagem de programação do fornecedor EPL
* DPL – Linguagem de programação do fornecedor DATAMAX
* IPL – Linguagem de programação do fornecedor INTERMEC

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*

*[Seleção de impressoras locais LinuxKubuntu](https://tdn.totvs.com/pages/viewpage.action?pageId=6065192)*
