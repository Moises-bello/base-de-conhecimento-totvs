---
article_id: 360039344333
category: Ativo Fixo - Solicitação Baixa ou Transferência
content_hash: 80423e468a0afd9dd8268f4fdbf8fcf44c6b72373aea1b369c5d6ebc51cb8fdc
fetched_at: '2026-06-28T22:41:49.100487+00:00'
product: protheus
section_id: 1500001547622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA125/ATFA126 - Solicitação
  de baixa ou transferência parâmetros MV_ATFWFM e MV_ATFWBX
type: support-article
updated_at: '2022-08-24T14:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039344333-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA125-ATFA126-Solicita%C3%A7%C3%A3o-de-baixa-ou-transfer%C3%AAncia-par%C3%A2metros-MV-ATFWFM-e-MV-ATFWBX
---

**Dúvida**Solicitação de baixa ou transferência parâmetros MV\_ATFWFM e MV\_ATFWBX

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo fixo  – A partir da versão 11  
  
**Solução**A utilização de workflow na execução das rotinas ATFA125 e ATFA126,  além dos parâmetros (MV\_ATFWFM e MV\_ATFWBX) é preciso configurar outros parâmetros como:

MV\_ATFRESP

MV\_ATFASBX

MV\_ATFASTR

MV\_ATFAAPS

MV\_ATFURL

Para este processo não é obrigatório a integração com o fluig.

Para aprovação não é preciso  acessar o Protheus, pois após as configurações necessárias, será enviado e-mail, ao aprovador que retorna, aprovando ou não a solicitação.

Os parâmetros abaixo são configurados com a localização e nome do arquivo modelo  HTML

MV\_ATFASBX

MV\_ATFASTR

MV\_ATFAAPS

Ex: C:\PROTHEUS\Protheus\_data\workflow\workflow html\SolBxAprovac.htm

**Saiba Mais**

Link de acesso ao boletim de controle para solicitação de baixa e transferência de ativo

<https://tdn.totvs.com/pages/releaseview.action?pageId=44401528>

[Solicitação de Baixa ou Transferência (ATFA125 - SIGAATF)](https://tdn.totvs.com/pages/viewpage.action?pageId=312159973)
