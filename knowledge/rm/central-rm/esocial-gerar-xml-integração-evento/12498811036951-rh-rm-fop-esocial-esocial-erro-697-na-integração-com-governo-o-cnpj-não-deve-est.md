---
article_id: 12498811036951
category: eSocial - Gerar XML/ Integração Evento
content_hash: 39a457d3ed3dd7476b55c5bc3108fb5e4085c3197171775f4a8fa022a4829050
fetched_at: '2026-06-28T22:47:13.008934+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - eSocial - Erro 697 na integração com governo:  O
  CNPJ não deve estar cadastrado na Tabela de Estabelecimentos e Obras no período
  especificado'
type: support-article
updated_at: '2026-01-26T16:00:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12498811036951-RH-RM-FOP-eSocial-eSocial-Erro-697-na-integra%C3%A7%C3%A3o-com-governo-O-CNPJ-n%C3%A3o-deve-estar-cadastrado-na-Tabela-de-Estabelecimentos-e-Obras-no-per%C3%ADodo-especificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24038050898327) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao realizar a transmissão de eventos é apresentado a mensagem **Código do erro: 697 Descrição: O CNPJ não deve estar cadastrado na Tabela de Estabelecimentos e Obras no período especificado. Ação Sugerida: O CNPJ informado NÃO deve existir na Tabela de Estabelecimentos e Obras (evento S-1005) no período especificado, favor verificar.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O erro geralmente é apresentado quando não é localizado no governo um S-1005 com número de inscrição vigente no período correspondente ao evento a ser enviado.

**Exemplo:** Transmissão de um S-1200 do período de apuração 09/2021 cujo grupo **ideEstabLot** tenha como **nrInsc** o valor 112233445566. No governo, não existe S-1005 com **nrInsc** (grupo **ideEstab**) com valor 112233445566 ou o S-1005 com o correto **nrInsc** possui início de validade posterior à 09/2021 (período de apuração do S-1200) enviado.   
  
**Solução**  
Para solucionar o erro 272, primeiramente, deve-se avaliar o **nrInsc** do evento a ser transmitido conforme relacionamento deste evento com o S-1005;

* S-1005: Campo **nrInsc** do grupo **ideEstab**
* S-1200/S-1202/S-2299 e S-2399: Campo **nrInsc** do grupo **ideEstabLot**
* S-2200 e S-2205: Campo **nrInsc** do grupo **localTrabGeral**

A partir daí, temos a seguintes cenários:

**Não existe nenhum S-1005 com nrInsc correspondente na fila de eventos**

1. Não existindo o S-1005 para o **nrInsc** devido, deve-se gerá-lo através do processo de gatilhos iniciais acessando o menu **eSocial | Gerar Gatilhos Eventos Iniciais** e selecionando o registro S-1005;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24038086622999)

2. Gere o XML do S-1005 e transmita para o governo. Após o S-1005 ser aceito pelo RET, transmita novamente o evento posterior desejado.  
  
**Existe o S-1005 correspondente na Fila de Eventos**

Existindo S-1005 com **nrInsc** correspondente ao evento enviado, deve-se então verificar se a data de validade do S-1005 engloba o período do evento a ser transmitido. Para isso, siga os passo abaixo:

1. Considerando a data de admissão do funcionário para o S-2200, a data de alteração para S-2206 e o período de apuração para os eventos periódicos, verifique se no S-1005 a tag **iniValid** é igual ou anterior à data do evento correspondente. **Exemplo**: S-2200 com admissão do funcionário em 01/07/2021. Deve existir então um S-1005 com início de validade igual ou anterior a 07/2021;  
2. Caso não exista S-1005 com validade correspondente, acesse a fila de eventos e inclua um novo registro. Preencha as informações do tipo do evento, operação, seção, etc. e antes de salvar, altere a informação do campo **Competência** com o mês e ano desejado. Para o nosso exemplo, o mês e ano necessário é 07/2021. Salve o registro;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24038050910103)

3. Gere o XML do gatilho incluído e transmita para o governo. Após o S-1005 ser aceito pelo RET, transmita novamente o evento posterior desejado.  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
     - [eSocial | RM - Entregas Legais](https://tdn.totvs.com/display/public/LRM/eSocial+%7C+RM+-+Entregas+Legais)   
     - [MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)
