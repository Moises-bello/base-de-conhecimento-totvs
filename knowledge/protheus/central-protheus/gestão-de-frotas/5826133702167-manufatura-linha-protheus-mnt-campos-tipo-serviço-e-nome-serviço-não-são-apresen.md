---
article_id: 5826133702167
category: Gestão de Frotas
content_hash: e8f24dc9f788121dee00138bb2f373d3760f4073731c509679a36c8612d07aa7
fetched_at: '2026-06-28T22:42:39.319603+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Campos Tipo Serviço e Nome Serviço não
  são apresentados S.S. - Solicitação de Serviço
type: support-article
updated_at: '2024-06-20T11:53:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5826133702167-Manufatura-Linha-Protheus-MNT-Campos-Tipo-Servi%C3%A7o-e-Nome-Servi%C3%A7o-n%C3%A3o-s%C3%A3o-apresentados-S-S-Solicita%C3%A7%C3%A3o-de-Servi%C3%A7o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Como realizar a configuração para que os campos **Tipo Serviço** e **Nome Serviço** sejam apresentados nas rotinas de **Solicitação de Serviço – MNTA280** e na rotina de **Distribuição de S.S. – MNTA295**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - A partir da versão **12.1.33****Solução**Com a migração para a **Release 12.1.33** e a segmentação dos processos de **Gestão de Frotas** - **SIGAGFR**, os campos **Tipo Serviço** **- TQB\_CDSERV** e **Nome Serviço** **- TQB\_NMSERV**, precisam de um ajuste manual no dicionário para serem habilitados no **SIGAGFR**, realize o seguinte procedimento:

* Acesse o módulo **Configurador** **- SIGACFG**, em **Base de Dados/Dicionário/Base de Dados** busque pela tabela **TQB - Solicitação de Serviço** e utilize a opção **alterar**.

![dic_dados.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5825898436375/dic_dados.PNG)

* Busque pelo campo **TQB\_CDSERV**, utilize a opção de **alterar**, na aba de **Módulos** marque a opção de **Utilizado por todos os módulos** e utilize a função **Salvar**.

![TQB_CDSERV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5825936386327/TQB_CDSERV.png)

* Realize o mesmo processo no campo **TQB\_NMSERV**, buscando pelo campo, utilize a opção de **Alterar**, na aba de **Módulos** marque a opção de **Utilizado por todos os módulos** e utilize a função salvar.

![TQB_NMSERV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5825993108759/TQB_NMSERV.png)

* Utilize a função de **Confirmar**.

![confirmar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5825980440855/confirmar.PNG)

* E por fim utilize a opção de **Atualizar base de dados**.

![atualizar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5826018886807/atualizar.PNG)

**Saiba mais**Para informações complementares verifique o *link* [13151483 DNG-15472 DT Ajuste para que o campo Tipo Serviço e Nome Serviço estejam habilitados no SIGAGFR](https://tdn.totvs.com/pages/releaseview.action?pageId=656829134)
