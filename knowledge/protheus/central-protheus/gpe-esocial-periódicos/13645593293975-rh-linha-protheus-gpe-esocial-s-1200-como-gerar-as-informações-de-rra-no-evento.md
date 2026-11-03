---
article_id: 13645593293975
category: GPE - eSocial - Periódicos
content_hash: 1a49db4314b384a51f3202c0c11fa1fb9c151071742bfbb8e7d248cf13ec4d87
fetched_at: '2026-06-28T22:45:07.708020+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar as informações de
  RRA no evento S-1200 referente ao calculo de dissidio retroativo
type: support-article
updated_at: '2024-06-19T18:13:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13645593293975-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-as-informa%C3%A7%C3%B5es-de-RRA-no-evento-S-1200-referente-ao-calculo-de-dissidio-retroativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como gerar as informações de RRA no evento S-1200 referente ao calculo de dissidio retroativo?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**De acordo com o **MOS Versão S-1.1**"Deve ser **considerado como RRA** tudo que for **pago e que se referir a competências de anos**  
**calendários anteriores ao do recebimento**. O RRA, a partir de 11 de março de 2015, está submetido à incidência do imposto sobre a renda com base na tabela progressiva, quando correspondentes a anos calendário anteriores ao do recebimento e são tributados exclusivamente na fonte, no mês do  
recebimento ou crédito, em separado dos demais rendimentos recebidos no mês.   
Neste sentido, em termos de eSocial o mês do recebimento ou crédito se refere ao perApur do S-1210, e os perRef do infoPerAnt discriminados no respectivo ideDmDev (identificado como RRA) do S-1200 compõem o período abrangido pela expressão “correspondentes a anos-calendário anteriores”. Deve ser lembrado que os **valores decorrentes de reclamatória trabalhista** devem ser informados em eventos específicos e **não no evento S-1200."**Para que o sistema gere as tag's de RRA corretamente no evento S-1200 referente ao cálculo de dissidio retroativo, devemos seguir os passos abaixo:  
  
**1º** Verificar o cadastro de verbas conforme documentação - [RH - Linha Protheus - GPE - Quais os identificadores de calculo para geração de RRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11279526271895)  
**2º** Cadastrar a tabela S034 - [RH - Linha Protheus - GPE - Como cadastrar a tabela S034 de IR para RRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10632803238679-RH-Linha-Protheus-GPE-Como-cadastrar-a-tabela-S034-de-IR-para-RRA-)  
**3º** Realizar o cadastro do Complemento Trabalhista   
**4º** Calcular o Dissidio Retroativo - [RH - Linha Protheus - GPE - Como parametrizar e calcular o dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034578653-RH-Linha-Protheus-GPE-Como-parametrizar-e-calcular-o-diss%C3%ADdio-retroativo)  
**5º** Após o cálculo, em **Outras Ações**, clique em **Gerar IR RRA**, para efetuar a apuração do IR do RRA  
**6º** Verificar se os valores foram levados para Manutenção de RRA  
**7º** Realizar a geração do dissidio retroativo para folha de pagamento  
- Informe o complemento trabalhista na pergunta **Complemento** e proceda com a geração das verbas. Caso o complemento não seja informado, as verbas de RRA não serão geradas  
**8º** Faça a geração do evento S-1200 - [RH - Linha Protheus - GPE - eSocial - S-1200 / S-1210 - Como gerar eventos periódicos com a folha aberta (SRC) no sigagpe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044700974)  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[RRA - Rendimentos Recebidos Acumuladamente](https://tdn.totvs.com/display/public/PROT/RRA+-+Rendimentos+Recebidos+Acumuladamente#main-complementar)  
  
**Próximos Treinamentos**[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
[TOTVS RESPONDE TOTVS RH (TODAS AS LINHAS) ESOCIAL](https://rhinforma.totvs.com/2023/04/04/totvs-responde-totvs-rh-todas-as-linhas-esocial-processo-trabalhista/)  
  
Essa documentação também pode ser **acessada 24h, através da Carolina**: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
