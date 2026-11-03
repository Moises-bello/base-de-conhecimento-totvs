---
content_hash: 684dc58258c469ecf43f725d4268f700961d255fd04bb73c638fdc0ba44f03e1
fetched_at: '2026-06-29T00:11:37.941171+00:00'
page_id: '780780906'
product: rm
source: tdn-rm
title: TCGI - Envio de E-mail
type: documentation
url: https://tdn.totvs.com/display/LRM/TCGI+-+Envio+de+E-mail
version: 5
---

# **ENVIO DE E-MAIL**

No tipo de ação Envio de E-mail deverá ser parametrizado as informações:

Para a ação de envio de Email, será possível definir o Assunto, informar um relatório para o corpo do E-mail e enviar o boleto (Para que o boleto seja enviado, o lançamento em atraso precisa possuir um boleto gerado e o [convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=551429165)utilizado precisa de um relatório de boleto associado).

**Assunto:** Define o texto que será incluído no campo Assunto. Será o mesmo texto para todos os e-mails.  
**Relatório do Corpo:**Deverá ser informado um relatório(**global**) que será utilizado para a criação do corpo do e-mail. Para orientações de como criar um relatório, acesse: [RM Reports](https://tdn.totvs.com/display/LRM/RM+Reports).  
**Nome do Remetente:**Nome que irá ser exibido como o Remetente que está enviando o e-mail.  
**E-mail do Remetente:**Endereço de e-mail que será exibido como do remetente, mas o e-mail oficial sempre será do cadastro de Globais.  
**Enviar Boleto:**Flag que indica se será enviado ou não o boleto em **anexo** no e-mail da cobrança. Somente lançamentos com **boleto** gerado e com o CNABSTATUS igual a **Registrado** ou **Registro On-line**, terão o boleto enviado no e-mail.

**OBS:** Na mesma régua pode ser criado mais de uma ação do tipo envio de e-mail, sendo assim as informações acima poderão ser diferentes para cada ação, como por exemplo o relatório do corpo do e-mail.

**Configuração de Uso - Ação de Cobrança  - E-MAIL**

# **Relatório**

***Em anexo no documento o Modelo de Relatório de Cobrança :*** [Modelo de Relatório de Cobrança](https://tdn.totvs.com/download/attachments/559286431/FORMULARIO%20MODELO%20COBRANCA.TotvsReport?version=2&modificationDate=1671014281877&api=v2)

Importar Estrutura do Relatório : Gestão | RM Reports |

Processos / Importar Estrutura de Relatório

# **Configurar E-mail**

**Exemplo para conta Google.**

Parâmetros Globais | Envio de E-mails

Ativar : Acesso ao APP menos seguro no google : <https://myaccount.google.com/security?rapt=AEjHL4M-3JcogSiI1sX7wa_Yip2m_CE4SnPD02VTWrpJOWvjs-nRmP2WL_ejcfab4bPGPFD2Ixe7M7cwaGGfNvlXvT7AVd8NEQ>

Importante!

**Importante**  
Esta tela possui parâmetros da coligada atual (define as configurações que serão utilizadas na coligada que o usuário está logado no momento) e da coligada global (define as configurações que serão usadas pela coligada global). Geralmente configuramos as mesmas informações para a coligada global e a atual, dependendo da necessidade da empresa estes dados poderão ser separados.

**Mais sobre configuração de E-mail :** [Envio de email - LINHA RM](https://tdn.totvs.com/display/LRM/Envio+de+email+-+LINHA+RM)

Testando envio de E-mail , Clicar no : 

Inserir E-mail destino e em seguida : Enviar.

Sistema avisa do envio da mensagem de teste.

E-mail enviado com sucesso.

Saiba Mais!

Verifique também estes documentos para saber mais sobre as formas de configurar o envio de email no RM:

[Framework - Linha RM - Frame - Configurar Envio de E-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001046067-Framework-Linha-RM-Frame-Configurar-Envio-de-E-mail)

[Framework - Linha RM - Frame - Realizar login com senha de app para envio de e-mail Gmail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6603997367319)

# **Gerando Ação Manual de Cobrança ( SEM BOLETO ) !**

**Gerando ação manual de cobrança:**

Igual do Assistente , usuário não vai gerenciar o assistente para quem será enviada a cobrança, usuário que define para quem será enviada a cobrança - muito parecido com do Assistente de cobrança que já existe no sistema 

Filtro é definido pelo usuário, Pegando lançamentos já vencidos ou por vencer.

Neste exemplo vou pegar um lançamento específico = Ref : 13829

Após filtrar o(s) lançamento(s) desejado(s) - Executar.

* **OBS:**Cadastro do Cli/For tem que estar com campo E-mail preenchido.

Executado o processo - Ação Manual de Cobrança.

E-mail enviado para o Cliente.

# **Gerando Ação Manual de Cobrança ( COM BOLETO ) !**

* **A tela abaixo demonstra a visão do processo de envio da cobrança manualmente.**
* **Para que o boleto gerado seja enviado junto ao email a flag "Enviar Boleto" deverá ser marcada.**
  + **Atenção: mesmo com o campo "Enviar Boleto" marcado, somente será enviado o boleto referente aos lançamentos que tiveram os boletos vinculados Registrado ou Registro On-line**  
      
    **SUGIRO REMOVER O TEXTO DA IMAGEM, fica difícil de pesquisar e não tem como traduzir. já temos os campos do print que não poderão ser traduzidos.**

Status Remessa : Registrado

Filtro para buscar o Lançamento com Boleto gerado e Registrado - Executar

E-mail enviado com Boleto em anexo.

# **Configurando Vários E-mail ao mesmo tempo**

Como na imagem abaixo, colocando mais de um email no campo "E-mail" e separando por ";". Ao gerar a cobrança para algum lançamento que tenha esse cliente associado, será enviado a mensagem para todos os e-mails informados no cadastro do mesmo cliente.
