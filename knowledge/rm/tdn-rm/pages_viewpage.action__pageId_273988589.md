---
content_hash: 1aaa631d0660335ccd9ec78dd6aec4a8788fac70ad4f63ad73d19c6be4e49c87
fetched_at: '2026-06-29T00:08:32.478861+00:00'
page_id: '273988589'
product: rm
source: tdn-rm
title: RMFIS00001_CAT 79/2003 - Convênio 115
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273988589
version: 9
---

# Assunto

|  |  |  |
| --- | --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |  |
| **Versões:** | 12.1.x |  |
| **Ocorrência:** | CAT 79/2003 - (Convênio 115) Energia Elétrica e Telecomunicações |  |
| **Ambiente:** |  |  |
|  |  |  |
| **Passo a passo:** | Os passos a seguir servirão de auxílio para a geração da CAT 79/2003 (Convênio 115) onde são gerados os arquivos Mestre, Item e Destinatário referentes aos lançamentos fiscais de Energia Elétrica e Telecomunicações.     **Parametrização**  Primeiramente, devemos conferir o local onde o sistema salvará os arquivos gerados pela rotina. Nos Parâmetros do Fiscal, defina o diretório para a geração dos arquivos etapa Rotinas Legais – Rotinas Estaduais – Diretório de Arquivos Temporários.      **Tela de Geração**  Para gerar a rotina, acesse o menu **“Obrigações Acessórias | Estaduais | Convênio ICMS 115/2003.**  Preencha os dados na tela: Filial, Período/Intervalo de Geração e a Situação do Arquivo(Normal ou Substituto). Informe também a Rotina Fiscal, previamente cadastrada, contendo os *Valores Campos x Rotinas*, como Tipo de Ligação, Tipo de Utilização, Grupo de tensão e etc.  Selecione o parâmetro *Calcular Código de Autenticação Digital do Documento Fiscal*, caso o Lançamento não esteja com este campo calculado.        **Arquivos Gerados**  Após a execução do processo, os arquivos *Mestre* de Documentos Fiscais, Itens dos lançamentos e Destinatários de Documentos Fiscais serão salvos na pasta do diretório temporário. Os arquivos são gerados conforme nomenclatura descrita na Legislação  da CAT 79/2003.    **Seleção dos Lançamentos**  Serão selecionados todos os documentos fiscais de Saída, nos quais, o código de modelo do documento(Tipo de Documento |Aba - Dados Adicionais)estão de acordo com as operações de Energia Elétrica e Telecomunicações(06, 21 e 22) e data do documento  dentro do período informado na tela de geração da Rotina.   **Especificação da rotina**   Especificação sobre a geração da rotina acesse:  Mais informações de geração de cada registro e campos acesse: [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.CAT.aspx) |  |
|  |  |  |
| **Observações:** |  |  |
