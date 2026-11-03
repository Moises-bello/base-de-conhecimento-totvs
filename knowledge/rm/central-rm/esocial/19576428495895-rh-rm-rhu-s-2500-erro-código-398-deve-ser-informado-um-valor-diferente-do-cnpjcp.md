---
article_id: 19576428495895
category: eSocial
content_hash: 425c00ed7b0a80d12b831bfc16b9a782ce89585c0cbb0603bff147713fc00a8f
fetched_at: '2026-06-28T22:47:15.351073+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2500: Erro código 398: Deve ser informado um valor diferente
  do CNPJ/CPF do empregador. Localização: /eSocial/evtProcTrab/ideEmpregador/ideResp/nrInsc'
type: support-article
updated_at: '2024-09-27T19:28:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19576428495895-RH-RM-RHU-S-2500-Erro-c%C3%B3digo-398-Deve-ser-informado-um-valor-diferente-do-CNPJ-CPF-do-empregador-Localiza%C3%A7%C3%A3o-eSocial-evtProcTrab-ideEmpregador-ideResp-nrInsc
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19576428408855) Tempo aproximado para leitura: **00:01:15 min****Dúvida**Ao gerar o XML do evento S-2500 aparece a mensagem de erro: **Erro código 398: Deve ser informado um valor diferente do CNPJ/CPF do empregador. Localização: /eSocial/evtProcTrab/ideEmpregador/ideResp/nrInsc.** O que fazer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155** e superiores.  
  
**Solução**De acordo com o layout disponibilizado pelo eSocial, o campo '**Número de inscrição**' - **guia Identificação do processo, disponível no cadastro do Processo Trabalhista** -  deve ser preenchido com as **Informações de identificação do contribuinte (responsável direto),** caso tenha havido imposição de responsabilidade indireta: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/26679521136023)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19576387883927)**Sendo realmente um processo cujo tenha havido imposição da responsabilidade é indireta, os campos **Tipo inscrição** e **Número de inscrição** devem ser preenchidos com os dados do empregador direto, responsável pelo reclamante, ou seja, diferente do CNPJ/CPF de sua Organização.  
Caso **não** se trate de um processo cujo a responsabilidade é indireta, os campos **Tipo inscrição** e **Número de inscrição** **não** devem ser preenchidos.  
  
**Importante**  
Deve ser um identificador válido e:  
a) Se [ideResp/tpInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideEmpregador_ideResp_tpInsc) = [1], deve ser informado com 14 (catorze) algarismos. Se o empregador for pessoa jurídica, a raiz do CNPJ informado deve ser diferente de [ideEmpregador/nrInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideEmpregador_nrInsc), exceto se [ideEmpregador/nrInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideEmpregador_nrInsc) tiver 14 (catorze) algarismos.  
b) Se [ideResp/tpInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideEmpregador_ideResp_tpInsc) = [2], deve ser diferente do CPF do trabalhador. Se o empregador for pessoa física, também deve ser diferente do CPF do empregador.  
  
**Saiba mais**Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543-RH-RM-RHU-eSocial-Processos-Trabalhistas-Perguntas-e-respostas-do-evento-webinar)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783-RH-RM-RHU-eSocial-S-2500-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2500)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855-RH-RM-RHU-eSocial-S-2501-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2501)
