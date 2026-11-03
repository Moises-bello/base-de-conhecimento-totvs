---
content_hash: 517dd5423142c4f5615eb743806342133f50046fa2eea9249446737bde1a6676
fetched_at: '2026-06-29T00:10:06.121106+00:00'
page_id: '452719311'
product: rm
source: tdn-rm
title: Layout Para Importação de Sindicatos (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719311
version: 16
---

Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
As tabelas abaixo são premissas para a importação, caso as mesmas estejam vinculadas a tabela de Sindicato da base de origem:

* PEVENTO

Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:

* 0 (zero) ou 1(um) em campos do tipo **Booleano**;
* Números (00) em campos do tipo**Inteiro**;
* Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;
* (ddmmyyyy) em campos do tipo **Data**;
* (GRR20071514) em campos do tipo **String**;
* Começam /@ e terminam com @/ em campos do tipo **MEMO**.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código do sindicato** | **String** | **10** | **1** | **PSINDIC.CODIGO** |
| **Descrição** | **String** | **120** | **2** | **PSINDIC.NOME** |
| Rua | String | 30 | 3 | PSINDIC.RUA |
| Número | String | 8 | 4 | PSINDIC.NUMERO |
| Complemento |  | 16 | 5 | PSINDIC.COMPLEMENTO |
| Bairro |  | 20 | 6 | PSINDIC.BAIRRO |
| Unidade da federação | String | 2 | 7 | PSINDIC.ESTADO |
| Cidade |  | 32 | 8 | PSINDIC.CIDADE |
| CEP |  | 9 | 9 | PSINDIC.CEP |
| Nome do país | String | 16 | 10 | PSINDIC.PAIS |
| Valor do salário mínimo | Real | 15 | 11 | PSINDIC.SALARIOMINIMO |
| Percentual de vale-transporte | Real | 6 | 12 | PSINDIC.PERCENTVALETR |
| Desconto único do vale-transporte | Booleano | 1 | 13 | PSINDIC.DESCUNICOVALETR |
| Usa 30 dias p/ desc. do vale transporte | Booleano | 1 | 14 | PSINDIC.USA30DIASVALETR |
| Desconta contribuição no mês de admissão | Booleano | 1 | 15 | PSINDIC.DESCCONTRIBMESADM |
| Considera mês de rescisão para média | Booleano | 1 | 16 | PSINDIC.MEDIAMESRESCISAO |
| Paga férias proporcionais na rescisão | Booleano | 1 | 17 | PSINDIC.PAGAFERIASPROP |
| Número mínimo de meses trabalhados | Inteiro | 2 | 18 | PSINDIC.MINIMOFERPROPORC |
| Paga médias da 1. parc. do 13. | Booleano | 1 | 19 | PSINDIC.PAGAMEDIA1APARC |
| Ignora evento de férias para média | Booleano | 1 | 20 | PSINDIC.IGNORAEVTFERMEDIA |
| Permite fér. part. p. menores de 18 anos | Booleano | 1 | 21 | PSINDIC.MENOR18PARTIDAS |
| Permite fér. part. p. maiores de 50 anos | Booleano | 1 | 22 | PSINDIC.MAIOR50PARTIDAS |
| Paga licença a func. com menos de 1 ano | Booleano | 1 | 23 | PSINDIC.LICENCAMENOS1ANO |
| Func.menos 1 ano gozam fér. prop. Int. | Booleano | 1 | 24 | PSINDIC.PROPINTEGRAIS |
| Func. com fér. venc. gozam fér.integrais | Booleano | 1 | 25 | PSINDIC.VENCIDASINTEGRAIS |
| Paga férias se per. aquis. não começou | Booleano | 1 | 26 | PSINDIC.PGFERPERFUTURO |
| Mínimo garantido pelo sindicato | Real | 20 | 27 | PSINDIC.MINIMOGARANTIDO |
| Fórmula para cálc. de 1/3 férias | String | 8 | 28 | PSINDIC.FORMTERCOCONSTIT |
| Fórm. para cálc. de indeniz.-art.479 | String | 8 | 29 | PSINDIC.FORMBASEINDENIZ479 |
| Fórmula de estabilidade | String | 8 | 30 | PSINDIC.FORMESTABILIDADE |
| Grupo de insalubridade | Inteiro | 2 | 31 | PSINDIC.GRUPOINSALUBRID |
| Fórmula de número de dias aviso prévio | String | 8 | 32 | PSINDIC.FORNUMDIASAVISO |
| Fórmula de garantia de salário | String | 8 | 33 | PSINDIC.FORGARANTIASAL |
| CNPJ | String | 20 | 34 | PSINDIC.CNPJ |
| C¾digo da entidade sindical | String | 20 | 35 | PSINDIC.CODENTIDADE |
| Cons. Mês atual p/ média de férias | Booleano | 1 | 36 | PSINDIC.MESATUALMEDIAFERIAS |
| Telefone do sindicato | String | 15 | 37 | PSINDIC.TELEFONE |
| Telefone | String | 15 | 38 | PSINDIC.TELEFONE1 |
| Pessoa de contato dentro do sindicato | String | 45 | 39 | PSINDIC.NOMECONTATO |
| Utiliza parâmetros média férias rescisão | Booleano | 2 | 40 | PSINDIC.USAMEDIAFERIASRESC |
| Utiliza parâmetros média 13 rescisão | Booleano | 2 | 41 | PSINDIC.USAMEDIA13RESC |
| Completa Per. de gozo se saldo<10 dias | Inteiro | 1 | 42 | PSINDIC.COMPLETAPERFERIAS |
| Ignora faltas em férias normais | Inteiro | 1 | 43 | PSINDIC.IGNORAFALTASFERIASNORMAIS |
| Numero da Agencia do Sindicato | String | 6 | 44 | PSINDIC.NUMAGENCIA |
| Digito verificador agencia do sindicato | String | 2 | 45 | PSINDIC.DIGAGENCIA |
| Coligada do cliente fornecedor |  | 2 | 46 | PSINDIC.CODCOLFORNEC |
| Código do cliente fornecedor | String | 25 | 47 | PSINDIC.CODFORNECEDOR |
| Paga férias proporcional por justa causa | Booleano | 2 | 48 | PSINDIC.PAGAFERIASPROPJUSTACAUSA |
| Ignora feriados na contagem de férias | Booleano | 2 | 49 | PSINDIC.IGNORAFERIADOSCONTAGEMFERIAS |
| Calcula média verific. nro de meses | Booleano | 2 | 50 | PSINDIC.CALCMEDCOMISSAOMES |
| Ignora feriados na contagem de férias Normais | Inteiro | 2 | 51 | PSINDIC.IGNORAFERIADOCONTAGFERNORMAIS |
| Mês adm. entra média férias se adm. dia | Inteiro | 2 | 52 | PSINDIC.DIAMESADMMEDIAFERIAS |
| Mês adm. entra média 13 se adm. até dia | Inteiro | 2 | 53 | PSINDIC.DIAMESADMMEDIA13 |
| Mês adm. entra média aviso se adm. dia | Inteiro | 2 | 54 | PSINDIC.DIAMESADMMEDIAAVISO |
| Considera fó[rm.adic.na](http://rm.adic.na) 1a.parcela de 13o | Booleano | 2 | 55 | PSINDIC.CONSIDERAFORMADIC1APARC |
| Paga Dias Frac. Férias Coletivas | Inteiro | 2 | 56 | PSINDIC.PAGADIAFRACIONADOFERIASCOL |
| Calculo Media 13º Salario | Inteiro | 2 | 57 | PSINDIC.FORMACALCMEDIA13SAL |
| Calculo Media Férias | Inteiro | 2 | 58 | PSINDIC.FORMACALCMEDIAFERIAS |
| Calculo Media Aviso Prévio | Inteiro | 2 | 59 | PSINDIC.FORMACALCMEDIAAVPREVIO |
| Código Formula calculo DSR | String | 8 | 60 | PSINDIC.CODFORMULADSR |
| Descons. parâm. média 13 resc. Provisão | Booleano | 2 | 61 | PSINDIC.DESCUSAMEDIA13RESCPROV |
| Antecipa dias próx.per.nas fér.coletivas | Booleano | 2 | 62 | PSINDIC.ANTECIPAFERIASPROXPER |
| Mês admissão entra cálculo licença mat. | Inteiro | 2 | 63 | PSINDIC.DIAMESADMMEDIALICENCAMAT |
| Tipo da Entidade Sindical | Inteiro | 2 | 64 | PSINDIC.TPENTIDADESINDICAL |
| Usa par.específicos p/ média comissão | Booleano | 2 | 65 | PSINDIC.USAPARMEDIACOMISSAO |
| Calcula média para Desconto de Aviso Prévio | Booleano | 2 | 66 | PSINDIC.CALCMEDIADESCONTOAVISO |
| Média de insalubridade considera salário mínimo atual | Booleano | 2 | 67 | PSINDIC.MEDINSALUBCONSSALMINATUAL |
| Lança indenização adicional na dispensa sem justa causa, no período de 30 dias antes da data base. | Booleano | 2 | 68 | PSINDIC.LANCAINDADIC30DIASDTBASE |
| Data Base da correção salarial |  | 8 | 69 | PSINDIC.DATABASECORRSALARIAL |
| Utiliza cálculo de média de Remuneração Base para Professor | Booleano | 2 | 70 | PSINDIC.USAMEDIAREMBASEPROFESSOR |
| Considera Ano Anterior | Booleano | 2 | 71 | PSINDIC.CONSIDANOANTERIOR |
| Ignora as Faltas | Booleano | 2 | 72 | PSINDIC.IGNORAFALTAS |
| Código da Aplicação | String | 1 | 73 | PSINDIC.APLICACAO |
| Compara Salario Comissão | Booleano | 2 | 74 | PSINDIC.COMPARASALCOMISSAO |
| Mês Atual Entra Média 13º | Inteiro | 2 | 75 | PSINDIC.MESATUALMEDIA13O |
| Considera Mes Atual(Média) se Data < 15 | Booleano | 2 | 76 | PSINDIC.MESATUALMENOR15DIAS |
| Data Base - Dia | Inteiro | 2 | 77 | PSINDIC.DIADATABASE |
| Data Base - Mês | Inteiro | 2 | 78 | PSINDIC.MESDATABASE |
| Não pagar 0,5 dia de abono pecuniário quando o saldo de Férias for fracionado | Booleano | 2 | 79 | PSINDIC.MESDATABASE |

### **ATENÇÃO: Houve alteração no leiaute conforme TDN  [DT - Importação e Exportação - Remoção de campos não utilizados nas tabelas de Sindicato e Função](https://tdn.totvs.com/pages/viewpage.action?pageId=969994406)**
