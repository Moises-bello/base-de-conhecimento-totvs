---
content_hash: 24beb2c0191c848ebafe2ed4f94f7bfd5788f6b67b48cc1c7a936c1b560dd7df
fetched_at: '2026-06-29T00:11:56.661217+00:00'
page_id: '867823930'
product: rm
source: tdn-rm
title: Utilitários - Portal/App - Notificações de Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867823930
version: 7
---

A ferramenta de envio de **Notificações de Atendimentos** notifica aos Clientes sobre a abertura e/ou novas discussões em atendimentos, diretamente no aparelho onde está instalado o app *[Meu Imóvel](https://tdn.totvs.com/pages/viewpage.action?pageId=640205520#tudo-sobre-Introducao)*.

Esta ferramenta visa melhorar a satisfação dos Clientes, reduzindo o número de contatos dos mesmos com a incorporadora, que antes eram necessários para confirmar o recebimento e andamento dos atendimentos.

Em sua execução, este processo verifica as seguintes parametrizações:

* **Para configurar o envio de notificações de *novos atendimentos***:
  + No cadastro de [Tipo de Atendimento](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI): valida a opção *Permite notificações push da abertura de atendimento pelo atendente.*

Neste cenário, será enviada a notificação apenas na abertura do novo atendimento sendo que, mesmo que no decorrer da análise do atendimento, o atendente marque para publicar a discussão no fórum, a notificação da inserção desta discussão não será enviada ao app do Cliente.

* **Para configurar o envio de notificações sobre novas discussões**:
  + No cadastro de [Tipo de Atendimento](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI): valida a opção *Permite notificações push da inclusão de uma discussão atendente*; e
  + Na tela de [edição do Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=732662538): valida a opção *Publicar discussão no fórum*.

Neste cenário, a notificação só será enviada caso as duas condições acima sejam atendida. Caso o Atendente insira uma discussão e queira que ela seja apenas interna, basta não marcar a opção para publicar no Fórum.

Caso necessário, ambas opções de envio acima podem ser marcadas, para melhorar a experiência com o Cliente.

* **Para enviar as notificações no APP meu imóvel:**Favor seguir esse caminho para acessar a tela, **Utilitários > Parametrizações do App > Notificações de atendimentos**, depois execute o processo para que seja enviada as notificações.

**Na tela de execução desta funcionalidade, o sistema exibe as orientação abaixo:**

*Serão enviadas notificações para novos atendimentos e novas discussões cuja a data de criação do atendimento ou da discussão seja igual a data atual.*

*Cada novo atendimento e discussão só terá notificações geradas uma única vez.*

Importante!

Recomendamos que sejam realizados pelo menos dois **agendamentos** diários deste envio de notificações de atendimento, uma vez que, conforme informado acima, este processo não enviará as notificações de atendimentos publicadas em datas anteriores à data de sua execução. Um desses agendamentos pode ser executado imediatamente após o término do expediente, não sendo recomendado a execução do mesmo ao final do dia, para não gerar nenhum incômodo aos Clientes.

Por questões de performance, caso algum atendimento tenha mais de uma discussão publicada, o sistema enviará uma única notificação ao cliente a cada execução, evitando assim, além do processamento de dados desnecessários, que o este receba notificações em excesso.

Caso o Cliente tenha o app *[Meu Imóvel](https://tdn.totvs.com/pages/viewpage.action?pageId=640205520#tudo-sobre-funcionalidades-interfaces)* instalado em mais de um aparelho, o sistema enviará as notificações apenas para o aparelho no qual ele fez o login mais recente.
