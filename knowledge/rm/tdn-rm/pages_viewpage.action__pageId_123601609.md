---
content_hash: ddaa4846853a0de2feea1fbcf865fe74fad2ae5da81567ea9b06a5efad71f7b7
fetched_at: '2026-06-29T00:05:55.042690+00:00'
page_id: '123601609'
product: rm
source: tdn-rm
title: Como definir as propriedades de um "Tipo de Dados" na Tabela em Metadados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=123601609
version: 11
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework |
| **Processo** | **:** | Metadados |
| **Subprocesso** | **:** | Como definir as propriedades de um "Tipo de Dados" na Tabela em Metadados |
| **Data da publicação** | **:** | 13/02/2014 |

**Objetivo**: Disponibilizar ao usuário uma forma de definir as propriedades do  [tipo de dados](http://tdn.totvs.com/display/public/rm/Tipos+de+Dados) criado em uma tabela.

As propriedades serão disponibilizadas de acordo com os tipos de dados inseridos na estrutura da tabela (Conforme coluna marcada na imagem abaixo).

|  |
| --- |

As propriedades estarão disponíveis de acordo com o banco de dados.

| Propriedades    1. Define o campo da tabela como Chave Primária.  2. Define o campo como de preenchimento obrigatório.  3. Define se o campo será visível na visão do metadados.  4. Define o campo como auto incremento.  5. Define se a pesquisa como lookup no campo do metadados será habilitada.  6. Define se o campo será exibido na edição do metadados.  7. Define a quantidade de caracteres que o campo aceitará na **Base de Dados**.  8. Define o valor default em caso do campo não ser preenchido.  9. Define a quantidade de casas decimais que o tipo de dados terá (Usado em tipos de dados que recebem **numéricos e decimais**). |
| --- |

O campo **TAMANHO** estará disponível nos tipos de dados que recebem (Textos, Numéricos e Decimais).

| O Campo tamanho definirá a quantidade máxima de caracteres que o banco de dados aceitará por registro naquela coluna.    Neste caso o tamanho máximo será de 100 caracteres por registro. |
| --- |

O campo **VALOR PADRÃO** estará disponível para todos os tipos de dados.

| O Campo valor Padrão serve no caso do campo não ser preenchido no metadados ele irá inserir o que estiver no campo valor padrão.    Caso o usuário não digite nada no campo do metadados e execute a inserção do registro será inserido no banco de dados o que estiver preenchido no campo valor padrão. |
| --- |

Os campos **TAMANHO** e **ESCALA** estarão disponíveis juntos **SOMENTE** nos tipos de dados que recebem (Numéricos e Decimais).

| Neste caso deveremos informar obrigatoriamente os campos Tamanho e Escala.  O Campo tamanho definirá a quantidade máxima de caracteres que o banco de dados aceitará.  O Campo escala definirá a quantidade de casas decimais que o banco de dados aceitará.    Neste caso o tamanho máximo será de 10 caracteres por registro sendo eles 2 reservados para casa decimal.  Exemplo: |
| --- |
|  |

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
