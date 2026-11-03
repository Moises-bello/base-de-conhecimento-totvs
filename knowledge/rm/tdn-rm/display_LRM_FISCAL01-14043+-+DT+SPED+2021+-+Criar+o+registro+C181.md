---
content_hash: 30b47ad5b8b0870c3677f699a3710b5fb75b7fc8dd4f839e37a1a26368e29321
fetched_at: '2026-06-29T00:10:52.297504+00:00'
page_id: '571787495'
product: rm
source: tdn-rm
title: FISCAL01-14043 - DT SPED 2021 - Criar o registro C181
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-14043+-+DT+SPED+2021+-+Criar+o+registro+C181
version: 2
---

## ****e s01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14043 |

## **02. SITUAÇÃO/REQUISITO**

Criar o registro C181 no SPED Fiscal:

O Registro C181 é “filho” do registro C170 que são os itens do Lançamento Fiscal. Este registro deve ser gerado para Lançamentos Fiscais que atendam às seguintes regras, SE o flag para geração dos registros de ressarcimento/complemento estiver marcado na tela de geração do SPED:

* Lançamentos de Entrada (Devolução de Venda);
* CFOP associado esteja marcado como operação que controla ressarcimento/complemento do ST (DCFOP.OPERACAOSTCOMPRA)
* CFOP com o Tipo “Devolução” habilitado (DCFOP.TIPODEVOLUCAO)
* Produto estiver marcado como tributado pelo ICMS ST nos Dados Fiscais por UF, considerando a UF da Filial (TPRDCODFISCAL.TRIBUTADOICMSST)
* Exista Lançamento de Saída referenciado
* Informações geradas baseado no Lançamento de Saída referenciado (Registro C185).

*Observação: Situação não deve gerar o* ***Registro C180****.*

## **03. SOLUÇÃO**

O novo registro, junto com suas regras e dependências foram implementadas no processo de geração do SPED Fiscal e serão exibidas na rotina a partir de 2021.
