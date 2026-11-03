---
content_hash: 5b354fc7483ee0c8581a090ade350d27e15e4ea3ce8c0c2e51e576eddecbb887
fetched_at: '2026-06-29T00:08:37.134955+00:00'
page_id: '284874153'
product: rm
source: tdn-rm
title: 95588 PONTO01-734 DT Apresenta Status Demitido no Ponto
type: documentation
url: https://tdn.totvs.com/display/LRM/95588+PONTO01-734+DT+Apresenta+Status+Demitido+no+Ponto
version: 101
---

# Apresenta status demitido no espelho do Portal RH

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Automação de Ponto* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Espelho de ponto *do Portal RH.** | *Espelho de ponto do Portal RH.* | |
| **Parâmetro(s):** | *Parametrizador RMPortal | Espelho funcionário | Apresenta status demitido no espelho do Portal RH* |
| **Tickets relacionados** | *95588* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | PONTO01-734 |
| **País(es):** | *Todos países.* |
| **Tabelas Utilizadas:** | *PPARAMQUIOSQUE* |

## Descrição

Foi implementado o parâmetro "Apresenta status demitido no espelho do Portal RH" a fim de inibir ou apresentar o status demitido ao funcionário no acesso ao espelho do Portal RH. O valor padrão deste parâmetro será marcado mantendo assim o funcionamento já conhecido para os usuários que não desejam inibir a informação para o funcionário.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. No módulo *TOTVS Automação de Ponto* acesse *o* menu *Configurações | Parametrizador | RM Portal | Espelho funcionário* e verifique que o parâmetro *"Apresenta Status demitido no espelho do Portal RH"* é criado conforme especificações abaixo:

|  |  |
| --- | --- |
| **Nome da Variável:** | ApresentaStatusDemitido |
| **Tipo:** | *Booleano* |
| **Descrição:** | *Apresentação ou inibição do status demitido no espelho do Portal RH.* |
| **Valor Padrão:** | *True* |

## Procedimento para Utilização

* Para utilização do parâmetro deverá acessar o módulo *TOTVS Automação de Ponto* e em seguida acessar o menu *Configurações | Parametrizador | RM Portal | Espelho funcionário*, nesta tela poderá visualizar o parâmetro *Apresenta Status demitido no espelho do Portal RH* ;
* O parâmetro *Apresenta Status demitido no espelho do Portal RH* terá como valor default verdadeira, ou seja, será apresentado marcado, isto para manter o funcionamento do sistema inalterado, caberá ao usuário desmarcar para inibir a apresentação do status de demitido no espelho do Portal RH.

divs
