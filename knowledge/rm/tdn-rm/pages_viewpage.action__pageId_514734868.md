---
content_hash: da9b7ecfbd3b8cbe892a2b021763b0ee8dde1daafbbe1085c2f0023878da1675
fetched_at: '2026-06-29T00:10:26.766759+00:00'
page_id: '514734868'
product: rm
source: tdn-rm
title: FISCAL01-10212 DT Cadastro de Lançamento de Ativo Imobilizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514734868
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro de Lançamento de Ativo Imobilizado |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FIS000205 |

## **02. SITUAÇÃO/REQUISITO**

Migrar as regras de negócios que existem na entidade de Manutenção de Lançamentos de ativo

## **03. SOLUÇÃO**

Foram implementadas as regras abaixo no cadastro de Lançamento de Ativo Imobilizado.

Serão carregados na visão de lançamentos de Ativo:

- Lançamentos cadastrados manualmente  
- Data de Entrada\Saída Maior que 01/08/2000  
- Exercício Fiscal e Filial do contexto.

Regras de Inclusão\Alteração:

- Calculo do Valor ICMS com O Valor ICMS Informado em Tela + Valor do Diferencial de Alíquota + Valor do Frete  
- Não será permitido incluir Lançamento com Data Entrada\Saída igual ou menor que 01/08/2000  
- O patrimônio selecionado deve ser do tipo Patrimônio ou Terceiros.

Regras de Alteração:

- Não é possível alterar lançamento de ativo de entrada incluído manualmente que possui lançamento de ativo de saída  
- Não é possível alterar lançamento de ativo que tenha como vinculo Lançamento Fiscal de Entrada\Saída.

Regras para Deletar registro:

- Não é possível deletar lançamento de ativo que tenha como vinculo Lançamento Fiscal de Entrada\Saída.
