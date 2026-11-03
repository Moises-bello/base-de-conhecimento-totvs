---
content_hash: 4571457e934449e1baae511b93472934932119efa275c7be186d42390c5e6f83
fetched_at: '2026-06-29T00:10:51.595088+00:00'
page_id: '568950616'
product: rm
source: tdn-rm
title: Layout Para Importação de Alteração de CPF para eSocial (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568950616
version: 3
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"   
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
-  Números (00) em campos do tipo **Inteiro**;  
-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;

-  (ddmmyyyy) em campos do tipo **Data**;

-  (GRR20071514) em campos do tipo **String**;

-  Começam /@ e terminam com @/ em campos do tipo **MEMO**.

Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Chapa** | **String** | **16** | **1** | **PFESOCIALCPF.CHAPA** |
| **Data fim de validade** | **Data** | **8** | **2** | **PFESOCIALCPF.DTFIMVALIDADE** |
| **CPF anterior** | **String** | **11** | **3** | **PFESOCIALCPF.CPFANTERIOR** |
| **Matrícula anterior do trabalhador no eSocial** | **String** | **30** | **4** | **PFESOCIALCPF.MATRICULAESOCIALANTERIOR** |
| Observação | String | 255 | **5** | PFESOCIALCPF.OBSERVACAO |

**Observação:**Para o campo matrícula eSocial o campo será obrigatório caso funcionário possua matrícula eSocial em seu cadastro
