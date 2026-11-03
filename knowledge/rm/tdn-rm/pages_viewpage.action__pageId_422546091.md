---
content_hash: bc8baa9554dcfab8da11bc836551a059ed8e74bf34deef4e0f65a051c104bbc6
fetched_at: '2026-06-29T00:09:23.294738+00:00'
page_id: '422546091'
product: rm
source: tdn-rm
title: CAT 115/2003 (Regras Gerais)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546091
version: 7
---

Rotina Estadual com periodicidade mensal gerada apenas para Lançamentos Fiscais de Saída cujo o CFOP's selecionados sejam iniciados por 5,6, e 7, que possuam o Código Modelo de Documento igual à 06-Nota Fiscal de Energia Elétrica, 21-Nota Fiscal de Comunicação e 22-Nota Fiscal de Telecomunicação.   
***Observação*:** Não será tratado pelo ERP o código de documento fiscal Nota Fiscal/Conta de Gás, modelo 1 disponibilizado no layout da rotina, serão considerados apenas os códigos citados acima.  
Disponibilizado no [TOTVS Gestão Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=198948859) a geração da Portaria CAT79/2003 através do menu [Obrigações Acessórias | Estaduais | Convênio ICMS 115/2003](http://tdn.totvs.com/pages/viewpage.action?pageId=422546091), onde devem ser selecionados os seguintes parâmetros:

* Filial
* Período Rotina
* Situação: Normal ou Substituto
* Calcula Código de Autenticação do Documento Fiscal.

***Observação*:** A opção **"Calcula Código de Autenticação do Documento Fiscal"** deve ser habilitada no momento da geração do arquivo apenas quando houver lançamentos gravados na base anteriormente à implementação da rotina. Lembrando que neste caso em específico, o campo **Código Autenticação Digital Documento Fiscal** do Lançamento Fiscal não será preenchido, será gerado apenas no arquivo no campo reservado ao Fisco.  
A rotina e composta de três arquivos no padrão txt:

* 'M' - MESTRE DE DOCUMENTO FISCAL;
* 'I' - ITEM DE DOCUMENTO FISCAL;
* 'D' - DADOS CADASTRAIS DO DESTINATÁRIO DO DOCUMENTO FISCAL.

**Geração dos Registros**

* Será gerado um grupo de arquivos para cada combinação do Código Modelo de Documento e série do Lançamento Fiscal. Os arquivos serão divididos quando ultrapassarem 100 (cem) mil documentos para contribuintes com volume mensal de emissão até 1(hum) milhão de documentos e 1(hum) milhão de documentos para os contribuintes com volume mensal de emissão superior à 1(hum) milhão de documentos;
* Não será gerado pelo [TOTVS Gestão Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=198948859) o registro de IDENTIFICAÇÃO E CONTROLE (Tipo C);
* Os arquivos são gerados na pasta "C:\Temp";
* O nome do arquivo será montado seguindo a seguinte regra:

  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- |
  | **Nome do Arquivo** | | | | | | **Extensão** |
  | 2 dígitos | 3 dígitos | 2 dígitos | 2 dígitos | 1 dígitos | 1 dígitos | 3 dígitos |
  | **UF** | **Série** | **Ano** | **Mês** | **Status** | **Tipo** | **Volume** |

  **UF** – Sigla da Unidade da Federação do emitente  
  **Série** – Série dos documentos fiscais.  
  **Ano** – Ano do período de apuração dos documentos.  
  **Mês** – Mês do período de apuração dos documentos.  
  **Status** – Indica se é "N - Normal" ou "S - Substituto".  
  **Tipo** – Pode assumir os valores:
* 'M' - MESTRE DE DOCUMENTO FISCAL;
* 'I' - ITEM DE DOCUMENTO FISCAL;
* 'D' - DADOS CADASTRAIS DO DESTINATÁRIO DO DOCUMENTO FISCAL.
