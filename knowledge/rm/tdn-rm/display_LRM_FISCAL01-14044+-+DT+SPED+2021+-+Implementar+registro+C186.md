---
content_hash: 9daed3c2f29ace4ee4a54808ba3efa7053c3bc36f6137923c0b0bfcad0f07016
fetched_at: '2026-06-29T00:10:52.454531+00:00'
page_id: '572516691'
product: rm
source: tdn-rm
title: FISCAL01-14044 - DT SPED 2021 - Implementar registro C186
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-14044+-+DT+SPED+2021+-+Implementar+registro+C186
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração de Arquivo EFD ICMS IPI |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14044 |

## **02. SITUAÇÃO/REQUISITO**

# Alteração Sped Fiscal - Layout 3.0.4 válido a partir de 01/01/2021

## Implementações necessárias

#### **REGISTRO C186: INFORMAÇÕES COMPLEMENTARES DAS OPERAÇÕES DE DEVOLUÇÃO DE ENTRADAS DE MERCADORIAS SUJEITAS À SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 1B, 04 e 55).**

O registro C186 é filho do C100 que é o documento fiscal. Este registro deve ser gerado para Lançamentos Fiscais que atendam às seguintes regras, se o flag para geração dos registros de ressarcimento/complemento estiver marcado na tela de geração do SPED:

* Lançamentos de Saída (Devolução de Compra);
* CFOP associado esteja marcado como Operação que controla ressarcimento/complemento do ST (DCFOP.OPERACAOSTCOMPRA)
* CFOP com o Tipo “Devolução” habilitado (DCFOP.TIPODEVOLUCAO)
* Produto estiver marcado como tributado pelo ICMS ST nos Dados Fiscais por UF, considerando a UF da Filial (TPRDCODFISCAL.TRIBUTADOICMSST)
* Exista Lançamento de Entrada referenciado
* Informações geradas baseado no Lançamento de Entrada referenciado (Registro C180).

Observação: Situação não deve gerar o Registro C185.

## **03. SOLUÇÃO**

O registro C186, junto com suas regras e dependências foram implementadas no processo de geração do SPED Fiscal e serão exibidas na rotina a partir de 2021.
