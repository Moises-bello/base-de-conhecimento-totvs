---
content_hash: 0392260c15480aa73e94b2209de5f6f857b5b2c5d036b2db9b5f2c1821d7731c
fetched_at: '2026-06-29T00:09:55.166159+00:00'
page_id: '447088004'
product: rm
source: tdn-rm
title: 4392401 FISCAL01-7457 DT EFD Contribuições Registro I100 - Erro CarregarFiltroTributoContaContabil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=447088004
version: 4
---

# EFD Contribuições Registro I100 - Erro CarregarFiltroTributoContaContabil

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Gerar a Rotina EFD Contribuições |
| **Situação/Requisito:** | Ao gerar o EFD Contribuições é apresentado a seguinte mensagem:  [19:02:34] ====================================================== [19:04:17] ====================================================== [19:04:17] Ocorreu um erro inesperado na geração. [19:04:17] [19:04:17] RM.Lib.RMSValidateException [19:04:17] Erro: Erro ao carregar os dados do processo Filtro do Tributo. Motivo: As colunas pai e filho não têm colunas de tipo correspondente. [19:04:17] ====================================================== [19:04:17] em RM.Fis.RotinasFiscais.Federais.FisGeracaoDadosEFD\_PisCofins.CarregarFiltroTributoContaContabil(Int32 codColigada) em RM.Fis.RotinasFiscais.FisGeradorSaidasModule.GetOperacoesInstitucionais() em RM.Gen.Runtime.GenRuntimeModule.OnExecute(List`1 files) em TNF.Gen.Runtime.RuntimeModule.Execute() [19:04:17] ====================================================== [19:04:17] Geração concluída com erros. Duração: 0:1:43,158 |
| **Solução/Implementação:** | Na geração do EFD contribuições registro I100 foi incluída uma consistência para execução em bases Oracle. Será convertido CODCOLIGADA e IDFILTROTRB em para o tipo NUMBER quando for realizado referencia entre as tabelas de filtros de tributos (Cadastro do processo), filtro da conta contábil e filtro de histórico contábil garantindo que os tipos sejam correspondentes.  Tabelas: DFILTROCONTA, DFILTROTRIBUTO, DFILTROHISTCONTABIL |
