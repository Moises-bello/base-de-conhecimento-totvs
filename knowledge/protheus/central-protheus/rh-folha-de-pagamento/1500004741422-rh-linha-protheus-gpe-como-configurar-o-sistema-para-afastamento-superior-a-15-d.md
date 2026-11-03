---
article_id: 1500004741422
category: RH - Folha de Pagamento
content_hash: a03a6b90c94469353e681f2754fa940dd68f2f9e4a3d484e100311de093280e4
fetched_at: '2026-06-28T22:44:13.324187+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o sistema para afastamento superior
  a 15 dias
type: support-article
updated_at: '2025-12-29T20:30:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004741422-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-afastamento-superior-a-15-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26334428832663) Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**  
Como configurar o sistema para afastamento superior a 15 dias  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Efetuado adaptação do sistema conforme o [Parecer SEI Nº 16120/2020/ME](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-) nos cálculos de folha e rescisão para que haja dedução na contribuição previdenciária patronal, contribuição de terceiros e SAT/RAT, além do desconto do INSS do segurado, referente aos 15 primeiros dias de afastamentos iniciados a partir de 01/10/2020 que resultem na concessão do benefício de auxílio-doença.

Para isso, será necessário alterar os tipos de ausências padrão e informar uma verba no novo campo **Verba Sup. (RCM\_PDSUP)** - verificar observação em destaque abaixo, que deverá ser baseada na verba padrão de pagamento do auxílio, mas **sem** incidência de INSS para folha (campo RV\_INSS) e incidência para o eSocial **00** (campo RV\_INCCP). Dessa forma, quando o afastamento tiver duração **igual ou inferior a 15 dias**, o sistema efetuará o pagamento do valor na verba informada em **Cod.Verba (campo RCM\_PD)**, mas caso seja **superior a 15 dias**ou o afastamento **não** possua data de retorno, o sistema efetuará o pagamento na verba informada em **Verba Sup. (RCM\_PDSUP)**. Como a verba informada em Verba Sup. (RCM\_PDSUP) não possui incidência para INSS para folha, o valor dessa verba não entrará para a base de INSS e automaticamente não será considerada no desconto de INSS do segurado, nem na contribuição previdenciária patronal, contribuição de terceiros e SAT/RAT.  
  
- **Criação da verba**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35162989504791)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35162989507479)

**Obs.:** No exemplo acima foi utilizado como exemplo o cadastro da verba para **Auxilio Doença**, esta deve ficar com FGTS = Sim. Para a configuração da verba de **Auxilio Acidente o FGTS deve ficar Não,** pois já esta configurado o FGTS integral dentro do cadastro de Tipo de Ausência.   
A aba eSocial deve ficar condizente com a aba Incidências.   
  
- **Atrelar no cadastro do Tipo de Ausência**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35163010776727)

Foi criado uma validação no Cadastro de Ausências para que caso seja incluído um afastamento com duração superior a 15 dias e com início a partir de 01/10/2020 referente a um tipo de ausência que não possua a verba informada no campo **Verba Sup. (RCM\_PDSUP)**, seja exibido uma mensagem solicitando confirmação se o cadastro poderá ser confirmado dessa forma mesmo ou se haverá revisão, retornando ao cadastro, uma vez que a orientação do governo é que os afastamentos superiores a 15 dias sejam informados ao eSocial em uma rubrica com **incidência CP 00**, lembrando que tal aviso é apenas uma sugestão, sem haver o bloqueio do cadastro.

Também foi criado o mnemônico **P\_DEDAFAS** para o controle do alerta:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006184762)  
  
Consulte exemplos de cálculo [aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=585672041#P_ENCEMPAF-P_ENCEMPAF1)

**Saiba Mais**  
[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Como deve ser preenchido o novo campo RCM\_PDSUP (Verba Susp.) no cadastro do tipo de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007496002-RH-Linha-Protheus-GPE-Como-deve-ser-preenchido-o-novo-campo-RCM-PDSUP-Verba-Susp-no-cadastro-do-tipo-de-aus%C3%AAncia)  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
