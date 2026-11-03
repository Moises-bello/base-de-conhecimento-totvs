---
content_hash: 264259624d6dab70fc95e68d8deeb410c3236d9814eba42911d9d77efbc5258f
fetched_at: '2026-07-02T19:24:26.571193+00:00'
page_id: '520672388'
product: protheus
source: tdn-tec
title: DBMonitor - Parâmetros de linha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520672388
version: 7
---

Parâmetros de linha

O true suporta a passagem de parâmetros de linha durante sua inicialização, conforme a sintaxe:

] [-p] [-l]]]>

---

## Parâmetros suportados

Os identificadores dos parâmetros devem ser informados em minúsculo.

A tabela a seguir descreve seus parâmetros e valores esperados:

| Parâmetro | Descrição | Observações |
| --- | --- | --- |
| ``` -s<host> ``` | O nome do host ou endereço IP do true. | Veja a sessão de observações do documento.   Não há espaço entre o "`-s`" e o endereço do host. |
| ``` -p<port> ``` | O número da porta do true. | Não há espaço entre o "`-p`" e o número da porta. |
| -l<language> | O idioma que deverá ser utilizado para exibição do true. | Veja a sessão de observações do documento para detalhes dos idiomas suportados.   Não há espaço entre o "`-l`" e o acrônimo do idioma. |

---

## Observações

* O parâmetro **-s** só está disponível em builds superiores a 20191119-20200213 do true
* O parâmetro **-l** só está disponível em builds superiores a 20191119-20200213 do true

Os idiomas suportados pelo true são:

| Idioma | Acrônimo | Observações |
| --- | --- | --- |
| Português (Brasil) | N/A | Este é o idioma padrão da aplicação e não precisa ser informado nos parâmetros de linha para ser utilizado. |
| English (United States) | en | Para utilizar este idioma é necessário ter o arquivo **monitor\_en\_us.qm** na mesma pasta onde está o executável do true. |
| Russo | ru | Para utilizar este idioma é necessário ter o arquivo **monitor\_ru\_ru.qm** na mesma pasta onde está o executável do true. |

---

## Exemplo

Exemplo de passagem de parâmetros para **versões iguais ou inferiores a 20191119-20200213** do true:

DBMonitor.exe srv01 -p7899
::: Linux - conexão com o host srv01 e porta 7899 :::
tec-sles12:/opt/totvs/dbaccess/ ./dbmonitor srv01 -p7899]]>

Exemplo de passagem de parâmetros para **versões superiores a 20191119-20200213** do true:

DBMonitor.exe -ssrv01 -p7899 -lru
::: Linux - conexão com o host srv01 e porta 7899 e uso do idioma russo :::
tec-sles12:/opt/totvs/dbaccess/ ./dbmonitor -ssrv01 -p7899 -lru]]>
