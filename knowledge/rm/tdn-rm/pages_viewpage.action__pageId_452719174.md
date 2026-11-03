---
content_hash: 1ad92f5dad766f70d014a1b3cc48796d3b8b3d542635754218f0e203817b37cf
fetched_at: '2026-06-29T00:10:03.920865+00:00'
page_id: '452719174'
product: rm
source: tdn-rm
title: Layout Para Importação de Campos Complementares dos Dependentes (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719174
version: 2
---

**Importante:**  
 Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
 **Campos obrigatórios estão destacados em negrito.**  
 DELIMITADOR DE CAMPOS: ";"  
 Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
 Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
 As tabelas abaixo são premissas para a importação de Campos Complementares dos Dependentes, caso as mesmas estejam vinculadas a base de dados origem.  
 - PFUNC  
 - PFDEPEND  
    
  **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
 -  F (false) ou T (true) em campos do tipo **Lógico**;  
 -  Números (00) em campos do tipo**Inteiro**;  
 -  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
 - (ddmmyyyy) em campos do tipo **Data**;  
 - (GRR20071514) em campos do tipo **String**;  
 - Começam /@ e terminam com @/ em campos do tipo **MEMO**.

Layout deverá ser criado conforme os campos existentes na tabela PFDEPENDCOMPL; apenas os campos RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY e RECMODIFIEDON não devem ser colocados no layout, todos os outros deverão constar no arquivo de importação, os campos CHAPA e NRODEPEND são fixos na posição 1 e 2 respectivamente. A partir daí, os demais campos devem ser inseridos no layout de acordo com a ordem dos mesmos na tabela PFDEPENDCOMPL.  
 Apenas os campos RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY e RECMODIFIEDON não deve ser colocado no layout, todos os outros deverão constar no arquivo de importação.  
    
 **Exemplo:** Na base foram criados dois campos complementares para dependentes, chamados SANGUE e AUXILIOCRECHE, estaremos importando para o dependente 2 da chapa 00125. Layout ficaria da seguinte forma:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **Posição** | **CAMPO** |
| **Chapa (00125)** | **String** | **16** | **1** | **PFDEPENDCOMPL.CHAPA** |
| **Número do dependente (2)** | **Inteiro** | **2** | **2** | **PFDEPENDCOMPL.NRODEPEND** |
| **Nome do campo (PFDEPENDCOMPL.SANGUE)** | **Varia de acordo com a criação do campo** | **Varia de acordo com a criação do campo** | **3** | **PFDEPENDCOMPL.SANGUE** |
| **Nome do campo (PFDEPENDCOMPL.AUXILIOCRECHE)** | **Varia de acordo com a criação do campo** | **Varia de acordo com a criação do campo** | **4** | **PFDEPENDCOMPL.AUXILIOCRECHE** |

**Observação:** O layout irá variar, podendo ter mais campos sendo eles separados por ponto e vírgula (. Por exemplo, se a base tiver 15 campos complementares dos dependentes, no layout deverá colocar CHAPA, NRODEPEND e os 15 campos complementares separados por ponto e vírgula (, com a sequência dos campos de acordo com a sequência da tabela PFDEPENDCOMPL.  
    
 O arquivo para importação ficou da seguinte forma, apresentando os valores preenchidos em cada campo complementar:  
 00125;2;O+;SIM;
