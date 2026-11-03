---
content_hash: 0ed63565c91965eb36cb5a68448095d18855e6db0c5135fcce46bfadca0b45ea
fetched_at: '2026-06-29T00:05:48.961052+00:00'
page_id: '1034783974'
product: rm
source: tdn-rm
title: DT - Smart View - Termo de Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1034783974
version: 2
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart View - Termo de Rescisão |
| País: | Brasil |
| Épico | [DRHCALCRM-9869](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-9869) |

## **02. VERSÃO**

12.1.2602 e superiores

## **03. S****ITUAÇÃO/REQUISITO**

Migrar o relatório **FOPREL00001** **- Termo de Rescisão - Portaria 16212010 12.1** para o novo modelo de ferramenta utilizando o Smart View e melhorar sua usabilidade.

Novo relatório no TOTVS Compartilhamento: **FOPTRP0024**

## **04. SOLUÇÃO**

Foi disponibilizado o objeto de negócio e o relatório no Smart View como um modelo unificado dos 3 relatórios de contrato de experiência. Este novo relatório possui informações semelhantes entre eles para melhorar a usabilidade e padronização.

| Campo | Descrição do Campo | Campo na Tabela |  |
| --- | --- | --- | --- |
| CPF | Filtra pelo CPF | PFUNC.CPF |  |
| Matrícula | Filtra pela matrícula do funcionário. | PFUNC.CHAPA |  |
| Mês da Competência | Filtra o código da seção de lotação do funcionário. | PFFINANC.MESCOMP |  |
| Ano da Competência | Filtra pelo código de situação do funcionário. | PFFINANC.ANOCOMP |  |
| Período | Filtra pela Filial | PFFINANC.NROPERIODO |  |
| Imprimir Pensão Alimentícia | Imprime no relatório se consta valores de pensão alimentícia | PFFINANC |  |
| Imprimir Verbas Rescisórias | Imprime no relatório os valores da rescisão | PFFINANC |  |
| Imprimir Campos em Branco | Imprime campos em branco | PFFINANC |  |
| Fórmula para Saldo de Salário | Define no filtro a fórmula para o saldo de salário | PEVENTO.CODIGOCALCULO |  |
| Fórmula para Dias de Salário | Define no filtro os dias de salário | PEVENTO.CODIGOCALCULO |  |
| Fórmula para Faltas/DSR | Define no filtro para ausências/faltas | PEVENTO.CODIGOCALCULO |  |
| Fórmula para Remuneração Mês Anterior Afastamento | Define no filtro os valores da remuneração anterior por afastamento | PEVENTO.CODIGOCALCULO |  |
| Fórmula para Pensão Alimentícia (%) FGTS | Define no filtro a fórmula para constar os valores de Pensão | PEVENTO.CODIGOCALCULO |  |
| Fórmula para Ressalvas | Define o filtro de ressalvas | PEVENTO.CODIGOCALCULO |  |
| Fórmula para Informações à CAIXA | Define no filtro as informações necessárias para CAIXA | PEVENTO.CODIGOCALCULO |  |
| Emissão dos Termos de Quitação / Homologação | Filtra os termos de Quitação/Homologação | PEVENTO.CODIGOCALCULO |  |
| Tipo de Contrato de Trabalho | Filtra pelo contrato de trabalho | PDADOSRESCISAO.TIPOCONTRATO |  |
| Fórmula para Tipo de Contrato de Trabalho | Define no filtro o tipo de contrato de trabalho | PEVENTO.CODIGOCALCULO |  |
| TRCT de Rescisão Complementar | Termo de rescisão complementar | PDADOSRESCISAO |  |
| Campo 66 e 67 Forçar valor do Envelope | Forçar valores de envelope 66 e 67 | PEVENTO.CODIGOCALCULO |  |
| Data Aviso Prévio Indenizado igual à data de demissão | Filtra a data de aviso prévio indenizado igual para data de demissão | PDADOSRESCISAO |  |
| Para Aviso Prévio Trabalhado considerar um dia útil antes do inicio do aviso | Define um dia útil antes do inicio do aviso prévio | PDADOSRESCISAO |  |
| Não Somar Média de Férias Vencidas | Define não somar média de férias vencidas | PEVENTO.CODIGOCALCULO |  |
| Não Somar Média de Férias Prop. | Define não somar média de férias proporcionais | PEVENTO.CODIGOCALCULO |  |
| **Campos 58 a 99 – Informação de verbas rescisórias proventos** | | |  |
| Campo 58 | Descanso Semanal Remunerado (DSR); | Rubricas criadas pelo usuário a partir do número 100 | PDADOSRESCISAO |
| Campo 59 | Reflexo do DSR sobre Salário Variável; |  | PDADOSRESCISAO |
| Campo 60 | Multa Art. 477, § 8º/CLT; | 009 - Multa Art. 477 | PDADOSRESCISAO |
| Campo 61 | Multa Art. 479/CLT; | Rubricas criadas pelo usuário a partir do número 100 | PDADOSRESCISAO |
| Campo 62 | Salário –Família; |  | PDADOSRESCISAO |
| Campo 63 | Décimo –Terceiro Salário Proporcional; |  | PDADOSRESCISAO |
| Campo 64 \*\*\* – (caso exista mais de uma verba diversa, criar os subitens 64.1, 64.2, 64.3...) | Décimo –Terceiro Salário Exercícios Anteriores |  | PDADOSRESCISAO |
| Campo 65 | Férias Proporcionais; |  | PDADOSRESCISAO |
| Campo 66 \* – (caso exista mais de uma verba diversa, criar os subitens 66.1, 66.2, 66.3...); | Férias Vencidas |  | PDADOSRESCISAO |
| Campo 67 \* – (caso exista mais de uma verba diversa, criar os subitens 67.1, 67.2, 67.3...); | Férias Vencidas (Reflexo/Dobra) |  | PDADOSRESCISAO |
| Campo 68 | Terço Constitucional de Férias; |  | PDADOSRESCISAO |
| Campo 69 | Aviso –Prévio Indenizado; |  | PDADOSRESCISAO |
| Campo 70 | Décimo –Terceiro Salário (Aviso–Prévio Indenizado); |  | PDADOSRESCISAO |
| Campo 71 | Férias (Aviso–Prévio Indenizado); |  | PDADOSRESCISAO |
| Campo 72 | Percentagem; | 006 - Percentagem | PDADOSRESCISAO |
| Campo 73 | Prêmios; | 008 - Prêmios | PDADOSRESCISAO |
| Campo 74 | Viagens; | 010 - Viagens | PDADOSRESCISAO |
| Campo 75 | Sobreaviso; | 015 - Sobreaviso | PDADOSRESCISAO |
| Campo 76 | Prontidão; | 016 - Prontidão | PDADOSRESCISAO |
| Campo 77 | Adicional por Tempo de Serviço; | 018 - Adicional Tempo de Serviço | PDADOSRESCISAO |
| Campo 78 | Adicional por Transferência de Localidade de Trabalho; | 019 - Adicional Por Transferencia de Localidade de Trabalho | PDADOSRESCISAO |
| Campo 79 | Salário Família Excedente ao Valor Legal; | 020 - Salario Familia no que exceder o valor legal obrigatorio | PDADOSRESCISAO |
| Campo 80 | Abono/Gratificação de Férias Excedente 20 Dias Salário; | 021 - Abono ou gratificacao de férias | PDADOSRESCISAO |
| Campo 81 | Valor Global Diárias para ViagemExcedente 50% Salário; | 022 - Diarias para viagem | PDADOSRESCISAO |
| Campo 82 | Ajuda de Custo Art. 470/CLT; | 023 - Ajuda de custo | PDADOSRESCISAO |
| Campo 83 | Etapas Marítimos; | 024 - Etapas Maritimo | PDADOSRESCISAO |
| Campo 84 | Licença –Prêmio Indenizada; | 025 - Licenca Premio | PDADOSRESCISAO |
| Campo 85 | Quebra de Caixa; | 026 - Quebra de caixa | PDADOSRESCISAO |
| Campo 86 | Participação nos Lucros ou Resultados; | 027 - Participacao nos lucros/resultados | PDADOSRESCISAO |
| Campo 87 | Indenização a Título de Incentivo à Demissão; | 028 - Indenizacao recebida | PDADOSRESCISAO |
| Campo 88 | Bolsa Aprendizagem; | 029 - Bolsa Aprendizagem | PDADOSRESCISAO |
| Campo 89 | Abonos Desvinculados do Salário; | 030 - Abonos Desvinculados | PDADOSRESCISAO |
| Campo 90 | Ganhos Eventuais Desvinculados do Salário; | 031 - Ganhos eventuais | PDADOSRESCISAO |
| Campo 91 | Reembolso Creche; | 032 - Reembolso Creche | PDADOSRESCISAO |
| Campo 92 | Reembolso Babá; | 033 - Reembolso baba | PDADOSRESCISAO |
| Campo 93 | Gratificação Semestral; | 034 - Gratificacao Semestral | PDADOSRESCISAO |
| Campo 94 | Salário do Mês Anterior à Rescisão; | Rubricas criadas pelo usuário a partir do número 100 | PDADOSRESCISAO |
| Campo 95 \* - (caso exista mais de uma verba diversa, criar os subitens 95.1, 95.2, 95.3...); | Outras Verbas |  | PDADOSRESCISAO |
| Campo 96 | Indenização Art. 9º, Lei n.º 7.238/84; |  | PDADOSRESCISAO |
| Campo 97 | Indenização Férias Escolares; |  | PDADOSRESCISAO |
| Campo 98 | Multa do Art. 476–A, § 5º, da CLT; | 036 - Multa do Art. 476-a, § 5º, da CLT | PDADOSRESCISAO |
| Campo 99 | Ajuste do saldo devedor. | Rubrica criada pelo usuário a partir do número 100 | PDADOSRESCISAO |
| **Campos 100 a 116 – Informação de verbas de deduções** | | |  |
| Campo 100 | Pensão Alimentícia; | Rubricas criadas pelo usuário a partir do número 100 | Rubricas relacionadas a eventos Desconto |
| Campo 101 | Adiantamento Salarial; |
| Campo 102 | Adiantamento de 13º Salário; |
| Campo 103 | Aviso –Prévio Indenizado; |
| Campo 104 | Indenização Art. 480 CLT; |
| Campo 105 | Empréstimo em Consignação; |
| Campo 106 | Vale –Transporte; |
| Campo 107 | Reembolso do Vale –Transporte; |
| Campo 108 | Vale –Alimentação; |
| Campo 109 | Reembolso do Vale –Alimentação; |
| Campo 110 | Contribuição para o FAPI; |
| Campo 111 | Contribuição Sindical Laboral; |
| Campo 112.1 | Previdência Social; |
| Campo 112.2 | Previdência Social13º Salário; |
| Campo 113 | Contribuição Previdência Complementar; |
| Campo 114.1 | IRRF; |
| Campo 114.2 | IRRF sobre 13º Salário; |
| Campo 114.3 | IRRF sobre Participação nos Lucros ou Resultados; |
| Campo 115{**}**\* - (caso exista desconto não especificado nos campos acima; havendo mais de um desconto, criar os subitens 115.1; 115.2...); | Outros Descontos |
| Campo 116 | Desconto de Valor Líquido de TRCT QuitadoDecisão Judicial. |
| Ordenação do relatório |  |  | |
| Data início do desligamento | Data de inicio do desligamento/demissão funcionário | PFUNC.DATAADMISSAO | |
| Data fim do desligamento | Data de fim do desligamento/demissão funcionário | PFUNC.DATAADMISSAO | |

## **05. DEMAIS INFORMAÇÕES**

* Smart View e RM
