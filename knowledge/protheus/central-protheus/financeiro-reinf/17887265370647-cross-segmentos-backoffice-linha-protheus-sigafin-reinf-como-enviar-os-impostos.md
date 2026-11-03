---
article_id: 17887265370647
category: Financeiro - Reinf
content_hash: ae2182fe655196f4c918cd77604be7a39d365ec2f22f1ffc7747b0602598109e
fetched_at: '2026-06-28T22:37:51.788796+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Como enviar
  os impostos IR, PIS, COFINS e CSLL agregados no bloco 40
type: support-article
updated_at: '2024-09-19T17:39:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17887265370647-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Como-enviar-os-impostos-IR-PIS-COFINS-e-CSLL-agregados-no-bloco-40
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17888167008535)**Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Na integração do bloco 40 com o TAF (rotina Extrator Fiscal) os impostos IR, PIS, COFINS e CSLL são enviados de forma individual, porém existe a possibilidade desses tributos serem enviados de forma agregada?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - REINF - Todas as versões

**Solução**

Foi ajustada a rotina **Extrator Fiscal (ExtFisxTaf)**, através do programa **FINA989 (componente do** **SIGAFIN)**, para que os dados possam ser enviados ao TAF agregando os impostos.

Para isso, deve ser configurado o parâmetro abaixo:

**MV\_RNFAGRE**:

**Descrição:** Define quais os tributos do **bloco 40 da EFD-Reinf** serão agregados na extração dos dados para o **TAF.**

**Tipo:** Caracter

**Conteúdos validos:**

**0=**Não agregar (padrão)**;**

**1=**Agregar PIS, COFINS e CSLL (CSRF)**;**

**2=**Agregar IR, PIS, COFINS e CSLL (COSIRF);

**Importante**

O parâmetro **MV\_AG10925** permite aglutinar o**PIS/COFINS/CSLL** na geração dos títulos do tipo **TX** do **código de retenção** **5952**, porém não terá impacto na geração dos dados do **REINF**. Para refletir no **REINF** deve ser ajustado o parâmetro**MV\_RNFAGRE**;

Escolher uma natureza de rendimento que esteja configurada para agregar;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18702999604503)

Outro ponto crucial: Após ajustar o parâmetro, o sistema acatará apenas para novos registros que não foram processos pelo extrator. Caso os registros tenham sido enviados separadamente e seja necessário reenviá-los, uma opção é gerar o Extrator Fiscal em formato TXT para importação manualmente através da rotina de importação de arquivos do módulo **Totvs Automação Fiscal**.

Para reenviar as informações, gerar o **arquivo TXT** através do **Extrator Fiscal**

![Gravar_2024_06_26_11_37_14_708.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24452133529367)

E importar o **TXT** pela rotina Importação de arquivos (**TAFA500**)

![Gravar_2024_06_26_11_33_49_926.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24452139225623)

Se os registros já foram transmitidos para a Receita e você precisa de orientação para reabri-los ou retransmiti-los com as informações agregadas, por favor, entre em contato com a equipe **Protheus REINF** para receber orientações do módulo TAF.

**Saiba mais:**

[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)

[FAQ - 0019 - Como enviar os impostos com valor agregado (CSRF/COSIRF)?](https://tdn.totvs.com/pages/viewpage.action?pageId=790658698)

[EFD-REINF - Evento R-4020 - Regras de Preenchimento das tags vlrAgreg e vlrBaseAgreg](https://tdn.totvs.com/display/ConSeg/EFD-REINF+-+Evento+R-4020+-+Regras+de+Preenchimento+das+tags+vlrAgreg+e+vlrBaseAgreg)
