---
content_hash: df924c9af5c21fe59450e387850492adac63da3a48c58ae03c0636a6616e4b56
fetched_at: '2026-06-29T00:11:16.972198+00:00'
page_id: '674908037'
product: rm
source: tdn-rm
title: Folha Agrária Importação de Falta por Justificativa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=674908037
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: |  |
| Segmento: | RH |
| Módulo: | Cadastro de Relógio , funçao e Importação da justificativa |
| Função: | Permitir a importação de Justificativa de faltas |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHJORNRM-1682 -DRHJORNRM-1670 -DRHJORNRM-1685 |

## **02. SITUAÇÃO/REQUISITO**

Permitir a importação da Justificativa da falta .

## **03. SOLUÇÃO**

No processo de Importação de batidas será importada apenas a  Justificativa da falta .

Para realizar a importação deverá ser criado um layout contendo a posição e tamanho da descrição e uma função com código de tratamento 0011-Gera somente Just.de ausência.

   1-Cadastrar um Layout  com informações no  campo descrição.O tamanho é limitado a 50 posições.

2-Cadastrar uma função de relógio, com tratamento de código 0011- Gera somente Just.de ausência.

3-A importação será realizada através do menu Entrada de dados -Importar

**Importante:**

-Deverá informar no campo layout do relógio,  o código correspondente ao layout criado com campo "Descrição".

-O sistema irá emitir um log no final da importação para o usuário , caso a falta no espelho não tenha sido calculada.

-O sistema irá emitir log no final da importação para o usuário, não será importada nenhuma batida devido a importação estar vinculada a função 0011-Gera Somente Just.ausência.

-O usuário poderá conferir o log da importação através do menu Entrada de dados -Memória da Importação.

As informações serão gravadas na tabela AJUSTFUN coluna Justificativa

**04. DEMAIS INFORMAÇÕES**

-Modelo do arquivo de importação:O arquivo de importação deverá conter a função de relógio e a descrição conforme exemplo:

Função código : F1000         Descrição:Consulta médica  e Consulta Dermatologista

Codcoligada,Chapa,dia,mês,ano,Cod.terminal,Cod.Função,Descrição

1;00001;09;09;2011;1A;F1000;Consulta Médica                                   ;  
1;00001;12;09;2011;1A;F1000;Consulta Dermatologista                      ;

## **05. ASSUNTOS RELACIONADOS**

**[Layout -Entrada de dados-Layout](https://tdn.totvs.com/pages/releaseview.action?pageId=452718923)**

**[Função -Entrada de dados Função de Relógio](https://tdn.totvs.com/pages/viewpage.action?pageId=452719507)**

Mais informações veja em: [Importação de Batidas](https://tdn.totvs.com/pages/viewpage.action?pageId=452719301)
