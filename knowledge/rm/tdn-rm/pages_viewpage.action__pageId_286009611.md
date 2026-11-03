---
content_hash: 37e367837285e6c45bd07e582358e8018519c996a508f42a84f4ed5b5fa85cac
fetched_at: '2026-06-29T00:08:39.090242+00:00'
page_id: '286009611'
product: rm
source: tdn-rm
title: 1024668 EDUCACIONAL01-1822 DT Digitação do Histórico Escolar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286009611
version: 105
---

# DIGITAÇÃO DO HISTÓRICO ESCOLAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Digitação do Histórico Escolar* |
| **Situação/Requisito:** | *Ao acessar a digitação de histórico e tentar alterar alguma informação na área de disciplinas o sistema apresenta a mensagem: "DataGridViewComboBoxCell value is not valid." Basta passar o mouse na região ou abrir a tela.* |
| **Solução/Implementação:** | *Foi acrescentado uma nova validação ao abrir a tela de Digitação de Histórico para caso a quantidade de registro de disciplinas ser maior que mil, caso ao abrir a tela o sistema apresente uma exceção de Não foi possível realizar a operação, porque foram retornados uma grande quantidade de registros de registro ser maior que mil será necessário ir em Serviços Globais | Serviços | Servidores de aplicação, selecionar o data server com o Id EduHistoricoEBData e aumentar o campo número máximo de registros. Isso ocorre por que o padrão do sistema é apresenta apenas mil registros.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
