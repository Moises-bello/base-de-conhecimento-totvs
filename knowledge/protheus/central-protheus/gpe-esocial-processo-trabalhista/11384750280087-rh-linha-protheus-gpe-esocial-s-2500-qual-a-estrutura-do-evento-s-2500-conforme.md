---
article_id: 11384750280087
category: GPE - eSocial - Processo Trabalhista
content_hash: 7ab0b5d1920bf79e047de9ed0466bf4f3c1b0b08938dd6c92c954ccafb707bea
fetched_at: '2026-06-28T22:45:00.691910+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Qual a estrutura do evento S-2500
  conforme leiaute S-1.1
type: support-article
updated_at: '2024-07-22T12:56:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11384750280087-RH-Linha-Protheus-GPE-eSocial-S-2500-Qual-a-estrutura-do-evento-S-2500-conforme-leiaute-S-1-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24475526230167) Tempo aproximado para leitura: **00:07:00 min** **Dúvida**Qual a estrutura/leiaute do evento S-2500 conforme leiaute S-1.1 disponibilizado pelo eSocial?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Este evento registra as informações decorrentes de processos trabalhistas perante a Justiça do Trabalho e de acordos celebrados no âmbito das Comissões de Conciliação Prévia - CCP e dos Núcleos Intersindicais – Ninter. Neste evento são prestadas informações cadastrais e contratuais relativas ao vínculo, as bases de cálculo para recolhimento de FGTS e da contribuição previdenciária do RGPS.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Tabela de Resumo dos Registros | | | | | | |
| Grupo | Grupo Pai | Nível | Descrição | Ocor. | Chave | Condição |
| [eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_eSocial) |  | 1 | eSocial | 1 | - | O |
| [evtProcTrab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500) | [eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_eSocial) | 2 | Evento Processo Trabalhista | 1 | [Id](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_Id) | O |
| [ideEvento](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideEvento) | [evtProcTrab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500) | 3 | Informações de identificação do evento | 1 | - | O |
| [ideEmpregador](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideEmpregador) | [evtProcTrab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500) | 3 | Informações de identificação do empregador ou do contribuinte que está prestando a informação | 1 | tpInsc\*, nrInsc\* | O |
| [ideResp](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideEmpregador_ideResp) | [ideEmpregador](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideEmpregador) | 4 | Identificação do contribuinte, caso tenha havido imposição de responsabilidade indireta | 0-1 | - | OC |
| [infoProcesso](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_infoProcesso) | [evtProcTrab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500) | 3 | Informações do processo judicial ou de demanda submetida à CCP ou ao NINTER | 1 | [nrProcTrab\*](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_infoProcesso_nrProcTrab) | O |
| [dadosCompl](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_infoProcesso_dadosCompl) | [infoProcesso](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_infoProcesso) | 4 | Informações complementares do processo ou da demanda | 1 | - | O |
| [infoProcJud](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_infoProcesso_dadosCompl_infoProcJud) | [dadosCompl](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_infoProcesso_dadosCompl) | 5 | Informações complementares do processo judicial | 0-1 | - | [O (se origem = [1]);](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_infoProcesso_origem) |
| N (nos demais casos) |
| [infoCCP](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_infoProcesso_dadosCompl_infoCCP) | [dadosCompl](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_infoProcesso_dadosCompl) | 5 | Informações complementares da demanda submetida à CCP ou ao NINTER | 0-1 | - | [O (se origem = [2]);](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_infoProcesso_origem) |
| N (nos demais casos) |
| [ideTrab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab) | [evtProcTrab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500) | 3 | Informações do trabalhador | 1 | [cpfTrab\*](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_cpfTrab) | O |
| [dependente](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_dependente) | [ideTrab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab) | 4 | Informações dos dependentes | 0-99 | [cpfDep](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_dependente_cpfDep) | [F (se existir contrato com indContr = [S]);](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_indContr) |
| OC (nos demais casos) |
| [infoContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr) | [ideTrab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab) | 4 | Informações do contrato de trabalho | jan/99 | matricula, codCateg, dtInicio | O |
| [infoCompl](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_infoCompl) | [infoContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr) | 5 | Informações complementares do contrato de trabalho | 0-1 | - | [O (se indContr = [N]);](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_indContr) |
| N (nos demais casos) |
| [remuneracao](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_infoCompl_remuneracao) | [infoCompl](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_infoCompl) | 6 | Informações da remuneração e periodicidade de pagamento | 0-99 | [dtRemun](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_infoCompl_remuneracao_dtRemun) | N (se (infoContr/tpContr for diferente de [6] e tpRegTrab = [2]); |
| O (se (infoContr/tpContr for diferente de [6] e tpRegTrab = [1]) ou se infoContr/codCateg = [721, 722, 771]); |
| OC (nos demais casos) |
| [infoVinc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_infoCompl_infoVinc) | [infoCompl](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_infoCompl) | 6 | Informações sobre o vínculo trabalhista | 0-1 | - | [O (se infoContr/tpContr for diferente de [6]);](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_tpContr) |
| N (nos demais casos) |
| [duracao](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_infoCompl_infoVinc_duracao) | [infoVinc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_infoCompl_infoVinc) | 7 | Duração do contrato de trabalho | 0-1 | - | [O (se tpRegTrab = [1]);](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_infoCompl_infoVinc_tpRegTrab) |
| N (nos demais casos) |
| [observacoes](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_infoCompl_infoVinc_observacoes) | [infoVinc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_infoCompl_infoVinc) | 7 | Observações do contrato de trabalho | 0-99 | - | OC |
| [sucessaoVinc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_infoCompl_infoVinc_sucessaoVinc) | [infoVinc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_infoCompl_infoVinc) | 7 | Grupo de informações da sucessão de vínculo trabalhista/estatutário | 0-1 | - | OC |
| [infoDeslig](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_infoCompl_infoVinc_infoDeslig) | [infoVinc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_infoCompl_infoVinc) | 7 | Informações do desligamento | 1 | - | O |
| [infoTerm](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_infoCompl_infoTerm) | [infoCompl](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_infoCompl) | 6 | Informações de término de TSVE | 0-1 | - | [OC (se infoContr/tpContr = [6];](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_tpContr) |
| N (nos demais casos) |
| [mudCategAtiv](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_mudCategAtiv) | [infoContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr) | 5 | Informação do novo código de categoria e/ou da nova natureza da atividade | 0-99 | [dtMudCategAtiv](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_mudCategAtiv_dtMudCategAtiv) | O (se indCateg = [S] ou se indNatAtiv = [S]); |
| N (nos demais casos) |
| [unicContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_unicContr) | [infoContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr) | 5 | Informações dos vínculos/contratos incorporados | 0-99 | matUnic, codCateg, dtInicio | [O (se indUnic = [S]);](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_indUnic) |
| N (nos demais casos) |
| [ideEstab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_ideEstab) | [infoContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr) | 5 | Identificação do estabelecimento | 1 | - | O |
| [infoVlr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_ideEstab_infoVlr) | [ideEstab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_ideEstab) | 6 | Informações dos períodos e valores | 1 | - | O |
| [idePeriodo](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo) | [infoVlr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_ideEstab_infoVlr) | 7 | Identificação do período ao qual se referem as bases de cálculo | 0-360 | [perRef](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_perRef) | [O (se repercProc = [1]);](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_ideEstab_infoVlr_repercProc) |
| N (nos demais casos) |
| [baseCalculo](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_baseCalculo) | [idePeriodo](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo) | 8 | Bases de cálculo de contribuição previdenciária e FGTS | 1 | - | O |
| [infoAgNocivo](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_baseCalculo_infoAgNocivo) | [baseCalculo](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_baseCalculo) | 9 | Grau de exposição a agentes nocivos | 0-1 | - | O (se o código de categoria for igual a [1XX, 2XX, 3XX, 731, 734, 738] ou se o código de categoria for igual a [4XX] com {categOrig} em S-2300 = [1XX, 2XX, 3XX, 731, 734, 738]); |
| N (nos demais casos) |
| [infoFGTS](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_infoFGTS) | [idePeriodo](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo) | 8 | Informações referentes a bases de cálculo de FGTS para geração de guia | 0-1 | - | OC |
| [baseMudCateg](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_baseMudCateg) | [idePeriodo](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#r_2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo) | 8 | Bases de cálculo já declaradas em GFIP, no caso de reconhecimento de mudança de código de categoria | 0-1 | - | [OC (se indCateg = [S]);](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2500_ideTrab_infoContr_indCateg) |
| N (nos demais casos) |

**Legenda:  
Condição -** refere-se a obrigatoriedade ou não da existência de registro para determinado grupo  
de informações. As condições podem ser:  
"O" = obrigatoriedade de prestação de informações naquele grupo;  
"N" = não pode ser informado;  
“F” = facultativo;  
"OC" = obrigatório se existir informação.  
 **Ocorrência (Ocor) -** os indicativos desta coluna podem ser compostos por apenas um número ou  
por dois, separados entre si por um hífen, conforme o seguinte:  
a) Se houver apenas o número [1], o grupo/campo é obrigatório (quantidade mínima e máxima de 1 registro);  
b) Se houver 2 números separados por hífen, o número antes do hífen indica a quantidade mínima e o número depois do hífen indica a quan**t**idade máxima de registros.  
Exemplo:   
0-1: grupo/campo não obrigatório ou com no máximo um registro;  
1-99: deve existir no mínimo um (portanto é obrigatório) e no máximo noventa e nove registros;  
0-999: campo não obrigatório com o máximo de 999 registros.  
  
**Chave** - É o conjunto de um ou mais campos, cujo conteúdo, considerando a sua combinação nunca se repete e pode ser usado como um índice para os demais campos da tabela do banco de dados.Para mais informações sobre a legenda, acesse: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-retificada-em-02122022.pdf/> **Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-2500 - Quais são os eventos para Processos Trabalhistas no leiaute S-1.1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11330081055895)  
[RH - Linha Protheus - GPE - eSocial - Como se adequar ao eSocial leiaute S-1.0 NT 06/2022 e leiaute S-1.1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8658568031127)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-retificada-em-02122022.pdf/)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
