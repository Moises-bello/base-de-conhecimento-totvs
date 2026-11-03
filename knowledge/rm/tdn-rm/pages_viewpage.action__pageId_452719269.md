---
content_hash: 9fabe5db93fd877e426c379f61a1cbea56b0b820351633be9c948a3b645a1ebb
fetched_at: '2026-06-29T00:10:04.996595+00:00'
page_id: '452719269'
product: rm
source: tdn-rm
title: Layout Para Importação de Dependentes (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719269
version: 16
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação de Dependentes;  
- PFUNC  
   
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
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFDEPEND.CHAPA** |
| **Nº do Dependente** | **Inteiro** | **2** | **2** | **PFDEPEND.NRODEPEND** |
| Nome do Dependente | String | 120 | 3 | PFDEPEND.NOME |
| CPF do Dependente | String | 12 | 4 | PFDEPEND.CPF |
| Data de Nascimento do Dependente | Data | 8 | 5 | PFDEPEND.DTNASCIMENTO |
| **Sexo do Dependente (M/F)** | **String** | **1** | **6** | **PFDEPEND.SEXO** |
| **Estado Civil do Dependente**  **C - Casado**  **D - Desquitado**  **E - União Estável**  **I - Divorciado**  **O - Outros**  **P - Separado**  **S - Solteiro**  **V - Viúvo)** | **String** | **1** | **7** | **PFDEPEND.ESTADOCIVIL** |
| Local de Nascimento do Dependente | String | 32 | 8 | PFDEPEND.LOCALNASCIMENTO |
| Nome do Cartório | String | 40 | 9 | PFDEPEND.CARTORIO |
| Nº do Registro | String | 10 | 10 | PFDEPEND.NROREGISTRO |
| Nº do Livro de Registro | String | 8 | 11 | PFDEPEND.NROLIVRO |
| Nº da Folha de Registro | String | 5 | 12 | PFDEPEND.NROFOLHA |
| Incidência de IRRF  (0-Não/1-Sim) | Inteiro | 1 | 13 | PFDEPEND.INCIRRF |
| Incidência de INSS  (0-Não/1-Sim) | Inteiro | 1 | 14 | PFDEPEND.INCINSS |
| Incidência de Assistência Médica  (0-Não/1-Sim) | Inteiro | 1 | 15 | PFDEPEND.INCASSISTMEDICA |
| Incidência de Pensão  (0-Não/1-Sim) | Inteiro | 1 | 16 | PFDEPEND.INCPESAO |
| Incidências Definíveis  ("\*" nas posições das incidências confirmadas e ' ' (branco) nas posições das incidências não confirmadas. Ex: \*\_ \_ \* \_ \_ \_ o dependente incide na Incidência 1 e na Incidência 4) | String | 20 | 17 | PFDEPEND.INCDEFINIVEIS |
| **Grau de Parentesco do Dependente**  **1-Filho (a) válido  3-Filho (a) inválido  5-Cônjuge  6-Pai  7-Mãe  8-Sogra  9-Outros  A- AVÔ(ó)  C-Companheiro(a)  D-Enteado  E–Excluído  G-Ex-Cônjuge  I-Irmã (o) Válido  N-Irmã (o) Inválido  P-Ex-companheiro(a)  S-Ex-Sogro(a)  T-Neto(a)  X-Ex-Enteado(a) M-Menor Pobre B-Incapaz** | **String** | **1** | **18** | **PFDEPEND.GRAUPARENTESCO** |
| Dependentes possui cartão vacina?  (0-Não/1-Sim) | String | 1 | 19 | PFDEPEND.CARTAOVACINA |
| Percentual da Pensão | String | 9 | 20 | PFDEPEND.PERCENTUAL |
| Tipo da Pensão | String | 2 | 21 | PFDEPEND.TIPOPENSAO |
| Banco de pagamento pensão | String | 3 | 22 | PFDEPEND.BANCO |
| Agencia de pagamento da Pensão | String | 6 | 23 | PFDEPEND.AGENCIA |
| Conta de Pagamento Pensão | String | 15 | 24 | PFDEPEND.CONTACORRENTE |
| Nome responsável | String | 45 | 25 | PFDEPEND.RESPONSAVEL |
| Fórmula cálculo | String | 8 | 26 | PFDEPEND.FORCALCULO |
| Cálculo da Pensão é sobre o bruto  (0-Não/1-Sim) | String | 1 | 27 | PFDEPEND.BRUTO |
| Data de entrega da certidão de nascimento | Data | 8 | 28 | PFDEPEND.DATAENTREGACERTIDAO |
| Flag apresentou compr frequência escolar?  (0-Não/1-Sim) | String | 1 | 29 | PFDEPEND.FREQESCOLAR |
| Universitário/Escola técnica 2º grau  (0-Não/1-Sim) | String | 1 | 30 | PFDEPEND.UNIVERSITARIO |
| Incidência Salário Família  (0-Não/1-Sim) | String | 1 | 31 | PFDEPEND.INCSALFAM |
| Observação | String | 80 | 32 | PFDEPEND.OBSERVACAO |
| Fórmula Adicional Pensão | String | 8 | 33 | PFDEPEND.FORMPENSAO |
| **Data de início do desconto da pensão** | **Data** | **8** | 34 | **PFDEPEND.DATAINICIODESCPENSAO** |
| Coligada do fornecedor | Inteiro | 5 | 35 | PFDEPEND.CODCOLFORNEC |
| Código do fornecedor | String | 25 | 36 | PFDEPEND.CODFORNECEDOR |
| Operação Bancária | String | 5 | 37 | PFDEPEND.CODCOLFORNEC |
| Valor fixo | Real | 9 | 38 | PFDEPEND.VALORFIXO |
| Número do Cartão SUS | String | 100 | 39 | PFDEPEND.NUMEROCARTAOSUS |
| Número da Declaração de Nascido Vivo - Resolução Normativa Nº 295 | String | 20 | 40 | PFDEPEND.NUMDECLARANASCVIVO |
| Data Fim do Desconto de Pensão | Data | 8 | 41 | PFDEPEND.DATAFIMDESCPENSAO |
| Informa se o dependente do beneficiário é pessoa com Doença Incapacitante (eSocial Órgão Público) | Inteiro | 1 | 42 | DEPENDENTEBENEFICIARIOINCAPAZ |
| Descrição do parâmetro Outros da tela de dependente | String | 100 | 43 | PFDEPEND.DESCRICAODEPENDENCIA |
| Dependente possui Retenção FGTS | Inteiro | 1 | 44 | PFDEPEND.RETENCAOFGTS |
| Incidência de Assistência Odontológica  (0-Não/1-Sim) | Inteiro | 1 | 45 | PFDEPEND.INCASSISTODONTO |
