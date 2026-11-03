---
article_id: 4403541989783
category: TAF - REINF
content_hash: 7f670ea9b280712592faebfa881b4b8f9e68a8bb8748b08d8870ceb2556054f5
fetched_at: '2026-06-28T22:41:33.580892+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Procedimento Completo
  Reinf
type: support-article
updated_at: '2025-06-13T20:38:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403541989783-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Procedimento-Completo-Reinf
---

**Dúvida**Qual é o procedimento para geração da **Reinf** utilizando o **TAF** como módulo do **Protheus**?  
  
**Ambiente**A partir de 12.1.27  
  
**Solução**

 Para gerar a **Reinf** no **TAF**, é necessário efetuar a integração dos dados com o TAF e a apuração dos eventos e transmissão dos eventos, na seguinte ordem:

1º passo: Atualização do ambiente

[TAF - REINF - Atualização Completa Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-Reinf?source=search)

2° passo: Wizard de Configuração

[TAF - REINF - Wizard Configuração do TAF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6172197751447-TAF-REINF-Wizard-Configura%C3%A7%C3%A3o-do-TAF-?source=search)

3° Configurar certificado digital

[Automação Fiscal - Configuração - Certificado Digital A1 - Como Efetuar Preparação do Certificado Digital e Configurá-lo no TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034159554-Automa%C3%A7%C3%A3o-Fiscal-Configura%C3%A7%C3%A3o-Certificado-Digital-A1-Como-Efetuar-Prepara%C3%A7%C3%A3o-do-Certificado-Digital-e-Configur%C3%A1-lo-no-TAF-?source=search)

4º passo: Integração TSI ou Extrator fiscal ( TSI não integra os layouts com informações do módulo financeiro, para bloco 40 recomendamos utilização do extrator fiscal).

[TAF - TSI - Como configurar o TSI (TAF Service Integration)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424759792151-TAF-TSI-Como-configurar-o-TSI-TAF-Service-Integration-?source=search)

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Configuração Extrator Fiscal para o Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422754983191-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Configura%C3%A7%C3%A3o-Extrator-Fiscal-para-o-Reinf?source=search)

5º passo: Complemento Cadastral

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como realizar o preenchimento do R-1000 no complemento cadastral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022208052-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-realizar-o-preenchimento-do-R-1000-no-complemento-cadastral)

6º passo: Apuração dos Eventos/ Transmissão dos Eventos.

[TAF - REINF - Procedimento de apuração e transmissão PAINEL REINF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6167421703447-TAF-REINF-Procedimento-de-apura%C3%A7%C3%A3o-e-transmiss%C3%A3o-PAINEL-REINF-?source=search)

**IMPORTANTE: Para integração(passo 3) deve ser realizado via TSI ou Extrator fiscal, somente pode ser utilizada uma das duas opções para não haver conflito, o TSI não integra informações de títulos/faturas lançados no financeiro.**

O **layout** da **REINF** atualmente em vigor é: 2.1, o parâmetro MV\_TAFVLRE precisa estar com o conteúdo 2\_01\_02

 A rotina **TAFXREINF** (Apuração dos Eventos) foi descontinuada na data 04/2022), sendo necessário a migração para a rotina **Painel** **Reinf**:

<https://tdn.totvs.com/display/public/TAF/Painel+REINF>

Como configurar o Painel Reinf: [TAF – REINF - Configuração Painel Reinf - Appserver](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409133202199-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-Reinf-Appserver?source=search)

Para mais informações, consulte: <https://tdn.totvs.com/display/public/TAF/EFD-Reinf>
