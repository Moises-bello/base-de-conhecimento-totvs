---
content_hash: 14cb069483f6e9c4d0a3b02607157425ec99f4f6c965011831aa7d6d14d344a0
fetched_at: '2026-06-29T00:09:23.828087+00:00'
page_id: '422546141'
product: rm
source: tdn-rm
title: RMD - São Paulo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546141
version: 10
---

Para se beneficiar das deduções previstas no [A](https://www.prefeitura.sp.gov.br/cidade/secretarias/upload/arquivos/secretarias/financas/legislacao/Decreto-53151-2012.pdf)[rt. 31, inciso I, alínea "a" do Decreto 53.151/2012](https://www.prefeitura.sp.gov.br/cidade/secretarias/upload/arquivos/secretarias/financas/legislacao/Decreto-53151-2012.pdf), o prestador de serviços de construção civil deverá inicialmente registrar os documentos fiscais que comprovem as deduções de materiais incorporados ao imóvel, com a identificação do número de inscrição no Cadastro de Obras de Construção Civil.

Embasamento Legal

* [Manuais](http://nfpaulistana.prefeitura.sp.gov.br/Nfe/empresas/informacoes-gerais/manuais)

**Parametrização**

**Filial**: Parametrizar a Filial para Emitir Livro de Construção Civil.

**Número de Inscrição da Obra**: Será gerado com o valor do campo complementar "Número de Inscrição da Obra" (NUMINSCOBRA), que deve ser criado no Projeto.

**Criação do campo complementar no cadastro de Projetos**:  
Nome da Coluna: NUMINSCOBRA  
Tipo: Alfanumérico  
Tamanho: 15  
Tipo texto: Texto O Projeto deve ser preenchido na Situação Tributária do Lançamento Fiscal, Tela "Prestação de Serviços".  
Observação: Caso não tenha sido preenchido o campo Complementar, o sistema gerará o Código do Projeto, conforme era o comportamento anterior.

**Seleção dos Dados**

Selecionar somente os Lançamentos de Entrada cuja a Natureza (CFOP) associado, esteja com o Campo "Classificação Operações Construção Civil" - na Pasta "Dados C.Civil", parametrizado.  
Selecionar somente Lançamentos Fiscais que tenho Projeto associado "Situação Tributária – Sub Pasta Prestação de Serviço".

**Geração da Rotina**

1. Importar Layout RMD no Gerador de Saídas no TOTVS Gestão Fiscal;
2. Após a importação do layout, acesse a tela de geração da rotina e preencha os dados;
3. O arquivo vai ser gerado na pasta Saídas, exemplo: C:\totvs\CorporeRM\RM.Net\Saídas
