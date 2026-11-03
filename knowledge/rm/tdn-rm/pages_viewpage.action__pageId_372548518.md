---
content_hash: 20724c4914bdfa3a067d9ded5cc45a21a8943af5c64b85d66ccc2ccedb39e094
fetched_at: '2026-06-29T00:09:01.121047+00:00'
page_id: '372548518'
product: rm
source: tdn-rm
title: DT_Transferência de Período com mais de 6 meses
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372548518
version: 4
---

# TRANSFERÊNCIA DE PERÍODO COM MAIS DE 6 MESES

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Automação de Ponto |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Liberação de Período | Liberação de Período | | Definir Período Ativo | Definir Período Ativo | |
| **Parâmetro(s):** | Quantidade de meses que não serão migrados para o arquivo morto na liberação ou definição de período ativo;  Transfere registros dos períodos oficiais, menor que x mes(es), para o arquivo morto. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | PONTO01-3888, PONTO01-3897 |
| **Tabelas Utilizadas:** | APARAM |
| **Versões/Release:** | 12.1.21 |

## Descrição

Foi disponibilizado no TOTVS Automação de Ponto o seguinte parâmetro:

**Quantidade de meses que não serão migrados para o arquivo morto:** Informe neste campo a quantidade de meses que será considerado para manter os dados na Tabela de Produção.

**Exemplo:** Foi informado nesse campo o total de 6 meses. Ao realizar a Liberação de Período ou Definição de Período Ativo, os últimos 6 meses anteriores ao Período Atual e Ativo permanecerão em Tabela de Produção. Os demais meses serão transferidos para o Arquivo Morto.

Para utilização deste parâmetro acesse: ***Configurações | Parâmetros Gerais | Parametrizador | Iniciais | Etapa 7 - Período***e informe a quantidade de meses desejado.

***Atenção:***

O tempo máximo para esta parametrização será de 100 meses.

Com esta nova implementação ao realizar a Liberação de Períodos, o parâmetro '***Transfere registros dos períodos oficiais, menor que x mes(es), para o arquivo morto***' será preenchido com a quantidade de meses informada no Parametrizador.

Executando a Liberação de Períodos com esta parâmetro marcado, o sistema manterá em tabela de produção, a quantidade de meses informado. Realizando a liberação sem marcar este parâmetro, apenas será feito a Liberação de Período, sem alterar as informações da Tabela de Produção e Arquivo Morto.

**Exemplo:**

* **Situação 1:** Foi informado no Parametrizador que será mantido apenas 5 meses na Tabela de Produção.
  + **Liberação de Período com o parâmetro marcado:** Será mantido na Tabela de Produção os 5 meses anteriores ao período Atual e Ativo, demais meses serão transferidos para o Arquivo Morto;
  + **Liberação de Período com o parâmetro desmarcado:** Será feito apenas a liberação de Período, sem alterar os registros da Tabela de Produção ou Arquivo Morto.
* **Situação 2:** Foi informado no Parametrizador que será mantido apenas 2 meses na Tabela de Produção. Após a Liberação de Período foi mantido somente esses 2 meses em produção e o restante ficou no arquivo morto. No mês seguinte foi alterado a parametrização para 5 meses. Para este cenário, ao realizar a liberação de período, ficará em produção os últimos 3 meses. Os meses que já estavam em arquivo morto, não serão alterados.
