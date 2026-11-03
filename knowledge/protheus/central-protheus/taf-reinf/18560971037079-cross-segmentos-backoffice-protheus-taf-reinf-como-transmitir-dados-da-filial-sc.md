---
article_id: 18560971037079
category: TAF - REINF
content_hash: 307d1f99ee4743a864f73fa1ea08efe87aa92da65cce19a1296135607968c067
fetched_at: '2026-06-28T22:41:33.781461+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como transmitir dados
  da filial SCP na Sócio Ostensiva quando o CNPJ da SCP  for diferente do CNPJ da
  SO?
type: support-article
updated_at: '2023-10-30T13:05:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18560971037079-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-transmitir-dados-da-filial-SCP-na-S%C3%B3cio-Ostensiva-quando-o-CNPJ-da-SCP-for-diferente-do-CNPJ-da-SO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18560971013271) Tempo aproximado para leitura: 00:05:00 min **Dúvida**Quando existir uma filial cadastrada no TAF onde ela trata-se de SCP (Sociedade em Conta de Participação) e é necessário transmitir o bloco 40 na Sócio Ostensiva quando a raiz do CNPJ for diferente, como deve ser gerada essa apuração?   
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as versões  
  
**Solução**

A filial SCP não possui personalidade jurídica, portanto, os documentos que serão transmitidos pela Sócio Ostensiva **não devem** ser lançados nessa filial SCP.

Ou seja, a integração dos documentos que irá gerar os registros R-4010 ou R-4020 devem ser integrados para a Sócio Ostensiva (que geralmente é a matriz que faz a transmissão da Reinf).

No cenário onde a filial **SCP** possui um **CNPJ distinto**, essa filial **não deve** ser cadastrada no **Complemento Cadastral** e sim, incluída na aba **Outras Filiais** da Matriz dentro do **TAF**, exemplo:

Grupo de empresa: 99

Matriz que é a Sócio Ostensiva: 9901

Filial SCP (CNPJ diferente da matriz) : 9902

Complemento cadastral:

![MATRIZ SO.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/18561012367895)

Aba Outras filiais da Matriz:

![FILIAL SCP OUTRAS FILIAIS.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/18561000299927)

Dessa forma, os registros serão integrados pela SO.

Após, deve ser efetuado o cadastro de FCI/SCP

O cadastro de FCI/SCP serve como base para geração das informações do evento R-1050 - Entidades Ligadas.

Este cadastro pode ser preenchido de forma manual por meio do programa TAFA536 ou pode ser integrado por meio do layout T159/T159AA.

Para que a amarração correta do evento R-1050 seja feita com os eventos de pagamento R-4010/R-4020 é necessário que os participantes que serão utilizados nos eventos de movimento estejam listados neste cadastro.

Exemplo de cadastro preenchido:

![](https://tdn.totvs.com.br/download/attachments/344474121/image2022-12-16_12-6-37.png?version=1&modificationDate=1671203198030&api=v2)

**Importante: Se houver movimentos integrados na filial SCP, esses movimentos devem ser excluídos do TAF, para não causar duplicidade.**

Pode ser usada a rotina Exclusão por Período fiscal para excluir os movimentos dessa filial, marcando apenas a opção "movimentos fiscais": [Exclusão por Período Fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024356232-Automa%C3%A7%C3%A3o-Fiscal-Funcionalidades-Limpeza-da-base-de-dados-para-retransmiss%C3%A3o-de-eventos-ao-Governo)

Para mais informações:

<https://tdn.totvs.com.br/display/public/TAF/EFD-Reinf>

<https://tdn.totvs.com/display/public/ConSeg/EFD-Reinf+-+Filial+SCP+-+CNPJ+Distinto+da+Matriz>
