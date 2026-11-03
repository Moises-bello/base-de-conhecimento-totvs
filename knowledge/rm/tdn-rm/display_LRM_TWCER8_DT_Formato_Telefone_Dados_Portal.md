---
content_hash: 10471f87e3c322df3d27e5770738f5b4a221135971b97774b3451fda3902a251
fetched_at: '2026-06-29T00:08:21.014459+00:00'
page_id: '268807276'
product: rm
source: tdn-rm
title: TWCER8_DT_Formato_Telefone_Dados_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TWCER8_DT_Formato_Telefone_Dados_Portal
version: 112
---

# DADOS DO CANDIDATO OU RESPONSÁVEL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Dados do candidato ou responsável* |
| **Situação/Requisito:** | *Os campos telefones do portal do processo seletivo só utilizam tipo de máscara de telefone, sendo que na tela de parâmetros é possível configurar dois tipos, sendo que se tentar informar o telefone no formato do segundo tipo de máscara o portal não aceita e informa que está inválido porém não informa qual é o formato de telefone correto.* |
| **Solução/Implementação:** | *Foi identificado que o portal do processo seletivo sempre utiliza a primeira máscara de telefone da tela de configurações, a máscara do tipo 'sem DDD' não é utilizada, sendo assim, para facilitar o entendimento foi adicionado uma mensagem na tela de configuração de máscaras alertando sobre a utilização correta das máscaras e também adicionado nos campos de telefone no portal do processo seletivo a sombra do formato que deve ser utilizado e também uma mensagem ao passar o cursor sobre o campo alertando que o nono dígito será configurado automaticamente se informado.*  *Tela de parâmetros:*      *Sombra do formato correto (será exibido conforme a máscara definida) e mensagem de nono dígito:* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | *N/A* |

divs
