---
content_hash: 2731351bfe49e2fc8ed733b3bc2fb5c5e685f9efda1720a5b4ef2bb4f956838c
fetched_at: '2026-06-29T00:08:23.359645+00:00'
page_id: '270081564'
product: rm
source: tdn-rm
title: Desinstalação do Rm pela prompt de comando do Windows
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270081564
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.XX |
| **Ocorrência:** | Desinstalação de biblioteca Rm |
| **Ambiente:** | Ambiente de Instalação - Windows 7 |
| **Passo a passo:** | Utilizamos o comando WMIC(Windows Management Instrumentation Command) no CMD. O WMIC é compatível com shells e comandos de utilitário existentes, utilizado para parametrizações e configurações via linha de comando.    1º : Acesse o cmd como administrador,        Digite o comando wmic;      2º : Execute product get name para verificar os programas instalados em seu ambiente. Veja como está a sintaxe da biblioteca Rm. No teste realizado em nosso ambiente, como pode ser visto no vídeo , exibiu-se como BibliotecaRm - 12.1.13.3.      3º : Digite : product where name="BibliotecaRm - 12.1.13.3" call uninstall  Esse comando irá solicitar a desinstalação do programa. Logo depois será perguntado se deseja realizar a desinstalação, digite Y , confirmando o processo.        4º : Aguarde a confirmação da desinstalação.      Vídeo abaixo de todo processo :    250 |
| **Observações:** | Ressaltamos que outros comandos poderão ser adicionados, conforme o sistema operacional e as particularidades de cada máquina. |
|  |  |
|  |  |
