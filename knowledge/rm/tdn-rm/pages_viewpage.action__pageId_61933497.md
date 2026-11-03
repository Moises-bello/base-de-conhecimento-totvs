---
content_hash: 5d0fcc866acedd791a453b8fc38b0b50034e7c35b93a6985f9c98bd97e60cf00
fetched_at: '2026-06-29T00:11:02.633360+00:00'
page_id: '61933497'
product: rm
source: tdn-rm
title: _Habilitando Máquina de Calculo.Net - RM Chronus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=61933497
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | RM Chronus                       **Versão:**11.00 |
| **Processo** | **:** | Máquina de Cálculo |
| **Subprocesso** | **:** | Habilitando Máquina de Cálculo.Net |
| **Data da publicação** | **:** | 05/07/2013 |

Implementação na versão 11.00 e 11.20 para que o parâmetro "Utiliza Novo Cálculo" seja habilitado para quem executa o sistema através do executável passando um argumento. Se este não for passado, o parâmetro aparecerá desabilitado conforme figura abaixo:

Para clientes novos, o parâmetro estará desabilitado e marcado, lembrando que em versões anteriores por default esta opção já é marcado desde a 11.00:

A chave a ser passada para ter controle sobre este campo é "/MC\_CHRONUS". O nosso executável deverá ser chamado dessa maneira:

a) Clique no botão iniciar da máquina.

b) Na opção "Executar" digite o comando "C:\TOTVS\CorporeRM\RMCHRONUS\RMChronus.exe **/MC\_CHRONUS"**

c) O sistema RM Chronus será executado. Na tela principal do mesmo vá ao menu "Opções | Parâmetros | Totvs Automação de Ponto".

d) Na visão de parametrização você deverá marcar a opção "Utiliza novo  
 Calculo":

e) Depois de habilitar o parâmetro, faça logout no sistema, selecione novamente a coligada. Vá ao menu "Opções | Parâmetros | Parametrizador".

f) Clique em avançar na tela seguinte.

g) Selecione a opção "Iniciais" e clique em "Avançar".

h) Selecione a opção "Cálculo" e no campo "Abono utilizado para Atestados do RM Labore" escolha a opção do abono que será lançado para o RM Labore:

i) Clique em "Avançar" até que o parametrizador conclua as alterações.

Obs.: Caso um dos menus mencionados neste documento não esteja habilitado será necessário habilitar o mesmo através das permissões de acesso, configurados no perfil do seu usuário.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
