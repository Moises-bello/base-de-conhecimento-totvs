---
article_id: 1500006915762
category: Meu RH - Home
content_hash: 350b10fab8dcc0adad1dc11515bb13bfdbe1a9b7a4cd73f897f3a540c5a9e236
fetched_at: '2026-06-28T22:47:34.656195+00:00'
product: rm
section_id: 1500000861702
source: central-rm
title: RH - RM - Meu RH - Consulta Alterações de Cadastro Pendentes de Aprovação
type: support-article
updated_at: '2024-10-10T13:30:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006915762-RH-RM-Meu-RH-Consulta-Altera%C3%A7%C3%B5es-de-Cadastro-Pendentes-de-Aprova%C3%A7%C3%A3o
---

**Dúvida**Como saber quais informações estão pendentes para aprovação na tabela PDADQUIOSQUE?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) – Meu RH – Todas as versões  
  
**Solução**Para verificar quais informações estão pendentes para aprovação, vá no modulo **Folha de Pagamento** no menu **Alterações Globais** e nele encontrará a opção **"Aprovação de Alterações Cadastrais"**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22327013421591)

Abaixo um exemplo ao alterar ter alterado via app Meu RH o apelido do funcionário de Mestre para Itamar:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009794522)  
  
Para verificar as informações pelo Banco de Dados use a seguinte sentença:

SELECT \* FROM PDADQUIOSQUE  
  
Para habilitar o menu o perfil deverá ter permissão, vá em **Serviços Globais**, menu **Segurança** e selecione a opção **Perfis**, nele selecione o perfil desejado, vá na pasta **Acesso a Menus** e selecione **Administração de Pessoal / Alterações Globais e selecione Aprovação de Alt. Cadastrais:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009096802)**

Caso queira que o próprio funcionário faça as alterações e não passe pela aprovação, deverá acessar o modulo **Folha de Pagamento / Configurações** e acessar o **Parametrizador**, nele acesse o menu **RM Portal** e selecione o grupo de quiosque desejado, depois vá no menu **Alterações Cadastrais**, nessa tela encontrará o campo **Enviar direto para o cadastro de funcionários**, ao marcar alguma opção o próprio funcionário terá a autonomia para atualizar sem precisar de aprovação.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009792602)  
  
**Importante**

As férias não ficam salvas na tabela PDADQUIOSQUE, relacionado ao funcionamento das férias, segue  a documentação abaixo:

**Saiba mais**

[RH - RM - Meu RH - Onde são armazenadas as aprovações de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005394901-RH-RM-Meu-RH-Onde-s%C3%A3o-armazenadas-as-aprova%C3%A7%C3%B5es-de-f%C3%A9rias)
