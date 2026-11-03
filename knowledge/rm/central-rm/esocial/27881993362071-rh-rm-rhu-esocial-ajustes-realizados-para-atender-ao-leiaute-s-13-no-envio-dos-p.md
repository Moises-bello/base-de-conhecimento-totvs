---
article_id: 27881993362071
category: eSocial
content_hash: d4120bd248e33905ea5d4770c7ed779b085c1091a81427950f383da94aa88ca1
fetched_at: '2026-06-28T22:47:15.319962+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: RH - RM - RHU - eSocial - Ajustes realizados para atender ao Leiaute S-1.3
  no envio dos Processos Trabalhistas
type: support-article
updated_at: '2024-12-02T13:51:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27881993362071-RH-RM-RHU-eSocial-Ajustes-realizados-para-atender-ao-Leiaute-S-1-3-no-envio-dos-Processos-Trabalhistas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27881993331095) Tempo aproximado para leitura: **00:03:30 min** **Dúvida**Quais as principais mudanças nos eventos dos Processos Trabalhistas com a entrada do Leiaute S-1.3?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - 12.1.2402.245, 12.1.2406.185, 12.1.2410.121 e superiores.  
  
**Solução**

As versões que contemplarão o Leiaute S-1.3 são:

* 12.1.2402.245;
* 12.1.2406.185;
* 12.1.2410.121 e superiores.

**Importante**! Deverá ser executado também o **RM.Atualizador.exe**.

Conforme cronograma disponibilizado pelo governo através do [Portal do eSocial](https://www.gov.br/esocial/pt-br), os prazos para implantação das versões são:

* **Produção Restrita:** 07/10/2024
* **Produção**: 02/12/2024

Está previsto período de **convivência das versões S-1.2 e S-1.3** sendo de **02/12/2024** a **02/02/2025**. Os eventos **S-1210 e S-2501** devem ser enviados **exclusivamente na versão S-1.3** a partir do **período de apuração 01/2025**, de acordo com a [notícia](https://www.gov.br/esocial/pt-br/noticias/publicacao-da-versao-s-1-3-dos-leiautes-do-esocial-e-da-nota-tecnica-no-04-2024-revisada) publicada pelo governo em 28/06/2024.

Abaixo segue as alterações que foram realizadas:

**S-2500 - Processo Trabalhista**

* Criação dos campos {**dtAdmRespDir**} e {**matRespDir**} no grupo {**ideResp**}

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27881993334423)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27882017196567)

Obs: Somente é possível preencher um dos dois campos. Não é possível preencher os dois. 

* Alteração da validação do campo {**codCateg**} do grupo {**mudCategAtiv**}

**ANTES**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27882017198871)

**AGORA**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27882017201047)

* Alteração na lista de opções do campo {**indReperc**} do grupo {**infoVlr**}

**ANTES**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27882017204247)

**AGORA**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27882017205527)

* Criação do grupo {**infoInterm**} que pertence ao grupo {**idePeriodo**}

Campo **Informações relativas ao trabalho intermitente** criado para que possa ser informado os dados referente ao trabalho intermitente para o período que está sendo incluído.

Só será obrigatório informar quando não existir os eventos S-2190, S-2200 e S-2300 e o código de categoria for igual a 111 ou quando existir os eventos S-2190, S-2200 e S-2300 e o código de categoria no RET for igual a 111.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884228472343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884228477079)

Validação no RM para os campos: 

**Dia do mês:** será validado se o dia é compatível com o mês informado no período.  
**Horas trabalhadas:** deve ser informado no formato hora, ou seja, 4 dígitos. Exemplo: 23:59

* Alteração na validação do grupo {**infoDeslig**}

**ANTES**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884228480023)

**AGORA   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884185874199)  
  
  
S-2501 - Informações de Tributos Decorrentes de Processo Trabalhista**

* Alteração da condição do grupo **{ideProc}:** criação do campo **{ideSeqProc}** no grupo **{ideProc}**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884228487063)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884185883799)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27905069843863)

Campo criado para as ações trabalhistas que abrangem um número muito elevado de  
reclamantes, no qual é necessário enviar mais de um S-2501 para o mesmo processo e mesmo período de apuração.

* Criação do grupo {**rendIsen0561**} que pertence ao grupo {**infoIR**}

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884228499095)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27905069848215)

Grupo **Rendimentos Isentos exclusivos do CR 0561** só é obrigatório caso o **Código de Receita** for igual a **056152 - IRRF - CCP/NINTER.** Além disso, os campos poderão receber valores nulos.

* Alteração na validação do campo {**vrCR**} e criação do campo {**vrCR13**} que pertencem ao grupo {**infoCRIRRF**}

**ANTES**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884228510487)

**AGORA**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884228514327)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27905069850007)

* Criação de campos no grupo {**infoIR**}

**ANTES**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884228524311)

**AGORA**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884185918615)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884185921431)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27905069855255)

* Alteração na validação do campo {**tpRend**} que pertence ao grupo {**penAlim**}

**ANTES**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884228547223)

**AGORA**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884185937687)

* Alteração na validação do campo {**dtLaudo**} que pertence ao grupo {**infoIRComplem**}

**ANTES**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884228556183)

**AGORA**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884185950231)

**S-2555 - Solicitação de Consolidação das Informações de Tributos Decorrentes de Processo Trabalhista**

**Conceito:** evento criado para solicitar a totalização no caso de envio de eventos S-2501  
múltiplos para o mesmo processo, e mesmo período de apuração.  
  
**Quem está obrigado:** todo declarante que necessitar enviar eventos S-2501 múltiplos para o mesmoprocesso e mesmo período de apuração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884659898263)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27884659900951)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27905069857431)

**Saiba Mais**

Para maiores informações, acesse: 

     - [Processo Trabalhista - Cadastros dos eventos S-2500 e S-2501](https://tdn.totvs.com/display/LRM/Processo+Trabalhista+-+Cadastros+dos+eventos+S-2500+e+S-2501?draft=true#ComoFunciona-Evento1.3)
