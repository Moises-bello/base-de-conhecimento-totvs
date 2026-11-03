---
article_id: 18701717777175
category: Meu RH - Gestão de Comunicados e Push Notification
content_hash: d2909e6cbd82012481eb2bb09a56cbf273c63a6a6c5410966c99f3d4e8a64826
fetched_at: '2026-06-28T22:47:26.594443+00:00'
product: rm
section_id: 37779496229783
source: central-rm
title: RH - RM - Meu RH - Como parametrizar o Push Notification no Meu RH
type: support-article
updated_at: '2026-04-13T14:55:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18701717777175-RH-RM-Meu-RH-Como-parametrizar-o-Push-Notification-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18701734167319) Tempo aproximado para leitura: **00:06:30 min**  
  
**Dúvida**  
Como parametrizar e utilizar o Push Notification no Meu RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2310.110

**Solução**  
O Push Notification possibilita enviar notificações para os usuários do Meu RH em seus dispositivos. Estas notificações são comunicados das rotinas contidas no aplicativo do Meu RH, como exemplo a disponibilização do envelope de pagamento.

Para utilizar essa funcionalidade, deverá realizar os seguintes passos:

1. Atualize o aplicativo MEU RH para a **última versão disponível.**  
2. Habilite o recebimento de notificações do aplicativo Meu RH nas configurações do dispositivo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26157654759191)

3. Marque o parâmetro: '**Utiliza push notification**', localizado em: **Folha de Pagamento** > **Configurações** > **Parametrizador** > **Push Notification**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18701726569239)

4. Acesse **Serviços Globais > Segurança > Perfis > Sistema: Folha de Pagamento** e libere as permissões **Push Notification** nas categorias [**11] Configurações** e **[19] Portal RH**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39708865938583)

5. Para que a notificação seja enviada corretamente é necessário observar as seguintes regras:

* O usuário deverá ter acessado o aplicativo ao menos uma vez após a atualização do MEU RH, pois através deste acesso será definido um token para o dispositivo;
* Possuir um envelope de pagamento para o colaborador, em que a **data de pagamento seja maior ou igual a data atual ao envio da notificação**;
* A data de pagamento do envelope deve estar compreendida no período definido no parametrizador para exibição do envelope de pagamento, em: **Folha de Pagamento > Configurações > Parametrizador > RM Portal >** ***Edite o quiosque do colaborador*** **> Demonstrativo de Pagamento;**  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703433210391)
* Caso o aplicativo do Meu RH esteja **aberto no momento do envio da notificação**, o usuário não irá receber a notificação, no entanto será mantido o salvamento do log;
* O processo do Gatilho poderá ser agendado, no entanto o agendamento apenas será considerado se estiver utilizando um ambiente em N camadas, caso contrário a notificação será enviada imediatamente;

6. Após realizar as parametrizações, para enviar a notificação para o aplicativo Meu RH, acesse o módulo **Folha de Pagamento > Configurações > Gatilho Envelope de Pagamento.**  
![](https://tdn.totvs.com/download/attachments/799247950/image-2023-10-23_17-36-18.png?version=1&modificationDate=1698093409610&api=v2)

Selecione os funcionários que deverão receber a notificação e informe a data e hora desejada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703450104727)

Será apresentada uma mensagem, indicando que deve ser realizado o lançamento da folha de pagamento, antes de executar o processo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703450111127)

Poderá customizar a mensagem marcando a flag **'Customizar mensagem**', uma vez a flag marcada não será permitido avançar sem preencher o título e subtítulo. Caso a flag esteja desmarcada, será enviado a mensagem padrão do sistema.![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703614561943)

Após preencher a mensagem desejada, selecione a opção **'Avançar'** para execução do processo.

Segue exemplo de notificação no dispositivo:

![image-2023-10-24_7-57-32.png](https://tdn.totvs.com/download/attachments/799247950/image-2023-10-24_7-57-32.png?version=1&modificationDate=1698145084157&api=v2)

**Saiba Mais:**  
Para mais informações, acesse o TDN: [**Push Notification**](https://tdn.totvs.com/display/NPR/Linha+RM)
