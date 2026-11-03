---
article_id: 4427635287319
category: Integração
content_hash: 9b1357f71c501dfe72d5f452af7316d69c240367313572b1efcd09e9c0ed989f
fetched_at: '2026-06-28T22:46:34.645613+00:00'
product: rm
section_id: 6045439793431
source: central-rm
title: RH - RM - PTO - Importação automática de batidas com integração via Clockin
  (Carol)
type: support-article
updated_at: '2025-02-27T17:52:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427635287319-RH-RM-PTO-Importa%C3%A7%C3%A3o-autom%C3%A1tica-de-batidas-com-integra%C3%A7%C3%A3o-via-Clockin-Carol
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503386650007) **Tempo aproximado para leitura: 00:01:30 min****Dúvida**Como realizar a importação automática de batidas com integração via Clockin (Carol)  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 12.1.29  
  
**Solução**

Para realizar o agendamento da importação automática de batidas no módulo **Automação de Ponto**, siga os passos abaixo:

* Acesse a guia **Entrada de Dados** e selecione a opção **Importar**.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29828397527447)
* Na janela de importação, realize as parametrizações desejadas para o agendamento da importação, como por exemplo selecionar uma opção para o Acerta Natureza. A opção de Utiliza integração com a Carol deve estar marcada e por se tratar de um agendamento, a opção de Considera o último NSR importado também deve ser marcado.   
  Observe que os campos não utilizados (**arquivo para importação, layout do relógio, terminal de coleta, botão de seleção de funcionários que está sem filtro e com todas as opções de situação, tipo e recebimento marcados, e sem uma chapa informada**) **"estão limpos"**.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30286082739863)
* Selecione o tipo de agendamento que deseja executar e quando terminar a parametrização, selecione o botão **Executar**. O job será agendado e iniciará sua execução de acordo com a parametrização realizada.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29828371497367)

**Importante**

* Somente ambientes em 3 camadas é que será possível efetuar agendamentos de job.
* No passo 2 atente-se na configuração para que não tenha nenhum tipo de filtro na tela, como por exemplo filtro na seleção de funcionários, ou mesmo alguma informação nos campos arquivo para importação, layout do relógio, terminal de coleta.
* Com o  parâmetro Considera último NSR importado marcado, a importação irá considerar o último NSR gerado pela Carol e não será permitida a importação por período (seleção de datas).  
  A opção Período de importação ficará desabilitada.
* Ao efetuar o agendamento, serão consideradas para importação as batidas dentro do período Ativo no momento da importação.
* **Para garantir um desempenho satisfatório do agendamento, recomenda-se que a recorrência tenha um intervalo de no mínimo de 1 hora.**

**Saiba mais**Para maiores informações sobre a integração Clockin x RM acesse o [link](https://tdn.totvs.com/pages/viewpage.action?pageId=441821303)  
Para maiores detalhes sobre a tela de recorrência do agendamento, acesse o link [recorrência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007124831-RM-Frame-Tipo-de-recorr%C3%AAncia-da-tabela-GJOBX)
