---
content_hash: e3435802e037e2b7235a46863cc4d37983ce701590a608c145d7bdb4fc693d40
fetched_at: '2026-06-29T00:10:22.499494+00:00'
page_id: '496801597'
product: rm
source: tdn-rm
title: Utilizando a Propriedade Máscara
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496801597
version: 20
---

# Índice:

---

.\*ndice:

# Objetivo:

---

           Esta documentação tem por objetivo exemplificar a utilização da propriedade “*Máscara*”.

# Introdução:

---

          A propriedade “*Máscara*”, possibilita a leitura de arquivos na conexão de origem e atribuir determinada nomenclatura aos arquivos gerados ao final do processo de execução de um Conceito.

* **Utilizando mascara na Conexão de Origem:**Na utilização de uma mascara na Conexão de Origem, pode ser utilizada uma combinação de caracteres de texto e curingas:

| Curinga | Representação |
| --- | --- |
| Asterisco (\*) | Zero ou mais caracteres |
| Interrogação (?) | Zero ou um caractere nessa posição |

**Exemplos:**

Faz a leitura de todos os arquivos iniciados com 2020 e tenha a extensão "txt".

|  |
| --- |

Faz a leitura de arquivos iniciados com 2020, tenha 2 caracteres após e a extensão "txt".

|  |
| --- |

* **Utilizando mascara na Conexão de Destino:**

          A propriedade “*Máscara*”, localizada na Conexão de Destino de um Conceito, possibilita atribuir determinada nomenclatura aos arquivos gerados ao final do processo de execução de um Conceito. Temos três formas para utilização da máscara. Abaixo seguem exemplos para utilização.

falseExemplos de Máscara1Sem Preenchimento

Neste caso o sistema irá gerar o arquivo atribuindo ao seu nome a data, hora, minuto, segundo no seguinte formato: ***yyyyMMddHHmmss.txt***

2Qualquer Valor

Irá gerar o nome com o valor inserido

3Valores entre [ ]

Esse caso permite colocar formatos de data para serem o nome do arquivo, exemplos:  
***[yyyyMMddHHmmssfff]******[yyyyMMddHH]******\*\*[yyyyMMdd]***

---

---

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Propriedade Máscara - Novo Conceito

falsefalse

**Status:** Finalizado

false

**Data:** 

false

**Autores:**
