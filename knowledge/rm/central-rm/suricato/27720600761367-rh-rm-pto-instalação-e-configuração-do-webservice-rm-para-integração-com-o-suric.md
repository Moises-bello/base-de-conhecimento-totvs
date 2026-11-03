---
article_id: 27720600761367
category: Suricato
content_hash: 1e3200e4f91fc09ff684182b71e51d1a57f7f16c8c6959b5b1fa6ef25f7c4ac4
fetched_at: '2026-06-28T22:46:26.374598+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: RH - RM - PTO - Instalação e configuração do Webservice RM para integração
  com o Suricato
type: support-article
updated_at: '2024-12-05T20:53:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27720600761367-RH-RM-PTO-Instala%C3%A7%C3%A3o-e-configura%C3%A7%C3%A3o-do-Webservice-RM-para-integra%C3%A7%C3%A3o-com-o-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600676247) Tempo aproximado para leitura: **00:10:00 min****Dúvida**

Como instalar e configurar o Webservice RM utilizado na integração com o Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH(Linha RM) - Automação de Ponto - A partir da versão 12.1  
  
**Solução**

Instalando o Webservice RM

1. Acesse a página de downloads da TOTVS: <https://suporte.totvs.com/portal/p/10098/download>

2. Na pesquisa busque pelo termo INTEGRACAOCHRONUSXTSA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28311910050967)

3. Baixe o arquivo MSI de acordo com a versão da biblioteca em seu ambiente.

4. Execute o instalador e será apresentado as seguintes telas no processo

* Tela de Boas-vindas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720617131159)

* Contrato de licença. Leia, aceite os termos e avance

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600687255)

* Pasta de destino da Instalação. Por padrão será criada a pasta com nome TSA no disco local C:\. Mas pode ser alterado para o local de preferência. Selecione o local desejado e avance

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600691095)

* Clique em Instalar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600692887)

* Uma nova janela será aberta para realizar algumas configurações. Avance.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600695447)

* Selecione o Alias que terá a base RM a ser utilizada na integração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720617145751)

* Servidor e Porta do Webservice Suricato. Essa informação pode ser conseguida com o suporte da empresa parceira Telemática

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600698903)

* Na seção IIS informe o nome do aplicativo que será criado no IIS. Nome padrão: TSA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600699927)

* Avance, salve e conclua o processo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720617151255)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600706455)

* Será criado no IIS o aplicativo TSA(nome do aplicativo escolhido na instalação) apontando para o caminho onde foi instalado o Webservice

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720617156759)

Após a instalação é necessário verificar e configurar os arquivos Alias.dat e Web.Config

1. Abra a pasta de instalação do Webservice RM (caminho padrão C:\TSA)

2. Edite o arquivo Alias.dat usando o programa de edição de texto (Bloco de notas, NotePad++...)

3. Confira se o Nome do Alias está correto e igual ao Alias utilizado para entrar no RM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600712727)

4. Ainda no arquivo Alias.dat do Webservice RM, informe um usuário e senha do banco de dados que tenha acesso a todas as tabelas do RM. Salve o arquivo após as alterações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600717975)

5. Agora abra o arquivo Web.config

6. Confira se na tag Alias o nome estará correto e igual ao Alias do RM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720617171863)

7. Ao final do arquivo Web.config terá as URLs do Webservice Suricato. Veja se o servidor e porta estão corretos. Essa informação pode ser conferida com o time da Telemática. Exemplo: http://Localhost:5000/

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600724887)

8. Troque nas URLs o termo tsa-ejb pelo termo suricato-totvs

* Antes da alteração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600727575)

* Depois da alteração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600728983)

9. Salve o arquivo e reinicie o IIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600732823)

10. Após a instalação e configuração, o webservice terá a url composta da seguinte forma:

* + Protoloco http ou https de acordo com as configurações do IIS
  + IP do Servidor ou o nome do Servidor onde foi instalado o Webservice RM
  + Nome do aplicativo/site criado no IIS após a instalação do Webservice RM (nome padrão TSA)
  + Arquivo TSService.asmx

Exemplo de URL: http://Localhost/TSA/TSService.asmx

Ao abrir a URL no navegador será apresentado a seguinte pagina:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27720600734103)

11. E esta URL do webservice RM será utilizada no módulo Integração nas configurações do RM para a integração.
