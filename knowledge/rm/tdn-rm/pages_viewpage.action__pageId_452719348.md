---
content_hash: 81e9f9cdb8eb1ce0472675cfbf13b6849ad68f635429ca75a4020fd97f67a930
fetched_at: '2026-06-29T00:10:06.902495+00:00'
page_id: '452719348'
product: rm
source: tdn-rm
title: Layout Para Importação de Funções (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719348
version: 9
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação, caso a mesma esteja vinculada a tabela de Funções da base de origem:  
- PCARGO  
   
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
-  Números (00) em campos do tipo**Inteiro**;  
-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
- (ddmmyyyy) em campos do tipo **Data**;  
- (GRR20071514) em campos do tipo **String**;  
- Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Código** | **String** | **10** | **1** | **PFUNCAO.CODIGO** |
| **Nome da Função** | **String** | **100** | **2** | **PFUNCAO.NOME** |
| Numero de Pontos (Formato 99999,99) | Real | 15 | 3 | PFUNCAO.NUMPONTOS |
| CBO | String | 08 | 4 | PFUNCAO.CBO |
| Código do Cargo | String | 16 | 5 | PFUNCAO.CARGO |
| Indicativo de Inatividade (0-Não/1-Sim) | Inteiro | 01 | 6 | PFUNCAO.INATIVA |
| Atividade de Transporte (0-Não/1-Sim) | Inteiro | 01 | 7 | PFUNCAO.ATIVTRANSP |
| Descrição (começa com /@ e termina com @/) | Memo | 250 | 8 | PFUNCAO.DESCRICAO |
| Faixa Salarial | String | 16 | 9 | PFUNCAO.FAIXASALARIAL |
| Limite de Funcionários | Inteiro | 10 | 10 | PFUNCAO.LIMITEFUNC |
| Valor Verba Q.Vagas | Real | 15 | 11 | PFUNCAO.VERBAQUADROVAGAS |
| Percentual Verba Q.Vagas | Real | 15 | 12 | PFUNCAO.PERCQUADROVAGAS |
| CBO 2002 | String | 10 | 13 | PFUNCAO.CBO2002 |
| Código da tabela | String | 10 | 14 | PFUNCAO.CODTABELA |
| Nro pontos disponíveis para a função | Inteiro | 10 | 15 | PFUNCAO.BENEFPONTOS |
| Objetivo da função | Memo | 100 | 16 | PFUNCAO.OBJETIVO |
| Descrição para o PPP | Memo | 100 | 17 | PFUNCAO.DESCRICAOPPP |
| Exibição no Organograma | Booleano | 01 | 18 | PFUNCAO.EXIBEORGANOGRAMA |
| Cód. função chefia | String | 10 | 19 | PFUNCAO.CODFUNCAOCHEFIA |
| Tipo de Função PPE | String | 02 | 20 | PFUNCAO.CODTIPOFUNCAO |
| Sigla da função/cargo | String | 30 | 21 | PFUNCAO.SIGLA |
| Definir se o cargo é de confiança ou não | Booleano | 01 | 22 | PFUNCAO.ESOCIALFUNCAOCONF |
| Integração GUPY: ´de para´ do nome da função utilizado para enviar CSV com dados da entidade | Booleano | 01 | 23 | PFUNCAO.SIMILARIDADEINTEGRACAOGUPY |

### **ATENÇÃO: Houve alteração no leiaute conforme TDN  [DT - Importação e Exportação - Remoção de campos não utilizados nas tabelas de Sindicato e Função](https://tdn.totvs.com/pages/viewpage.action?pageId=969994406)**
