---
content_hash: f6ebed9a25214ae92d7e7601407c59a376a187c3ee95b25c7ed948183f89eb1d
fetched_at: '2026-06-29T00:10:26.731385+00:00'
page_id: '514729256'
product: rm
source: tdn-rm
title: DT Login Novo Portal do Professor
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Login+Novo+Portal+do+Professor
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Novo Portal do Professor |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | PORTALMOBILE01-8019 |

## **02. SITUAÇÃO/REQUISITO**

Deve ser criado o login do novo portal do professor com possibilidade de configurar as imagens que serão exibidas no banner.

## **03. SOLUÇÃO**

Foi criado o login do novo portal do professor.

Nos arquivos de configuração do portal deve ser informado o nome das imagens que serão exibidas no banner na propriedade imgBannersLogin que recebe um array de objetos com o nome da imagem juntamente com sua extenção.

As imagens definidas no passo anterior devem ser disponibilizadas na pasta banners-login que fica em assets/img/banners-login
