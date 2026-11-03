---
article_id: 4409778078999
category: esocial - Periódicos
content_hash: af241c7fb999f87ae8376c933e7a2b1874bcacde5ff4000d6368a5cd2fcab42c
fetched_at: '2026-06-28T22:47:09.277964+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 267 ao transmitir S-1200: Rubrica incompatível
  com Estagiário'
type: support-article
updated_at: '2025-07-02T16:59:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409778078999-RH-RM-FOP-eSocial-Erro-267-ao-transmitir-S-1200-Rubrica-incompat%C3%ADvel-com-Estagi%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24482229736855) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao realizar a transmissão do S-1200, o sistema apresenta o erro: **267 - Rubrica incompatível com Estagiário.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28859582041111)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**A inconsistência é retornada pelo RET (governo) quando no evento S-1200 do estagiário é informada uma rubrica/verba (S-1010) cujo código de incidência tributária de contribuição previdenciária (**codIncCP**) ou código de incidência tributária de FGTS (**codIncFGTS**) seja diferente de **00** - **Não é Base de Cálculo**.  
  
**Solução**Verifique na mensagem de erro qual a rubrica listada como incompatível. O código da rubrica estará no formato **#39;código da rubrica#39;**. No *print* utilizado no item **Ocorrência**, por exemplo, o código da rubrica é 0200. Acesse o portal do eSocial (eSocial Web) e pesquise pela verba nas **Tabelas de Rubrica**. Certifique-se que os campos **Incidência CP** e **Incidência FGTS** estejam com valor **00**.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410001411223)

Caso os campos estejam com valor diferente de **00**, deve-se alterar o S-1010 da verba para correção da incidência. Para isso, siga os passos abaixo:

1. No TOTVS Folha de Pagamento, acesse o menu **Administração de Pessoal | Eventos** e edite a verba deseja;  
1.1. Verifique na aba **Inc. Proventos** ou na **Inc. Descontos** se há alguma incidência marcada para a verba. Caso afirmativo, remova;  
2. Caso tenha realizado alterações no evento, será gerado um gatilho na **Fila de Eventos** do eSocial. Caso não tenha alterado a verba, insira o gatilho manualmente clicando no botão **Incluir** da fila;  
2.1. Faça a edição do gatilho da verba e no campo **Competência** informe o mês e ano a partir do qual o governo deverá validar aquela incidência. O mês e ano deverá ser **igual ou anterior** ao período de apuração do S-1200 enviado;

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410001643927)

2.2. Salve o gatilho, gere o XML e transmita para o governo. Após o S-1010 ser aceito pelo RET, transmita novamente o S-1200.

**Importante**  
Algumas verbas possuem **codIncCP** e **codIncFGTS** gerados conforme o seu código de cálculo. Sendo assim, caso esteja utilizando alguma verba com código de cálculo no pagamento, verifique no mapeamento do S-1010 se esse código gera automaticamente alguma incidência.  
  
**Saiba Mais**Para mais informações, acesse:   
     - [Mapeamento dos eventos eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679)  
     - [Admissão de estagiários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015767591-RM-eSocial-Admiss%C3%A3o-de-estagi%C3%A1rios)  
     - [Onde informar a natureza de rubrica eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403023133719)  
     - [MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)
