---
content_hash: 12a0620a495d2308c2aa34d8e6236e24d025db20656f23aca34f929a1ff74db5
fetched_at: '2026-06-28T21:35:27.223079+00:00'
page_id: '506384805'
product: fluig
source: tdn-fluig
title: Como aumentar o limite de upload da plataforma
type: documentation
url: https://tdn.totvs.com/display/fluig/Como+aumentar+o+limite+de+upload+da+plataforma
version: 29
---

4.\*ndice

# Objetivo

---

Este guia mostra como aumentar o limite máximo de *upload* no TOTVS Fluig Plataforma.

# Como aumentar o limite de *upload* da plataforma

---

Para aumentar o limite de *upload*, siga os passos abaixo:

Atenção!

A realização deste procedimento pode causar problemas de performance na plataforma. Recomendamos que seja realizado em ambiente de **homologação antes de configurar em produção**.

false11Passo 1

* Pare os serviços do Fluig.

2Passo 2

* **A partir da atualização 2.0**:  
  Localize o arquivo **standalone.xml**, que está disponível em **[diretório\_instalação]/appserver/standalone/configuration**, e abra em um editor de texto utilizando um usuário com permissões de administrador.

* **Para atualizações 1.6.5 até 1.8.2**:  
  Localize o arquivo **domain.xml**, que está disponível em **[diretório\_instalação]/appserver/domain/configuration**, e abra em um editor de texto utilizando um usuário com permissões de administrador.
3Passo 3

* No arquivo correspondente à atualização do Fluig que você utiliza (standalone.xml ou domain.xml), procure pela tag **http-listener** e o seu atributo **max-post-size**. Altere o valor para "2147483648" para permitir até 2GB de *upload*.

xml



]]>4Passo 4

* Se você possuir HTTPS na plataforma, precisará editar também o valor do parâmetro **https-listener max-post-size**. Se você não tiver HTTPS na plataforma, só existirá o primeiro parâmetro.

xmlExemplo:
]]>5Passo 5

* Salve e inicie os serviços do Fluig na ordem correta.

6Passo 6

* Tente publicar o arquivo em seguida.

Importante!

Ao alterar o limite padrão de *upload* na configuração do serviço Fluig acima do valor padrão, a performance para todos os usuários da plataforma poderá ser afetada durante o *upload* de arquivos com tamanho superior ao limite padrão.

# Escolhendo o valor correto

---

## Unidade de medida

Uma boa prática para determinar o novo valor da propriedade **max-post-size** em bytes, é utilizar um a potência de base 2 (Ex.: 210, 220, 230, ...), **conforme norma IEC 80000-13 : 2008**. Isto se deve ao fato de que todos os dispositivos de armazenamento são projetados para guardar um volume de dados, sendo este um número múltiplo de dois, justamente por causa da natureza binária do bit, embora comercialmente seja utilizado o sistema internacional (Ex.: 101, 102, 103, ...).

Segue abaixo alguns exemplos de valores baseados nesta lógica:

| **Tabela 1 - Valores de armazenamento conforme norma IEC 80000-13 : 2008** | | | | | |
| --- | --- | --- | --- | --- | --- |
| Potência de base 2 | gibibyte (GiB) | mebibyte (MiB) | quibibyte (KiB) | Bytes | bits |
| ​20 | 0 | ​0 | 0 | **​0** | ​1 |
| 21 | 0 | 0 | 0 | **0** | 2 |
| 23 | 0 | 0 | 0 | **1** | 8 |
| 210 | 0 | 0 | 1 | **1024** | 8192 |
| 220 | 0 | 0 | 1024 | **1048576** | 8388608 |
| 230 | **1** | **1024** | **1048576** | **1073741824** | **8589934592** |
| 231 | ***2*** | ***2048*** | ***2097152*** | ***2147483648*** | ***17179869184*** |

| Tabela 2 - Múltiplos do Byte |
| --- |
| ​ | [Prefixo binário](https://pt.wikipedia.org/wiki/Prefixo_bin%C3%A1rio "Prefixo binário") ([IEC](https://pt.wikipedia.org/wiki/Comiss%C3%A3o_Eletrot%C3%A9cnica_Internacional "Comissão Eletrotécnica Internacional")) | | |  | [Prefixo do SI](https://pt.wikipedia.org/wiki/Sistema_Internacional_de_Unidades "Sistema Internacional de Unidades") | | | | --- | --- | --- | --- | --- | --- | --- | | Nome | Símbolo | Múltiplo |  | Nome | Símbolo | Múltiplo | | [byte](https://pt.wikipedia.org/wiki/Byte "Byte") | B | 20 |  | [byte](https://pt.wikipedia.org/wiki/Byte "Byte") | B | 100 | | [kibibyte](https://pt.wikipedia.org/wiki/Kibibyte "Kibibyte") | KiB | 210 |  | [kilobyte](https://pt.wikipedia.org/wiki/Kilobyte "Kilobyte") | kB | 103 | | [mebibyte](https://pt.wikipedia.org/wiki/MebiByte "MebiByte") | MiB | 220 |  | [megabyte](https://pt.wikipedia.org/wiki/Megabyte "Megabyte") | MB | 106 | | [gibibyte](https://pt.wikipedia.org/wiki/Gibibyte "Gibibyte") | GiB | 230 |  | [gigabyte](https://pt.wikipedia.org/wiki/Gigabyte "Gigabyte") | GB | 109 | | [tebibyte](https://pt.wikipedia.org/wiki/Tebibyte "Tebibyte") | TiB | 240 |  | [terabyte](https://pt.wikipedia.org/wiki/Terabyte "Terabyte") | TB | 1012 | | [pebibyte](https://pt.wikipedia.org/wiki/Pebibyte "Pebibyte") | PiB | 250 |  | [petabyte](https://pt.wikipedia.org/wiki/Petabyte "Petabyte") | PB | 1015 | | [exbibyte](https://pt.wikipedia.org/wiki/Exbibyte "Exbibyte") | EiB | 260 |  | [exabyte](https://pt.wikipedia.org/wiki/Exabyte "Exabyte") | EB | 1018 | | [zebibyte](https://pt.wikipedia.org/wiki/Zebibyte "Zebibyte") | ZiB | 270 |  | [zettabyte](https://pt.wikipedia.org/wiki/Zettabyte "Zettabyte") | ZB | 1021 | | [yobibyte](https://pt.wikipedia.org/wiki/Yobibyte "Yobibyte") | YiB | 280 |  | [yottabyte](https://pt.wikipedia.org/wiki/Yottabyte "Yottabyte") | YB | 1024 |  | |

]]>
