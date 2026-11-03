---
article_id: 360028910152
category: RH - Benefícios
content_hash: 8ed33eb089059d949effb11fd6c2c2b247c7e4da3dc9b362d64d4945dc224e80
fetched_at: '2026-06-28T22:44:03.549948+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro e Cálculo do Vale Alimentação
type: support-article
updated_at: '2025-10-02T13:47:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028910152-RH-Linha-Protheus-GPE-Cadastro-e-C%C3%A1lculo-do-Vale-Alimenta%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33153211099287) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como Cadastrar e Calcular o Vale Alimentação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**Para cadastro e cálculo do Vale Alimentação, realize os seguintes passos:

**1.** Acessar **Atualizações**> **Definições de Cálculo**> **Períodos,** cadastre o **Roteiro VAL** e deixe o roteiro Ativo.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153211101591)

**2.** Acessar em **Atualizações**> **Definições de Cálculo**> **Manutenção de Tabelas** e realize o cadastro nas seguintes tabelas:  
  
**S018 - Fornecedores de Benefícios:** Cadastre o fornecedor do benefício de vale alimentação  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153221592599)

**S011 - Tipos de Benefícios:** Cadastre o benefício de vale alimentação  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153211105175)  
  
  
  
**3.** Acessar **Atualizações**> **Definições de Cálculo**> **Verbas** e cadastre as verbas de Desconto do Funcionário e a verba de Base Empresa **(sem Id de Cálculo);**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153211107223)  
  
  
  
**4.** Acessar **Atualizações**> **Definições de Cálculo**> **Mnemônicos**e informe no Mnemônico **P\_PDVAEMP** a verba de Base Empresa, e no mnemônico **P\_PDVADES** a verba de desconto do funcionário;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153221598743)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153221602455)

**5.** Cadastre o vale refeição em: **Atualizações**> **Benefícios**> **VT/VR/VA**> **Cadastro Vale Alimentação.** Informe o código, descrição, valor, percentual de desconto e tipo de beneficio referente ao vale alimentação. Utilize o ***help*** de campo para auxiliar no preenchimento.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153221604503)  
  
  
**6.** Para vincular o vale alimentação ao funcionário acessar em **Atualizações**< **Benefícios**> **VT/VR/VA**> **Atualização**, selecione o funcionário, inclua o Vale Alimentação, a quantidade de vales por dias úteis e a quantidade de vales em dias não úteis (caso o funcionário trabalhe em dias não úteis "Sab, dom e feriado".). Utilize o ***help*** de campo para auxiliar no preenchimento.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153211112983)  
  
  
**7.** Realizar o cálculo do VAL em **Atualizações**> **Benefícios>** **VT/VR/VA**> **Cálculo.** Preencha os parâmetros de cálculo conforme necessidade.  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153221607959)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153221610263)

**- Prop. Admissão/Reintegração:** Informe se o cálculo deverá ser proporcional a admissão ou reintegração  
**- Prop. Férias/Afast.:** Informe se o cálculo deverá ser proporcional à férias/afastamento  
**- Prop. Férias Progr.:** Informe se o cálculo deverá ser proporcional à férias programadas  
**- Descontar Faltas:** Informe se as faltas serão abatidas no benefício  
**- Qtde. Vales a Deduzir:** Informe a quantidade de vales a deduzir, caso seja necessário  
**- Calcular períodico:** Informe se o cálculo é periódico, caso seja o cálculo mensal deixe com não  
**- Verifica data fim contrato:** Informe se o cálculo irá verificar a data fim do contrato determinado  
**- Complemento por H.E:** Informe se deseja efetuar o cálculo do complemento devido a hora extra, caso seja o cálculo mensal, deixe com não.

**8.** Para conferir o cálculo existem duas opções:  
  
**- Impressão do Mapa/Relatório -** Acessar em **Atualizações**> **Benefícios**> **VT/VR/VA**> **Impressão do Mapa.** Veja a documentação sobre a geração do relatório [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053523094-RH-Linha-Protheus-GPE-Mapa-de-benef%C3%ADcios-em-planilha-GPER009)

**- Consulta de cálculo individual** - Acessar em **Atualizações**> **Benefícios>** **VT/VR/VA**> **Atualização,** selecione o funcionário e verifique o cálculo no grid central. No grid inferior é possível visualizar o detalhamento do cálculo de forma analítica.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153211118103)

**9.** Após conferência do cálculo, integre o Roteiro VAL a folha, acessando: **Atualizações**> **Benefícios** > **VT/VR/VA**> **Integração com a Folha.** Veja a documentação sobre a integração de roteiros [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027259251-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-dos-roteiros-com-a-folha)

**Saiba Mais**[RH - Linha Protheus - GPE - Como gerar um título de Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405047881879-RH-Linha-Protheus-GPE-Como-gerar-um-t%C3%ADtulo-de-Vale-Alimenta%C3%A7%C3%A3o?source=search)  
[RH - Linha Protheus - GPE - Não foram informadas as verbas de vale alimentação nos mnemônicos P\_PDVAEMP e/ou P\_PDVADES. Vale alimentação não foi integrado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022257211-RH-Linha-Protheus-GPE-N%C3%A3o-foram-informadas-as-verbas-de-vale-alimenta%C3%A7%C3%A3o-nos-mnem%C3%B4nicos-P-PDVAEMP-e-ou-P-PDVADES-Vale-alimenta%C3%A7%C3%A3o-n%C3%A3o-foi-integrado?source=search)  
[RH - Linha Protheus - GPE - Ao realizar a Integração do roteiro VAL com a folha gera o valor de desconto integral para o funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9782099436311-RH-Linha-Protheus-GPE-Ao-realizar-a-Integra%C3%A7%C3%A3o-do-roteiro-VAL-com-a-folha-gera-o-valor-de-desconto-integral-para-o-funcion%C3%A1rio?source=search)
