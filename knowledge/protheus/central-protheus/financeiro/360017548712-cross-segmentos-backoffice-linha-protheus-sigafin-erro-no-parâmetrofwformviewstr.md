---
article_id: 360017548712
category: Financeiro
content_hash: fc92d68efa06f0a7ceabac7863eb51045511184891c5854063f99d9e13db24ca
fetched_at: '2026-06-28T22:38:02.949577+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - erro no parâmetroFWFormViewStruct:
  O erro no método SETPROPERTY: Campos FKG_PERCEN / FKG_CALCUL / FKE_CALCUL / FKE_PERCEN'
type: support-article
updated_at: '2022-06-21T00:10:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017548712-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-erro-no-par%C3%A2metroFWFormViewStruct-O-erro-no-m%C3%A9todo-SETPROPERTY-Campos-FKG-PERCEN-FKG-CALCUL-FKE-CALCUL-FKE-PERCEN
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**Mensagem apresentada **{ parâmetroFWFormViewStruct: O erro no método SETPROPERTY: Campo FKG\_PERCEN / FKG\_CALCUL / FKE\_CALCUL / FKE\_PERCEN }**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Dicionário desatualizado.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

* Acesse o Portal do Cliente: <http://suporte.totvs.com>
* *Menu* > *Downloads* e Atualizações
* Linha: *Protheus*
* Microsiga *Protheus* Versão 12.1.XX (onde XX é a versão da *Release* do P12 que você vai utilizar)
* Todos
* **Categoria: Dicionário de dados**
* Baixe **REINF - DICIONARIO DE DADOS RELEASE 12.1.17 - DIFERENCIAL - BRASIL**

**Importante**: Caso não apareça as versões, em "Filtros de pacotes" selecione "Todos pacotes disponíveis" e categoria novamente.

* Descompacte o arquivo baixado **TXT** na pasta ***Systemload*** do Protheus.
* Atualize os arquivos na pasta e execute o **UPDDISTR**.

**Saiba mais:**

[Atualizador de dicionário e base de dados - UPDDISTR](http://tdn.totvs.com/pages/viewpage.action?pageId=181965468)

- **REINF**

[Pacote de atualização REINF - 2018](http://tdn.totvs.com/pages/viewpage.action?pageId=346489720)
