---
content_hash: 6e64931096540a5271aa0ea0a615d4e46d970fa8901090cf31078d553a49ffed
fetched_at: '2026-06-29T00:11:22.083301+00:00'
page_id: '698288682'
product: rm
source: tdn-rm
title: Relatório do Espelho do Cartão de Ponto - Nome Civil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=698288682
version: 17
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: |  |
| Segmento: | RH |
| Módulo: | Relatórios - Espelho do Cartão |
| Função: | Permitir  a emissão do Relatório pelo Nome Civil ou Nome Social |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHJORNRM-2475](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2475)  [DRHJORNRM-2246](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2246) |

## **02. SITUAÇÃO/REQUISITO**

Permitir a geração do relatório do espelho do cartão de ponto pelo *Nome Civil.*

## **03. SOLUÇÃO**

O relatório do espelho do cartão passou a obter por padrão o *"Nome Social", caso tenha sido informado no cadastro do funcionário.*

*Para a geração do relatório considerando o "Nome Civil"  deverá no passo 3 marcar a opção "Imprimir apenas Nome Civil ", caso contrário, será visualizado o "Nome Social" do cadastro do funcionário.*

## **04. EXEMPLO DE UTILIZAÇÃO**

11Parametrização

No Automação de Ponto para que seja impresso o *Nome Civil*, basta marcar no Relatório do espelho no passo 3 , o parâmetro *"Imprimir apenas Nome Civil".*

Para exibir o Nome Social no  App MeuRH é necessário a criação de um perfil  [MEURH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012116682-RH-RM-Meu-RH-Como-parametrizar-e-exportar-o-relat%C3%B3rio-de-espelho-de-ponto-no-Meu-RH) e  marcar o parâmetro "Exibir Nome Social do Funcionário", disponível em RM | RH | Gestão de Pessoas | Configurações | Parametrizador | Configurações | Portal Meu RH.

2Relatório do Espelho do Cartão de Ponto

No cadastro do funcionário temos os campos Nome e Nome Social.

Quando a opção  "Imprimir apenas "Nome Civil" for marcada, o sistema irá considerar as informações do campo Nome, caso contrário, será impresso o Nome Social.

No menu Cadastros-Funcionário foi informado Nome e Nome Social.

Na geração do relatório no passo 3, marcada a opção *"Imprimir apenas Nome Civil"*

O relatório do espelho será visualizado da seguinte forma: Apenas informações do Campo Nome.

Realizada nova geração Espelho do cartão passo 3, desmarcada  a opção *"Imprimir apenas Nome Civil"*

O relatório do espelho será visualizado da seguinte forma: Apenas informações do Campo Nome Social.

**04. ASSUNTOS RELACIONADOS**

**[Relatório do Espelho do Cartão de Ponto](https://tdn.totvs.com/pages/viewpage.action?pageId=452719152)**
