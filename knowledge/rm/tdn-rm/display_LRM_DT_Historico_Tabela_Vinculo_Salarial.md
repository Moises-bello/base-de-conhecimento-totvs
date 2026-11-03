---
content_hash: 428fd701d0446644377b8da7c767e1339447dd02e0bd9dc7172f95c26831686b
fetched_at: '2026-06-29T00:06:06.302784+00:00'
page_id: '201729836'
product: rm
source: tdn-rm
title: DT_Historico_Tabela_Vinculo_Salarial
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Historico_Tabela_Vinculo_Salarial
version: 8
---

# HISTÓRICO DA TABELA DO VÍNCULO SALARIAL

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Pessoas** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Opção de Menu** | | **Assistente de Vinculação de Tabela Salarial** | *Valorização* | | *Histórico de Tabela Salarial* | *Planejamento e captação* | |
| **Versão:** | *12.1.8* |

## Descrição

Criação histórico de vinculação de tabelas salarias por função e lotação

## Procedimento para Utilização

O **Data de Vínculo** serve para agrupar funções e lotações.

A estrutura de armazenamento de histórico de vinculação de tabela salarial para os agrupamentos de função e lotação contém os seguintes campos:

IDHISTORICO; - Chave Composta da Tabela  
CODCOLIGADA; - Chave Composta da Tabela  
CODTABELA; - Chave Composta da Tabela  
CODNIVEL; - Chave Composta da Tabela  
CODFAIXA; - Chave Composta da Tabela  
VALORSALARIO;  
CODSECAO (Para o caso de lotação);  
CODFUNCAO;  
DATAINICIOVINCULO;  
DATAFIMVINCULO;

O histórico de vinculação de tabela salarial salva o histórico de acordo com a inclusão/exclusão/atualização de vinculação de tabela salarial considerando a data de vinculo da inclusão de vinculação e data de exclusão/atualização da vinculação de uma tabela salarial. O histórico também considera os níveis estabelecidos em cada vinculação, bem como todas as suas faixas.

No Assistente de Vinculação de Tabela Salarial tem um botão para excluir todos os vínculos da seleção atual.

Caminho: **Valorização / Vinculação**

 

O anexo para exibição do histórico de vinculação de tabela salarial deverá ser somente leitura, não permitindo inclusão/alteração/exclusão de registros

O novo anexo deve ser adicionado as visões de Função e Lotação, e devem exibir o histórico de acordo com os agrupadores a época da vinculação. O anexo de histórico irá mostrar em sua visão o nome da tabela e as datas de vinculação da tabela salarial. Nessa tabela que será somente leitura, mostra o detalhe do histórico da tabela contendo o nível, faixa e valor do salário da tabela.

Ex.: Hoje o usuário realiza uma vinculação de tabela salarial considerando o agrupador por função. Amanhã o usuário realiza uma vinculação de tabela salarial considerando o agrupador por lotação.

Este parâmetro está localizado no seguinte caminho: **RH / Gestão de Pessoas / Configurações / Parametrizador / Validações / Usar Seção e/ou Lotação na organização das Tabelas Salariais**

Para Histórico de tabela salarial vá em **Planejamento e Captação / Funções / Anexo / Histórico de Vinculação** **de Tabela Salarial – Função**
