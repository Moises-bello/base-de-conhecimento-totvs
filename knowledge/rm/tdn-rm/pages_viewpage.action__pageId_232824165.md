---
content_hash: c8e3d736895d71aff6e986513eef5f4bce7ba4f0146a9e9254619b7289b75832
fetched_at: '2026-06-29T00:06:27.521933+00:00'
page_id: '232824165'
product: rm
source: tdn-rm
title: INT0001_Faturamento_de_Movimento_Gerado_pelo_Solum_(TOTVS_Construção_e_Projetos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232824165
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 12.1 e superiores |
| **Ocorrência:** | Faturamento/Recebimento de Movimentos gerados do Solum |
| **Ambiente:** | Faturamento/Recebimento de Movimento |
| **Passo a passo:** | No momento de faturar um movimento no RM Nucleus que foi originado da integração com o RM Solum, a mensagem abaixo pode ser apresentada impedindo que o faturamento seja concluído:      O erro somente é apresentado quando os parâmetros dos tipos de movimento (Origem e Destino) estão divergentes. Os campos que o sistema consiste são:   * **USARETENCAOIT -** Etapa Itens Valores Financeiros 2/2 - Campo Utilizar Retenção      * **VERPRJTRF -** Etapa Projetos - Campo Informa Projeto/Tarefa     Para poder identificar de forma rápida, pode-se executar o select abaixo:  SELECT USARETENCAOIT, \* FROM TTMVEXT WHERE CODTMV = '1.1.04' OR CODTMV = '1.2.11' SELECT VERPRJTRF, \* FROM TITMTMV WHERE CODTMV = '1.1.04' OR CODTMV = '1.2.11'  Obs.: Os tipos de movimentos são meramente ilustrativos.    Portanto, basta igualar os parâmetros para que o erro não seja apresentado novamente. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
