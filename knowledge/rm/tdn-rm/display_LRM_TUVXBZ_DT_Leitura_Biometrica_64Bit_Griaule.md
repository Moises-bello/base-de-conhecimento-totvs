---
content_hash: 89137a6ba00eee9d2f07b308ee165ee2661085a414ca8f53ba7be40729b30f48
fetched_at: '2026-06-29T00:08:08.318951+00:00'
page_id: '238030397'
product: rm
source: tdn-rm
title: TUVXBZ_DT_Leitura_Biometrica_64Bit_Griaule
type: documentation
url: https://tdn.totvs.com/display/LRM/TUVXBZ_DT_Leitura_Biometrica_64Bit_Griaule
version: 115
---

# LEITURA BIOMÉTRICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Leitura biométrica - Cadastro de usuários - Movimentações* |
| **Situação/Requisito:** | *Foi identificado que a leitura biométrica não está funcionado, ao tentar cadastrar uma impressão digital ou localizar um usuário pela tela de movimentações utilizando impressão digital o sistema retorna um erro informando que o driver do dispositivo não está instalado, porém o leitor biométrico está instalado e funcionando.* |
| **Solução/Implementação:** | *Foi identificado que o erro é causado pelos arquivos (dll) da "Griaule" que estão em 32bit e RM.exe está sendo executado e 64bit, para solução do problema é necessário executar o "CorFlags.exe" para o "RM.exe" para que seja executado em 32Bit e assim fazendo com que a leitura biométrica funcione corretamente para o cadastro de usuários e para a tela de movimentações.* *Obs: é necessário a utização da versão "Griaule Fingerprint SDK 2009"*  ***Segue abaixo as instruções para execução do CorFlags:***  1. ***Abra o prompt de comando e navegue até o diretório onde está instalado o RM.exe*** 2. ***Execute o comando:* *CorFlags.exe RM.exe /32BIT+***   ***Para que o RM.exe seja obrigatoriamente executado em 32Bit***   * + ***CorFlags.exe RM.exe /32BIT+***  ***Para remover a obrigatoriedade do RM.exe ser executado em 32Bit***  * + ***CorFlags.exe RM.exe /32BIT-*** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
