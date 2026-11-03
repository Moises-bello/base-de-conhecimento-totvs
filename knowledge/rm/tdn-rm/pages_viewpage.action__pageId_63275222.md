---
content_hash: 556acbc31a196c8cfd50578a8ec620f410530be819cb02272415f728db36eccb
fetched_at: '2026-06-29T00:11:05.914035+00:00'
page_id: '63275222'
product: rm
source: tdn-rm
title: Inserção de Filtro em Relatório - Delphi
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63275222
version: 11
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**XX |
| **Processo** | **:** | Gerador de Relatórios |
| **Subprocesso** | **:** | Inserção do Filtro no Relatório - Delphi |
| **Data da publicação** | **:** | 05/07/2013 |

Para que você possa visualizar o filtro de um relatório no cabeçalho do mesmo proceda seguindo as orientações abaixo:

Primeiro o seu relatório deverá ter o campo que será utilizado como parâmetro. No exemplo abaixo estarei utilizando a data de admissão dos funcionários. Depois de inserido o campo eu clico na opção de "Filtros" para criar um novo filtro.

Criei o filtro para a data de movimento pegando o período de 01/01/2004 até 31/12/2004. Depois de preenchido os valores do filtro clique no botão OK.

Depois de criado o filtro para o relatório volte para tela principal do relatório e clique no ícone "Filtro":

O Gerador irá abrir um pequeno formulário onde irá conter todos os filtros que existirem elaborados para o relatório.

Arraste o filtro desejado para o cabeçalho do relatório. Será salvo um campo com a descrição Filtro#1. Selecione este mesmo campo e dê um Control C em seguida Controle V. Será criado o campo Filtro#2. É necessária a criação deste segundo campo baseado na copia do primeiro para que o filtro da data de admissão possa ser impresso no relatório o período  
 inicial e final do filtro.

Para definirmos qual dos campos será o período inicial e final devemos selecionar com o botão direito do mouse o campo "Filtro#1", escolher a opção propriedades. Abrirá um segundo formulário menor. Selecione a guia "Formatação" configure o campo informando se o campo irá trazer o período inicial ou final.

Repita o processo para o segundo campo, porem modificando as propriedades a fim de o segundo campo ser entendido como o período final. Salve as alterações e gere o relatório.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
