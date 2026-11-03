---
article_id: 360019903231
category: Ativo Fixo - Transferência
content_hash: 4b01b2abfb630d80be7b0884cbe1d2eac78f0355ce26e86076a84ed17a80666d
fetched_at: '2026-06-28T22:41:52.164055+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA060 - CANCELAMENTO
  DE TRANSFERENCIA DE FILIAL
type: support-article
updated_at: '2022-10-06T18:11:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019903231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-CANCELAMENTO-DE-TRANSFERENCIA-DE-FILIAL
---

**Dúvida**

* Existe a possibilidade cancelar transferência?

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - Todas as versões

**Solução**

* Ao configurar o parâmetro MV\_ATFCATR para que seja possível cancelar a transferência de bens entre filiais, sendo possível excluir o ativo na filial de origem e a nota fiscal de entrada, caso seja necessário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015590071/mceclip0.png)

**Importante :**

Para garantir a integridade dos dados foi criada a validação na exclusão do ativo não sendo possível excluir o ativo caso não tenha sido cancelado.

Este cancelamento somente é permitido caso o ativo não tenha nenhum movimento além da aquisição e da transferência.  
Essa opção realiza as seguintes operações:

* Exclusão do ativo na filial de destino (Atual).
* Cancelamento de baixa na filial de origem.

Caso sejam efetuadas várias transferências de filial do mesmo ativo no período, é necessário cancelar essas operações na ordem inversa.

Exemplo:  
1. Transferência 01: Filial 01 > Filial 02  
2. Transferência 02: Filial 02 > Filial 03  
3. Transferência 03: Filial 03 > Filial 05

Cancelamento:  
1. Transferência 03  
2. Transferência 02  
3. Transferência 01

Saiba mais :

[ATF0029\_Regra\_do\_Cancelamento\_da\_Tranferencia](http://tdn.totvs.com/display/PROT/ATF0029_Regra_do_Cancelamento_da_Tranferencia)

[MP - SIGAATF - ATFA060 - HELP ao cancelar transferência: AF060RECNO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021746292-MP-SIGAATF-ATFA060-HELP-ao-cancelar-transfer%C3%AAncia-AF060RECNO?source=search)
