---
article_id: 11960385759895
category: GPE - eSocial - Processo Trabalhista
content_hash: 19b20b7984c73c5ab1d7925b29f3b97bff174d1c960f61a463698b432334190f
fetched_at: '2026-06-28T22:45:00.378613+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2501 - Como funciona o De / Para dos
  campos entre GPE x TAF no leiaute S-1.2
type: support-article
updated_at: '2025-03-27T18:07:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11960385759895-RH-Linha-Protheus-GPE-eSocial-S-2501-Como-funciona-o-De-Para-dos-campos-entre-GPE-x-TAF-no-leiaute-S-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19401604610967) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Para o evento S-2501 como funciona o De / Para de campos Protheus com leiaute eSocial, entre GPExTAF?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Consulte abaixo detalhadamente a estrutura de campos entre GPE e TAF para o evento S-2501:

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **eSocial** | **Protheus Recursos Humanos** | | | | **Protheus TAF** | | | | **Descrição / Validação** | **Leiautes:** |
| **S-1.1/S-1.2** |
| **tag xml** | **Rotina** | **Tabela** | **Campo** | **Nome** | **Rotina** | **Tabela** | **Campo** | **Nome** | **\* Ambas versões** |
| nrProcTrab | APTA100 | RE0 | RE0\_PROJUD | Número do Processo | TAFA609 | V7C | V7C\_NRPROC | Número do processo | Preencher com a identificação do processo judicial ou administrativo. | \* |
| perApurPgto | APTA101 | E0E | E0E\_PERAP | Período de Apuração | TAFA609 | V7C | V7C\_PERAPU | Per. Apur. Pgto. | Período de Apuração (formato AAAA-MM) em que é devida a obrigação de pagar a parcela prevista no acordo/sentença. | \* |
| obs | APTA101 | E0E | E0E\_CMEM | Observação | TAFA609 | V7C | V7C\_OBS | Obs. Referente | Observação | \* |
| cpfTrab | APDA020 | RD0 | RD0\_CIC | CPF | TAFA609 | V7D | V7D\_CPFTRA | Cpf Benef. | CPF do Reclamante | \* |
| perRef | APTA101 | E0E | E0E\_COMPET | Periodo de Referência | TAFA609 | V7E | V7E\_PERREF | Periodo de Referencia | Período de Referência (formato AAAA-MM) relacionado ao Tributos do Processo. Deve ser um período existente no evento S-2500 do trabalhador. | \* |
| vrBcCpMensal | APTA101 | E0E | E0E\_BSINSS | Base Cálculo INSS | TAFA609 | V7E | V7E\_VRMEN | Vl. contrib. Previ. | Valor da base de cálculo da contribuição previdenciária sobre a remuneração mensal do trabalhador. | \* |
| vrBcCp13 | APTA101 | E0E | E0E\_BS13 | Base Cálculo 13º | TAFA609 | V7E | V7E\_VRCP | Remuneraçao base de 13. | Valor da base de cálculo da contribuição previdenciária sobre a remuneração do trabalhador referente ao 13º salário. | \* |
| vrRendIRRF | APTA101 | E0E | E0E\_RDIRRF | Rendimento IRRF | TAFA609 | V7E | V7E\_VERREN | Trib. Impost. Renda. | Valor do rendimento tributável do Imposto de Renda. | S-1.1 |
| vrRendIRRF13 | APTA101 | E0E | E0E\_RDIR13 | Rendimento IRRF 13º | TAFA609 | V7E | V7E\_VRIRRF | IRRF 13º salário | Valor do rendimento tributável do Imposto de Renda referente ao 13º salário - Tributação exclusiva. | S-1.1 |
| tpCR | APTA101 | E0F | E0F\_TPCR | Código da Receita | TAFA609 | V7F | V7F\_IDCODR | Id. Cod. Receita | Informe Código de Receita - CR relativo a contribuições sociais devidas à Previdência Social e a Outras Entidades e Fundos (Terceiros), conforme legislação em vigor na competência ou Código de Receita - CR relativo a Imposto de Renda Retido na Fonte conforme o Tipo do Tributo informado. | \* |
| vrCR | APTA101 | E0F | E0F\_VRCR | Valor da Receita | TAFA609 | V7F | V7F\_VRCR | Vl. receita | Informe Valor correspondente ao Código de Receita - CR. | \* |
| vrRendTrib | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8X | V8X\_VLRTRI | vr.Rend.Trib | Valor do rendimento tributável mensal do Imposto de Renda. | S-1.2 |
| vrRendTrib13 | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8X | V8X\_VLRT13 | vr.RendTrib | Valor do rendimento tributável do Imposto de Renda referente ao 13º salário - Tributação exclusiva. | S-1.2 |
| vrRendMoleGrave | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8X | V8X\_VLRIMG | vr.Rend.Mole | Valor do rendimento isento por ser portador de moléstia grave atestada por laudo médico. | S-1.2 |
| vrRendIsen65 | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8X | V8X\_VLRI65 | vr.RendI.sen | Valor de parcela isenta de aposentadoria para beneficiário de 65 anos ou mais. | S-1.2 |
| vrJurosMora | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8X | V8X\_VLJRMO | vr juros.Mo | Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função. | S-1.2 |
| vrRendIsenNTrib | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8X | V8X\_VLRINT | vrRendIsenNT | Valor de outros rendimentos isentos ou não tributáveis. | S-1.2 |
| descIsenNTrib | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8X | V8X\_DCRINT | Descr. Trib | Descrição do rendimento isento ou não tributável informado em vrRendIsenNTrib. | S-1.2 |
| vrPrevOficial | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8X | V8X\_VLPRVO | vr.Prev.Ofic | Valor referente à previdência oficial. | S-1.2 |
| descRRA | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8Y | V8Y\_DESCRA | Desc RRA | Descrição dos Rendimentos Recebidos Acumuladamente - RRA. | S-1.2 |
| qtdMesesRRA | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8Y | V8Y\_QTMRRA | Núm RRA | Número de meses relativo aos Rendimentos Recebidos Acumuladamente - RRA. | S-1.2 |
| vlrDespCustas | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8Y | V8Y\_VLRCUS | Vl Custo Jud | Preencher com o valor das despesas com custas judiciais. | S-1.2 |
| vlrDespAdvogados | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8Y | V8Y\_VLRADV | Vl Desp Adv | Preencher com o valor total das despesas com advogado(s). | S-1.2 |
| tpInsc | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8K | V8K\_TPINSC | Tipo Inscr. | Preencher com o código correspondente ao tipo de inscrição. | S-1.2 |
| nrInsc | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8K | V8K\_NRINSC | Num. Inscr. | Informar o número de inscrição do advogado. | S-1.2 |
| vlrAdv | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8K | V8K\_VLRADV | Vlr. Des Adv | Valor da despesa com o advogado, se houver. | S-1.2 |
| tpRend | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8L | V8L\_TPREND | Tp. Rendimen | Tipo de rendimento. | S-1.2 |
| cpfDep | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8L | V8L\_CPFDEP | CPF Depend. | Informar o número de inscrição do dependente no CPF. | S-1.2 |
| vlrDeducao | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8L | V8L\_VLRDED | Vl. Base Cal | Preencher com o valor da dedução da base de cálculo. | S-1.2 |
| tpRend | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8M | V8M\_TPREND | Tipo de Rend | Tipo de rendimento. | S-1.2 |
| cpfDep | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8M | V8M\_CPFDEP | CPF Dependen | Número do CPF do dependente/beneficiário da pensão alimentícia. | S-1.2 |
| vlrPensao | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8M | V8M\_VLPENS | Vl. Pensão D | Valor relativo à dedução do rendimento tributável correspondente a pagamento de pensão alimentícia. | S-1.2 |
| tpProcRet | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8N | V8N\_TPPRCR | Tipo de Proc | Preencher com o código correspondente ao tipo de processo. | S-1.2 |
| nrProcRet | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8N | V8N\_NRPRCR | Num.Proc. | Informar o número do processo administrativo/judicial. | S-1.2 |
| codSusp | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8N | V8N\_CODSUP | Cod Susp | Código do indicativo da suspensão, atribuído pelo empregador em S-1070. | S-1.2 |
| indApuracao | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8O | V8O\_INDAPU | Ind. Apuraçã | Indicativo de período de apuração. | S-1.2 |
| vlrNRetido | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8O | V8O\_VLNRET | Vl de Retenç | Valor da retenção que deixou de ser efetuada em função de processo administrativo ou judicial. | S-1.2 |
| vlrDepJud | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8O | V8O\_VLDEPJ | Vl deps Judc | Valor do depósito judicial em função de processo administrativo ou judicial. | S-1.2 |
| vlrCmpAnoCal | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8O | V8O\_VLCPAC | Vl. Comps. R | Valor da compensação relativa ao ano calendário em função de processo judicial. | S-1.2 |
| vlrCmpAnoAnt | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8O | V8O\_VLCPAA | Vl Ant funçã | Valor da compensação relativa a anos anteriores em função de processo judicial. | S-1.2 |
| vlrRendSusp | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8O | V8O\_VLRSUS | Vl Exig Susp | Valor do rendimento com exigibilidade suspensa. | S-1.2 |
| indTpDeducao | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8P | V8P\_TPDEDU | Tipo Dedução | Indicativo do tipo de dedução. | S-1.2 |
| vlrDedSusp | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8P | V8P\_VLSUSP | Vl Exig susp | Valor da dedução da base de cálculo do imposto de renda com exigibilidade suspensa. | S-1.2 |
| cpfDep | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8Q | V8Q\_CPFDEP | CPF Dependen | Número de inscrição no CPF. | S-1.2 |
| vlrDepenSusp | APTA101 | E0F | E0F\_MEM | (Memo) | TAFA609 | V8Q | V8Q\_VLDEPS | Vl Dedu Depe | Valor da dedução relativa a dependentes ou a pensão alimentícia com exigibilidade suspensa. | S-1.2 |
| dtLaudo | APTA101 | E0E | E0E\_MEM | (Memo) | TAFA609 | V8S | V8S\_DTLAUD | Dt. Laudo | Data da moléstia grave atribuída pelo laudo. | S-1.2 |
| cpfDep | APTA101 | E0E | E0E\_MEM | (Memo) | TAFA609 | V8S | V8S\_CPFDEP | CPF Depend. | Número de inscrição no CPF. | S-1.2 |
| dtNascto | APTA101 | E0E | E0E\_MEM | (Memo) | TAFA609 | V8S | V8S\_DTNASC | Dt. Nasc. Dp | Preencher com a data de nascimento. | S-1.2 |
| nome | APTA101 | E0E | E0E\_MEM | (Memo) | TAFA609 | V8S | V8S\_NOME | Nome Dep. | Nome do dependente. | S-1.2 |
| depIRRF | APTA101 | E0E | E0E\_MEM | (Memo) | TAFA609 | V8S | V8S\_DEPIR | Dep. Ir | Somente informar este campo em caso de dependente do trabalhador para fins de dedução de seu rendimento tributável pelo Imposto de Renda. | S-1.2 |
| tpDep | APTA101 | E0E | E0E\_MEM | (Memo) | TAFA609 | V8S | V8S\_TPDEP | Tipo Dep. | Tipo de dependente. | S-1.2 |
| descrDep | APTA101 | E0E | E0E\_MEM | (Memo) | TAFA609 | V8S | V8S\_DESCDE | Descr. Dep | Informar a descrição da dependência. | S-1.2 |

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - eSocial - Como se adequar ao eSocial leiaute S-1.2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8658568031127)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina:[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
