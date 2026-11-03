---
article_id: 360015964612
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 1e9ad97a81ab139b3d41efea5db46e07bf7e1692a04eb7c5a8a2abf0d67cc0e9
fetched_at: '2026-06-28T22:42:06.698548+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  e EFD Contribuições - Preenchimento da Conta Contábil
type: support-article
updated_at: '2023-03-14T19:13:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015964612-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-e-EFD-Contribui%C3%A7%C3%B5es-Preenchimento-da-Conta-Cont%C3%A1bil
---

**Dúvida**O arquivo magnético do Sped Fiscal e EFD Contribuições está com erro de validação devido ao não preenchimento da **Conta Contábil**.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Causa**O erro de **conta contábil** nos validadores do **Sped Fiscal** e **EFD Contribuições** ocorrem pela falta do preenchimento da **conta contábil** nas tabelas de onde o sistema busca a informação que será levada para o arquivo.  
  
**Solução**Nos bloco **A, C e D,** esse incidente ocorre pela falta de informação da **conta contábil** no campo **FT\_CONTA.**As informações deste campo têm origem da tabela do **Cadastro de Plano de Contas** (**CT1**). Este registro é gerado com a **Conta Contábil** informada na nota fiscal.  
  
Para o preenchimento automático dos campos **D1\_CONTA** e **C6\_CONTA** é necessário utilizar o campo **B1\_CONTA** no **Cadastro de Produtos** (**SB1**). Ao escriturar o documento fiscal, o número da **Conta Contábil** será gravada na tabela **SD2** (**D2\_CONTA**) para Nota fiscal de Saída e na tabela **SD1** (**D1\_CONTA**) para Documentos de Entrada. Na tabela de Item do Livro Fiscal (**SFT**) a **conta contábil** será gravada no campo **FT\_CONTA**.  
  
Se não houver o preenchimento do campo **B1\_CONTA**, então, a **conta contábil** deverá ser informada no momento da Inclusão do Pedido/Documento nos seguintes campos:  
  
- Pedido de Vendas (**C6\_CONTA**)  
- Documento de Entrada (**D1\_CONTA**)

**Importante**: O fonte de geração dos arquivos do **SPED FISCAL** e **EFD Contribuições** (**FISA008**) considera as informações gravadas no **Livro Fiscal** e dessa forma será considerada a **Conta Contábil** gravada no campo **FT\_CONTA.**   
  
**Especificamente para os registros do bloco F do arquivo magnético EFD Contribuições, verifique as informações abaixo:**

**Registro F100 e F560:**A **Conta Contábil** destes registros será gerada através do campo **ED\_CONTA** no **Cadastro de Natureza**. A informação deste campo será gravada no campo **CL2\_CTA** após a apuração do **PIS/COFINS**.  
Quando o registro **F100** for gerado pela rotina **Demais Documentos** (**FISA048**), o sistema irá buscar o conteúdo do campo **CF8\_CODCTA.**O conteúdo deste campo também será gravado no campo **CL2\_CTA.**A rotina **FISA008** buscará o conteúdo do campo **CL2\_CTA** para gerar esta informação da **conta contábil** no arquivo magnético.  
  
**Registro F120:**A **conta contábil** deste registro será gerada através do campo **N3\_CDEPREC** no **Cadastro de Ativo Fixo**. A informação deste campo será gravada no campo **CL2\_CTA** após a apuração do PIS/COFINS.   
A rotina **FISA008** buscará o conteúdo do campo **CL2\_CTA** para gerar esta informação da **conta contábil** no arquivo magnético.  
  
**Registro F130:**A **conta contábil** deste registro será gerada através do campo **N3\_CCONTAB**no **Cadastro de Ativo Fixo**. A informação deste campo será gravada no campo **CL2\_CTA** após a apuração do **PIS/COFINS**.   
A rotina **FISA008** buscará o conteúdo do campo **CL2\_CTA** para gerar esta informação da **conta contábil** no arquivo magnético.  
  
**Registro F150:**A informação da **conta contábil** deste registro será gerada a partir do campo**CF9\_CODCTA**.  
  
**Registro F500 e F510:**A **Conta Contábil** destes registros será gerada através do campo **ED\_CONTA** no **Cadastro de Natureza**. A informação deste campo será gravada no campo **CL1\_CODCTA** após a apuração do **PIS/COFINS**.   
A rotina **FISA008** buscará o conteúdo do campo **CL1\_CODCTA** para gerar esta informação da **conta contábil** no arquivo magnético.  
  
**Registro F525:**A **Conta Contábil** deste registro será gerada através do campo **ED\_CONTA** no **Cadastro de Natureza**. A informação deste campo será gravada no campo **CL7\_CODCTA** após a apuração do **PIS/COFINS**.  
A rotina **FISA008** buscará o conteúdo do campo **CL7\_CODCTA** para gerar esta informação da **conta contábil** no arquivo magnético.

A informação da **Conta Contábil** deste registro será gerado através do campo **FT\_CONTA**, quando o título for oriundo de lançamentos realizados na tabela **SFT** e **SF3**.  
  
**Registro F550:**A **Conta Contábil** deste registro será gerada através do campo **ED\_CONTA** no **Cadastro de Natureza**, quando o título for ser gerado diretamente no módulo **Financeiro**.

A **Conta Contábil** deste registro será gerada através do campo **FT\_CONTA**, quando o título for oriundo de lançamentos realizados na tabela **SFT** e **SF3**.  
  
**Especificamente para os registros do bloco M do arquivo magnético EFD Contribuições, verifique as informações abaixo:**  
  
**Registros M115 e M515, M225 e M625:**Os ajustes oriundos de documentos fiscais irão gravar a **conta contábil** na tabela **CL4**. Estes ajustes são com base em documentos fiscais, logo o conteúdo do campo **FT\_CONTA** irá alimentar o campo **CL4\_CODCTA**.  
A rotina **FISA008** buscará o conteúdo do campo**CL4\_CODCTA**para gerar a informação nos registros **M115, M515, M225 e M625**.  
  
**M400 e M410, M800 e M810:**A **Conta Contábil** destes registros será gerada com base nas informações dos blocos **A, C, D e F**. Os documentos lançados com**CSTs 04, 05, 06, 07, 08 e 09** serão gravados na tabela **CKT** (**Receita PIS/COF Nao Tributada**). O sistema irá gravar a informação da **conta contábil** no campo **CKT\_CONTA**.  
A rotina **FISA008** buscará o conteúdo do campo**CKT\_CONTA**para gerar a informação nos registros **M400, M410, M800 e M810.****Registro P100:**Para o preenchimento da conta contábil no registro P100, o sistema irá verificar as notas fiscais de saída com configuração para o CPRB e buscará a informação do campo FT\_CONTA (mesma regra de preenchimento dos registros dos Blocos A, C e D). A informação do campo**FT\_CONTA** irá ser levada para o campo**CKX\_CONTA** no momento da apuração da EFD Contribuições.

A rotina FISA008 irá pegar o conteúdo do campo **CKX\_CONTA** para gerar a informação no registro P100.

**Atenção:**Para os casos de operações que possuem rateio (duas ou mais **contas contábeis**) ou quando algum dos campos acima não possam ser preenchidos, será necessário utilizar o **ponto de entrada** **SPDPIS07** para gravação correta da **conta contábil** nos registros acima e no registro **0500:**

Para mais informações sobre o ponto de entrada **SPDPIS07** acesse:

<https://tdn.totvs.com/pages/releaseview.action?pageId=656057151>
