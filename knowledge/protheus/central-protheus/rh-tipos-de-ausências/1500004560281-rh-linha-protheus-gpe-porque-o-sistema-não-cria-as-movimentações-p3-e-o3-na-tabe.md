---
article_id: 1500004560281
category: RH - Tipos de Ausências
content_hash: 44ef7f60dfbc33daf108934eb5313be621fb5f6e1919eca0e2cca43a6e17926d
fetched_at: '2026-06-28T22:43:21.033633+00:00'
product: protheus
section_id: 360011967353
source: central-protheus
title: RH - Linha Protheus - GPE - Porque o sistema não cria as movimentações P3 e
  O3 na Tabela S046 para relacionar aos Tipos de Ausência
type: support-article
updated_at: '2025-08-15T12:18:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004560281-RH-Linha-Protheus-GPE-Porque-o-sistema-n%C3%A3o-cria-as-movimenta%C3%A7%C3%B5es-P3-e-O3-na-Tabela-S046-para-relacionar-aos-Tipos-de-Aus%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29455896534423) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Porque o sistema não cria as movimentações P3 e O3 na Tabela S046 para relacionar aos Tipos de Ausência?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.1.17.  
  
**Solução**Na rotina **Tipos de Ausência** é possível incluir apenas **um tipo** de movimentação por Tipo de Ausência, porém conforme *layout* da **Sefip**, para o mesmo afastamento, pode ter **mais** de uma **movimentação,** pois **até 15 dias** é considerada **uma** movimentação e **após o 15º outra** movimentação para afastamentos por acidente de trabalho e auxilio doença.  
  
Sendo assim, no padrão temos apenas as movimentações **P1** e **O1,** elas que devem ser **associadas** aos Tipos de Ausência por motivo de **auxilio doença** ou **acidente de trabalho,** dessa forma, o Sistema gera as movimentações da **Sefip** conforme o *layout* internamente na geração da Sefip, conforme dias de afastamento dos funcionários.

**Saiba Mais**

[RH - Linha Protheus - GPE - Campo Verba Sup - RCM\_PDSUP bloqueado para edição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005088861-RH-Linha-Protheus-GPE-Campo-Verba-Sup-RCM-PDSUP-bloqueado-para-edi%C3%A7%C3%A3o)  
[RH - Linha Protheus - GPE - Como criar o campo Verba Sup - RCM\_PDSUP no cadastro de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006379841-RH-Linha-Protheus-GPE-Como-criar-o-campo-Verba-Sup-RCM-PDSUP-no-cadastro-de-aus%C3%AAncia)  
[RH - Linha Protheus - GPE - Verba não aparece para ser selecionada nos campos de Verba do Tipo de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15114225514519-RH-Linha-Protheus-GPE-Verba-n%C3%A3o-aparece-para-ser-selecionada-nos-campos-de-Verba-do-Tipo-de-aus%C3%AAncia)  
[RH - Linha Protheus - GPE - Como configurar o sistema para afastamento superior a 15 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004741422-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-afastamento-superior-a-15-dias)  
[RH - Linha Protheus - GPE - Não aparece verba cadastrada para vincular ao Tipo de Ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15669629352343-RH-Linha-Protheus-GPE-N%C3%A3o-aparece-verba-cadastrada-para-vincular-ao-Tipo-de-Aus%C3%AAncia)  
[RH - Linha Protheus - GPE - Como é calculado o valor na verba de ID 1432 - Valor de afastamento por acidente pago pela Previdência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057227834-RH-Linha-Protheus-GPE-Como-%C3%A9-calculado-o-valor-na-verba-de-ID-1432-Valor-de-afastamento-por-acidente-pago-pela-Previd%C3%AAncia)  
[RH - Linha Protheus - GPE - Como deve ser preenchido o novo campo RCM\_PDSUP (Verba Susp.) no cadastro do tipo de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007496002-RH-Linha-Protheus-GPE-Como-deve-ser-preenchido-o-novo-campo-RCM-PDSUP-Verba-Susp-no-cadastro-do-tipo-de-aus%C3%AAncia)
