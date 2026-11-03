---
article_id: 4409231317399
category: esocial - Periódicos
content_hash: 8f93f308ac8da90129bfb373bc790264548b807a5086303b71ba4ca2f3eb61fe
fetched_at: '2026-06-28T22:47:09.342077+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro código 272: A inscrição informada deve ser
  o CPF do empregador, caso de empregador doméstico, ou ser um estabelecimento do
  empregador devidamente cadastrado no sistema no período'
type: support-article
updated_at: '2025-12-29T14:43:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409231317399-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-272-A-inscri%C3%A7%C3%A3o-informada-deve-ser-o-CPF-do-empregador-caso-de-empregador-dom%C3%A9stico-ou-ser-um-estabelecimento-do-empregador-devidamente-cadastrado-no-sistema-no-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24227775110167) Tempo aproximado para leitura: **00:03:30 min**  
  
**Ocorrência**  
Ao realizar a transmissão dos eventos de periódicos ou não periódicos ocorre o erro: **272 - A inscrição informada deve ser o CPF do empregador, caso de empregador doméstico, ou ser um estabelecimento do empregador devidamente cadastrado no sistema no período**.

![](https://totvssuporte.zendesk.com/attachments/token/l3DKpGvaf5u3yHko630lJt1Ho/?name=inline1084283228.png)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todos as versões  
  
**Causa**  
O erro geralmente é apresentado quando não é localizado no governo um S-1005 com número de inscrição vigente no período correspondente ao evento a ser enviado.

Exemplo: Transmissão de um S-1200 do período de apuração 09/2021 cujo grupo **ideEstabLot** tenha como **nrInsc** o valor 112233445566. No governo, não existe S-1005 com **nrInsc** (grupo **ideEstab**) com valor 112233445566 ou o S-1005 com o correto **nrInsc** possui início de validade posterior à 09/2021 (período de apuração do S-1200) enviado. Neste caso, o governo retornaria o erro **272** supracitado.  
  
**Solução**  
Para solucionar o erro 272, primeiramente, deve-se avaliar o **nrInsc** do evento a ser transmitido conforme relacionamento deste evento com o S-1005;

* S-1005: Campo **nrInsc** do grupo **ideEstab**
* S-1200/S-1202/S-2299 e S-2399: Campo **nrInsc** do grupo **ideEstabLot**
* S-2200 e S-2205: Campo **nrInsc** do grupo **localTrabGeral**

A partir daí, temos a seguintes cenários:

**Não existe nenhum S-1005 com nrInsc correspondente na fila de eventos**

1. Não existindo o S-1005 para o **nrInsc** devido, deve-se gerá-lo através do processo de gatilhos iniciais acessando o menu **eSocial | Gerar Gatilhos Eventos Iniciais** e selecionando o registro S-1005;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409391896983)

2. Gere o XML do S-1005 e transmita para o governo. Após o S-1005 ser aceito pelo RET, transmita novamente o evento posterior desejado.

**Existe o S-1005 correspondente na Fila de Eventos**

Existindo S-1005 com **nrInsc** correspondente ao evento enviado, deve-se então verificar se a data de validade do S-1005 engloba o período do evento a ser transmitido. Para isso, siga os passo abaixo:

1. Considerando a data de admissão do funcionário para o S-2200, a data de alteração para S-2206 e o período de apuração para os eventos periódicos, verifique se no S-1005 a tag **iniValid** é igual ou anterior à data do evento correspondente. **Exemplo**: S-2200 com admissão do funcionário em 01/07/2021. Deve existir então um S-1005 com início de validade igual ou anterior a 07/2021;  
2. Caso não exista S-1005 com validade correspondente, acesse a fila de eventos e inclua um novo registro. Preencha as informações do tipo do evento, operação, seção, etc. e antes de salvar, altere a informação do campo **Competência** com o mês e ano desejado. Para o nosso exemplo, o mês e ano necessário é 07/2021. Salve o registro;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409386720407)

3. Gere o XML do gatilho incluído e transmita para o governo. Após o S-1005 ser aceito pelo RET, transmita novamente o evento posterior desejado.

**Saiba Mais**  
Para saber mais consulte os links abaixo:   
     - [eSocial | RM - Entregas Legais](https://tdn.totvs.com/display/public/LRM/eSocial+%7C+RM+-+Entregas+Legais)   
     - [MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
     - [Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
