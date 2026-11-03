---
content_hash: bd1cb2c3c0d753ea9494e76b89a3b7912eb8916c3759561c251835339e295710
fetched_at: '2026-06-29T00:05:54.069592+00:00'
page_id: '107381145'
product: rm
source: tdn-rm
title: Parâmetros no Gerador de saídas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=107381145
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                    **Versão:**11.50 |
| **Processo** | **:** | Gerador de Saídas |
| **Subprocesso** | **:** | Parâmetros no Gerador de Saídas |
| **Data da publicação** | **:** | 04/12/2013 |

**PROCESSO:** *PARÂMETROS NO GERADOR DE SAÍDAS*

**INTRODUÇÃO:** Este guia ajudará na criação de um Layout do Gerador de Saídas com Parâmetros.

Sentença Utilizada:

**SELECT** PFUNC.CHAPA, PFUNC.NOME, PFDEPEND.NOME **AS** 'NOME DEPENDENTE',PFDEPEND.DTNASCIMENTO, PFDEPEND.SEXO

**FROM**PFUNC **INNER** **JOIN**

PFDEPEND **ON** PFUNC.CODCOLIGADA = PFDEPEND.CODCOLIGADA

**AND** PFUNC.CHAPA = PFDEPEND.CHAPA

**WHERE** PFUNC.CODSITUACAO = :CODSITUACAO

**AND** PFDEPEND.SEXO = :SEXO

Ao adicionar os parâmetros na sentença SQL, é necessário informá-los na tela do Contexto.

Neste exemplo, vamos utilizar a passagem deste parâmetro ao gerar o arquivo.

Assim deve ser adicionado ao Layout um contexto de parâmetros da Geração:

Desta Forma é apresentada as configurações para este parâmetro que será apresentado ao gerar o Layout desejado:

Neste exemplo foram configurados os dois parâmetros da sentença:

**CODSITUACAO – Situação do Funcionário;**

**SEXO – Sexo dos Dependentes;**

Após esta configuração dos parâmetros, se faz necessário configurar a ligação deste parâmetro com o contexto da sentença SQL.

Nas configurações do contexto da SQL na guia dos parâmetros temos esta opção como print abaixo:

Para que o contexto dos parâmetros da geração seja adicionado, os campos devem ser arrastados para configuração de ligação:

Após arrastar os campos, é apresentado em negrito o nome do contexto e o campo:

Assim após estas parametrizações, o Layout ao ser Gerado solicitará a passagem dos parâmetros:

Obs.: Repare que os nomes de dependentes são apenas do Sexo Feminino como solicitamos no parâmetros:

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
