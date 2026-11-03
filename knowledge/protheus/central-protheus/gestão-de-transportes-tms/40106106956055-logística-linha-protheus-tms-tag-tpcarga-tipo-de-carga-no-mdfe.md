---
article_id: 40106106956055
category: Gestão de Transportes (TMS)
content_hash: 5b6f2114524653fee47995d790a8cba8b42fa13404c2c0384ba1b72c766fd42a
fetched_at: '2026-06-28T22:45:27.203232+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS -  Tag <tpCarga> - Tipo de Carga no MDFe
type: support-article
updated_at: '2026-04-30T13:25:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40106106956055-Log%C3%ADstica-Linha-Protheus-TMS-Tag-tpCarga-Tipo-de-Carga-no-MDFe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40106106915991) Tempo aproximado para leitura: **00:01:20 min**  
  
**Dúvida**  
Como é preenchida a tag <**tpCarga> -Tipo de Carga** no **XML** do **MDFe**?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**  
A *tag* **tpCarga - Tipo de Carga** indica no **XML** do **MDFe** o tipo de carga do produto predominante com as opções:

* 01-Granel sólido;
* 02-Granel líquido;
* 03-Frigorificada;
* 04-Conteinerizada;
* 05-Carga Geral;
* 06-Neogranel;
* 07-Perigosa (granel sólido);
* 08-Perigosa (granel líquido);
* 09-Perigosa (carga frigorificada);
* 10-Perigosa (conteinerizada);
* 11-Perigosa (carga geral).

No **TMS**, a *tag* **<tpCarga>** é preenchida com base no tipo de operação da viagem.  
Se a viagem possui o campo **DTQ\_TPOPVG** - **Tipo de Operação da Viagem** preenchido, o Sistema busca o código desse registro na tabela **DLO - Tipo de Operação da Viagem** e utiliza o campo **DLO\_CODTPC - Codigo Tipo Carga ANTT** para preencher a *tag* **<tpCarga>**.  
Caso a viagem esteja com o campo **DTQ\_TPOPVG** - **Tipo de Operação da Viagem** em branco, o Sistema preenche a *tag* **<tpCarga>** com o valor padrão **05 - Carga Geral**.  
  
**Saiba mais**  
[DT Tipo de Operação da Viagem](https://tdn.totvs.com.br/pages/viewpage.action?pageId=425443149)  
  
**Glossário**  
**ANTT** - Agência Nacional de Transportes Terrestres  
**MDFe** - Manifesto de Documentos Fiscais eletrônico  
**XML** - *Extensible Markup Language*
