---
article_id: 11379447201431
category: GPE - eSocial - Processo Trabalhista
content_hash: c179b7663902d0fd3e00046a1c59bfaf7ee939b7a880076bed8dc6fb2fb3e0ed
fetched_at: '2026-06-28T22:45:00.702127+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2501 - Qual a estrutura do evento S-2501
  conforme leiaute S-1.1
type: support-article
updated_at: '2024-07-22T12:57:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11379447201431-RH-Linha-Protheus-GPE-eSocial-S-2501-Qual-a-estrutura-do-evento-S-2501-conforme-leiaute-S-1-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25071358281879) Tempo aproximado para leitura: **00:06:00 min** **Dúvida**Qual a estrutura do evento S-2501 conforme **leiaute S-1.1** disponibilizado pelo eSocial?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Este evento deve ser utilizado para informar os valores do imposto sobre a renda da pessoa física e das contribuições sociais previdenciárias, inclusive as destinadas a Terceiros, incidentes sobre as base de cálculo constantes das decisões condenatórias e homologatórias de acordo proferidas nos processos trabalhistas perante a Justiça do Trabalho e nos acordos celebrados no âmbito das Comissões de Conciliação Prévia - CCP e dos Núcleos Intersindicais – Ninter, que foram informados no evento S-2500.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela de Resumo dos Registros** | | | | | | |
| **Grupo** | **Grupo Pai** | **Nível** | **Descrição** | **Ocor.** | **Chave** | **Condição** |
| [eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2501_eSocial) |  | 1 | eSocial | 1 | - | O |
| [evtContProc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2501) | eSocial | 2 | Evento Informações de Tributos Decorrentes de Processo Trabalhista | 1 | Id | O |
| [ideEvento](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2501_ideEvento) | evtContProc | 3 | Informações de identificação do evento | 1 | - | O |
| [ideEmpregador](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2501_ideEmpregador) | evtContProc | 3 | Informações de identificação do empregador ou do contribuinte que está prestando a informação | 1 | tpInsc\*, nrInsc\* | O |
| [ideProc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2501_ideProc) | evtContProc | 3 | Identificação do processo | 1 | nrProcTrab\*, perApurPgto\* | O |
| [ideTrab](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2501_ideTrab) | evtContProc | 3 | Identificação do trabalhador | 1-N | cpfTrab | O |
| [calcTrib](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2501_ideTrab_calcTrib) | ideTrab | 4 | Identificação do período e da base de cálculo dos tributos | 1-360 | perRef | O |
| [infoCRContrib](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2501_ideTrab_calcTrib_infoCRContrib) | calcTrib | 5 | Informações das contribuições sociais | 0-99 | tpCR | OC |
| [infoCRIRRF](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/index.html#2501_ideTrab_infoCRIRRF) | ideTrab | 4 | Informações de IRRF | 0-99 | tpCR | OC |

Legenda:  
**Condição** - refere-se a obrigatoriedade ou não da existência de registro para determinado grupo  
de informações. As condições podem ser:  
"O" = obrigatoriedade de prestação de informações naquele grupo;  
"N" = não pode ser informado;  
“F” = facultativo;  
"OC" = obrigatório se existir informação.  
  
**Ocorrência (Ocor)** - os indicativos desta coluna podem ser compostos por apenas um número ou  
por dois, separados entre si por um hífen, conforme o seguinte:  
a) Se houver apenas o número [1], o grupo/campo é obrigatório (quantidade mínima e máxima  
de 1 registro);  
b) Se houver 2 números separados por hífen, o número antes do hífen indica a quantidade  
mínima e o número depois do hífen indica a quantidade máxima de registros.  
Exemplo:   
0-1: grupo/campo não obrigatório ou com no máximo um registro;  
1-99: deve existir no mínimo um (portanto é obrigatório) e no máximo noventa e nove registros;  
0-999: campo não obrigatório com o máximo de 999 registros.  
  
**Chave** - É o conjunto de um ou mais campos, cujo conteúdo, considerando a sua combinação  
nunca se repete e pode ser usado como um índice para os demais campos da tabela do banco de dados.  
  
Para mais informações sobre a legenda, acesse: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-retificada-em-02122022.pdf/>  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-2500 - Quais são os eventos para Processos Trabalhistas no leiaute S-1.1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11330081055895)  
[RH - Linha Protheus - GPE - eSocial - Como se adequar ao eSocial leiaute S-1.0 NT 06/2022 e leiaute S-1.1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8658568031127)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-retificada-em-02122022.pdf/)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
