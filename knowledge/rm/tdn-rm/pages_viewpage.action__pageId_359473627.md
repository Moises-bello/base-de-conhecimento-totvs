---
content_hash: 9cb2720499368a6fcda8ef6df77827e83e8935f2168c6a0f6ea29d102b09b0e0
fetched_at: '2026-06-29T00:08:58.123125+00:00'
page_id: '359473627'
product: rm
source: tdn-rm
title: 'RM - Erro: "Ocorreu erro que impediu a execução do processo. System.Exception:
  Não foi possível fazer a integração do lote com o TAF.  Código erro TAF: 803..."'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=359473627
version: 7
---

Erros e AçõesErro

Erro: Ocorreu erro que impediu a execução do processo. System.Exception: Não foi possível fazer a integração do lote com o TAF. Código erro TAF: 803.

Descrição erro TAF: O valor do campo sourceBranch (TAFFIL) não está cadastro no complemento de empresas.  
 em RM.Fop.Esocial.FopEsocialIntegrarTafMod.Enviar(Int16 codColigada, String codUsuario, List`1 eventosList, RMSExecProgress progress, RMSServerLog log, Int32& numErros, Int32& totalIntegracaoTaf, String ticketCode, DateTime dataIntegracao)

Ação

Ação:

* Acesse o cadastro de "Complemento Cadastral" do TAF e verifique qual é o Cod.Filial que está informado no registro:

* Acesse o Parametrizador do RM e verifique qual é Código da Filial TAF que está informado:

* O código da filial informado no Parametrizador deve ser o mesmo informado no cadastro do Complemento Cadastral do TAF no campo Cod.Filial:

Maiores informações:
