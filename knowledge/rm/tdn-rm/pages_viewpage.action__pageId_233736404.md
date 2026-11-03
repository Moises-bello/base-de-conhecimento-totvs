---
content_hash: 25a82ae31ce8b0b4ce9a903921a172804807f9e5d177e003f7c7757122e14e45
fetched_at: '2026-06-29T00:06:27.853278+00:00'
page_id: '233736404'
product: rm
source: tdn-rm
title: DT_PCREQ-8869_Edição/Mostra campo Desconto integrado com o Solum
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233736404
version: 119
---

# Edição/Mostra campo Desconto integrado com o Solum

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Movimento | MovMovimentoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Bloquear Desconto Movimento Sup Fat | PrjContratoPdoMod.BloquearDescontoMovimentoSupFat | |  |  | |
| **Cadastros Iniciais:** | Contrato do TOP, Medição de Item de Contrato no TOP, Liberar Periodo, Gerar integração com Suprimento/Faturamento |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Movimento |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | * [PCREQ-8869](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-8869 "PCREQ-8869") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER, ORACLE |
| **Tabelas Utilizadas:** | TMOV, TITMMOV |
| **Sistema(s) Operacional(is):** | Windows XP SP1 ou superior. |

## Descrição

O objetivo desta implementação é identificar os movimentos gerados através de contratos do TOTVS Obras e Projetos que contenham dedução e discriminação de valor de dedução e retenção, para impedir que  o Desconto do movimento seja alterado pelo TOTVS Gestão de Estoques, Compras e Faturamento..

## Procedimento para Utilização

Durante a edição de um movimento qualquer pelo TOTVS Gestão de Estoques, Compras e Faturamento..o sistema irá verificar a origem do movimento e caso este seja proveniente de contratos do TOTVS Obras e Projetos que contenham dedução e discriminação de valor de dedução e retenção, o sistema irá bloquear a edição do campo Desconto no movimento..Qualquer outra rotina que por ventura venha a afetar o valor do desconto do movimento será consistido e apresentará a mensagem ao usuário ao salvar o movimento.

**Exemplo:**

       1.            Através do TOTVS Obras e Projetos gere uma medição de contrato que contenha dedução e discriminação de valor de dedução e retenção e execute o processo Gerar integração com Suprimento/Faturamento

O sistema gera um movimento no TOTVS Gestão de Estoques, Compras e Faturamento

       2.            Acesse o TOTVS Gestão de Estoques, Compras e Faturamento e edite o movimento que foi gerado anteriormente.

O campo Desconto na aba Tributos e Valores estará desabilitado.

       3.            Tente editar um outro campo que afete o desconto do movimento e clique em salvar

O sistema identifica que o campo esta sendo alteração e apresenta a mensagem de consistência.

**Observação:**

Alguns parâmetros do TOTVS Gestão de Estoque, Compras e Faturamento. podem afetar o desconto no movimento que será gerado pelo TOTVS Obras e Projetos nesse caso consulte a documentação de Integração para mais informações. Um exemplo disso é o parâmetro **Afeta desconto do Movimento** nos parâmetros do item de movimento que faz sobrescrever o desconto do movimento com a soma dos descontos dos itens de movimento. Esse comportamento pode gerar inconsistências que não poderão ser alteradas após a geração do movimento.

Durante o faturamento parcial do movimento originado no TOP  o campo desconto pode ser recalculado e proporcionalizado de acordo com o faturamento parcial.

divs
