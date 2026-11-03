---
content_hash: ed9cc3f41acccbfd621f4528431502951ecb058a13213bc209847e00345bd191
fetched_at: '2026-06-29T00:11:17.334725+00:00'
page_id: '679159137'
product: rm
source: tdn-rm
title: 13835455 FISCAL01-17755 - DT - DCTF Mensal - Permitir a escolha do diretório
  para a geração do arquivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679159137
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Gerar DCTF |
| País: | Brasil |
| Ticket: | 13835455 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17755 |

## **02. SITUAÇÃO/REQUISITO**

Nas rotinas DCTF e GIA-ST os arquivos são gerados por padrão na pasta de instalação do RM na subpasta Saídas.

Os usuários que não possuem acesso a pasta da instalação ficam impossibilitados de acessar os arquivos.

## **03. SOLUÇÃO**

Disponibilizado um novo campo na tela de geração da rotina que permite ao usuário escolher uma pasta para salvar o arquivo.

Para habilitar o campo de definição do diretório basta marcar a opção "Ignorar diretório padrão".

O usuário poderá escolher uma pasta local em seu computador ou uma pasta compartilhada em rede.

Imagem
