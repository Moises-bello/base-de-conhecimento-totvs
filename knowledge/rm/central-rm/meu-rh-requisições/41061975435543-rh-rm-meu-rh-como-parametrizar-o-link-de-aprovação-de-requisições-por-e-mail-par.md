---
article_id: 41061975435543
category: Meu RH - Requisições
content_hash: 6060ca88d3c858eb28e6b33f679b21cf894291079b8590bb27faaf5fab575a99
fetched_at: '2026-06-28T22:47:28.009928+00:00'
product: rm
section_id: 26902073559319
source: central-rm
title: RH - RM - Meu RH - Como parametrizar o link de aprovação de requisições por
  e-mail para direcionar ao Meu RH
type: support-article
updated_at: '2026-06-09T19:29:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41061975435543-RH-RM-Meu-RH-Como-parametrizar-o-link-de-aprova%C3%A7%C3%A3o-de-requisi%C3%A7%C3%B5es-por-e-mail-para-direcionar-ao-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41061997017367) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como configurar o link de aprovação de requisições enviado por e-mail para que ele direcione o usuário para o portal Meu RH em vez do Corpore RM.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões

**Solução**  
Por padrão, o produto faz com que as mensagens automáticas criadas pelo sistema e disparadas por e-mail aos aprovadores das requisições contenham um redirecionamento somente ao portal Corpore RM.

Para parametrizar o redirecionamento ao portal Meu RH, se faz necessário a criação de uma mensagem customizada e a vinculação desta mensagem customizada criada nos tipos de requisições desejadas.

A opção para criação de mensagens customizadas se encontra dentro do módulo de Gestão de Pessoas, aba Configurações, opção Mensagens Customizadas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41061975410583)

Na tela de Mensagem Customizada são exibidas as mensagens já criadas. Clique no botão Incluir para cadastrar um novo registro. Devem ser preenchidos os campos Cód. da Mensagem, ser informado o Tipo da mensagem, que é e-mail e informado um assunto, que será o título do e-mail. Neste exemplo, está sendo criada uma mensagem para informar que uma requisição de Aumento de Quadro foi inserida no fluxo de aprovação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41061975414807)

Clique na aba Corpo do E-mail, nela, será possível informar o texto que será exibido na mensagem que o gestor receberá. Neste momento, devem ser utilizados os parâmetros para criação de mensagem customizada desejados para que sejam exibidos na mensagem, além de incluir o endereço do portal Meu RH da empresa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41061997026455)

Segue abaixo a mensagem cadastrada no corpo do e-mail, para ser usada de exemplo para criação da mensagem customizada

```
Olá!

 
Foi aberta requisição [IDREQ] de [TIPOREQUISICAO] para aprovação.

Para visualizar a requisição, acesse o portal Meu RH, clicando no link abaixo:

http://localhost/FrameHTML/web/app/RH/PortalMeuRH/#/login

Atenciosamente,
Equipe RH.
```

Após realizar a criação da mensagem, salve a mensagem criada. Em seguida, clique na opção Tipos de Requisição e edite a requisição de Aumento de Quadro. No campo ‘E-mail requisição inserida no fluxo’, vincule a mensagem customizada que foi criada e salve a alteração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41061997027607)

Com isso, após o cadastro da requisição, os gestores envolvidos no fluxo de aprovação receberão um e-mail contendo o texto cadastrado na mensagem, com o link para acesso ao portal Meu RH.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41061975418263)

Podem ser criadas mensagens customizadas para cada etapa de cada tipo de requisição e cada tipo de requisição tem parâmetros específicos dependendo da etapa. A documentação abaixo contém as instruções de como realizar criar esta customização das mensagens:

[Mensagem customizada - E-mail](https://tdn.totvs.com/display/public/LRM/Mensagem+customizada+-+E-mail)
