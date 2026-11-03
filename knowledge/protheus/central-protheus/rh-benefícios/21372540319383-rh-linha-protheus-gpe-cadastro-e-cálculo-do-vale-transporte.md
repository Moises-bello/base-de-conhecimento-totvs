---
article_id: 21372540319383
category: RH - Benefícios
content_hash: 2c5bd98f2222f3ac4c1fb0e48ee272d852d533a9013e360971f8a8978bd3bb40
fetched_at: '2026-06-28T22:44:03.559420+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro e Cálculo do Vale Transporte
type: support-article
updated_at: '2026-06-24T18:51:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21372540319383-RH-Linha-Protheus-GPE-Cadastro-e-C%C3%A1lculo-do-Vale-Transporte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21372540264471) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como Cadastrar e Calcular o Vale Transporte?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para cadastro e cálculo do Vale Transporte, realize os seguintes passos:

**1.** Acessar em **Atualizações**> **Definições de Cálculo**> **Períodos,** cadastre o Roteiro VTR e deixe o roteiro Ativo. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32608779854615)  
  
**2.** Acessar em **Atualizações**> **Definições de Cálculo**> **Manutenção de Tabelas** e realize o cadastro nas seguintes tabelas:  
  
**S018 - Fornecedores de Benefícios:** Cadastre o fornecedor do benefício de vale transporte  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32608786771095)

**S011 - Tipos de Benefícios:** Cadastre o benefício de vale transporte  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32608779866775)

**3.** Acessar em **Atualizações>** **Definições de Cálculo>** **Verbas** e cadastre as verbas as seguintes verbas:  
  
**Verba de Desconto VT -** A verba deve ser de **tipo Desconto**, possuir o **id 0051** e com **percentual** do desconto informado (EX: 6%): ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32608779870999)

**Verba de Base Empresa -** A verba deve ser de **tipo Base (Provento),** possuir o **id 0210** e com **percentual** parte empresa informado (EX: 94%):![](https://centraldeatendimento.totvs.com/hc/article_attachments/32608786778391)

**4.** Cadastre o **Meio de Transporte** em: **Atualizações**> **Benefícios**> **VT/VR/VA**> **Meios Transporte.** Informe o código, descrição, valor unitário e tipo de beneficio referente ao vale transporte.  
Utilize o ***help*** de campo para auxiliar no preenchimento.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32608779877911)

**5.** Para vincular o meio de transporte ao funcionário acesse: **Atualizações**> **Benefícios**> **VT/VR/VA**> **Atualização**, selecione o funcionário, inclua o benefício, a quantidade de vales por dias úteis e a quantidade de vales em dias não úteis (caso o funcionário trabalhe em dias não úteis "Sab, dom e feriado".).   
Utilize o ***help*** de campo para auxiliar no preenchimento.![](https://centraldeatendimento.totvs.com/hc/article_attachments/32608779880855)

**6.** Realize o cálculo do VTR em: **Atualizações**> **Benefícios>** **VT/VR/VA**> **Cálculo.** Preencha os parâmetros de cálculo conforme necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32608786781463)![](https://centraldeatendimento.totvs.com/hc/article_attachments/32608786782615)

**- Calcular para:** Informe se o cálculo é refere-se ao Vale Transporte (mensal), Diferença de VT ou periódico  **- Prop. Admissão/Reintegração:** Informe se o cálculo deverá ser proporcional a admissão ou reintegração  
**- Prop. Férias/Afast.:** Informe se o cálculo deverá ser proporcional à férias/afastamento  
**- Prop. Férias Progr.:** Informe se o cálculo deverá ser proporcional à férias programadas  
**- Descontar Faltas:** Informe se as faltas serão abatidas no benefício  
**- Qtde. Vales a Deduzir:** Informe a quantidade de vales a deduzir, caso seja necessário  
**- Verbas Somar Salar:** Informe as verbas que serão somadas ao Salário base para cálculo  
**- Verifica data fim contrato:** Informe se o cálculo irá verificar a data fim do contrato determinado  
**- Complemento por H.E:** Informe se deseja efetuar o cálculo do complemento devido a hora extra, caso seja o cálculo mensal, deixe com não.

**7.** Para conferir o cálculo existem duas opções:  
**Impressão do Mapa/Relatório -** Acessar em **Atualizações**> **Benefícios**> **VT/VR/VA**> **Impressão do Mapa.**Veja a documentação sobre a geração do relatório [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053523094-RH-Linha-Protheus-GPE-Mapa-de-benef%C3%ADcios-em-planilha-GPER009)

**Consulta de cálculo individual** - Acessar em **Atualizações**> **Benefícios**> **VT/VR/VA**> **Atualização,** selecione o funcionário e verifique o cálculo no grid central. No grid inferior é possível visualizar o detalhamento do cálculo de forma analítica.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32608786783511)

**8.** Após conferência do cálculo, integre o Roteiro VTR a folha, acessando: **Atualizações**> **Benefícios**> **VT/VR/VA**> **Integração com a Folha.**  
Veja a documentação sobre a integração de roteiros [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027259251-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-dos-roteiros-com-a-folha)

**Obs.:** A forma de cálculo do desconto do vale transporte pode variar de acordo com que foi definido no parâmetro **MV\_CVTPROP**, consulte [a documentação aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014665512-RH-Linha-Protheus-GPE-Como-utilizar-par%C3%A2metro-MV-CVTPROP?source=search)

**Saiba Mais**[RH - Linha Protheus - GPE - Recálculo (Diferença) de Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25157432507799-RH-Linha-Protheus-GPE-Rec%C3%A1lculo-Diferen%C3%A7a-de-Vale-Transporte)  
[RH - Linha Protheus - GPE - Como descontar valor Fixo de Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406270401047-RH-Linha-Protheus-GPE-Como-descontar-valor-Fixo-de-Vale-Transporte)  
[RH - Linha Protheus - GPE - Complemento de benefícios por horas extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25168379802903-RH-Linha-Protheus-GPE-Complemento-de-benef%C3%ADcios-por-horas-extras)  
[RH - Linha Protheus - GPE - Controle de saldo de benefício ou compra da diferença faltante](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051035414-RH-Linha-Protheus-GPE-Controle-de-saldo-de-benef%C3%ADcio-ou-compra-da-diferen%C3%A7a-faltante)
