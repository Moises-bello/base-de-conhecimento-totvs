---
content_hash: 63be5351fd45c0272a479d6218e3500bf4d4bbe56ec3fe5d246f2e64ed8988c1
fetched_at: '2026-06-29T00:08:25.812379+00:00'
page_id: '271157136'
product: rm
source: tdn-rm
title: RPT00003.2.1 - PDF (Compatibilidade e Versões)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271157136
version: 22
---

# Índice:

---

.\*ndice:

# 1 - PDF/A

---

O **PDF/A** é um **formato de ficheiro** para arquivamento de longo prazo de documentos eletrônicos. Baseia-se na versão 1.4 do **PDF** de referência da **Adobe Systems Inc**. (implementado no **Adobe Acrobat[5](https://pt.wikipedia.org/wiki/Adobe_Acrobat "Adobe Acrobat")** e versões posteriores) e é definido pela **norma ISO 19005-1:2005**.

O **PDF/A** é, na verdade, um subconjunto de **PDF** obtido excluindo as características supérfluas para arquivamento de longo prazo, de forma semelhante à definição do subconjunto **PDF/X** para **impressão** e **artes gráficas**. Além disso, a norma impõe uma série de requisitos aos programas para a visualização de ficheiros **PDF/A**. Um programa de visualização que atenda aos requisitos deve seguir certas regras, incluindo a conformidade com as normas para o gerenciamento de cores, o uso de **fontes** incorporadas para visualização, ou a possibilidade de fazer anotações pelo utilizador.

# 1.1 - Padrões

---

| Nº | Abrev. | Descrição | Publicado | Padrão | Baseado em |
| --- | --- | --- | --- | --- | --- |
| **1** | PDF/A-1 | Parte 1 : Uso do PDF 1.4 |  | ISO 19005-1 | PDF 1.4 (Adobe Systems, *PDF Reference*, terceira edição) |
| **2** | PDF/A-2 | Parte 2 : Uso do ISO 32001-1 |  | ISO 19005-2 | PDF 1.7 (ISO 32000-1:2008) |
| **3** | PDF/A-3 | Parte 3 : Uso do ISO 32001-1 com suporte a arquivos embutidos |  | ISO 19005-3 | PDF 1.7 (ISO 32000-1:2008) |

# 1.2 - Descrição:

---

Este padrão não define uma estratégia para o armazenamento nem pretende alcançar as metas de um sistema de armazenamento. O que identifica um **"perfil"** de documentos eletrônicos que assegure que poderão ser reproduzidos com precisão no futuro. Um elemento fundamental para alcançar este objetivo é a exigência de que documentos **PDF/A** devam ser **100% autocontidos**. Todas as informações necessárias para mostrar o documento de forma consistente devem estar presentes no ficheiro. Isso inclui, entre outras coisas, o conteúdo propriamente dito (texto, imagens e gráficos vetoriais), as fontes utilizadas e as informações de cor. Não é permitido que um documento **PDF/A** dependa de fontes externas (por exemplo, **programas de tipografia** e **hiperlinks**).

Outros elementos-chave de compatibilidade **PDF/A** incluem:

* Não é permitido utilizar áudio e vídeo.
* Não é permitido utilizar **JavaScript** ou executar arquivos.
* Todas as fontes devem estar integradas e não devem ter quaisquer restrições que possam causar problemas legais no futuro. Isto também se aplica a fontes **PostScript** padrão, como **Times** ou **Helvetica**. Espaços de cor especificados independentemente do dispositivo.
* Não é permitido o uso de **criptografia**.
* É obrigatório o uso de **metadados** baseados em padrões.

****Nível de Conformidade e Versões:****

falseIPDF/A-1

A **Parte 1** desse padrão foi publicada em 1 de Outubro de 2005 e especifica dois níveis de conformidade para arquivos **PDF**:

* **PDF/A-1b** – Conformidade **Nível B**
* **PDF/A-1a** – Conformidade **Nível A**

A conformidade de **Nível B** requere apenas que o padrão utilize o necessário para reproduzir fielmente a aparência visual do documento enquanto a conformidade **Nível A** inclui todos os requisitos do **Nível****B** mais outros recursos que melhorem a acessibilidade do documento assim como:

* Especificação de Linguagem
* Estrutura Hierárquica
* Textos de marcação e textos descritivos para imagens e símbolos
* Mapeamento dos caracteres para **Unicode**

A conformidade de **Nível A** foi desenvolvido para melhorar a acessibilidade de arquivos para usuários com algum tipo de debilidade, permitindo que programas que contam com acessibilidade, como leitores de tela, possam ser mais precisos ao extrair e interpretar os conteúdos dos arquivos.

PDF/A-2

A**Parte 2** desse padrão publicada em 1 de julho de 2011 traz alguns recursos novos com as versões **1.5**, **1.6** e **1.7** da documentação do **PDF**(PDF Reference). Os Arquivos **PDF/A-1** não estão necessariamente em conformidade com o padrão **PDF/A-2**, e ps arquivos **PDF/A-2**estão necessariamente em conformidade com arquivos **PDF/A-1**.

A **Parte 2** do padrão **PDF/A**é baseado tanto no padrão **PDF 1.7 (ISO 32000-1)**, quanto no padrão **PDF** **1.4** e oferece um numero de novos recursos:

* Compressão de imagem **JPEG 2000**
* Suporte a efeitos de transparência e painéis
* Suporte a fontes **OpenType**
* Permite assinaturas digitais em acordo com o padrão **PAdES (PDF Advanced Electronic Signatures)**
* Opção de embutir arquivos **PDF/A**para facilitar o arquivamento de vários documentos em um único arquivo.

A Parte 2 define três níveis de conformidade . **PDF/A-2a**, **PDF/A-2b,**correspondentes aos níveis de conformidade a e b no **PDF/A-1**. Um novo nível de conformidade, **PDF/A-2u**, representa a conformidade **Nível B** **(PDF/A-2b)**com requisitos adicionais onde todo texto no documento tenha o mapeamento **Unicode**.

PDF/A-3

A Parte 3 desse padrão foi publicado em 15 de Outubro de 2012 e difere-se do padrão **PDF/A-2** em um único ponto – Permite embutir arquivos de formatos variados (como **XML**, **CSV**, **CAD**, documentos de processamento de texto (**DOC, por exemplo**), documentos com dados em tabelas (**XLS, por exemplo**), e outros) dentro de documentos no padrão **PDF/A**.

# 2 - Limitações (Devexpress)

---

Utilizamos no **RM** um conjunto de componentes de uma empresa terceira chamada **"Devexpress"**, onde o **RM** Reports tem como base o **Xtrareports**, pertencente a esse conjunto de componentes.

A funcionalidade de **Exportar para** **PDF/A** não é suportado pela versão atual **(14.1)** das bibliotecas disponibilizadas pela **Devexpress**.

Tanto a versão **10.1** dos componentes **Devexpress** utilizada na versão **11.8x** do **RM**, quanto a versão **14.1** dos componentes da **Devexpress** utilizada na versão **12.1.x** do **RM**, essa funcionalidade não é suportada.

Existem diversas respostas do suporte da **Devexpress**, em vários intervalos de tempo diferentes, porém colocamos a resposta mais recente que contempla a versão **14.1** da **Devexpress**, apresentada abaixo, traduzida.

**TÓPICO PRINCIPAL : [PDF Report Export conforms to PDF/A ? (Exportação PDF de acordo com o padrão PDF/A ?)](https://www.devexpress.com/Support/Center/Question/Details/Q319735)**

falseTradução

**[...]**

Atualmente, o Relatório (XtraReports) não suporta essa funcionalidade. Entretanto, nós temos uma sugestão similar registrada em nosso banco de dados: [Export to PDF - Support PDF/A (PDF - Archive format)](https://www.devexpress.com/Support/Center/p/S130819.aspx). Por favor, acompanhe-o para estar informado do nosso progresso.

**[...]**

**[...]**  
Atualmente, nós não temos planos de implementar esse recurso no Relatório (XtraReports) na versão 2011 v1. Provavelmente, nós iremos implementar essa sugestão em uma versão futura do Relatório (XtraReports). Por favor, aceite nossas sinceras desculpas pela inconveniência.  
**[...]**

**SUBTÓPICO 1 : [Export to PDF - Support PDF/A (PDF - Archive format) (Exportação para PDF - Suporte PDF/A (Arquivo de Formato PDF))](https://www.devexpress.com/Support/Center/Question/Details/S130819)**

falseTradução

**Implementado:**

* **v2014 vol 1.3**

**Informações Adicionais:**

No Preview de Impressão do Relatório, a opção '**PDF/A-2b**' estará disponibilizada na tela de **Opções de Exportação PDF**.

**SUBTÓPICO 2 : [Export to PDF - Support PDF/A (PDF - Archive format) (Exportação para PDF - Suporte PDF/A (Arquivo de Formato PDF))](https://www.devexpress.com/Support/Center/Question/Details/S130819)**

falseTradução

**[...]**

**Implementado:**

* **v2014 vol 2.6**

**Informações Adicionais:**

Nós adicionamos suporte ao padrão **PDF/A-3b** na exportação na presente versão.  
As novas propriedades adicionados fazem parte da classe **PdfExportOptions**.  
   
**PdfExportOptions.AdditionalMetadata** - Especifica dados adicionais à ser adicionados ao metadados do PDF se a propriedade **PdfExportOptions.PdfACompatible** for verdadeira.  
**PdfExportOptions.Attachments** -Lista de documentos embutidos (anexados). 

**[...]**

**Propriedade PdfACompatible:**

| Nº | Nome | Descrição | Versão Devexpress | Versão RM |
| --- | --- | --- | --- | --- |
| **1** | Pdf | O documento suporta o padrão ISO 32000-1:2008. | 10.1 (superiores) | 11.80, 12.1.x |
| **2** | PdfA1b | O documento suporta o padrão ISO 19005-1:2005. | 14.1 (v 1.3) | 12.1.x |
| **3** | PdfA2b | O documento suporta o padrão ISO 19005-2:2011. | 14.1 (v 1.3) | 12.1.x |
| **4** | PdfA3b | O documento suporta o padrão ISO 19005-3:2012. | 14.1 (v 2.6) | Não suportado |

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** PDF (Compatibilidade e Versões)

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
