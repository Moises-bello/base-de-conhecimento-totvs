---
content_hash: 02783d159b4f3efe4736c5be4dd8cc0a4a73ee52ffe06d7b04b2035b155262ed
fetched_at: '2026-06-29T00:09:13.346501+00:00'
page_id: '419547656'
product: rm
source: tdn-rm
title: RMFIN00002_Cartão de Crédito - Configurações do CheckOut da Cielo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=419547656
version: 18
---

**Configurações do CheckOut**

Visando **bom funcionamento** da modalidade CheckOut no pagamento com cartão de crédito pela operadora CIELO, é necessário seguir algumas orientações importantes recomendadas pela operadora:

* O servidor de recebimento de Post deve ter o ***IP público***;
* O ***Firewall do Windows*** deve permitir que a rede faça envio e recebimento de arquivos;
* O ***Antivírus*** deve ser configurado para não barrar o recebimento de Post.

Para que o **RM** tenha uma boa comunicação com a Cielo é importante que as parametrizações, pastas e configurações dentro do **RM** e do **BackOffice da Cielo** estejam corretas para que não haja perda de dados dos pagamentos efetuados.

No **BackOffice da Cielo**, o link nas configurações devem estar direcionados corretamente para o **Servidor** e para pasta correta dentro do **Corpore.Net** onde se encontra os arquivos de recebimento de ‘*Post*’ de mudança do status.

**Ex**.:

Notificação: <http://138.219.88.92/PortalSQA/Source/Fin-Financeiro/RM.Fin.Lan/CheckoutCielo/FinLanCartaoNotificacao.aspx>

URL status: [http://138.219.88.92/PortalSQA/Source/Fin-Financeiro/RM.Fin.Lan/CheckoutCielo/FinLanCartaoMudancaStatus.aspx](http://138.219.88.92/PortalSQA/Source/Fin-Financeiro/RM.Fin.Lan/CheckoutCielo/FinLanMudancaStatus.aspx)

**A URL é formada por:**

- /Source/Fin-Financeiro/RM.Fin.Lan/CheckoutCielo/FinLanCartaoNotificacao.aspx: Caminho do servidor de aplicação onde está localizado os arquivos de recebimento dos ***Post*s** de transação, como exibido na imagem abaixo:

**E se apresentar erro no momento do pagamento?**

Um dos mais frequentes problemas encontrados na implantação do BackOfice da Cielo  para pagamento pelo portal do Educacional, está relacionado a digitação incorreta das URLs de direcionamento e comunicação com a Cielo, ocasionando  a mensagem de erro como mostra o exemplo a baixo. Neste caso, deve ser verificado se as URLs de comunicação da Cielo estão corretas na parametrização do RM.  Após correção das URLs, deve-se reiniciar o Host.

**Pontos importantes para a comunicação correta entre o *RM* e o *CheckOut*:**

* O caminho informado nas configurações do **BackOffice** não pode estar diferente do caminho na pasta do **Corpore.Net** do servidor. Os arquivos de Mudança e Notificação devem estar dentro da pasta para leitura do *Post*, caso contrário o status do lançamento não será alterado. Estes são criados automaticamente na instalação do portal do EDU;
* No ambientedo **BackOffice** **Cielo**, a opção **‘*Configuração de Captura Automática’*** para **ambiente de teste** não realiza nenhuma ação, podendo ser realizado somente a captura manual selecionando a opção **‘*Nunca fazer a Captura Automática’*** e enviando manualmente o status do pagamento por dentro da parcela utilizando o botão;
* Para o **ambiente de produção** todas as opções de captura funcionam corretamente. Caso alguma das opções não estejam disponíveis, deve ser levado em consideração o contrato do estabelecimento com a Cielo;
* Caso o estabelecimento esteja utilizando a **‘*Captura Automática’*** e o sistema não realizar nenhuma ação sobre a parcela/lançamento, como por exemplo baixa, deve ser verificado os links configurados no **BackOffice Cielo** e o caminho onde se encontram os arquivos de mudança de status. Também deve ser verificado as orientações da Cielo para perfeito funcionamento;
* No caso de não baixar ou cancelar uma transação, também deve ser verificado com a Cielo se o serviço do site de envio do status de pagamento está funcionando corretamente, pois muitas das vezes mesmo que a captura esteja Automática, se o site estiver com instabilidade, o ***Post*** não é enviado nem reenviado automaticamente, causando assim a incompatibilidade de informações entre o **RM** e o **BackOffice Cielo**;
* É necessário que exista um usuário com o código e nome igual a **'rm'** e associar um cadastro de acesso que possua usuário e senha do SGBD com **permissão total** para gravações e alterações no banco de dados.

Atenção: Atualmente a parametrização **“*Gravar arquivo de log quando ocorrer erro no processamento de notificação e mudança de status*”**, não salva os logs em ambiente 3 camadas e Data Center.
