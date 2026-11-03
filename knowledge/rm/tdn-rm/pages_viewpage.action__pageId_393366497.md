---
content_hash: 59236d1c03c78d0292a8ce93a4c6aff147604d078f88723528c9db1d6e5d29e3
fetched_at: '2026-06-29T00:09:09.748973+00:00'
page_id: '393366497'
product: rm
source: tdn-rm
title: 1473969 DEDUINTEGRACOES-699 DT Preenchimento do Endereço de Prestação do Serviço
  - Movimento gerado através do Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393366497
version: 5
---

# Geração de Movimento (Regime de caixa e competência)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de movimento |
| **Situação/Requisito:** | Cliente informa que gera movimentos através do Educacional. Para o envio de NFS-e para o município de Petrópolis, quando o local de prestação do serviço é diferente do Endereço do Tomador é necessário informar o endereço de prestação.  No caso de empresas do ramo Educacional, o endereço de prestação do serviço é igual ao endereço da Filial, diferente do endereço do tomador.  Atualmente, para gerar esta informação no XML da NFS-e é necessário que alguns campos do movimento sejam preenchidos, são eles:   * Tipo do Endereço (TIPOENDPREST      Tipo: Texto      Tamanho: 10 * Endereço (ENDPREST                            Tipo: Texto      Tamanho: 60) * Número (NUMPREST                              Tipo: Texto      Tamanho: 9) * Complemento (COMPLPREST              Tipo: Texto        Tamanho: 60) * Bairro (BAIRPREST                                  Tipo: Texto        Tamanho: 40) * Cep (CEPPREST                                      Tipo: Texto          Tamanho: 8)   Campos complementares criados pelo cliente (Tabela TMOVCOMPL).  Regra no manual da Prefeitura de RPS da Prefeitura: Verificar que a tag do número 28 se torna obrigatório quando o município de prestação é diferente do município do Cliente. Com isto é necessário preencher as tags 29, 30, 31, 32, 33, 34 e 35 que são geradas de acordo com os campos citados acima. |
| **Solução/Implementação:** | Regra implementada:  Para a geração de movimento do Educacional no regime de caixa ou competência o sistema vai verificar se para o tipo de movimento os campos complementares abaixo estão parametrizados.   * Tipo do Endereço (TIPOENDPREST      Tipo: Texto      Tamanho: 10 * Endereço (ENDPREST                            Tipo: Texto      Tamanho: 60) * Número (NUMPREST                              Tipo: Texto      Tamanho: 9) * Complemento (COMPLPREST              Tipo: Texto        Tamanho: 60) * Bairro (BAIRPREST                                  Tipo: Texto        Tamanho: 40) * Cep (CEPPREST                                      Tipo: Texto          Tamanho: 8)   Se os campos complementares acima estiverem parametrizados no tipo de movimento, o sistema vai verificar se o município do responsável financeiro(cliente) da parcela para o regime de caixa é diferente do município da Filial e para o regime de competência se o município do responsável financeiro do contrato ou aluno é diferente do município da Filial, se sim, o Educacional vai copiar automaticamente durante a geração de movimento as informações do endereço da Filial para os respectivos campos complementares parametrizados.  Observações:  - Os campos complementares criados no movimento devem seguir exatamente a nomenclatura citada acima (nome, tipo e tamanho).  Para mais informações consulte o Wikihelp <http://wikihelp.totvs.com.br/WikiHelp/EDU/EDU.nfe.aspx> |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
| **Pacote:** | Informe o [linkdopacote] |
