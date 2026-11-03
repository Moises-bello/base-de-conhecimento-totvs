---
content_hash: 4884611c947b5b4a5fcbd208e9d21019ca1650c09a2887522e94d03b2907433f
fetched_at: '2026-06-29T00:06:15.439213+00:00'
page_id: '210055921'
product: rm
source: tdn-rm
title: DT_Evolucoes_Orcamento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Evolucoes_Orcamento
version: 5
---

# EVOLUÇÃO DO MÓDULO DE ORÇAMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **RH** |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Orçamento* | *Evolução* | |
| **Versões/Release:** | **12.1.6** |

## Descrição

Melhorias do módulo de Orçamento

## Procedimento para Utilização

**Chapa Base**

**• Perfil de Admissão**O campo Chapa Base era utilizado apenas para preenchimento de dados no cadastro do perfil. O cadastro foi criado para o campo ser gravado na base e foi criado a função de fórmula **CHAPABASE** para recuperar a chapa informada. Desta forma, é possível criar fórmulas para recuperar demais informações do funcionário base.

**• Step de Admissão**No step de admissão também foi criado o campo Chapa Base. Desta forma, mesmo não utilizando um Perfil de Admissão é possível informar uma chapa base.  
Após selecionar a chapa base os campos Seção, Função, Tipo de Funcionário, Tipo de Recebimento, Sindicato, Horário, Faixa e Nível salarial serão preenchidos com os dados do funcionário base. É possível utilizar o perfil ou a chapa base. Ao selecionar um perfil o campo chapa base ficará desabilitado. O mesmo acontecerá ao selecionar uma chapa base, neste caso o campo perfil será desabilitado.

****Campos Complementares****

Os Campos Complementares de Orçamento são utilizados apenas para admissões feitas no orçamento.  
Os valores destes campos podem ser informados no ***Step de Admissão.***A função de fórmula **TABCOMPLORC** serve para retornar o valor de um campo complementar de orçamento.  
Para os funcionários já existentes na base, ao executar o cálculo do orçamento onde existam fórmulas que utilizem valores de campos complementares, os valores serão recuperados dos campos complementares atuais do funcionário (PFCOMPL), ou seja, não será possível fazer a edição dos campos complementares no módulo de orçamento.

**Itens de Orçamento**

No cadastro para Itens de Orçamento são informados um código, uma descrição e os eventos que compõe o item de orçamento.  
Sua finalidade é funcionar com um agrupador de eventos para gerar relatórios e informações gerenciais.
