---
article_id: 360049654714
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: e4a9f5cc68864a823d1ec30e9c695425c5557a25eb73c92d6e0199085451376a
fetched_at: '2026-06-28T22:45:21.175961+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Integração - O valor 'x' informado na tag
  cpfTrab existe na base de dados, mas está atualmente com status 'x'
type: support-article
updated_at: '2026-06-26T11:58:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049654714-RH-Linha-Protheus-TAF-eSocial-Integra%C3%A7%C3%A3o-O-valor-x-informado-na-tag-cpfTrab-existe-na-base-de-dados-mas-est%C3%A1-atualmente-com-status-x
---

**Dúvida**

Ao integrar os eventos para o TAF ocorre falha ao integrar os eventos para o sistema:

O valor '**x**' informado na **tag cpfTrab** existe na base de dados, mas está atualmente com status '**x**'

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - Todas as Versões.

**Solução:**

1 - Verifique se o trabalhador está com *status* diferente de "Aceito RET". Para verificar o cadastro do trabalhador, acesse o artigo abaixo para acessar a rotina de cadastro do trabalhador e veja se o mesmo está com o número de recibo preenchido:

[RH - Linha Protheus - TAF - eSocial - Eventos Não Periódicos - S-2200/S-2300 - Como acessar a rotina de cadastro do trabalhador no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036524534)

2 - Se não estiver preenchido o número do protocolo, verifique se o mesmo foi transmitido para o e-Social no Painel eSocial do TAF:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25782018019735)

3 - Verifique qual a mensagem da inconsistência ou se o mesmo não foi transmitido e efetue a regularização do registro deste funcionário;

4 - Ao regularizar o status deste registro, regere o XML em seu ERP e integre novamente ao TAF.
