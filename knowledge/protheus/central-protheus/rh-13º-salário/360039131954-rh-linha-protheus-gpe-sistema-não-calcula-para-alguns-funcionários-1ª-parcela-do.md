---
article_id: 360039131954
category: RH - 13º salário
content_hash: b9b033ed91e0ae1fd0f3d0017120ee64329aa8ac3481b8e21ad64d6d531caa81
fetched_at: '2026-06-28T22:44:00.384559+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE -  Sistema não calcula para alguns funcionários 1ª
  parcela do 13º salario, Pela EndCalc() - S_ADT13PGT
type: support-article
updated_at: '2026-06-24T19:48:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039131954-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-para-alguns-funcion%C3%A1rios-1%C2%AA-parcela-do-13%C2%BA-salario-Pela-EndCalc-S-ADT13PGT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33450460041623) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao executar o cálculo pela rotina de **Cálculo de Roteiros**, através de rotina **GPEM020,**não é calculado a **1ª parcela de 13º** salário para alguns funcionários, apresentando a mensagem: **Calculo Finalizado Pela FinalCalc() ou Pela** ***EndCalc*****() - S\_ADT13PGT**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causas**  
1. Fórmula S\_ADT13PGT fora do padrão do sistema;  
2. Datas de referencia fora do ano de cálculo.  
3. Quando efetuado antecipação de 13º em férias no ano corrente.  
4. Particularidade do Funcionário como Reintegração ou Alteração de Contrato;  
5. Resíduos em tabela temporária anteriores ao período de calculo;  
3. Base desatualizada;  
  
  
**Solução**  
Analise os seguintes passos abaixo:  
  
**1.** Analise se a Fórmula encontra-se no padrão:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10261807241623)

**2.** Valide se as datas de referencia estão dentro do ano de cálculo, por exemplo, se cálculo for referente a 2025, as datas de referência devem ser dentro de 2025:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36639782371607)  
  
**3.** Quando efetuada antecipação em férias no ano corrente o help apresentado está correto, só não será apresentado caso esteja calculando complemento do calculo de 131.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36639761925143)

**4.** Verifique se existe alguma particularidade para este funcionário como: Reintegração, Transferência ou alteração no contrato de Intermitente para Indeterminado. Para esses cenários, o funcionário também pode ter já ter recebido o 13º, então só será calculado o complemento da 1ª parcela se houver.

**5.** Verifique se existe nas tabelas SRC e SRD do ano corrente, verbas de calculo do 13º Salário como os i**d's 0022, 0024, 0028, 0114, 0115** . Caso tenha, significa que já foi pago o 13º e por isso realmente não vai calcular para o funcionário. Caso haja verbas de anos anteriores dentro da SRC (tabela temporária), deve-se deletar os registros.  
  
**3.** Caso o Ambiente esteja desatualizado, atualize com o ultimo pacote disponível na Central de Atualizações - [Expedição contínua RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como incluir lançamentos no cálculo da Primeira Parcela do 13° Salario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412601175191-RH-Linha-Protheus-GPE-Como-incluir-lan%C3%A7amentos-no-c%C3%A1lculo-da-Primeira-Parcela-do-13-Salario?source=search)  
[RH - Linha Protheus - GPE - Primeira parcela do 13º parcelada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057497433-RH-Linha-Protheus-GPE-Primeira-parcela-do-13%C2%BA-parcelada?source=search)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409855157399-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionadas-ao-c%C3%A1lculo-da-1%C2%AA-parcela-do-13-Sal%C3%A1rio?source=search)
