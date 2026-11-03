---
content_hash: e6f0ee64c874cb2a94abb2e39fd03028851d491d979de55970db8ca66d5e3c23
fetched_at: '2026-06-29T00:08:17.774925+00:00'
page_id: '258834620'
product: rm
source: tdn-rm
title: Ao definir o idioma a instalação  do RM trava
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=258834620
version: 4
---

# Orientações para correção de travamento de instaladores RM

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.XX; 12.1.XX |
| **Ocorrência:** | Ao definir o idioma a instalação  do RM trava |
| **Ambiente:** | Ambiente de Instalação |
| **Passo a passo:** | Ao definir o idioma a instalação  do RM trava  Objetivo:  Esse documento tem como objetivo corrigir as inconsistências que ocorrem ao instalar a biblioteca RM.            Normalmente, costuma-se travar a instalação no momento de definir o idioma ao selecionar se a instalação será local ou 3 camadas.  Informamos que esse é um problema que está associado ao componente da Microsoft [Framework.net](http://Framework.net), e não do RM . As atualizações do Windows Update podem também corromper alguns arquivos do usuário.  Veja abaixo como aplicar as configurações durante a instalação:  1º Passo :  Antes de iniciar a instalação verifique os itens :  • Firewall desabilitado.  • Antivírus desabilitado.  • UAC Controle de acesso de usuários desabilitado.  No momento da instalação, caso esses aplicativos não estiverem desabilitados, algumas funcionalidades do RM poderão ser bloqueadas.    2º Passo :  Delete todos os arquivos temporários do caminho abaixo e realizar o teste de reinstalação da Biblioteca .MSI:  C:\Users\nome\_do\_usuario\AppData\Local\Temp  Onde lê-se nome\_do\_usuario (será apresentado o nome do usuário – obs.: A pasta AppData pode estar oculta), ou informe %temp% no menu Executar do Windows.    3º Passo :  Instale a última versão do Microsoft [Framework.net](http://Framework.net).  <https://www.microsoft.com/pt-br/download/details.aspx?id=53321>    Observação: Por padrão o Windows 10 já vem com o Microsoft [Framework.net](http://Framework.net) 4.6.1.  Informamos que a versão 4.5.2 é uma versão estável. Caso esteja com a versão 4.6.1 e não esteja conseguindo instalar a biblioteca Rm, remova o Microsoft [Framework.net](http://Framework.net) 4.6.1 e instale a 4.5.2 e faça o teste.    4º Passo:  Reinicie a máquina. Após a reinicialização do windows, efetue o  login com um usuário diferente do atual (que está com problemas) e abra uma aplicação em .Net para garantir que esteja funcionando.  **No final desse documento , faça o download do app "Teste\_Framework\_V4" para atender esse teste, basta seguir a instrução de clicar no texto.**  Com o teste realizado, feche o aplicativo e efetuar logoff para então retornar ao usuário anterior (que estava com problemas).  Pode-se iniciar a instalação da BibliotecaRM novamente.  **150** |
| **Observações:** | Um teste a ser realizado é realizar o procedimento de instalação , com um novo usuário. Crie um novo usuário com perfil de administrador do sistema.    Desinstale o .Net Framework instalado e instale a versão anterior (exemplo remova o 4.5.2 e instale o 4.0).     Realize a instalação da Biblioteca novamente. |
