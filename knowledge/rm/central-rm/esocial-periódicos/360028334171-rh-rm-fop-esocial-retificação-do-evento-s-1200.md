---
article_id: 360028334171
category: esocial - Periódicos
content_hash: c0a78fb79c17b9e3357811c3f11ef8a6dbc33c08d2f8231a3bca7357b4dad66b
fetched_at: '2026-06-28T22:47:09.473218+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Retificação do evento S-1200
type: support-article
updated_at: '2024-12-02T12:13:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028334171-RH-RM-FOP-eSocial-Retifica%C3%A7%C3%A3o-do-evento-S-1200
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20822312653079) Tempo aproximado para leitura: **00:02:00 min****

**Dúvida**Como realizar a retificação do evento **S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social**?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões

**Solução**  
 Segundo o Manual de Orientações do eSocial, a retificação de um evento **S-1200** somente será aceita se houver correspondência com o valor líquido informado no **S-1210**. Assim, caso haja desconformidade de valor, impõe-se excluir o **S-1210** antes da retificação do **S-1200**. Além disso, devemos considerar se a retificação será realizada na competência atual ou em competências já liberadas no sistema.   
Após os ajustes da folha ou das informações que serão retificadas, siga os passos abaixo para cada uma das situações:  
  
• Retificação sem alteração do líquido  
      1. Acesse **eSocial | Eventos Periódicos** e selecione o evento **S-1200** a ser retificado;  
      2. Clique em **Processos | Gerar Retificação Arquivo eSocial**. Será incluído um novo registro na fila com tipo de operação **Retificação.**  
  
• Retificação em [competência atual](http://tdn.totvs.com/pages/viewpage.action?pageId=491459434)  
      1. Acesse **eSocial | Eventos Periódicos** e selecione o evento **S-1210** correspondente ao **S-1200** a ser retificado;  
      2. Clique em **Processos | Gerar Evento de Exclusão (S-3000)**;  
      3. Após transmissão do **S-3000** e aceite pelo governo, acesse novamente **eSocial | Eventos Periódicos** e selecione o **S-1200** a ser retificado;  
      4. Clique em **Processos | Gerar Retificação Arquivo eSocial**. Será incluído um novo registro na fila com tipo de operação **Retificação**;  
      5. Acesse **eSocial | Gerar XML** (Eventos Periódicos) e execute o processo selecionando o período de apuração desejado e o evento **S-1210**;  
  
• Retificação em [competência anterior](http://tdn.totvs.com/pages/releaseview.action?pageId=438289252)  
      1. Acesse o menu **Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/5** e no campo **Retificação folha/rescisão** informe o número de um período que será utilizado para a inclusão das verbas retificadas. O valor deve ser entre 10000 e 30000;  
      2. Acesse o menu **Folha Mensal | Lançamentos | Retificação da Folha de Pagamento;**   
      2.1. Selecione a chapa, mês, ano e período que deverá ser retificado. Selecione também o **Período lancto. retificação**, que corresponde ao período que será criado no envelope com as verbas retificadas;  
      2.2. Avance a tela e cadastre o(s) evento(s) que deseja incluir ou alterar no período selecionado. Caso o evento já exista no envelope de pagamento, este será incluído com o comportamento de adicionar valor, ou seja, se um evento de **Hora Extra 100%** está no envelope com referência 10 horas e o correto seria 15 horas, basta informar na retificação o evento com referência 5 horas;  
      3. Ao fim do processo, serão gerados os eventos **S-1200** e **S-1210** de retificação no mês e período de lançamento selecionados no passo 2.1.  
  
**Importante**  
A [distribuição do tomador de serviço](http://tdn.totvs.com/display/LRM/Distribuir+SEFIP) deverá ser feita para o período retificado.  
Para a retificação em competências anteriores, o sistema fará o cálculo dos valores de INSS conforme tabela da época e o cálculo do rateio do centro de custo será feito conforme o rateio atual informado no cadastro do funcionário.
