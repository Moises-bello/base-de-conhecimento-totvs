---
content_hash: 75f48a9d29291f9caad9e0a0ad2b43d87d03fea378e9dbe9c3871d6d04b8a879
fetched_at: '2026-06-29T00:10:26.830711+00:00'
page_id: '514750327'
product: rm
source: tdn-rm
title: 6327922 FISCAL01-10192 DT NF-e - Fórmula visual para salvar XML das notas fiscais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514750327
version: 1
---

Parâmetro para salvar o arquivo XML no Server

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Salvar XML |
| Ticket: | 6327922 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Salvar XML |

## **02. SITUAÇÃO/REQUISITO**

O cliente criou uma fórmula visual para salvar o XML de nota fiscal eletrônica emitida pelo sistema, de um forma que futuramente a mesma possa ser agendada salvando o XML em uma determinada pasta da máquina.  
  
Ao término da execução da fórmula visual, é apresentada a mensagem informando que os arquivos foram salvos no 'C:', porém ao verificar o caminho especificado não existe arquivos gerados com o nome indicado.

## **03. SOLUÇÃO**

**Funcionalidade: Salvar XML**

**Cenário I: Salvando o arquivo no Servidor por Fórmula Visual**  
Dado que o parâmetro do processo "ManterServidor" está atribuído como Verdadeiro (1),  
E o diretório e o nome do arquivo estão configurados,  
Ao executar o processo via fórmula visual,  
O sistema deve salvar o arquivo de xml no local especificado no servidor.

**Cenário II: Salvando o arquivo no Client via Tela**  
Dado que o diretório e o nome do arquivo estão configurados,  
E a arquitetura está em 3 camadas  
Ao executar o processo via tela do RM,  
O sistema deve salvar o arquivo de xml no local especificado no client.
