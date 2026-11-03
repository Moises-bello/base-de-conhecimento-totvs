---
article_id: 36976700440599
category: Gestão de Transportes (TMS)
content_hash: 7cc304813c687b05dcf6d9413450a1567aac6fd429c407210bbd3bbbf93b3940
fetched_at: '2026-06-28T22:45:32.571867+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 318 - Valor do IBS UF difere do
  calculado
type: support-article
updated_at: '2026-05-15T11:22:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36976700440599-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-318-Valor-do-IBS-UF-difere-do-calculado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36976700418071) Tempo aproximado para leitura: **00:02:10 min**  
  
**Ocorrência**  
Ao transmitir o **CTe** contendo os tributos **CBS** e **IBS**, ocorre a rejeição **318 - Valor do IBS UF difere do calculado**.  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Causa**  
Segundo o manual da **SEFAZ** - CTe\_Nota\_Técnica\_2025\_001 - RTC\_v1.10, página 10, ocorre quando:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36977258487831)

No **XML** do **CTe**, teríamos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36977322500503)

Aplicando a fórmula matemática do manual do **SEFAZ**, o resultado na tag **vIBSUF** seria de 0,04, considerando o exemplo do **XML**.  
  
**Solução**  
Para solucionar essa rejeição, temos as seguintes possibilidades:  
  
1. No **Configurador de Tributos**, em **Regra de Cálculo - Documentos Fiscais**, o campo de **Configuração de Arredondamento** deve estar cadastrado como **1 - Arredonda**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36977869297687)

2. No **Configurador de Tributos**, em **Regra de Base de Cálculo**, no campo **Valor Origem**, utilize 11 - Fórmula Manual, e, na **Composição da Fórmula**, utilize **Valor da Mercadoria.**  
Para o **TMS**, o **Valor da Mercadoria** será o valor do campo **Valor do Frete - DT6\_VALFRE**. A orientação de uso desta base de cálculo parte da compreensão da **LEI COMPLEMENTAR Nº 214, DE 16 DE JANEIRO DE 2025, artigo 12** que diz: "A base de cálculo do **IBS**e da **CBS**é o valor da operação". O valor da base de cálculo do **IBS** e **CBS** não deve conter os valores de impostos, como **ICMS**, **PIS** e **Cofins**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36977855246359)

3. No **Configurador de Tributos**, em **Regra de Escrituração**, a escrituração do **CBS** e **IBS** deve estar configuradas como **Incidência -** **Isento** e **Total da nota - Sem Ação**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36978298350231)

4. Se estiver utilizando o **CTESEFAZ3** customizado, validar com o **RDMAKE** padrão disponível neste link - [Logística - Linha Protheus - TMS - RDMAKES para o CTe e MDFe](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXqoj6IhY6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBg2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzI0MzM5NDg3OTU5NzAzLUxvZyVDMyVBRHN0aWNhLUxpbmhhLVByb3RoZXVzLVRNUy1SRE1BS0VTLXBhcmEtby1DVGUtZS1NREZlBjsIVDoOc2VhcmNoX2lkSSIpZWI5MGJlYjUtYTZiOS00NzAxLWE1OTQtNzBmMzg0YzJlM2I0BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPdG1zIHJkbWFrZQY7CFQ6EnJlc3VsdHNfY291bnRpAsgD--ab9c0c64d8353506ef20a10da1a435fb518b0680).  
  
5. Segundo o manual da **SEFAZ**, existe a tolerância de 0,01 a mais ou a menos. No exemplo destacado no **XML** acima, temos a tag **vIBSUF** com o valor de 0,03, onde o valor esperado seria de 0,04, ou seja, dentro da margem de tolerância. Caso após os ajustes sugeridos, a diferença de 0,01 centavo e a rejeição persistirem, deve entrar em contato com o **SEFAZ** via consulta protocolada questionando este retorno.   
  
**Saiba mais**  
Documentação Configurador de Tributos do **Fiscal**: [CFGTRIB - Configurador de Tributos - P12](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+P12)  
Documentação do **TMS**sobre uso do Configurador no **TMS**: [Logística - Linha Protheus - TMS - Exemplo de uso do Configurador de Tributos no TMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32213798486167-Log%C3%ADstica-Linha-Protheus-TMS-Exemplo-de-uso-do-Configurador-de-Tributos-no-TMS)  
Documentação do **TMS**sobre os novos impostos no **XML**do **CTe**: [Logística - Linha Protheus - TMS - Como gerar CBS e IBS no XML do CTe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35970385689623-Log%C3%ADstica-Linha-Protheus-TMS-Como-gerar-CBS-e-IBS-no-XML-do-CTe)  
  
**Glossário**  
**CBS** - Contribuição sobre Bens e Serviços  
**CTe** - Conhecimento de Transporte eletrônico  
**IBS** - Imposto sobre Bens e Serviços  
**SEFAZ** - Secretaria da Fazenda  
**XML** - Extensible Markup Language
