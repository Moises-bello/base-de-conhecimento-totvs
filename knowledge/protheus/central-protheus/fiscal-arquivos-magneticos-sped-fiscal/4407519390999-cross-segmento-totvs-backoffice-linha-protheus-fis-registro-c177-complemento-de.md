---
article_id: 4407519390999
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 0dfc9f06510f22717384d957332b99d4ea067ac8dff6ec343dc79f117a31c631
fetched_at: '2026-06-28T22:42:00.792795+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - REGISTRO C177:
  COMPLEMENTO DE ITEM - OUTRAS INFORMAÇÕES (código 01, 55) - (VÁLIDO A PARTIR DE 01/01/2019)'
type: support-article
updated_at: '2021-08-31T17:10:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407519390999-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-REGISTRO-C177-COMPLEMENTO-DE-ITEM-OUTRAS-INFORMA%C3%87%C3%95ES-c%C3%B3digo-01-55-V%C3%81LIDO-A-PARTIR-DE-01-01-2019
---

**Dúvida**

REGISTRO C177: COMPLEMENTO DE ITEM - OUTRAS INFORMAÇÕES (código 01, 55) -  
(VÁLIDO A PARTIR DE 01/01/2019)   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12  
  
**Solução**

Este registro deverá ser apresentado somente pelos contribuintes obrigados por legislação específica de cada UF, com o objetivo de agregar informações adicionais ao item, de acordo com tabela a ser publicada pela UF.

Publicada no site do SPED como tabela: 5.6 - Tabela de Informações Adicionais dos Itens do Documento Fiscal.

Para verificar a lista completa dos lançamentos e os Estados que já publicaram os códigos, acesse a seção de [Tabelas de Códigos](http://www1.receita.fazenda.gov.br/sistemas/sped-fiscal/tabelas-de-codigos.htm) no site do SPED. 

Os códigos referentes as Informações Adicionais dos Itens do Documento Fiscal são automaticamente importados para a tabela F2Y - Inf. Adic. de ítems del Doc., quando é rodada a rotina IMPSPED

Ao executar o compatiblizador  U\_IMPSPED como programa inicial, será necessário informar o diretório que contém os arquivos com código da Tabela 5.6, disponibilizada pelo estado  (no formato .\*txt) para que o sistema possa importá-los automaticamente.

Portanto previamente, baixe estes arquivos do site do SPED e copie-os para uma pasta no servidor. 

**Importante:**

**Para importação correta na tabela F2Y deve-se renomear o arquivo TXT baixado do site do SPED referente a tabela 5.6 para TABELA56.txt**

Após a importação desses códigos, acesse rotina de Cadastro de Tipos de Ent/Saida (MATA080), e informe no **campo Inf. item (F4\_INFITEM)** código  referente a tabela 5.6.

Ao Processar arquivo SPED FISCAL será apresentado registro **C177 - Complemento de Item – Outras informações (Cód. 01, 55)**

Os código poderão ser visualizados através da rotina FISA 157 (Inf. Adic. dos Itens do Doc)

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407519305879/mceclip0.png)**

Informações adicionais:

Cadastro de Informações Adicionais dos Itens do Documento Fiscal

<https://tdn.totvs.com/pages/releaseview.action?pageId=435109122>
