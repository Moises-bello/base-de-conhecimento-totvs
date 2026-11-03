---
content_hash: 09ae0a90f617362126d8186ebc3ecc977d8c6bc2d6e5596eb6398c29743b9e98
fetched_at: '2026-06-29T00:10:47.815127+00:00'
page_id: '560653923'
product: rm
source: tdn-rm
title: Grupo específico para obras (construcao)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653923
version: 33
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **construcao** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **G** | **0-1** | **Grupo com informações de construção** |  | **O Grupo será preenchido conforme informações do Projeto, que pode ser informado no movimento ou no Item do movimento.**  Para habilitar o vínculo do projeto, acesse *Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > Etapa 72 - Projeto > Informa Projeto/Tarefa*. |
| codigoobra | construcao | E | 0-1 | CNPJ do projeto associado ao movimento, é necessário que o CNPJ seja um CEI valido | MPRJ.CGC | Especificamente para Rio de Janeiro:  Se houver um CEI válido, este será o valor do campo.  SE o campo complementar 'CODOBRAPREF' estiver preenchido, e não houver um CEI válido o valor deste campo será levado para a tag. Como criar o campo complementar... No Módulo Construção|Obras e Projetos acesse o menu:  Cad. Gerais|Campos Complementares|Projeto  **Criar campo complementar com os seguintes dados:**  **Nome da Coluna** = CODOBRAPREF **Tipo** = Alfanumérico **Subtipo** = texto   SENÃO Se o código do projeto estiver preenchido com valor diferente de 'COI' e o CEI for inválido, preenche com 'CO' + código do projeto.  Para todos os outros municípios que não sejam Rio de Janeiro: esta tag será preenchida a partir do campo CNPJ do projeto. |
| cCIB | construcao | E | 0-1 | Cadastro Imobiliário Brasileiro | MPRJ.CIB |  |
| art | construcao | E | 0-1 | Código Art. do projeto | MPRJ.ART | SE o ART do serviço da nota estiver vazio preenche com o campo ART do projeto, OU com o campo ART da nota. SENÃO, preenche com o ART do serviço da nota. |
| tipoobra | construcao | E | 0-1 | Código do tipo da Obra | MPRJCOMPL.TIPOOBRA | Criar campo complementar TIPOOBRA no projeto |
| xLogObra | construcao | E | 0-1 | Logradouro | MPRJ.RUA |  |
| xComplObra | construcao | E | 0-1 | Complemento Obra. | MPRJ.COMPLEMENTO |  |
| vNumeroObra | construcao | E | 0-1 | Número Obra. | MPRJ.NUMERO |  |
| xBairroObra | construcao | E | 0-1 | Bairro Obra. | MPRJ.BAIRRO |  |
| xCepObra | construcao | E | 0-1 | CEP Obra. | MPRJ.CEP |  |
| cCidadeObra | construcao | E | 0-1 | Código IBGE Cidade Obra. | MPRJ.CODMUNICIPIO |  |
| xCidadeObra | construcao | E | 0-1 | Nome Cidade Obra. | MPRJ.CIDADE |  |
| xUfObra | construcao | E | 0-1 | UF Obra. | MPRJ.ESTADO |  |
| cPaisObra | construcao | E | 0-1 | Código País Obra. | MPRJ.IDPAIS |  |
| xPaisObra | construcao | E | 0-1 | Nome País Obra. | MPRJ.PAIS |  |
| numeroArt | construcao | E | 0-1 | NúmeroART. | MPRJ.ART |  |
| numerocei | construcao | E | 0-1 | Código do CEI. Cadastro específico do INSS. | MPRJ.CGC ou GFILIAL.CGC | Apesar de existir um campo de CNO que substitui o CEI na REINF, para NFS-e o sistema não considera o CNO e busca o número CEI do campo CNPJ do cadastro de projeto. |
| numeroProj | construcao | E | 0-1 | Número Projeto. |  | Não será gerado |
| numeromatri | construcao | E | 0-1 | Número da Obra. Código que representa a matrícula da obra no sistema de cadastro de obras. | MPRJCOMPL.NUMINSCOBRA | Criar campo complementar NUMINSCOBRA no projeto |
| numeroEncap | construcao | E | 0-1 | Número Encap. |  | Não será gerado |
| *inscmunobra* | construcao | E | 0-1 | Inscrição Municipal da Obra. Caso o obra não seja do município preencher com 000000000 (9 ZEROS), caso a obra seja do município preencher com a Inscrição Municipal da obra formatada Seguindo Anexo 09. | MPRJCOMPL.INSCMUNOBRA | Criar campo complementar INSCMUNOBRA no projeto  Caso a obra não seja do município preenche a tag com 000000000 (9 ZEROS), caso a obra seja do município preenche com a Inscrição Municipal da obra.  Para o correto funcionamento do sistema é necessário que o CNPJ e o endereço do Projeto estejam preenchidos em Construção => Obras e Projetos => Projeto.  Também é essencial preencher o campo "Informa Projeto/Tarefa", localizado em Ambiente => Parâmetros => Gestão de Estoque => Etapa 72 - Projeto |
| *codservobra* | construcao | E | 0-1 | Código do serviço de construção civil prestado de acordo com o Anexo 09. | MPRJCOMPL.CODSERVOBRA | Serviço Obra  Criar campo complementar CODSERVOBRA no projeto, com tamanho e tipo descrito no manual |
| *alvara* | construcao | E | 0-1 | Alvará |  | Não será gerado |
