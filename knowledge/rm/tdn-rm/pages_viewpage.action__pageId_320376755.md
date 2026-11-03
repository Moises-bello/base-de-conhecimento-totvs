---
content_hash: 7955e31e6948273a84e3fd55fe1533d60a6e43a8a48b99888aa080630f67bad1
fetched_at: '2026-06-29T00:08:47.774608+00:00'
page_id: '320376755'
product: rm
source: tdn-rm
title: DT Cadastro de Valores de Integração Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=320376755
version: 17
---

# Cadastro de Valores de Integração Financeira

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro* | *Valores de Integração Financeira* | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *DEDUINTEGRACOES-1063.* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *FLanIntegracaoDef* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

Com o objetivo de flexibilizar a integração entre os módulos Educacional e Financeiro foi liberado o cadastro de valores de integração financeira em ambos os módulos.

todostodosCadastro Valores de Integração no TOTVS Gestão Educacional

No módulo Educacional o cadastro está disponível no menu "Financeiro / Contábil →  Geração → Financeiro →  Valores de Integração Financeira"

No módulo TOTVS Educacional poderá ser cadastrado o valor de integração financeira com sua descrição, ação (descontar, acrescentar, nada) e sua ordem.

O valor de integração financeira presente no lançamento financeiro oriundo do módulo Educacional, o TOTVS Gestão Financeira irá interpretá-los na Baixa de Lançamentos Financeiro conforme a ação definida na sua origem.

Na inclusão do lançamento financeiro oriundo do módulo Educacional, os valores de integração financeira criados serão inseridos conforme a  do sistema.

Cadastro Valores de Integração no TOTVS Gestão Financeira

## No módulo Financeiro o cadastro está disponível no menu "Cadastros → Valores de Integração"

No módulo Financeiro poderá ser cadastrado o valor de integração financeira com sua descrição, ação (descontar, acrescentar, nada), sua ordem e sua fórmula.

O valor de integração criado no módulo Financeiro presente no lançamento financeiro oriundo do módulo Educacional, o TOTVS Gestão Financeira irá interpretá-los na Baixa de Lançamentos Financeiro conforme a ação definida na sua origem.

Na inclusão dos valores de integração criados no TOTVS Gestão Financeira serão inseridos no lançamento financeiro oriundo do módulo Educacional conforme a  no TOTVS Gestão Educacional

O TOTVS Financeira possibilita a inclusão de valores de integração default para lançamentos gerados a partir de outros módulos, ou seja todo lançamento gerado para Educacional poderá ser criado possuindo um valor de integração  
com regra especifica determinada pelo cliente, que pode ser definidas manualmente ou por fórmula.

Observação:  
Este recurso foi disponibilizado para as versões 12.1.25 e superiores ou igual a 12.1.28, para habilitar a opção entre em contato com o Suporte.  
Para saber mais detalhes consulte [FIN - Valores de Integração Financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=532041706).
