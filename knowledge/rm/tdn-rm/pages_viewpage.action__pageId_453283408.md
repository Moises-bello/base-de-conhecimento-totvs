---
content_hash: 9ce981ffda4bae5dcbba4794a2551d15401fda58bf5f6e2e74b9c3faf5db7110
fetched_at: '2026-06-29T00:10:11.763294+00:00'
page_id: '453283408'
product: rm
source: tdn-rm
title: FISCAL01-6521 - DANFE 4.0 - Criação do provider para o DANFE 4.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453283408
version: 13
---

# DANFE 4.0 - Criação do provider para o DANFE 4.0

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Relatório DANFE |
| **Situação/Requisito:** | Criar um provider para gerar o relatório DANFE 4.0 |
| **Solução/Implementação:** | Foi criado o provider para o DANFE 4.0 e os contextos do DANFE, do emitente, transporte, dados da autorização, volume do transporte, total de imposto, fatura e da filial, retirada e entrega, conforme abaixo:  **Dados Autorização:**   * DADOSDAAUTORIZACAO.CONSULTA * DADOSDAAUTORIZACAO.DADOSNFECONTIGENCIA * DADOSDAAUTORIZACAO.DATAAUTORIZACAO * DADOSDAAUTORIZACAO.MSGDPEC * DADOSDAAUTORIZACAO.STATUS * DANFE.MSGPROTOCOLO   **Filial:**   * DADOSFILIAL.DESCRICAO * DADOSFILIAL.INSCMUN * DADOSFILIAL.NUMERO * DANFE.IMAGEM   **Volume Transporte:**   * VOLUMETRANSP.ESPECIE * VOLUMETRANSP.MARCA * VOLUMETRANSP.PESOL * VOLUMETRANSP.PESOB * VOLUMETRANSP.NUMERACAOVOL * VOLUMETRANSP.QVOL   **Total de Imposto:**   * TOTALIMPOSTO.ISSQNTOTALSERVICO * TOTALIMPOSTO.ISSQNTOTVBC * TOTALIMPOSTO.ISSQNTOTVISS * TOTALIMPOSTO.VALORDESCONTO * TOTALIMPOSTO.VALORFRETE * TOTALIMPOSTO.VALORICMS * TOTALIMPOSTO.VALORICMSST * TOTALIMPOSTO.VALORIPI * TOTALIMPOSTO.VALORNF * TOTALIMPOSTO.VALOROUTROS * TOTALIMPOSTO.VALORPRODUTOS * TOTALIMPOSTO.VALORSEGURO * TOTALIMPOSTO.VALORBCICMSST * TOTALIMPOSTO.VALORBCICMS   **Fatura:**   * FATURA.NDUP * FATURA.DATAVENCIMENTO * FATURA.VDUP   **Retirada:**   * RETIRADA.CEP * RETIRADA.CGC (CPF ou CNPJ) * RETIRADA.EMAIL * RETIRADA.TELEFONE * RETIRADA.INSCRICAOESTADUAL * RETIRADA.NUMERO * RETIRADA.UF * RETIRADA.BAIRRO * RETIRADA.COMPLEMENTO * RETIRADA.LOGRADOURO * RETIRADA.MUNICÍPIO * RETIRADA.NOME * RETIRADA.PAIS     **Entrega:**   * ENTREGA.CEP * ENTREGA.CGC (CPF ou CNPJ) * ENTREGA.EMAIL * ENTREGA.TELEFONE * ENTREGA.INSCRICAOESTADUAL * ENTREGA.NUMERO * ENTREGA.UF * ENTREGA.BAIRRO * ENTREGA.COMPLEMENTO * ENTREGA.LOGRADOURO * ENTREGA.MUNICÍPIO * ENTREGA.NOME * ENTREGA.PAIS    Observação As informações de: **CEP, Código do País, Nome do País, Telefone** e **E-mail** não foram implementadas pelo TOTVS Gestão de Estoque, Compras e Faturamento, mas já estão ligadas e preencherão os campos assim que for implementado e o conteúdo retornado pelo serviço. |
