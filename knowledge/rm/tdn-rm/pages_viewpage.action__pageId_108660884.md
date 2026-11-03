---
content_hash: 9bae2549aa271dd271fdc079263df392c83c4ced2f7312ad3bc693c950d962a0
fetched_at: '2026-06-29T00:05:54.792923+00:00'
page_id: '108660884'
product: rm
source: tdn-rm
title: Remoção do Produto RM e reinstalação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=108660884
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                         **Versão:** 11.xx |
| **Processo** | **:** | Instalação |
| **Subprocesso** | **:** | *Como Desinstalar e Reinstalar Aplicativos RM* |
| **Data da publicação** | **:** | 08/01/2014 |

**Introdução**

*Este documento tem por objetivo auxiliar a Desinstalação do Produto RM e a reinstalação do mesmo n**a ORDEM correta.* ***O mesmo poderá ser aplicado para ambientes 32 ou 64 bits***

**1º PASSO**

Para realizar a instalação em ambientes WIN32 ou 64bits deve-se realizar o seguinte procedimento:

-Realizar a desinstalação completa dos produtos através do painel de controles, caso já estejam instalados.

**(Abaixo segue processo para desinstalação e reinstalação).**

1)Remover através do painel de controle os aplicativos TOTVS **seguindo a ordem**:

a) Aplicativos(RMFluxus,RMLabore,RMVitae...etc..);  
 b) BibliotecaRM;   
 2) Excluir a pasta TOTVS que encontra-se no diretório c:\TOTVS;  
 3) Pesquisar se existe algum arquivo RM ainda existente noWindows;  
 4) Reiniciar a máquina.

**2º PASSO**

-Após realizar a desinstalação do produto por completo em sua máquina, deverá ser realizado no Windows a seguinte parametrização (No caso de sistema operacionais WIN7).

-Em pesquisar digite a opção:(UAC), controle de conta de usuário,o controle de conta de usuário deverá possuir a barra na opção "nunca notificar" (Conforme Exemplo abaixo):

-Desabilitar por completo o Firewall do Windows;  
 -Desabilitar o antiVírus somente para realização do processo de instalação dos produtos;  
 -Reiniciar a Máquina caso tenha sido realizado algum destes procedimentos sugeridos.

**3º PASSO**

Ao acessar novamente o Windows (após a reinicialização), deverá ser realizada novamente a instalação do produto, porém, ao instalar clique com o botão direito do mouse em cima do instalador e selecione a opção: "instalar como administrador".

Abaixo segue a ordem que deverá ser efetuada para a instalação do produto:

1) Instale os aplicativos seguindo a sequencia: **(lembrar da opção"instalar como administrador)**

a)BibliotecaRM;  
 b)BibliotecaRM(Patch);  
 c)BibliotecaRM(Especifica);  
 d)Aplicativos.

**INFORMAÇÕES COMPLEMENTARES**

**-IMPORTANTE OBSERVAR QUE O FRAMEWORK DEVERÁ ESTAR INSTALADO NA VERSÃO 4.0.** **BAIXAR PELO SITE DA MICROSOFT.**

**-O LICENCE SERVER (TOTVS MONITOR) DEVERÁ ESTAR PARAMETRIZADO E JÁ CONFIGURADO.**

 

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha);
