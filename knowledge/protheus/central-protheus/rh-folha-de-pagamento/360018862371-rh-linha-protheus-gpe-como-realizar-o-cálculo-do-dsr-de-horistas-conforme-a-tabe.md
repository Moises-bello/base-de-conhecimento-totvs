---
article_id: 360018862371
category: RH - Folha de Pagamento
content_hash: 8e839c970d8fb1e15ecdf9b4f8a39e4c9ddb83995a55bbd9405c8bb54769369e
fetched_at: '2026-06-28T22:44:14.760422+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar o cálculo do DSR de horistas conforme
  a tabela de Horário Padrão do módulo SIGAPON
type: support-article
updated_at: '2024-09-12T12:21:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018862371-RH-Linha-Protheus-GPE-Como-realizar-o-c%C3%A1lculo-do-DSR-de-horistas-conforme-a-tabela-de-Hor%C3%A1rio-Padr%C3%A3o-do-m%C3%B3dulo-SIGAPON
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26320479373719) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**No módulo Gestão de Pessoal, como realizar o cálculo do DSR de horista conforme a tabela de horário padrão do módulo SIGAPON.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**O sistema não possibilita realizar o cálculo do DSR de Horistas utilizando exclusivamente as horas de DSR definidas na tabela de Horário Padrão do módulo Ponto Eletrônico (SIGAPON), mesmo definindo o parâmetro  **P\_LDSRHRSP** com valor **.T.****Solução**Foi implementada uma **melhoria** no sistema para possibilitar a **apuração das Horas de DSR** exclusivamente pela Tabela de Horário padrão.  
  
Essa melhoria foi disponibilizada por meio do mnemônico **P\_NDSRHORI**, que agora possui a nova opção 3 entre as configurações possíveis, conforme segue:  
  
0 - Padrão, como é feito atualmente: horas dias (RA\_HRSDIA) X Nº Dias DSR (RCF\_DIADSR)   
1 - Per.GPE, apuração dos dias por meio do período do SIGAGPE  
2 - Per.PON, apuração dos dias por meio do período do SIGAPON  
3 - Tab.PON, apuração dos dias por meio da tabela de Horário Padrão do SIGAPON   
  
Observação: **a opção 3 será avaliada pelo sistema** somente quando as horas do trabalhador Horista estiverem sendo apuradas conforme a tabela de Horário do Ponto Eletrônico - Mnemônico P\_LDSRHRSP com valor .T.  
  
Maiores informações sobre o mnemônico P\_NDSRHORI podem ser obtidas no TDN no *link* abaixo:  
*Link*: reduzido: <http://tdn.totvs.com/x/Fp9SDg> 

**Saiba Mais**  
[TVKTW6\_DT\_Mnemonico\_PNDSRHORI\_Apuracao\_DSR\_e\_Horas\_Normais\_Horistas](https://tdn.totvs.com/display/public/PROT/TVKTW6_DT_Mnemonico_PnDSRHori_Apuracao_DSR_e_Horas_Normais_Horistas#exemplo-3)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
