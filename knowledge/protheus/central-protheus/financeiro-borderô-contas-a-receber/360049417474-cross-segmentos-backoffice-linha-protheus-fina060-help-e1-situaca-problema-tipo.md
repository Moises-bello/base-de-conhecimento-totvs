---
article_id: 360049417474
category: Financeiro - Borderô contas a Receber
content_hash: b68c0c273a9a9f4d0fa627d62618175e982f3d7582589848336fd68a88bca9ab
fetched_at: '2026-06-28T22:37:39.703193+00:00'
product: protheus
section_id: 35057237655191
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - FINA060 - HELP: E1_SITUACA Problema
  Tipo de Operação bancária na qual o título foi negociado junto ao agente cobrador'
type: support-article
updated_at: '2026-01-21T19:09:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049417474-Cross-Segmentos-Backoffice-Linha-Protheus-FINA060-HELP-E1-SITUACA-Problema-Tipo-de-Opera%C3%A7%C3%A3o-banc%C3%A1ria-na-qual-o-t%C3%ADtulo-foi-negociado-junto-ao-agente-cobrador
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25916490791191)**Tempo aproximado para leitura: 00:10 **min**

**Ocorrência**  
Na rotina de **Transferências,** ao alterar a situação do título do Contas a Receber de banco para cartório, apresenta a mensagem "HELP: E1\_SITUACA"?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
O acionamento do **Help** ocorre em decorrência da configuração do parâmetro **MV\_TRFBCO**, sendo necessário observar e aplicar as orientações a seguir:

Quando o parâmetro **MV\_TRFBCO** estiver configurado com o valor **2**, será necessário limpar os campos **Portador**, **Agência** e **Conta**, bem como alterar o conteúdo do campo **Situação** para **“0 – Carteira”** e salvar o registro. Somente após esse procedimento será possível realizar a transferência da situação para **“1 – simples”**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37837910796951)

Quando o parâmetro **MV\_TRFBCO** estiver definido com o valor **1**, o sistema permitirá a alteração da situação da carteira de forma direta, dispensando a obrigatoriedade de alteração prévia para a situação **“0 – Carteira”**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37837910799255)

**Saiba mais**  
[MV\_TRFBCO](https://tdn.totvs.com/pages/releaseview.action?pageId=458753100)
