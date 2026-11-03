---
content_hash: 05501e0e0d9acf75464ffb36c120ba4af49cef9c467c5b6797562ec9712023a0
fetched_at: '2026-06-29T00:11:02.568277+00:00'
page_id: '61932714'
product: rm
source: tdn-rm
title: FAQ - WikiHelp Local
type: documentation
url: https://tdn.totvs.com/display/LRM/FAQ+-+WikiHelp+Local
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.XX |
| **Processo** | **:** | Wikihelp |
| **Subprocesso** | **:** | WikiHelp Local |
| **Data da publicação** | **:** | 05/07/2013 |

**1)** **Pergunta:** Ao apresentar a mensagem abaixo eu preciso obrigatoriamente instalar o "Wikihelp local" para acessar ajuda dos aplicativos?

**Resposta:** Não. A mensagem é apresentada devido às parametrizações feitas em "preferências de usuário" estarem com os seguintes parâmetros marcados: "Ajuda local" e "Não exibir novamente a janela de escolha da fonte de ajuda", conforme figura abaixo. Esta parametrização deverá ser utilizada somente se o cliente não possuir ou não permitir acesso à internet de forma alguma.

Devemos sempre incentivar o cliente a utilizar parametrização de ajuda online e, caso tenha restrições de acesso à internet para usuários, solicitar liberação para o domínio [http://wikihelp.totvs.com.br.](http://wikihelp.totvs.com.br/) Utilizando o help online os usuários terão sempre acesso fácil às melhorias e atualizações feitas nos Helps.   
   
   
 **2)** **Pergunta:** Quero usar help local, pois não tenho internet na minha empresa. Como fazer?

**Resposta:** Para utilizar ajuda local, é necessário possuir uma máquina com sistema operacional Windows Server onde será o servidor do "WikiHelp local", e esta deverá possuir o SharePoint 3.0 instalado com hotfix de atualização. Ao rodar o instalador do "Wikihelp local" no Windows Server, será informada a exigência de versão do SharePoint com o hotfix mínimo para poder restaurar o help local. Também será perguntado se deseja abrir as páginas onde poderão ser feitos os downloads, conforme figuras abaixo.

Para facilitar seguem os links para download: Sharepoint v3.0 SP2 português:

<http://www.microsoft.com/downloads/details.aspx?FamilyID=ef93e453-75f1-45df-8c6f-4565e8549c2a&DisplayLang=pt-br>

Hotfix:

<http://support.microsoft.com/hotfix/KBHotfix.aspx?kbnum=2276474>  
   
   
 **3)** **Pergunta:** Instalei o Sharepoint, hotfix mas não consigo finalizar a instalação do Wikihelp. O que pode estar ocorrendo?

**Resposta:** A instalação da ajuda local nada mais é do que a restauração do backup de nosso site wikihelp.totvs.com.br. Todo site é instalado utilizando uma porta de instalação e na instalação do "Wikihelp local" é necessário informar qual a porta será restaurado o site, caso não tenha um site criado no SharePoint na porta informada não será possível restaurar o site no SharePoint. Por padrão, caso o cliente não possuía instalado o SharePoint e instalou neste momento, existirá o site previamente criado na porta 80 não sendo necessário fazer nenhuma modificação no processo de instalação para restauração do site.   
   
   
 **4)** **Pergunta:** Após finalizada a instalação do "Wikihelp local" com sucesso já consigo utilizar a ajuda local?

**Resposta:** Não ainda. É necessário parametrizar as informações do servidor SharePoint para os sistemas saberem onde buscar as páginas de ajuda. Para saber como parametrizar acesse a página:

<http://wikihelp.totvs.com.br/WikiHelp/Adm/WikiHelpLocal.aspx>

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
