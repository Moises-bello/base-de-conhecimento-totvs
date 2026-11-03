---
article_id: 21744068792471
category: eSocial
content_hash: 17989adfc8b91c42160dd559894121a4db13e218fcd10e2d2d8f201d1ac412a5
fetched_at: '2026-06-28T22:47:39.053633+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2240: Em caso de agente nocivo incluído por determinação
  administrativa ou judicial, preencher com o número do processo'
type: support-article
updated_at: '2025-08-21T19:11:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21744068792471-RH-RM-SMT-S-2240-Em-caso-de-agente-nocivo-inclu%C3%ADdo-por-determina%C3%A7%C3%A3o-administrativa-ou-judicial-preencher-com-o-n%C3%BAmero-do-processo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21744068750615) Tempo aproximado para leitura: **00:01:57 min** **Dúvida**Ao gerar o XML do evento S-2240 é exibida a mensagem de erro: **Campo de preenchimento obrigatorio: Em caso de agente nocivo incluido por determinacao administrativa ou judicial, preencher com o numero do processo. Localização: /eSocial/evtExpRisco/infoExpRisco/agNoc/nrProcJud**. O que fazer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - 12.1.34.263, 12.1.2205.211, 12.1.2209.155 e superiores.  
  
**Solução**

A partir do Leaiute S-1.2, o campo **nrProcJud** passou a ser obrigatório de preenchimento se o código de agente nocivo for igual a [05.01.001]:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34353364864151)  
  
Sendo assim, valide se para este código de agente nocivo que informou, existe um processo judicial para que possa inserir neste campo no XML.  
  
Caso exista, deverão atualizar o sistema para uma das versões abaixo, pois foram nestas que o desenvolvimento incluiu o campo de **Número de Processo** no cadastro da Avaliação de Risco.

* *12.1.2302.268*
* *12.1.2306.230*
* *12.1.2310.170*
* *12.1.2402.110*
* *12.1.2406*

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/22702765559063)***Após atualização da biblioteca, deve atualizar os scripts pendentes através do **RM.Atualizador.exe**: [RH - RM - FOP - RM Atualizador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5893403025687)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21832482407319)

Caso contrário, e não tenha um processo judicial para que possa informar ao utilizar este código, deverá avaliar os códigos existentes na tabela 24 e alterar este tipo de agente nocivo para os riscos mapeados ao funcionário.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21745143552407)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21745087798039)

**Importante**  
Caso precise de orientação para saber qual código da tabela 24 do eSocial deve ser vinculado ao Tipo de Agente cadastrado no seu sistema, valide essa informação com o time de SESMT ou com o Responsável pelos Registros Ambientais da sua empresa.  
  
**Saiba Mais**  
Para acessar a tabela 24 e consultar os Agentes Nocivos disponíveis atualmente, acesse:

* [Tabela 24 - Agentes Nocivos e Atividades](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/tabelas.html#24)
