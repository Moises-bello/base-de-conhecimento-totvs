---
content_hash: c36625cf344deb2853d1e6c540ce10bb81835c24e94ff4bc28a061cde03baab7
fetched_at: '2026-06-29T00:09:02.469264+00:00'
page_id: '379313790'
product: rm
source: tdn-rm
title: 1684309 FISCAL01-2550 DT EFD Contribuições F120, F130
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379313790
version: 1
---

# EFD Contribuições

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração do Arquivo EFD Contribuições |
| **Situação/Requisito:** | Ao gerar a rotina do EFD Contribuições, o sistema apresenta uma mensagem de inconsistência.  Esta mensagem está diretamente relacionada ao fato de não terem convertido o Gestão Patrimonial para o novo modelo de cálculo.  No ambiente da 12.1.18, não temos mais o executável do cálculo, em Delphi.    [15:08:36] Ocorreu um erro inesperado na geração. [15:08:36] [15:08:36] System.Exception [15:08:36] Erro: Erro ao carregar os dados do Ativo Imobilizado: Invalid object name 'IGRUPOCONTA'. [15:08:36] ====================================================== [15:08:36] at RM.Fis.Sped.FisSpedContextGeradorLoader.CarregaAtivoImob(FisSpedParams parametros, DataSet dataSet, String filtroFilial) |
| **Solução/Implementação:** | Na geração da EFD Contribuições para carregar os contextos dos registros F120 ou F130  será verificado se a coligada possui integração do Patrimônio (Bonum) com o Gestão Fiscal (Liber). |
| **Requisito:** | FIS000385 |
| **Documento de Referência:** | [WikiHelp Bloco F](http://wikihelp.totvs.com.br/WikiHelp/FIS/Fis.BlocoF.aspx) |
