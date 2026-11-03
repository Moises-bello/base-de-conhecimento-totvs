---
content_hash: c417bcd1394ae7b67b7ccf52ace5f17c176331a37ce25e47daf26ba8b8f4f383
fetched_at: '2026-06-29T00:05:51.681315+00:00'
page_id: '105316390'
product: rm
source: tdn-rm
title: Formatação Condicional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=105316390
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Reports                      **Versão:**11.50 x 11.80x |
| **Processo** | **:** | Formatação Condicional |
| **Subprocesso** | **:** | Formatação de campos |
| **Data da publicação** | **:** | 27/11/2013 |

#### Introdução

A formatação condicional permitirá o usuário parametrizar o relatório para que seja possível configurar um determinado campo ou dado com uma visualização diferenciada (cor, fonte, tamanho)

**O exemplo** abaixo utilizaremos a consulta SQL na tabela PFUNC onde ao imprimir o CODIGO DA SITUAÇÃO (CODSITUACAO) do funcionário estiver ATIVO (A) o mesmo será impresso c/ a **"Cor Vermelha"**

#### Desenvolvimento / Procedimento

1- Inserimos a consulta SQL da tabela PFUNC onde disponibilizamos no relatório os campos NOME e CODSITUACAO.:

2- Selecione as propriedades do campo CODSITUACAO,  para realizar a parametrização selecione a opção: "REGRAS DE FORMATAÇÃO"

**Clique em Editar Regra Folha**

**Siga os passos para Parametrização**

Ao Salvar as alterações e acessa-las observe que o relatório será gerado com as formatações parametrizadas.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
