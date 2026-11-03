---
content_hash: cc8c0b0e7ad8e5521dd3fcfc6b69ddd2659d4e709831ba5d386607564f8c95ba
fetched_at: '2026-06-29T00:08:42.986033+00:00'
page_id: '301179058'
product: rm
source: tdn-rm
title: RMFIS00001_Geração da GIA SP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301179058
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 11.82 - 12.1.x |
| **Ocorrência:** | Informações sobre a tela de geração da GIA SP |
| **Ambiente:** | Corpore RM |
| **Passo a passo:** | Para gerar a GIA SP acesse:     * RM Liber | Rotinas Legais | Rotinas Estaduais | Apuração do ICMS | Informe o Estado - São Paulo e a Rotina GIA.   OBS: Até o momento a GIA SP não foi migrada para a Nova MDI e por esse motivo deve ser gerada pelo executável do aplicativo RM Liber.exe (Delphi).   Por esta opção, o sistema irá gerar o arquivo em meio magnético para a Apuração do ICMS do Estado de SP, respeitando o layout pré definido.pela Secretaria deste Estado.     Na tela de geração da rotina serão apresentados os seguintes campos:    Campos:  **Arquivo Texto:** É possível informar o nome do arquivo texto a ser gerado pelo sistema, porém ele já vem preenchido automaticamente com o nome padrão GIA0800.PRF.    **Filial:** Informe a filial para a qual será gerada a guia.    **Tipo de Apuração:** As opções são: 1 - Gia Normal 2 - Gia Substitutiva 3 – Gia Coligada – Gerada    **Versão Pré-formatado:**  É possível informar o numero da versão para geração do arquivo, porém esse campo já vem preenchido automaticamente com a versão vigênte da GIA.    **Referência**: Informe o período para geração do arquivo  OBS::A referência associada poderá ser superior a um determinado período cadastrado, caso o campo Tipo de Regime da Empresa, informado em Cadastro de Filiais, for igual a **Regime por Estimativa.** Para tanto, o usuário deverá indicar no campo segundo campo de referência , qual a data final do período para geração da rotina.  Cadastros | Filial | Selecione a Filial | Anexos - Dados Fiscais.        **Consolidada**: Habilitando esse campo o sistema gera uma única GIA selecionando os Lançamentos Fiscais das Filiais que possuem mesma Inscrição Estadual e UF da Filial selecionada na tela da rotina.    **GIA já Transmitida:** Informe se a GIA já foi transmitida anteriormente ao Órgão da Secretaria da Fazenda    **ICMS Fixado p/ Período:** Informe o valor do ICMS fixado para o Período  **OBS.:** Este campo somente será editado se o campo Tipo de Regime da Empresa, informado no cadastro da Filial, for igual a **Regime por Estimativa.**    **Classificação de Municípios:** Informe a Classificação de Municípios que será utilizada na geração da rotina.  A Classificação de Município é cadastrada em Cadastros | Tabelas Auxiliares | Classificação de Município.      O campo será preenchido automaticamente de acordo com o cadastro de Classificação de Município informado em Opções | Parâmetros | Gerais/Tabelas | Rotinas Legais | Rotinas Estaduais | GIA (São Paulo) | Parâmetros Por Filial | Clique duas vezes na Filial | Classificação Estadual Municipio.          **Destino:** Marque onde deverá ser gerado o arquivo, se no drive A, B ou C.  **OBS.:** Na escolha do drive c: o arquivo gerado por esta rotina, será gravado no caminho indicado pelo campo “**Diretório Arq. Temporários”.**  Opções | Parâmetros | Gerais/Tabelas | Rotinas Legais | Rotinas Estaduais | GIA (São Paulo) | Dir. Arquivos Temporários.      Para correta geração do arquivo, deverá ser informado o **Regime da Empresa** em Cadastros | Filial | Selecione a Filial | Anexos - Dados Fiscais. |
| **Observações:** |  |
