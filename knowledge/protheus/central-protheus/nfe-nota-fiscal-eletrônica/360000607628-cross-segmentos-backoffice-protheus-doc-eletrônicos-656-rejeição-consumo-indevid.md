---
article_id: 360000607628
category: NFe - Nota Fiscal Eletrônica
content_hash: b9398b3e626ff61babcdbcea5843063039e66a03d9003e8cc0cd6bb960e9544f
fetched_at: '2026-06-28T22:40:01.529790+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 656 Rejeição :
  Consumo Indevido '
type: support-article
updated_at: '2024-04-04T17:04:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000607628--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-656-Rejei%C3%A7%C3%A3o-Consumo-Indevido
---

**Dúvida**

Como corrigir a 656 Rejeição : Consumo Indevido ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução:**

**1. Atualização do ambiente TSS (repositório e schemas)**

1. Atualizar o **repositório** com o último pacote de**expedição continua do TSS** disponível no link:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:

<https://suporte.totvs.com/portal/p/10098/download?e=761857>

**Saiba Mais:** [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

3. Este problema ocorre quando há um grande volume de consultas no servidor da SEFAZ em um período muito curto.

O TSS faz em **media 5 consultas no servidor da SEFAZ** e quando o cliente clica no **REFRESH** é adicionada mais uma consulta a cada clique. Neste momento a SEFAZ bloqueia as consultas, retornando então a **Rejeição 656 - consumo indevido.**  
  
Para solucionar essa ocorrência, basta aguardar a autorização das Notas.

* ***Saiba mais:***

04/03/2022 - Atualização das Regras de Uso Indevido do Web Service NFeDistribuicaoDFe - NT 2014.002

Visando garantir a sustentabilidade dos serviços de download de NF-e, Web Service NFeDistribuicaoDFe, regulamentados pela NT 2014.002, estará vigente a partir de 10/03/22, concomitante com o retorno das consultas consChNFe e consNSU, as seguintes regras de uso indevido: 

**1 - O uso indevido relativo ao****Web Service NFeDistribuicaoDFe****na consulta com tag:distNSU:**

1.1 - Não há mais documentos a distribuir e usuário continua consultando: 

Se não existir mais documentos a serem retornados (cStat=137) o usuário deve aguardar uma hora para realizar nova consulta. A realização de novas consultas em 1h, após receber a mensagem cStat137, gerará o uso indevido, retornando cStat=656. Nesse caso, o CNPJ é bloqueado por 1 hora, sendo impedido de realizar novas consultas nesse intervalo. Decorrido o intervalo de tempo, o desbloqueio será automático.

O campo xMotivo traz a seguinte descrição para ajudar o usuário a entender o que está causando o uso indevido: "*Rejeicao: Consumo Indevido. Deve ser aguardado 1 hora para efetuar nova solicitação caso não existam mais documentos a serem pesquisados. Tente após 1 hora"*

1.2 - Usuário não está consultando os NSU de forma sequencial: 

O usuário deve sempre realizar a consulta baseada no ultNsu retornado na consulta anterior, ou seja, *deve usar os valores do ultNSU retornados pelo serviço nas chamadas subsequentes. O valor do ultNSU corresponde ao ponto de onde a leitura dos blocos de documentos deve continuar. Quando ultNSU for igual ao valor do maxNSU retornado pelo serviço, quer dizer que não existem mais documentos para serem recuperados. Neste caso, para não haver bloqueio por uso indevido, deve-se aguardar 1 hora para realização de novas consultas.*

Se consultar fora da sequência, será bloqueado. Decorrido o intervalo de tempo, o desbloqueio será automático.

O campo xMotivo traz a seguinte mensagem: "*Rejeicao: Consumo Indevido. Deve ser utilizado o ultNSU nas solicitacoes subsequentes. Tente apos 1 hora"*

**Atenção**: Se diversas aplicações do mesmo ator (emitente ou destinatário ou transportador na NF-e ou indicado no campo autxml) da NF-e efetuarem consultas por NSU para o mesmo CNPJ (14 dígitos - informado na requisição xml), essas devem seguir a mesma sequência de numeração ordenada e de forma ascendente. Caso contrário, enquadrar-se-ão na categoria de uso indevido.  

**2 - O uso indevido relativo ao Web Service NFeDistribuicaoDFe nas consultas com tag:****consChNFe****e tag: consNSU:**

As consultas por chave de acesso e por NSU foram construídas para permitirem ao usuário buscar pontualmente alguma NF-e e de um período retroativo máximo de 90 (noventa) dias. Se o usuário necessitar buscar todas as NF-es de no máximo 90 dias de um CNPJ ator interessado, deve ser usada a consulta "distNSU".   

2.1 Consultada uma quantidade de NF-e ou NSU superior ao limite permitido por hora: 

Será permitido um número limitado de consultas por chave de acesso ou NSU em um período de 1hora. Se o usuário continuar consultando após atingir o limite de consultas por chave de acesso ou NSU em 1h, retornará a mensagem *656 - Consumo indevido - ultrapassou o limite de 20 consultas por hora*. Nesse caso, o CNPJ é bloqueado por 1 hora, sendo impedido de realizar novas consultas nesse intervalo. Decorrido o intervalo de tempo, o desbloqueio será automático.

**Observação**: Em quaisquer dos três tipos de consulta, quando o usuário receber a mensagem 656 - consumo indevido, deve aguardar 1hora. Se retomar a consulta antes de completar 1 (uma) hora, o tempo é zerado e a contagem reiniciará até completar 1hora.
