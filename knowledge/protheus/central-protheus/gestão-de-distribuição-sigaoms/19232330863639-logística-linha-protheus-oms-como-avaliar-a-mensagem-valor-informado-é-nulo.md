---
article_id: 19232330863639
category: Gestão de Distribuição (SIGAOMS)
content_hash: 108d31db0314d4b378497d9e9a3f3635289346104e0e31cd377e6be9d66bc43c
fetched_at: '2026-06-28T22:45:49.618242+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como avaliar a mensagem Valor informado
  é Nulo
type: support-article
updated_at: '2025-05-24T13:15:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19232330863639-Log%C3%ADstica-Linha-Protheus-OMS-Como-avaliar-a-mensagem-Valor-informado-%C3%A9-Nulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19232324881047) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**No envio do Pedido de Venda do **TOTVS OMS** ao **TRE**, como avaliar a mensagem **Valor informado é Nulo**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) – Todas as versões.  
  
**Solução**No Envio de Pedidos de Venda pela rotina **Envio de Pedidos -** **OMSXCPL6** para o **TRE**, se o arquivo **XML** de envio estiver com os campos **Altura**, **Comprimento** e **Largura** dos **Produtos** com **valores quebrados**, será retornando a mensagem:  
  
**Precisa ser um número inteiro  
Valor informado é Nulo**Abaixo seguem as *tag's* do arquivo **XML** e de quais campos no **TOTVS OMS** são consideradas as informações para o preenchimento das *tag's*:

* **Height: Altur.Armaz - B5\_ALTURLC informado Complemento de Produto - MATA180**
* **Width:  Compr.Armaz - B5\_COMPRLC informado Complemento de Produto - MATA180**
* **Lenght: Largu.Armaz - B5\_LARGLC informado Complemento de Produto - MATA180**

Exemplo de arquivo **XML** com **valores quebrados**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19303875827607)

Exemplo de arquivo **XML** com **valores inteiros**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19303843567255)

**Importante**Na integração com a solução **TOL**, são aceitos valores quebrados, conforme o exemplo acima 0.00100000, porém na integração com o **TRE**, essa solução os valores deverão ser inteiros, conforme exemplo acima 2.00000000  
  
**Saiba Mais**Mais informações poderão ser acessadas no *link* abaixo:  
[Logística - Linha Protheus - OMS - Envio de Pedidos do TOTVS OMS para TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011610682-Log%C3%ADstica-Linha-Protheus-OMS-Envio-de-Pedidos-do-TOTVS-OMS-para-TOL-TRE)  
  
**Glossário****TOL** - **TOTVS Otimização Logística**  
**TRE** - **TOTVS Roteirização e Entrega**  
**TOTVS OMS** - *Order Management System***XML** - *Extensible Markup Language*
