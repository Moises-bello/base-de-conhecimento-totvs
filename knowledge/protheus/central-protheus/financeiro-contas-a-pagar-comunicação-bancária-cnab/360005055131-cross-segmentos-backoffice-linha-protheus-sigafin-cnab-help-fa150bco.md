---
article_id: 360005055131
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: bdfe26d99073ac82a760417e3dcbb32d11e7056dcbc7260782eaf32a4af2de55
fetched_at: '2026-06-28T22:37:55.276577+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  CNAB - HELP: FA150BCO'
type: support-article
updated_at: '2022-06-24T00:56:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005055131-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-HELP-FA150BCO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00min  
  
Ocorrência**Ao realizar a geração do CNAB é exibido o Help: FA150BCO  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões

**Causa**Banco selecionado nos parâmetros (**SX1**) da rotina para geração do **arquivo de remessa** não está cadastrado na **FILIAL** que está logado, ou o tamanho dos campos no grupo de perguntas estão diferentes da **SX3**.

**Solução**Verificar se o **Banco** a ser processado existe na filial que está logado, caso a tabela **SA6** ( **Cadastro de Bancos**) seja exclusiva.

Verifique a **SX3** os tamanhos dos campos **A6\_COD, A6\_AGENCIA** e **A6\_NUMCON** estão de acordo com o tamanho dos campos de pesquisa na **SX1** no grupo "**AFI150**"

**Veja mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
