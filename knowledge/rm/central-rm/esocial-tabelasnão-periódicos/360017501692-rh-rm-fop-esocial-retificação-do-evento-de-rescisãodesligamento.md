---
article_id: 360017501692
category: eSocial - Tabelas/Não Periódicos
content_hash: a56c2544c7cd98a99a93d79c4ab2fe3b08397efcb40c2d29c2748934cd0df0a3
fetched_at: '2026-06-28T22:47:10.568063+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP- eSocial - Retificação do evento de rescisão/desligamento
type: support-article
updated_at: '2026-03-12T00:10:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017501692-RH-RM-FOP-eSocial-Retifica%C3%A7%C3%A3o-do-evento-de-rescis%C3%A3o-desligamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20822371414295)** **Tempo aproximado para leitura:****00:02:00 min**

**Dúvida**  
Como gerar retificação (dissídio **não**) dos eventos de desligamento S-2299 / S-2399?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Existem duas formas de realizar a retificação do desligamento:

1. [Retificação gerada pela **Fila de Eventos**](http://tdn.totvs.com/pages/viewpage.action?pageId=417700835#1-1) - quando a alteração no movimento da rescisão já foi realizada, porém precisa enviar um evento de retificação;  
2. Retificação gerada pelo Cálculo de **Rescisão Complementar** - quando a alteração no movimento da rescisão ainda precisa ser realizada.

O cenário para retificação também irá influenciar a forma de realizar o processo, sendo:

**Retificação na mesma competência da Rescisão**

1. Acesse **Rescisão | Complementar** e preencha os dados da rescisão complementar;  
2. Selecione **Não** no parâmetro **Dissídio/Convenção/Acordo Coletivo**;  
3. Ao avançar a tela, informe os eventos que serão inseridos na retificação.

Realizando os passos acima, o sistema irá lançar as verbas informadas no mês da rescisão do funcionário. Assim, deverá enviar:  
   • Um **S-2299** de retificação (gerar a [retificação da rescisão através da Fila de Eventos](https://tdn.totvs.com/pages/releaseview.action?pageId=697266588));  
   • Um **S-1210** do período da rescisão.

**Retificação em competência posterior à Rescisão**

**•** Parametrização [sem lançamento de líquido de retificação](https://tdn.totvs.com/pages/releaseview.action?pageId=498701193)

1. Acesse o menu **Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/7** ;  
1.1. Cadastre o **Período Inicial** da **Retificação folha/rescisão** que será apresentado na tela do processo de rescisão complementar. O valor deve ser entre 10000 e 30000;  
1.2. Selecione o parâmetro **Não lançar Líquido de Retificação no Envelope da Competência Atual**;  
2. Acesse **Rescisão | Complementar** e preencha os dados da rescisão complementar;   
2.1. Selecione **Não** no parâmetro **Dissídio/Convenção/Acordo Coletivo** e marque o parâmetro **Retificar rescisão** informando o período do lançamento**;**  
2.2. Ao avançar a tela, informe os eventos que serão inseridos na retificação.

Realizando os passos acima, o sistema irá criar um novo período na competência da rescisão de acordo com o período de lançamento parametrizado. Neste período será lançado o evento a serem retificados com data de pagamento atual. Assim, será gerado:  
   • Um **S-2299** de retificação do período da rescisão;  
   • Um **S-1210** do período atual.

• Parametrização [com lançamento de líquido de retificação](https://tdn.totvs.com/pages/releaseview.action?pageId=417700835)

1. Acesse o menu **Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/7** ;  
1.1. Cadastre o **Período Inicial** da **Retificação folha/rescisão** que será apresentado na tela do processo de rescisão complementar. O valor deve ser entre 10000 e 30000;  
1.2. Desmarque o parâmetro **Não lançar Líquido de Retificação no Envelope da Competência Atual**;  
2. Acesse **Rescisão | Complementar** e preencha os dados da rescisão complementar;   
2.1. Selecione **Não** no parâmetro **Dissídio/Convenção/Acordo Coletivo**;  
2.2. Ao avançar a tela, informe os eventos que serão inseridos na retificação.

Realizando os passos acima, o sistema irá criar um novo período na competência da rescisão de acordo com o período de lançamento parametrizado. Neste período será lançado o evento a ser retificado com data de pagamento da competência original. Também seria gerado na competência atual as verbas vinculadas ao líquido da retificação, que terá data de pagamento atual. Assim, será gerado:  
   • Um **S-2299** de retificação do período da rescisão;  
   • Um **S-1210** do período da rescisão;  
   • Um **S-1200** do período atual com o Tipo F (deve ser gerado **manualmente** através do menu **eSocial | Gerar XML (Eventos Periódicos)**;  
   • Um **S-1210** do período atual (deve ser gerado **manualmente** através do menu **eSocial | Gerar XML (Eventos Periódicos).**

**Importante**  
Realizando o processo sem o lançamento do líquido, todos os processos de Folha como contabilização, SEFIP, lançamento financeiro, CNAB etc. deverão ser gerados na competência da rescisão;

Sempre que um evento **S-2299** for retificado e, consequentemente, seu **líquido for alterado**, deve-se **excluir o S-1210** enviado anteriormente e enviar um novo S-1210 com o líquido atualizado;

Quando a coligada trabalhar com tomador de serviços e, o lançamento da retificação for fora da competência, é necessário **Distribuir SEFIP marcando a*****flag*****Distribuição Somente de Retificação.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26081300640279)
