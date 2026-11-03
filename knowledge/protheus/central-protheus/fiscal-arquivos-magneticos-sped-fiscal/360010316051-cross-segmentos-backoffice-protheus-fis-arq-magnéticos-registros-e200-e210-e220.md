---
article_id: 360010316051
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 3f693f83c1bdac0c83e3c641a477718918a3188401601bae7afe642a037872ab
fetched_at: '2026-06-28T22:42:01.003705+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - REGISTROS E200,
  E210, E220 e E250
type: support-article
updated_at: '2025-02-11T20:55:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010316051-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-REGISTROS-E200-E210-E220-e-E250
---

#### **Dúvida**

#### Procedimentos para gerar os registros E200, E210, E220 e E250

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80

**Solução**

Parâmetro

MV\_ESTADO = SP   -> Deve ser o estado que está sendo gerado apuração

MV\_USASPED = T

MV\_P9SPED = T

MV\_P9AUTO = T

MV\_STUF=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO

MV\_STUFS=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO

**MV\_SUBTRIB** = preenchido com estado + inscrição estadual (todos os estados que possuírem inscrição estadual para recolhimento do ICMS ST)

Exemplo

MV\_SUBTRIB = Preenchido com UF + Inscrição Estadual

Exemplo: MV\_SUBTRIB=SP1234567/MG1234567

MV\_STNIEUF = Preencher com as unidades onde não é necessário ter inscrição estadual para recolhimento do ST. Preencher com UF concatenadas Exemplo: **MGPR/SPRJ** (de Minas Gerais para Paraná, de São Paulo para Rio de Janeiro).

**MV\_CFE210 =****Deve ser informado todas as CFOP´s referente a devolução**

**Exemplo: MV\_CFE210 =** **1410, 1411, 1414, 1415, 1660, 1661, 1662, 2410, 2411, 2414, 2415, 2660, 2661 e 2662**.

**SITUAÇÃO 1 – Geração E200, E210 e E250**

Empresa inscrita no estado substituto parâmetro MV\_SUBTRIB preenchido.

1- Parâmetro

 MV\_SUBTRIB = Preenchido com a inscrição estadual do estado Exemplo: MV\_SUBTRIB=SP1234567/MG1234567

2- TES

Crd. ICMS ST (F4\_CREDST) = 2- Retido ST

3 Gerar a apuração do ICMS com perguntas da Wizad

 Livro Selecionado= \*

Apuração = Mensal

Período = 1º

Gera guia de recolhimento = sim

Imprime créditos de ST = Não

Exclui GNR = Sim

4 - Gere a guia de recolhimento e verifique se foram salvas informações na tabela CDH nos campos CDH\_GNRE, CDH\_ESTGNR e CDH\_VALOR.

 Verifique se as informações da guia encontram-se na tabela SF6.

5 – Gerar arquivo SPEDFICAL geração dos registros E200, E210 e E250.

**SITUAÇÃO 02 - Geração E200, E210 e E250**

 Empresa não inscrita o estado substituto:

1- Parâmetro

MV\_STNIEUF = Preencher com as unidades onde não é necessário ter inscrição estadual para recolhimento do ST. Preencher com UF concatenadas Exemplo: **MGPR/SPRJ** (de Minas Gerais para Paraná, de São Paulo para Rio de Janeiro).

2- TES

Crd. ICMS ST (F4\_CREDST) = 2- Retido ST

3 Gerar a apuração do ICMS com perguntas da Wizad

 Livro Selecionado= \*

Apuração = Mensal

Período = 1º

Gera guia de recolhimento = sim

Imprime créditos de ST = Não

Exclui GNR = Sim

4 - Gere a guia de recolhimento e verifique se foram salvas informações na tabela CDH nos campos CDH\_GNRE, CDH\_ESTGNR e CDH\_VALOR.

 Verifique se as informações da guia encontram-se na tabela SF6.

5 – Gerar arquivo SPEDFICAL geração dos registros E200, E210 e E250.

**SITUAÇÃO 03  - Geração E200, E210 e E250**

Empresa não inscrita no estado substituto onde valor de ICMS ST não deve ser apresentado na apuração ICMS mais deve ser gerado os registros E210 e E250 na apuração.

1-Parâmetro

MV\_STNIEUF = Preencher com as unidades onde não é necessário ter inscrição estadual para recolhimento do ST. Preencher com UF concatenadas Exemplo: **MGPR/SPRJ****(de Minas Gerais para Paraná, de São Paulo para Rio de Janeiro).**

2- TES

Crd. ICMS ST (F4\_CREDST) = 3- Debita

Agrega. Solid. (F4\_INCSOL) = Não

LF ICMS ST (F4\_LFICMST) = Não

Mkp ICM. Comp (F4\_MKPCMP) = Não

3 – Ao faturar nota fiscal de saída será apresentado guia de ICMS ST antecipada e não deverá ser apresentado o valor de ICMS ST na apuração de ICMS.

Verifique se as informações da guia encontram-se na tabela SF6.

4- Gerar a apuração do ICMS com perguntas da Wizad

 Livro Selecionado= \*

Apuração = Mensal

Período = 1º

Gera guia de recolhimento = sim

Imprime créditos de ST = Não

Exclui GNR = Sim

Importante

Não será gravado valor de ICMS ST na apuração de ICMS referente a guia recolhida no momento do faturamento do documento fiscal.

5 – Gerar arquivo SPEDFICAL geração dos registros E200, E210 e E250.

**Atenção:**

Valores de credito de ICMS ST referente a notas fiscais de entrada não será levada ao arquivo SPEDFISCAL.

Conforme consta do próprio **Guia Prático do SPED FISCAL**, em regra, não há direito ao crédito do ICMS/ST. Caso haja direito à apropriação do crédito, o valor do ICMS/ST destacado na nota fiscal deve ser lançado na apuração do ICMS-ST, observando-se o tratamento legal. Existindo legislação estadual que preveja que o valor deve ser informado como ajuste, identifique o código específico da Tabela 5.3 (ajuste de documento), do Ato COTEPE/ICMS 09/08. Se o código de ajuste não existe, utilize um código de ajuste de apuração, conforme tabela 5.1.1, do Ato COTEPE/ICMS 09/08.

Caso tenha que levar os valores referente ao credito de ICMS ST de períodos anteriores na apuração de ICMS deve ser configurado.

Parâmetro

MV\_APURANT = T

Wizard da apuração ICMS rotina MATA953

 Arq. Período Ante. ? = Fica com conteúdo branco.

Desse forma será lido pela apuração os valores de períodos anteriores da pastas sistema referente os arquivos .IC0  referente ICMS e .ST0 Referente ao ICMS ST.

#### **REGISTRO E220: AJUSTE/BENEFÍCIO/INCENTIVO DA APURAÇÃO DO ICMS SUBSTITUIÇÃO TRIBUTÁRIA.**

Estes ajustes são os códigos de subitens lançados manualmente na **Apuração de ICMS - ST**, transportados para o meio magnético.  
**Importante**  
Os ajustes feitos na **Apuração de ICMS-ST** são buscados na **tabela de apuração (CDH)**. Eles devem ser previamente configurados no **arquivo de ajustes (CD0)**

Para mais informações sobre o Sped Fiscal, acessar:

<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
