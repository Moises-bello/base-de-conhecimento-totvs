---
content_hash: 00899f33b157eba4b4743f0407c96bae6352037e1809876b40b288aeeded2736
fetched_at: '2026-06-29T00:06:18.415579+00:00'
page_id: '215484814'
product: rm
source: tdn-rm
title: SAU0059_Parâmetro_Limitar_Requisição_para_Paciente_na_Movimentação_de_Estoque_com_Data_Futura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=215484814
version: 1
---

# Parâmetro Limitar Requisição p/ Paciente na Movimentação de Estoque com Data Futura

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Hospitalar |
| **Versões:** | A partir da 12.1.6 |
| **Ocorrência:** | Qual o uso do parâmetro **Limitar Requisição p/ Paciente na Movimentação de Estoque com Data Futura**? |
| **Passo a passo:** | O parâmetro possibilita limitar a quantidade de dias (data futura) para realizar uma requisição para paciente na movimentação estoque.     1. Acesse **Opções/Parâmetros/Parâmetros Gerais**, aba **Estoques II**. 2. Infome o número máximo de dias que o sistema irá permitir requisições para paciente com data futura. 3. Acesse **Estoques/ Movimentação de Estoque**. 4. Faça uma nova movimentação do tipo “**Requisição para Paciente**”. 5. Se for informada uma data que atende ao intervalo de dias parametrizado anteriormente, o sistema permitirá a data de requisição. 6. Caso contrário, se a data extrapolar o período parametrizado, o sistema não permitirá a data informada e emitirá uma mensagem. |

divs
