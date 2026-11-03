---
article_id: 9607092232599
category: Gestão de Transportes (TMS)
content_hash: 4623735bf9f92da0c1e732bd8ca86284438c29c94ca6fc561eeceb6745c6fd74
fetched_at: '2026-06-28T22:45:27.586450+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: 'Logística - Linha Protheus - TMS - Contrato de Carreteiro Com Retenção INSS '
type: support-article
updated_at: '2022-10-18T18:38:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9607092232599-Log%C3%ADstica-Linha-Protheus-TMS-Contrato-de-Carreteiro-Com-Reten%C3%A7%C3%A3o-INSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:25 min** **Dúvida**Como gerar Contrato de Carreteiro com Retenção de **INSS - Instituto Nacional do Seguro Social** no **TOTVS Logística TMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**

A retenção do valor do INSS era tratada pelo **TOTVS Logística TMS** por meio do campo **DTR\_INSRET - INSS Retido** na rotina **TMSA240 - Complemento de Viagem**, quando o tipo de frota do veículo é **terceiro** ou **agregado**. Quando o tipo de frota é **própria**, processo não habilitado.  
  
Seguindo a atualização do Módulo Financeiro o campo de **INSS Retido** por viagem **não será mais utilizado**, sendo necessário a partir de Setembro 2022, informar no **FINA027 - Cadastro de Retenções Prévias** **INSS**.  
  
Para utilizar este processo no **TOTVS Logística TMS**, é indicado que esteja com seu ambiente atualizado com o seguinte pacote, datado de 07/10/2022 ou fontes posteriores: 

* 12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1084093>;
* 12.1.33: <https://suporte.totvs.com/portal/p/10098/download?e=1084094>;
* 12.1.2210: <https://suporte.totvs.com/portal/p/10098/download?e=1084095>;

**Saiba mais**Exemplo de Utilização Contrato de Carreteiro Com Retenção INSS: [Exemplo de Utilização Contrato de Carreteiro Com Retenção INSS (TMSA250 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=714227582)  
FINA027 - Cadastro de Retenções Prévias INSS: [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA027 - Cadastro Previa de INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021009912-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA027-Cadastro-Previa-de-INSS)
