---
content_hash: 1964a1cf33f94122f6e78e4ec9a50215493cc479d8b4b7cd08eeea68ba3e7fc6
fetched_at: '2026-06-29T00:12:15.327629+00:00'
page_id: '976143740'
product: rm
source: tdn-rm
title: DT - Smart View - Relatório de Admitidos e Desligados - Turnover
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=976143740
version: 11
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart View - Declaração de Encargos de Família para Fins de Imposto de Renda |
| País: | Brasil |
| Épico | [DRHROTRM-14208](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14208) |

## **02. VERSÃO**

12.1.2510 e superiores.

## **03. S****ITUAÇÃO/REQUISITO**

Elaborar um relatório que reúna os dados dos relatórios, abaixo, adaptando-os ao novo modelo de ferramenta com o uso do Smart View:

* **FOPREL00071 - Admitidos no Mês.TotvsReport**
* **FOPREL00041 - Demitido no Mês.TotvsReport**
* **FOPREL00040 - Demitidos no Mês-1.TotvsReport**
* **FOPREL00111 - Relação de Funcionários Alfabética  Data Admissão.TotvsReport**

**FOPREL00040 - Demitidos no Mês**

**FOPREL00071 - Admitidos**

**FOPREL00111 - Relação de Funcionários Alfabética Data Admissão**

## **04. SOLUÇÃO**

Foi disponibilizado o objeto de negócios e o relatório no Smart View, a nova ferramenta de análise de dados da TOTVS. Este novo relatório possui a interface mais amigável para o usuário.

**Turnover**  
  
**Colaboradores anteriores ativos**: Quantidade de colaboradores que possuem data de admissão e data de demissão menor que o início do período de referência  
  
**Transferência de colaboradores**: Quantidade de Funcionários admitidos com Transferência = 'Sim'  
  
**Novos colaboradores**: Quantidade de colaboradores com data de admissão dentro do período de referência.  
  
**Total de colaboradores ativos**: Quantidade de colaboradores que possuem data de admissão dentro do período de referência e de demissão fora do período de referência  
  
**Admissões**: Igual o campo Novos colaboradores  
  
**Desligamentos**: Data de demissão dentro do período de referência  
  
**Redução de colaboradores**: Quantidade de demissões dentro do período + quantidade que saíram por transferência dentro do período  
  
**Total de rotatividade**: Admissões - Desligamentos   
  
**Rotatividade admissional (%)**: (Admissões dentro do período / Número total de colaboradores ativos no final do período) x 100  
  
**Rotatividade de desligados (%)**: (Demissões dentro do período/ Número total de colaboradores ativos no período) x 100  
  
**Rotatividade de transferências (%):** (Qtde de transferências de entrada e saída / Quantidade total de funcionários ativos no período) x 100  
  
**Turnover atual (%)**: (Admissões dentro do período+ Demissões dentro do período / 2) / Número total de colaboradores x 100

| Campo relatório | Tabela e campo |
| --- | --- |
| Nome da Empresa | GCOLIGADA.NOMEFANTASIA |
| CNPJ/CPF | GCOLIGADA.CGC |
| Estabelecimento/Filial | GFILIAL.NOMEFANTASIA |
| Matrícula | PFUNC.CHAPA |
| Data de Admissão | PFUNC.DATAADMISSAO |
| Nome da Pessoa Colaboradora | PFUNC.NOME |
| Cargo/Função | PFUNCAO.NOME |
| Tipo Contratação | PFUNC.TIPOADMISSAO |
| Salário Contratual | PFUNC.SALARIO |
| Transferência | PFUNC.TIPOADMISSAO |
| Data Desligamento | PFUNC.DATADEMISSAO |
| Aviso Prévio | PFUNC.TEMAVISOPREVIO, PFUNC.DESCONTAAVISOPREVIO, PFUNC.DTAVISOPREVIOTRAB |
| Código/Motivo do Desligamento | PFUNC.MOTIVODEMISSAO |
| PCD | PPESSOA.DEFICIENTEAUDITIVO,  PPESSOA.DEFICIENTEFISICO, PPESSOA.DEFICIENTEINTELECTUAL, PPESSOA.BRPDH, PPESSOA.DEFICIENTEFALA, PPESSOA.DEFICIENTEVISUAL, PPESSOA.DEFICIENTEMENTAL |
| Feminino, Masculino | PPESSOA.SEXO |
| Branco, Pardo, Amarelo, Preto e Indígena | PPESSOA.CORRACA |
| Aprendiz | PFUNC.CODTIPO |
| Estágio | PFUNC.CODTIPO |

## **05. DEMAIS INFORMAÇÕES**

Smart View e RM

[FOPTRP0021 - Relatório de Admitidos e Desligados - Turnover](https://tdn.totvs.com/pages/editpage.action?pageId=977835958)
