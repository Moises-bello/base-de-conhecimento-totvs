---
article_id: 29453272009239
category: RH - Folha de Pagamento
content_hash: 9f092d216d4d1688384a89422970c32583767b03c74cdc46cc3f4e9cf2606708
fetched_at: '2026-06-28T22:44:13.199797+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular Salário para Funcionários Expatriados
  que recebem integralmente no exterior
type: support-article
updated_at: '2025-04-28T19:58:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29453272009239-RH-Linha-Protheus-GPE-Como-calcular-Sal%C3%A1rio-para-Funcion%C3%A1rios-Expatriados-que-recebem-integralmente-no-exterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29453280819735) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como calcular Salário para Funcionários Expatriados que recebem integralmente no exterior?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões  
  
**Solução**Para funcionários expatriados que recebem o Salário integralmente no Exterior, foi necessário implementar a possibilidade de efetuar o pagamento do salário do funcionário Brasileiro residente no exterior de categoria Mensalista em uma verba diferente do id 0031, devido a necessidade de configurar a verba com natureza de rubrica e incidências diferentes no esocial.  
Foram criados os campos Tipo Remuneração e Verba Pag na rotina Histórico de Contratos GPEA900.

Para solucionar essa dúvida, realize os seguintes passos:  
**1.** Cadastre a verba para pagamento do Salário sem id do Tipo Provento em Atualizações > Definições de Cálculos > Verbas, configure a aba Esocial com a natureza de rubrica 9906 - <https://tdn.totvs.com/display/public/ConSeg/eSocial+-+Expatriado+-+Rubrica+de+Pagamento;>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29453271987095)

**2.** Preencha o campo **Res. Exterior** com **Sim** na aba Endereço no cadastro do funcionários em **Atualizações > Funcionários > Funcionários (GPEA010)**, preenchendo os campos de endereço com endereço do exterior **e preencha também** o campo **Calcula INSS** na aba Estrangeiros;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29453271988119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29453280824983)

**3.** Preencha o Histórico de contrato do funcionário em Atualizações > Funcionários > Histórico Contratos (GPEA900) preenchendo as informações da aba Residente exterior;

![](https://i.imgur.com/x2Yb4yA.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29453280826135)

**Importante:** as informações da parte de Impostos dos campo Benef. Rend, Rendimento, Forma Trib, Cod Retenção, Perc IR, deve ser informado conforme o entendimento da empresa.

**4.** Preencha no Histórico de contrato do funcionário na aba Outros, se deverá calcular encargos e quais encargos serão calculados para esse funcionário. Lembrando que, esse preenchimento também é conforme o entendimento da empresa;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29453271989271)

![](https://i.imgur.com/QgRfbxI.png)

**5.** Realize o calculo para o funcionário expatriado. Como o campo Verba Pagamento foi preenchido com a nova verba cadastrada e o funcionário tem uma remuneração paga integral no exterior, o sistema despreza a verba 0031 no calculo da folha de pagamento e calcula o Salário na nova verba;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29453271989783)

**Saiba mais:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=665275792>

<https://tdn.totvs.com/pages/releaseview.action?pageId=266971250>

<https://tdn.totvs.com/display/public/PROT/1132957+DRHPAG-256+DT+Encargos+Sociais+Residentes+no+Exterior>

[RH - Linha - Protheus - GPE - Como cadastrar Funcionário Expatriado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058349473-RH-Linha-Protheus-GPE-Como-cadastrar-Funcion%C3%A1rio-Expatriado)
