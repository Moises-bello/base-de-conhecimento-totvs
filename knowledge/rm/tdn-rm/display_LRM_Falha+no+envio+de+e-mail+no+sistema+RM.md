---
content_hash: 702dbddb6e5b12cb7a6c74fe018970535b8e103813c49be6ac0f2fd4316d0f92
fetched_at: '2026-06-29T00:05:57.736303+00:00'
page_id: '181964445'
product: rm
source: tdn-rm
title: Falha no envio de e-mail no sistema RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Falha+no+envio+de+e-mail+no+sistema+RM
version: 20
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Teste Email Global                       **Versão:**2.0 |
| **Processo** | **:** | Parâmetros Globais e-mail |
| **Subprocesso** | **:** | Orientações de utilização da ferramenta TestaEmailGlobal.exe |
| **Data da publicação** | **:** |  |

**Introdução**

Este aplicativo foi criado para auxiliar ao usuário na configuração da tela Global de envio de e-mails dos aplicativos CorporeRM.

Preencha o maior número de informações possíveis para que ele tenha um maior número de opções de envio.

Ele tenta enviar e-mail com todas as combinações possíveis de configuração desta tela (autenticação, domínio, porta e conexão segura).

Se a porta não for informada, ele tenta enviar com a porta padrão de envio de e-mails (25). Quando ele envia sem o usuário e senha, ele busca as credenciais utilizadas no sistema operacional.

Ocorrendo alguma falha no envio, o sistema registra no arquivo Log.txt a mensagem completa retornada na tentativa de conexão e envio com o servidor SMTP.

Se o aplicativo não conseguir enviar o e-mail de nenhuma forma, então o problema não está na configuração do envio de e-mail do CorporeRM, mas em alguma, das várias configurações de ambiente que podem impedir este processo, como Firewall, Conexão com internet, Antivírus, Softwares de bloqueio, etc...

O aplicativo irá gerar um log no fim do processo informando se conseguiu enviar e com quais configurações conseguiu enviar. Informará também se não conseguiu e com quais configurações não conseguiu enviar

**Dica:** Avaliar a necessidade de ativar o recurso Aplicativos Integrados (ou no caso do GMAIL "Aplicativos de terceiros") nas configurações de seu Provedor de E-mail.  
Office 365: <https://docs.microsoft.com/pt-br/office365/admin/misc/integrated-apps?view=o365-worldwide>  
GMAIL: <https://www.google.com/settings/security/lesssecureapps>  
<https://accounts.google.com/DisplayUnlockCaptcha>

**1 - Segue abaixo o link para as orientações e parametrização de envio de e-mail sobre a tela Opções\Parâmetros\Globais\Envio de E-Mails:**

       Para verificar se determinada informação é obrigatória ou não para o servidor SMTP, você pode usar o aplicativo TestaEmailGlobal.exe disponível em anexo ao final do documento.

       Existem diversas variáveis de ambiente que podem impedir o envio de mensagens pelo sistema, como antivírus, firewall, etc. Desative-os e faça os procedimentos abaixo.

**2 - Ao executar o aplicativo TestaEmailGlobal.exe será apresentada a tela de informações sobre o mesmo, após ler as informações, clique em fechar:**

**3 - Preencha todos os campos de acordo com as configurações do seu provedor de e-mail e clique em "Enviar e-mail" (sugerimos preencher todas as informações para que sejam apresentadas todas as possíveis combinações bem sucedidas passíveis de configurar os parâmetros globais):**

Após clicar no menu “Enviar e-mail” o aplicativo irá realizar diversas tentativas utilizando todas informações possíveis para o envio de e-mail. Quando finalizar apresentará um "log" contendo as informações das tentativas.

Utilize as informações de sucesso do "log" para parametrização do e-mail no sistema RM.

Segue abaixo o PRINT de um exemplo do log contendo diversas informações utilizadas para o envio do e-mail, o seu log apresentará mensagens similares.

Após a exibição do "log", você pode preencher os campos conforme informações de envio, segue dois exemplos no PRINT abaixo:

**Exemplo 01:**

**Exemplo 02:**

**Importante:**

Para alguns Provedores de E-mail, é possível cadastrar apenas um e-mail como validador dos e-mails enviados. Dessa forma, deverá configurar o usuário e senha do validador do Provedor nos campo de usuário validador e senha (conforme item 1 demonstrado no exemplo abaixo ) e marcar a flag "Utilizar usuário de e-mail como remetente" (item 2):

**Abaixo está o aplicativo TestaEmailGlobal versão 3.0 para download:**

250

Após o download efetuado, descompacte-o em uma pasta onde será criado o "log".

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
