---
article_id: 360006611532
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: cebf91ae4eacbc3d3c22c17bd0e6b63f885bb0e4ca10020798ba20022a367bec
fetched_at: '2026-06-28T22:37:55.326279+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Como parametrizar
  o sistema para geração do CNAB
type: support-article
updated_at: '2022-05-31T02:05:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Como parametrizar o sistema para gerar o CNAB?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Para a realização das configurações de **CNAB** - **Centro Nacional de Automação Bancária**, indicamos a solicitação de um consultor in loco para realizar tal procedimento. A configuração e ajustes no arquivo de CNAB é de responsabilidade do cliente, uma vez que estas se alternam de cliente para cliente.

Caso o cliente possua conhecimento para a realização da configuração do **CNAB,**indicamos aquialgumas orientações que poderão ser úteis para realizar tal ação.

Porém, caso o cliente tenha conhecimento para a realização da configuração do **CNAB** estaremos enviando conforme abaixo os **CNAB**'s e algumas orientações que poderão ser úteis:  
  
Para envio e retorno do **CNAB**, são necessários os seguintes cadastros:

* **Banco** (Financeiro).
* **Parâmetros de Banco** (Financeiro).
* **Ocorrências** **CNAB** (Financeiro).
* **Arquivo de Configuração** (Configurador).

Será gerado o arquivo (.txt) de remessa através do módulo **Financeiro**. Assim que o Banco retornar o arquivo com as baixas, é necessário processar o arquivo no módulo **Financeiro** para que o sistema processe o mesmo de acordo com as ocorrências informadas pelo Banco (Baixas, alterações, etc).

**Veja mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
