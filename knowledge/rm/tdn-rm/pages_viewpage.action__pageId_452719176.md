---
content_hash: a3f6c822bd7cd473109a40a8105e019d135383df3ac8416e6a4306041fedaca1
fetched_at: '2026-06-29T00:10:03.939930+00:00'
page_id: '452719176'
product: rm
source: tdn-rm
title: Layout Para Importação de Campos Complementares para Funcionário (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719176
version: 3
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação de Campos Complementares para Funcionário  
- PFUNC  
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
-  Números (00) em campos do tipo**Inteiro**;  
-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
- (ddmmyyyy) em campos do tipo **Data**;  
- (GRR20071514) em campos do tipo **String**;  
- Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
Layout deverá ser criado conforme os campos existentes na tabela PFCOMPL; apenas os campos RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY e RECMODIFIEDON não devem ser colocados no layout, todos os outros deverão constar no arquivo de importação, o campo CHAPA é fixo na posição 1. A partir daí, os demais campos devem ser inseridos no layout de acordo com a ordem dos mesmos na tabela PFCOMPL.  
   
**Exemplo:** Na base foram criados dois campos complementares, chamados SANGUE e POSSUICESTABASICA, estaremos importando para a chapa 00125. Layout ficaria da seguinte forma:  
 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa (00125)** | **String** | **16** | **1** | **PFCOMPL.CHAPA** |
| **Sangue (O+)** | **Varia de acordo com a criação do campo** | **Varia de acordo com a criação do campo** | **2** | **PFCOMPL.SANGUE** |
| **Possui cesta básica (SIM)** | **Varia de acordo com a criação do campo** | **Varia de acordo com a criação do campo** | **3** | **PFCOMPL.POSSUICESTABASICA** |

   
**Observação:** O layout irá variar, podendo ter mais campos sendo eles separados por ponto e vírgula (. Por exemplo, se a base tivesse 15 campos complementares para funcionários, no layout deveria colocar CHAPA e os 15 campos complementares separados por ponto e vírgula (, com a sequência dos campos de acordo com a sequência da tabela PFCOMPL.  
O arquivo para importação ficou da seguinte forma, apresentando os valores preenchidos em cada campo complementar:  
00125;O+;SIM;  
**Modelo 1 do Layout**  
00125;O+;SIM;  
**Modelo 2 do Layout**  
CHAPA;SANGUE;POSSUICESTABASICA  
02877;1234;5678  
   
No modelo 2 do layout o usuário não precisa colocar todos os campos, ele pode simplificar, inserindo apenas os campos que deseja importar em maiúsculo, não esquecendo que o **campo chapa é obrigatório,**para qualquer layout criado.
