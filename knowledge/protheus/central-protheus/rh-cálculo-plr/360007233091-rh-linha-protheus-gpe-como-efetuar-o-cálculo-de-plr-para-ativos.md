---
article_id: 360007233091
category: RH - Cálculo PLR
content_hash: 5946c80f49ceedf67addaa4f3523dad3d0884da189ac143d13b9040076301dff
fetched_at: '2026-06-28T22:43:12.881109+00:00'
product: protheus
section_id: 360010855894
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o cálculo de PLR para ativos
type: support-article
updated_at: '2024-07-18T13:51:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007233091-RH-Linha-Protheus-GPE-Como-efetuar-o-c%C3%A1lculo-de-PLR-para-ativos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24989090773655) Tempo aproximado para leitura: **00:03:SS min  
  
Dúvida**Como efetuar o cálculo de PLR para ativos?   
Calculo IR para PLR  
Cadastro do PLR no sindicato

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão pessoal - Versão 12  
  
**Solução**Para configuração do **cálculo do PLR** o cliente deverá seguir a parametrização dos seguintes itens abaixo:  
  
**1.** Cadastre o IR da PLR  em **Atualizações > Definições Cálculos > Manutenção Tabelas (GPEA320) > selecione a tabela S044 - Tabela de IR para PLR**:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989090776599)**

**2.** Execute o cadastro dos id's em **Atualizações > Definições cálculos > Verbas (GPEA040)**;  
As informações contidas nesta rotina serão armazenadas na tabela**SRV.**-Cadastre uma verba com ID p/ Cálculo**0151** - Pagamento PLR - **Verba de Provento**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989840232599)**-Cadastre uma verba com ID p/ Cálculo**0152** - IRRF PLR - **Verba de Desconto**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989796154263)**-Cadastre uma verba com ID p/ Cálculo**0300** - Ded. Dep. IR PLR - **Verba de Base (Provento)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989796158871)**

-Cadastre uma verba com ID p/ Cálculo**0835**- Base IRRF PLR - **Verba de Base (Provento)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989840244247)**-Cadastre uma verba com ID p/ Cálculo**0836** - Liquido PLR - **Verba de Base (Provento)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989796173079)**- Cadastre uma verba com ID p/ Cálculo **1279** - Desconto 1ª parcela PLR - **Verba de Desconto**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989847742743)**

**3.** Em **Atualizações > Cadastros > Sindicatos (GPEA340)**, Aba PLR,  informe os valores para calcular o PLR automaticamente:  
  
No exemplo abaixo será calculado 100% do salário contratual do empregado:![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989090780695)

**4.** Em **Atualizações > Definições de Cálculos > Períodos (GPEA400)**, inclua o roteiro PLR:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989090784407)

**5.** Vincule o sindicato no cadastro do funcionário em **Atualizações > Funcionários > Funcionários (GPEA010)**:   
Nesse exemplo o Funcionário foi admitido em 15/12/2023 - PLR proporcional - 1 meses (dez de 2023)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989097479447)

**6.** Execute o cálculo do roteiro PLR em **Miscelânea > Cálculos > Por roteiros (GPEM020)**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989090788631)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989097482519)  
  
**7.** Consulte o cálculo em **Consultas > Cálculos > Por funcionário (GPEA580)**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24989090794135)

Conferência:

Salário: 2663,18 / 12 (meses do ano) \* 1 (meses de direito) = R$221,93

**Dúvidas frequentes:**  
- O Roteiro PLR faz integração com a folha?  
Não, na Versão 12 ela é tratada separadamente, onde é possível a qualquer momento impressão de Recibos, Folha e gerar individualmente o arquivo CNAB.  
  
- Existe a possibilidade dessas verbas entrarem na folha?  
Se deixar habilitado o campo INTEGRA? do Roteiro de calculo PLR, através de customização há a possibilidade, na modo padrão não.

Documento referente ao ponto de entrada GPM19INTEG <http://tdn.totvs.com/pages/releaseview.action?pageId=243007532>  
  
- O sistema não está proporcionalizando o avos de direito do PLR do funcionário?  
Observe o Ano de Referencia mencionado no cadastro do sindicato (Aba PLR), a admissão do funcionário tem que ser referente ao ano mencionado. Ex. Admissão 10/05/2017 - Ano de Referencia 2017

**Saiba mais:**

[RH - Cálculo PLR](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855894-RH-C%C3%A1lculo-PLR)
