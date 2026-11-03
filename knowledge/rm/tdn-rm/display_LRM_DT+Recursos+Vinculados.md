---
content_hash: 95d0afd3c188913744b4957e425a69953015ac89329f03d8c0febbf8a1fbacaa
fetched_at: '2026-06-29T00:09:38.766249+00:00'
page_id: '431662159'
product: rm
source: tdn-rm
title: DT Recursos Vinculados
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Recursos+Vinculados
version: 5
---

# RECURSOS VINCULADOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Obras e Projetos |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Recursos Vinculados | Recursos Vinculados |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Recursos de Composição | Recursos de Composição | |
| **Cadastros Iniciais:** | Projeto, Insumos, Composições, Recursos de Composições (Insumos e Composições Auxiliares) |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-4900](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-4900) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Possibilidade de vincular um Recurso de Composição do tipo Insumo à um Recurso Composição Auxiliar.

## Procedimento para Utilização

No cadastro de Recursos de Composição, existe o anexo de **"Recursos Vinculados"**que permite que recursos da mesma composição "mãe" insumo possam ser vinculados à um recurso do tipo composição auxiliar que esteja presente na mesma composição principal. Essa necessidade se deu a partir de informações e regras do DNIT que define que uma composição auxiliar pode representar um custo do tempo ou do transporte de um determinado material, como pode ser visto na imagem abaixo:

No exemplo acima, é possível notar que o Material **"M0082** **Areia média lavada"** está presente na composição como **MATERIAL**, **TEMPO FIXO** e **MOMENTO DE TRANSPORTE,**porém trata-se somente de um material. No caso dos outros grupos, o que representa o custo com o material, seriam as composições 5914647 para tempo fixo e 5914359, 5914374 e 5914389 para momento de transporte.

Sendo assim, para que essa representação possa ser considerada e que um relatório possa exibir essa "amarração" existe o cadastro de Recursos Vinculados:

Para composições auxiliares do tipo "Momento de Transporte", se faz necessário que no momento do cadastro do Recurso Vinculado, sejam definidos os valores dos DMT's que são específicos para cada recurso relacionado ao transporte, onde o cálculo realizado afim de definir o Valor Parcial da composição auxiliar considera essas grandezas, como no exemplo a seguir:

Algumas considerações são importantes, tais como:

* Somente recursos da mesma composição principal podem ser vinculados;
* Somente em Recursos do tipo Composição que é possível realizar o vínculo;
* A soma das quantidades dos recursos vinculados atualiza a quantidade do recurso pai;
* Tanto o cálculo da composição pai quanto o cálculo do projeto atualizam a quantidade do recurso que tem vinculo;
* O campo quantidade da visão de recursos e da tela são somente leitura para recursos que possui vinculados;
* O mesmo recurso só pode ser vinculado uma única vez em outro recurso;
* Os DMT's somente podem ser definidos para Tipos de Associação LN, RP ou P sendo que é possível apenas um dos tipos.
