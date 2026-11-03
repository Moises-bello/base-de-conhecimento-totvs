---
content_hash: 63778a932a0afdc3250a3178c99080292dfdc6c5b7579e25cd6145aa0d64ba68
fetched_at: '2026-06-29T00:08:31.725394+00:00'
page_id: '273307181'
product: rm
source: tdn-rm
title: NFE0033_NF-e_Produtor Rural – Contra Nota
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273307181
version: 4
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.16 |
| **Ocorrência:** | Contra Nota |
| **Passo a passo:** | **Introdução:**  Este documento tem por finalidade auxiliar a emissão da NF-E Contra Nota para os produtores rurais. Conforme a regra de negocio de cada empresa, deverá ser realizado a emissão de um movimento referente a NF de entrada (emitida pelo produtor rural), que será referenciada na emissão da NF-E Contra Nota.  **Parametrizações Cliente/Fornecedor**  No cadastro do cliente / Fornecedor, é necessário realizar o preenchimento básico, como o CPF, Inscrição Estadual, endereço. Para este processo, obrigatoriamente, deve selecionar na aba Dados Fiscais, sub aba outros Dados, que o mesmo é Produtor rural, conforme a imagem:      **1 . Parametrizações do Tipo de Movimento de Entrada (emitido pelo produtor rural)**  Especificamente para este processo, é necessário selecionar um tipo de documento que tenha o código do modelo do documento “04” (NF Produtor Rural) selecionada nos parâmetros do tipo de movimento, etapa FIS - Escrituração 1/2. Para selecionar o tipo de documento default, o parâmetro referente a Gerar Escrituração deve estar marcado:    **2 . Parametrizações do tipo de movimento NF-E – Contra Nota**  Primeiramente, deve ser realizada a parametrização da NF-E de entrada, conforme documento: [NFE0010\_Parametrizar\_movimento\_de\_entrada\_para\_a\_emissao\_de\_NF-e](http://tdn.totvs.com/display/LRM/NFE0010_Parametrizar_movimento_de_entrada_para_a_emissao_de_NF-e)   Após as parametrizações, selecione na etapa MOV – OUTROS DADOS, o motivo de referência “ 24 – NF-e Produtor Rural - Contra Nota “.      **3 . Gerar movimento NF-E - Contra Nota**  Como o movimento deverá ter as referencias da NF gerada pelo produtor rural, basta acessar o menu Processos, Assistente por copia por referência, filtrando o movimento referente a NF do produtor rural conforme a imagem:    Selecionar o tipo de movimento que deu entrada na nota de Produtor Rural:          Após preencher as devidas informações do movimento que foi gerado a referência, após salvar e efetuar o envio da NF-e.      Verificando o XML da nota que será emitida , pode ser verificado que foi gerado o grupo de informações:          **Reprodução do manual de orientação do contribuinte com o significado dos campos:**  Grupo refNFe:     Grupo refNF: |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
