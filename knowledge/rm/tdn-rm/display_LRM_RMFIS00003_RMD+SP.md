---
content_hash: 3f91014c2ca2e49c3266c09abea9f346c27e9c24c146cafa9246d01c6786f75b
fetched_at: '2026-06-29T00:08:50.086815+00:00'
page_id: '331862251'
product: rm
source: tdn-rm
title: RMFIS00003_RMD SP
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00003_RMD+SP
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Fiscal |
| **Versões:** | 12.x |
| **Ocorrência:** | Geração da rotina RMD de SP |
| **Ambiente:** |  |
| **Passo a passo:** | Para se beneficiar das deduções previstas no art. 31, inciso I, alínea “a” do Decreto 53.151/2012, o prestador de serviços de construção civil deverá inicialmente registrar os documentos fiscais que comprovem as deduções de materiais incorporados ao imóvel, com a identificação do número de inscrição no Cadastro de Obras de Construção Civil.  <http://nfpaulistana.prefeitura.sp.gov.br/Nfe/empresas/informacoes-gerais/manuais>    **Parametrização**  Nos parâmetros a opção "Emitir Livro de Construção Civil" deverá estar marcada.    Ambiente/ Parâmetros/ Totvs Gestão Fiscal/ Identificação de regras / ISS - 03.01.03/ Regras ISS por filial / Edite a filial em questão        **Número de Inscrição da Obra**    Deverá criar o campo complementar “Número de Inscrição da Obra” (NUMINSCOBRA). Este campo deve ser criado no Projetos.    Acesse o módulo Projetos e em Cad Gerais faço o cadastro conforme orientações abaixo:         Dados para a criação do campo  **Nome da Coluna:**NUMINSCOBRA  **Tipo:**Alfanumérico  **Tamanho:**15  **Tipo texto:**Texto        Acesse o projeto e preencha o campo complementar criado.      **Seleção dos Dados**  O sistema irá selecionar somente os Lançamentos de Entrada cuja a Natureza (CFOP) informada esteja com o Campo "Classificação Operações Construção Civil" - na Pasta "Dados C.Civil", parametrizado.        E serão selecionados somente Lançamentos Fiscais que tenham o Projeto informado na "Situação Tributária – Sub Pasta Prestação de Serviço".  Será preenchido na rotina o valor informado no campo complementar. Caso não esteja preenchido, será gerado na rotina o código do projeto associado no lançamento.        **Geração da rotina:**  Importar Layout RMD no Gerador de Saídas do Gestão Fiscal (Liber)    Após a importação do Layout acesse a Tela de geração da rotina e preencha os dados.      O arquivo será gerado na pasta Saídas.  Exemplo: C:\totvs\CorporeRM\RM.Net\Saídas |
| **Observações:** |  |
