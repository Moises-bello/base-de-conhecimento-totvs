---
article_id: 360035384293
category: RH - Férias
content_hash: 25d47ef9cf6bc378900d070defc819dd1a5d833051cef6ebd81cce470e88ef70
fetched_at: '2026-06-28T22:43:58.120376+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o Desconto de Pensão Alimentícia nas
  Férias do Mês e Férias Mês Seguinte
type: support-article
updated_at: '2025-09-26T15:49:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035384293-RH-Linha-Protheus-GPE-Como-efetuar-o-Desconto-de-Pens%C3%A3o-Aliment%C3%ADcia-nas-F%C3%A9rias-do-M%C3%AAs-e-F%C3%A9rias-M%C3%AAs-Seguinte
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26566076478487) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como efetuar o **Desconto de Pensão nas Férias do Mês e Férias Mês Seguinte?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Para efetuar o Cálculo de **Pensão Alimentícia nas Férias**, faça o procedimento abaixo:  
  
1. Acesse **Atualizações/ Definições de Cálculo/ Verbas** e parametrize as verbas de **Férias Mês** e **Férias Mês Seguinte** com **Sim** para incidência de Pensão conforme abaixo.![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045364634)

**OBS:** Caso queira que **outras verbas geradas nas férias** entrem também para o cálculo da pensão, basta configurar da mesma forma, com **Sim para Pensão.**  
  
2. Ainda no Cadastro de Verbas, crie uma Verba **sem Id de Cálculo**, para o **Desconto de Pensão Alimentícia nas Férias,** conforme exemplo abaixo:  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019201502)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019444421)**3. Acesse **Atualizações/ Funcionários/ Beneficiários,** clique em Incluir  e informe os dados do Beneficiário da Pensão conforme abaixo.Neste exemplo abaixo, será calculado 30% sobre o Salário Líquido. **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019444861)  
  
-Nome Benef -** Informe o Nome do Beneficiário  
**-Data Nasc -** Informe a data de Nascimento do Beneficiário  
**-Perc. Benef -** Informe o Percentual de desconto referente a pensão. Caso seja um percentual sobre o salário, deixe o campo a seguir, Nr. Sal Min em branco, ou, caso seja um percentual sobre salário mínimo, informe a quantidade de salários mínimos que o percentual será aplicado, no campo Nr. Sal. Min.  
**-Verb. Bs Calc -** Selecione as verbas que compõe o cálculo da Pensão Alimentícia (Férias Mês, Férias Mês Seguinte, 1/3 De Férias, 1/3 de Férias Mês Seguinte), ou então, pode deixar o campo em branco, assim, o sistema considerará todas as verbas para base de cálculo quando a incidências de Pensão no cadastro de verbas estiver com Sim  
**-Verba Férias -** Informe o código da verba de Pensão sobre Férias criada no passo 1  
**-Valor Fixo** - Caso a pensão tenha um valor fixo determinado, preencha este campo e os campos Perc. Benef e Nr. Sal Min deixe em Branco  
**-Cal. Sobr. Liq** - Informe se o cálculo será sobre o **Bruto - Não,** para que o sistema considere apenas a soma dos proventos e aplique o percentual**,** ou sobre o **Líquido - Sim,** para que o sistema considere os proventos - descontos legais para montar a base para desconto e então aplique o percentual.  
  
**4.** Após as configurações acima, calcule as férias para gerar o cálculo da pensão. **![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019202942)  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019203302)  
  
Resumo do Cálculo**  
Verbas com **Sim para Pensão:**  
100 - Férias - **R$ 3.333,33**  
101 - 1/3 Férias - **R$ 1.111,11**  
428 - Inss Férias - **R$ 473,50**  
432 - Irrf Férias - **R$ 67,18   
  
Soma dos Proventos: 3.333,33 + 1.111,11 = 4.444,44  
Soma dos Descontos: 473,50 + 67,18 = 540,68  
  
Base para Pensão: 4.444,44 - 540,68 = 3.903,76  
Valor Pensão: 3.903,76 \* 30% = 1.171,13**

**Saiba Mais**[RH - Linha Protheus - GPE - Como calcular pensão alimentícia pelo percentual do salário líquido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056461354-RH-Linha-Protheus-GPE-Como-calcular-pens%C3%A3o-aliment%C3%ADcia-pelo-percentual-do-sal%C3%A1rio-l%C3%ADquido)  
[RH - Linha Protheus - GPE - Como conferir o cálculo de pensão alimentícia sobre o líquido quando há incidência de IRRF no adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044532413-RH-Linha-Protheus-GPE-Como-conferir-o-c%C3%A1lculo-de-pens%C3%A3o-aliment%C3%ADcia-sobre-o-l%C3%ADquido-quando-h%C3%A1-incid%C3%AAncia-de-IRRF-no-adiantamento)  
[RH - Linha Protheus - GPE - Como verificar quais verbas possuem incidência para Pensão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011999661-RH-Linha-Protheus-GPE-Como-verificar-quais-verbas-possuem-incid%C3%AAncia-para-Pens%C3%A3o)
