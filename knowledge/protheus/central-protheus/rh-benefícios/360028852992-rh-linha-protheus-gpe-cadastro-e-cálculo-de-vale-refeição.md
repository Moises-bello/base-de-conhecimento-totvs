---
article_id: 360028852992
category: RH - Benefícios
content_hash: 95b8fd6234dc179df29c46d514d091e3bd14cfa183505b22950c975edd2d903f
fetched_at: '2026-06-28T22:44:03.535167+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro e Cálculo de Vale Refeição
type: support-article
updated_at: '2025-10-02T13:35:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028852992-RH-Linha-Protheus-GPE-Cadastro-e-C%C3%A1lculo-de-Vale-Refei%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32588869561623) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**Como Cadastrar e Calcular o Vale Refeição?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**Para cadastro e cálculo do Vale Refeição, realize os seguintes passos:

**1.** Acessar em **Atualizações**> **Definições de Cálculo**> **Períodos,** cadastre o **Roteiro VRF** e deixe o roteiro Ativo.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32588907022615)  
  
  
**2.** Acessar em **Atualizações**> **Definições de Cálculo**> **Manutenção de Tabelas** e realize o cadastro nas seguintes tabelas:  
  
**S018 - Fornecedores de Benefícios:** Cadastre o fornecedor do benefício de vale refeição  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32588907026967)

**S011 - Tipos de Benefícios:** Cadastre o benefício de vale refeição   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32588907028887)  
  
  
**3.** Acessar em **Atualizações>** **Definições de Cálculo>** **Verbas** e cadastre as verbas de Id **0050** (Desconto do Funcionário) e Id **00212** (Parte Empresa).   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32588869572759)

**4.** Cadastre o vale refeição em **Atualizações**> **Benefícios**> **VT/VR/VA**> **Cadastro Vale Refeição.** Informe o código, descrição, valor, percentual de desconto e tipo de beneficio referente ao vale refeição.  
Utilize o ***help*** de campo para auxiliar no preenchimento.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32588907033239)

**5.** Para vincular o vale refeição ao funcionário acessar em **Atualizações**> **Benefícios**> **VT/VR/VA**> **Atualização**, selecione o funcionário, inclua o Vale Refeição, a quantidade de vales por dias úteis e a quantidade de vales em dias não úteis (caso o funcionário trabalhe em dias não úteis "Sab, dom e feriado".).   
Utilize o ***help*** de campo para auxiliar no preenchimento.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32588907036823)

**6.** Realize o cálculo do VRF em **Atualizações**> **Benefícios>** **VT/VR/VA**> **Cálculo.** Preencha os parâmetros de cálculo conforme necessidade.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32588907038231)![](https://centraldeatendimento.totvs.com/hc/article_attachments/32588907042199)

**- Prop. Admissão/Reintegração:** Informe se o cálculo deverá ser proporcional a admissão ou reintegração  
**- Prop. Férias/Afast.:** Informe se o cálculo deverá ser proporcional à férias/afastamento  
**- Prop. Férias Progr.:** Informe se o cálculo deverá ser proporcional à férias programadas  
**- Descontar Faltas:** Informe se as faltas serão abatidas no benefício  
**- Qtde. Vales a Deduzir:** Informe a quantidade de vales a deduzir, caso seja necessário  
**- Calcular períodico:** Informe se o cálculo é periódico, caso seja o cálculo mensal deixe com não  
**- Verifica data fim contrato:** Informe se o cálculo irá verificar a data fim do contrato determinado  
**- Complemento por H.E:** Informe se deseja efetuar o cálculo do complemento devido a hora extra, caso seja o cálculo mensal, deixe com não.   
  
  
**7.** Para conferir o cálculo existem duas opções:  
  
**-Impressão do Mapa/Relatório -** Acessar em **Atualizações**> **Benefícios**> **VT/VR/VA**> **Impressão do Mapa.** Veja a documentação sobre a geração do relatório [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053523094-RH-Linha-Protheus-GPE-Mapa-de-benef%C3%ADcios-em-planilha-GPER009)

**-Consulta de cálculo individual** - Acessar em **Atualizações**> **Benefícios**> **VT/VR/VA**> **Atualização,** selecione o funcionário e verifique o cálculo no grid central. No grid inferior é possível visualizar o detalhamento do cálculo de forma analítica.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32588907043863)

**8.** Após conferência do cálculo, integre o Roteiro VRF a folha, acessando em **Atualizações**> **Benefícios**> **VT/VR/VA**> **Integração com a Folha.** Veja a documentação sobre a integração de roteiros [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027259251-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-dos-roteiros-com-a-folha)

**Saiba Mais**[RH - Linha Protheus - GPE - Desconto de Vale Refeição em Valor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035781854-RH-Linha-Protheus-GPE-Desconto-de-Vale-Refei%C3%A7%C3%A3o-em-Valor?source=search)  
[RH - Linha Protheus - GPE - Cálculo avulso para Vale Transporte, Vale Refeição e Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049769114-RH-Linha-Protheus-GPE-C%C3%A1lculo-avulso-para-Vale-Transporte-Vale-Refei%C3%A7%C3%A3o-e-Vale-Alimenta%C3%A7%C3%A3o?source=search)  
[RH - Linha Protheus - GPE - Valor total do benefício de vale refeição conforme determinação do MOS da versão S-1.0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14597169300503-RH-Linha-Protheus-GPE-Valor-total-do-benef%C3%ADcio-de-vale-refei%C3%A7%C3%A3o-conforme-determina%C3%A7%C3%A3o-do-MOS-da-vers%C3%A3o-S-1-0)
