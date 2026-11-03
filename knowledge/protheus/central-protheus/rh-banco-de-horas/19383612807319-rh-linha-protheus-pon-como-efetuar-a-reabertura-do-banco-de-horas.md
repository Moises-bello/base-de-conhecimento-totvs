---
article_id: 19383612807319
category: RH - Banco De Horas
content_hash: 74b244017f18342300afa398df9127c320a5a87d02f2851f8196350074fd7aae
fetched_at: '2026-06-28T22:44:54.204792+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar a reabertura do banco de horas
type: support-article
updated_at: '2025-09-08T19:17:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19383612807319-RH-Linha-Protheus-PON-Como-efetuar-a-reabertura-do-banco-de-horas
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34789876846103) Tempo aproximado para leitura: 00:02:00 min**  
Dúvida**Como efetuar a reabertura do **Banco de Horas?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para configuração e liberação da rotina de reabertura de **Banco de Horas**, siga as orientações abaixo:  
  
**1.** Foi disponibilizada a rotina PONM100 que permite realizar a Reabertura do Banco de Horas para os eventos que foram baixados dentro do período de apontamento atual. Ou seja, só poderá ser realizado a reabertura com a condição de que o período de apontamento ainda esteja aberto.  
  
Para utilizar deverá seguir com os passos abaixo:  
  
Acesse o Configurador e siga no caminho: Ambiente - Cadastros - Menus e marque apenas o módulo de Ponto Eletrônico:  
![](https://tdn.totvs.com/download/attachments/515294516/image2019-9-20_12-35-3.png?version=1&modificationDate=1568993704757&api=v2)  
  
Clique em Adicionar para enviar todos os menus do Ponto Eletrônico para a direita:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32616539222295)

Clicar no menu em que deseja que a rotina seja incluída e selecionar **Novo Item**.  
(A rotina pode ser incluída em qualquer menu; a imagem abaixo é apenas um exemplo).

**Caminho de exemplo:** Miscelânea → Fechamentos![](https://centraldeatendimento.totvs.com/hc/article_attachments/32616526556311)

Ao clicar em Novo Item faça conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32616539231383)  
  
Clicar em ok e gerar o MENU, preencha a opção abaixo e gerar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32616539233687)  
  
Com o MENU gerado ao acessar o módulo 16-SIGAPON e ir no caminho da rotina de Reabertura do Banco de Horas, PONM100, será apresentada uma tela onde é possível selecionar os parâmetros para o filtro dos funcionários que serão processados. Segue exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19383633282967)

Após preencher os parâmetros desejados e confirmar, o sistema apresenta todas as informações conforme a tela abaixo:

1- Funcionários selecionados com base nos parâmetros informados;  
  
2- Eventos do banco de horas com o **Status** **Baixado** e com a **Data** de **Baixa** dentro do período de apontamento atual; Após o processamento os eventos selecionados serão alterados, o campo Status e Data de Baixa ficarão em branco.  
  
3- Verbas geradas nos Resultados do Ponto ao realizar o fechamento do banco de horas, são apresentadas apenas as verbas que estiverem vinculadas aos eventos do ponto com os IDs 023A, 024A e 042A; As Verbas selecionadas serão excluídas dos resultados.  
  
4- Verbas que foram integradas para a folha de pagamento e estão no Lançamento Mensal, tabela RGB; São apresentadas apenas as verbas que estiverem vinculadas aos eventos do ponto com os IDs 023A, 024A e 042A; As Verbas selecionadas serão excluídas do lançamento mensal.

![Tela com as informações que serão alteradas na rotina de reabertura do banco de horas](https://tdn.totvs.com/download/attachments/747318086/image2023-3-24_15-37-6.png?version=1&modificationDate=1679683023973&api=v2&effects=drop-shadow "Tela com as informações que serão alteradas na rotina de reabertura do banco de horas")  
 **Dica:**É possível marcar e desmarcar os Funcionários, Eventos e Verbas que deseja alterar.

Ao marcar/desmarcar um funcionário as demais tabelas também serão marcadas/desmarcadas.  
Caso o funcionário esteja desmarcado não será possível selecionar os Eventos e Verbas daquele funcionário.

Ao clicar em confirmar o sistema irá gravar as alterações na tabela do Banco de Horas, SPI, e excluir os registros selecionadas das tabelas de resultados e Lançamentos Mensais, SPB e RGB.  
Será apresentado um Log com as alterações que foram realizadas:  
![Log com o resumo das alterações realizadas pela rotina.](https://tdn.totvs.com/download/attachments/747318086/image2023-3-24_15-52-21.png?version=1&modificationDate=1679683938337&api=v2&effects=drop-shadow "Log com o resumo das alterações realizadas pela rotina.")

Caso o funcionário não tenha dados nas tabelas de Banco de Horas, Resultados e Lançamentos mensais, ou a data da baixa esteja fora do período de apontamento aberto ao selecionar essa matricula nos parâmetros sistema vai gerar uma mensagem de Help.   
![](https://tdn.totvs.com/download/attachments/747318086/image2023-4-3_17-29-17.png?version=1&modificationDate=1680553757773&api=v2&effects=drop-shadow)  
  
**Saiba mais**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[Reabertura do Banco de Horas](https://tdn.totvs.com/pages/releaseview.action?pageId=747318086)[RH - Linha Protheus - PON - Configuração para que as horas sejam apuradas no Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013674751-RH-Linha-Protheus-PON-Configura%C3%A7%C3%A3o-para-que-as-horas-sejam-apuradas-no-Banco-de-Horas?source=search)[MP - PON - Como cadastrar os eventos para Folha de Pagamento ou Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532-MP-PON-Como-cadastrar-os-eventos-para-Folha-de-Pagamento-ou-Banco-de-Horas?source=search)  
[MP - PON - Banco de Horas não é calculado e não grava registro na tabela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047548594-MP-PON-Banco-de-Horas-n%C3%A3o-%C3%A9-calculado-e-n%C3%A3o-grava-registro-na-tabela)  
[RH - Linha Protheus - PON - Forma correta de cadastro para valorizar evento de Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058922053-RH-Linha-Protheus-PON-Forma-correta-de-cadastro-para-valorizar-evento-de-Banco-de-Horas)
