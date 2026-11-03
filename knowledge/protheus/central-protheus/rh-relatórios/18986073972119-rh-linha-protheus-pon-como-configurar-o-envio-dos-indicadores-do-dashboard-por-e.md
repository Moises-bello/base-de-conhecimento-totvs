---
article_id: 18986073972119
category: RH - Relatórios
content_hash: 76b5bf9c12515934d67f99bd22e73277058e6b63416adf4986b2aa9500b9660e
fetched_at: '2026-06-28T22:44:43.430582+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Como configurar o envio dos indicadores do Dashboard
  por email
type: support-article
updated_at: '2025-10-08T14:23:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18986073972119-RH-Linha-Protheus-PON-Como-configurar-o-envio-dos-indicadores-do-Dashboard-por-email
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18986060608919) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como configurar o envio dos indicadores do *Dashboard* por e-mail?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**No ***Dashboard*** temos a opção de tirar uma fotografia dos indicadores e enviar por e-mail, mas para que o *e-mail* seja enviado corretamente, são necessárias algumas configurações, como por exemplo, o servidor de e-mail, endereço do servidor, usuário, senha e etc.  
  
Para realizar as configurações, é necessário acessar o módulo **Configurador (SIGACFG)**, acessar a rotina **Ambiente > E-mail/proxy > Configurar.**Preencha os campos conforme o servidor de e-mail que será utilizado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18986369931543)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18986360689815)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19040978044823)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19041029174039)

Após a configuração do *e-mail*, deve ser preenchido o conteúdo do parâmetro **MV\_GPEMAIL**, este parâmetro será responsável por armazenar o destinatário do *e-mail* contendo as informações do *Dashboard.*Se o parâmetro MV\_GPEMAIL não estiver preenchido, o sistema irá utilizar o **MV\_RELAUSR**.   
Caso nenhum dos parâmetros sejam preenchidos, o sistema não irá enviar o e-mail.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18986369950871)

Após a atualização dos indicadores, é possível enviar os dados clicando no botão **Enviar *E-mail.*** Se as configurações mencionadas acima estiverem corretas, será enviado um *e-mail* para o destinatário definido no parâmetro **MV\_GPEMAIL**.   
  
Para enviar os indicadores por e-mail, deverá gerar os indicadores via módulo do **Ponto Eletrônico(SIGAPON)**, acessando a rotina rotina Dashboard **(PONA480) em Relatórios > Mensal > Dashboard.**Para o envio do *e-mail* todos os indicadores deverão ter sido carregados, caso exista qualquer indicador sendo carregado, o *e-mail* não será enviado e apresentará a seguinte mensagem:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19041236356375)  
  
Ao gerar e carregar os indicadores em tela com sucesso, basta clicar no botão Enviar E-mail, veja exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19111612781207)  
  
Após clicar em enviar E-mail, veja abaixo um exemplo do *e-mail* enviado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19040478942743)  
  
Será encaminhado em anexo no e-mail a Imagem seguinte:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19040478949015)  
  
  
  
**Saiba mais:**[RH - Linha Protheus - PON - Como utilizar o Dashboard do Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19054544447639-RH-Linha-Protheus-PON-Como-utilizar-o-Dashboard-do-Ponto-Eletr%C3%B4nico?source=search)[Dashboard Ponto Eletrônico](https://tdn.totvs.com/display/public/PROT/SIGAPON+-+Dashboard+Ponto%20Pacote%20de%20Expedi%C3%A7%C3%A3o%20Cont%C3%ADnua%20Acumulado%20de%20RH)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
