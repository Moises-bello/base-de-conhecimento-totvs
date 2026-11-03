---
article_id: 1500006242301
category: RH - Benefícios
content_hash: fe64f8adbf867f917ac3a6ae2a1cb3b52427efb15fdc5ae441971c512aa1d536
fetched_at: '2026-06-28T22:44:03.870964+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como utilizar as tabelas S059 e S060 para assistência
  médica/odontológica por faixa salarial/etária
type: support-article
updated_at: '2025-09-05T18:40:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006242301-RH-Linha-Protheus-GPE-Como-utilizar-as-tabelas-S059-e-S060-para-assist%C3%AAncia-m%C3%A9dica-odontol%C3%B3gica-por-faixa-salarial-et%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32481363828887) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como utilizar as tabelas **S059 e S060** para assistência médica/odontológica por faixa salarial/etária  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**As tabelas auxiliares S059 (Ass. Med. Faixa Salarial/Etária) e S060 (Ass. Odo. Faixa Salarial/Etária) contém a seguinte estrutura:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32481373338263)

**Detalhamento dos campos:  
  
- CODIGO:** Código do Plano de Saúde/Odontológico que será vinculado ao funcionário, dependente e/ou agregado.  
**- DESCRICAO:** Descrição do Plano de Saúde/Odontológico  
**- SAL. BASE ATE:** Limite salarial para a faixa do plano de saúde  
**- IDADE ATE:** Limite de idade para a faixa do plano de saúde  
**- VL. AGREG.:** Valor do plano de saúde referente ao agregado  
**- VL. DEPEND**.: Valor do plano de saúde referente ao dependente  
**- VL. TITULAR:** Valor do plano de saúde referente ao titular  
**- % DESC. AGR.:** Percentual do plano de saúde que será descontado do agregado  
**- % DESC. DEP.:** Percentual do plano de saúde que será descontado do dependente  
**- % DESC. TIT.:** Percentual do plano de saúde que será descontado do titular  
**- CÓDIGO DO FORNECEDOR:** Código da operadora\fornecedor do plano de saúde

**Regra de Cálculo:**  
Sobre o valor do plano do titular, dependente e agregado será aplicado a % definida nas tabelas S059/S060 para o titular, dependente e agregado.  
  
**a) Valor do titular:**  
Valor Desconto Titular => Valor Titular X % Desconto Titular.  
Valor Empresa Titular => Valor Titular - Valor Desconto Titular.  
  
**b) Valor do dependente:**  
Valor Desconto Dependente => Valor Dependente X % Desconto Dependente.  
Valor Empresa Dependente => Valor Dependente - Valor Desconto Dependente.  
  
**c) Valor do agregado:**  
Valor Desconto Agregado => Valor Agregado X % Desconto Agregado.  
Valor Empresa Agregado => Valor Agregado - Valor Desconto Agregado.  
  
**Exemplo** **de preenchimento:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32481373339159)  
  
**Por exemplo**, caso o titular do plano de saúde tenha sido cadastrado no Plano 02, com uma remuneração mensal de R$ 5.000,00 e idade de 54 anos, ele se enquadra na última faixa etária desse plano. Nessa faixa, o valor total do plano é de R$ 100,00.  
Dessa quantia, 50% (R$ 50,00) são descontados diretamente do titular, enquanto os outros R$ 50,00 são custeados pela empresa.

**Saiba Mais**[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11223604924695-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-plano-de-sa%C3%BAde)  
[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11245418684951-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-plano-odontol%C3%B3gico)  
[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11301756760855-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-coparticipa%C3%A7%C3%A3o)
