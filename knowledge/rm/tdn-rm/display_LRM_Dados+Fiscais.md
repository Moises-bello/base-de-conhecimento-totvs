---
content_hash: 5a3ad4f0710b171f22af56b647d33fe8dca42c1be32c0185411b8687e9ef96d6
fetched_at: '2026-06-29T00:09:20.633929+00:00'
page_id: '422545725'
product: rm
source: tdn-rm
title: Dados Fiscais
type: documentation
url: https://tdn.totvs.com/display/LRM/Dados+Fiscais
version: 42
---

**Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

falsePara esta opção serão cadastradas as informações Fiscais da Filial.

350px

1Tipo de Estabelecimento

**Optante Regime Simplificado**

Simples consiste no pagamento unificado de tributos e contribuições administrados pela Receita Federal e de contribuições previdenciários (IRPJ / IPI / CSL / PIS-PASEP / COFINS / CONTRIBUIÇÕES PARA SEGURIDADE SOCIAL, a cargo da pessoa jurídica, de que tratam o [art. 22 da](http://www.planalto.gov.br/ccivil_03/LEIS/L8212cons.htm) [Lei nº 8.212 de 24 de julho de 1991](http://www.planalto.gov.br/ccivil_03/LEIS/L8212cons.htm) e a [Lei Complementar nº 84, de 18 de janeiro de 1996](http://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp84.htm).)

O campo Sublimite excedido deverá ser marcado quando a Filial optante pelo regime simplificado exceder o limite de faturamento para enquadramento. Com este parâmetro habilitado, a tag <CRT> das Notas Fiscais Eletrônicas emitidas a partir da marcação terão o valor 2 - Simples Nacional, excesso sublimite de receita bruta  no lugar do valor 1 - Simples Nacional.

**Órgão Público**

Em **Anexos | Dados Fiscais |**Aba **Tipo Estabelecimento** é possível informar se a filial é um Órgão Público Federal, Estadual ou Municipal.

Imagem

Esta informação se refere a geração do evento [R-1000 da EFD-Reinf](https://tdn.totvs.com/display/LRM/Eventos+Cadastrais).

**Forma de Tributação da Contribuição Previdenciária**

No cadastro de Filiais, Aba Dados Adicionais, selecionar o Ramo de Atividade **"Produtor Rural"** e salvar.

Em **Anexos | Dados Fiscais |** Aba **Tipo Estabelecimento** a flag *Forma de Tributação da Contribuição Previdenciária será habilitada* .

Imagem

Esta informação se refere a geração do evento [R-2055 da EFD-Reinf](https://tdn.totvs.com/pages/viewpage.action?pageId=506387467).

**Optante pelo Regime Regular do IBS/CBS**

 Em **Anexos | Dados Fiscais |**Aba **Tipo Estabelecimento** é possível informar se a filial é ou não optante pelo **regime regular** dos tributos IBS e CBS.

   A flag é exibida **exclusivamente** quando a filial estiver configurada como **Matriz**.

ImagemContador

**CRC Contabilista**

O Campo "CRC do Contabilista" gerado nas Rotinas Legais é formado pelos campos: Tipo Inscrição CRC, UF CRC, CRC e Digito CRC, exemplo:

1
complete
UF CRC = PR CRC

2
complete
Contador = 343434

3
complete
Tipo Inscrição CRC = Originário Digito

4
complete
CRC Contador = 2 O campo "CRC do Contabilista" será gravado da seguinte forma no arquivo: PR343434O2
RepresentanteTributos

**Utiliza Crédito Outorgado:**Informe se a Filial fará a opção de trabalhar sob o Regime de Crédito Outorgado de ICMS, conforme determina Artigo 11, Anexo III, Decreto 45.490/2000 do RICMS de São Paulo, válido para os estabelecimentos Prestadores de Serviço de Transporte.

**Apuração de ISS**

O campo Apuração de ISS é utilizado nas seguintes Rotinas Legais:

1. DES BH - O Campo Natureza de Operação receberá o Regime ISS Empresa selecionado. Se o Regime ISS Empresa estiver marcado Construção Civil, por exemplo, a natureza de Operação receberá o valor "G".
2. DMS Salvador - O campo ISS Retido na Fonte ou ISS Retido na Fonte Deduzido no Registro Documentos Fiscais Emitidos também receberá o Regime ISS Empresa selecionado. Se o Regime ISS Empresa estiver marcado Imune, por exemplo, o campo receberá "I".
3. DS Recife - O campo Tipo de Recolhimento Notas Fiscais Emitidas receberá o Regime ISS selecionado. Se o Regime ISS Empresa estiver marcado Sociedade Profissional, por exemplo, receberá o valor "S". Caso a Empresa

Tomadora retenha ISS na Entrada o campo "Responsável Retenção ISS" deverá ser habilitado. Se o campo estiver habilitado recebe o valor "1" se estiver desabilitado recebe o valor "0". Esse valor poderá ser utilizado para realizar consistências em Fórmulas de Base de Cálculo do ISS no TOTVS Gestão de Estoque, Compras e Faturamento | Cadastros | Fórmulas. O usuário, por exemplo, poderá criar fórmulas utilizando esse campo para determinar como será a retenção do imposto. O nome da tabela para este campo é DFILIAL.RETENCAOISS.   
***Observação*:**O campo Porte será utilizado no Registro 85 da SISIF-CE e no Registro 88SP03 SAPI-MG. O campo Inscrição no Suframa é utilizado na rotina Ato Cotepe.

**Tipo Apuração -  CPRB (Regime de Caixa):**Este campo será utilizado para identificar que o método de apuração da CPRB, Regime de Competência (DESMARCADO) ou pelo Regime de Caixa (MARCADO). Campo disponível na pasta Tributos .Se o Campo estiver habilitado pelo Regime de Caixa , a Apuração do Tributo será executado com base na Data da Baixa dos Lançamentos Financeiros parametrizados.

***Atenção!*** Uma vez que a CPRB é apurada na Filial Matriz., este novo parâmetro só poderá ser editado na Filial Matriz ou na Filial SCP.

Apuração do CPRB

**Marque****o campo HABILITA NF 2018.05 para emissão do DANFE da NF-e de acordo com  os padrões estabelecidos por esta Norma Técnica.  
  
Apuração de ISS:**

Ao emitir uma nota fiscal de serviço (NFS-e) no Padrão Nacional onde o Regime de ISS da NFS-e for **Imune** é obrigatório o preenchimento do campo Tipo de Imunidade para autorização da nota.

Campo Tipo Imunidade

Campo Tipo Imunidade disponível a partir do ultimo patch da versão 12.1.2310.

Campo Regime Especial de Tributação do ISS

O campo **Regime Especial de Tributação do ISS** refere-se aos tipos de regimes especiais de tributação municipal, como **Ato Cooperado**, **Estimativa**, entre outros.

Este campo é opcional e, quando preenchido, seu valor será considerado para a geração da tag <regEspTrib> da NFS-e.

Campo Regime Especial de Tributação ISS está disponível a partir do ultimo patch da versão 12.1.2502.

Dados Adicionais

**Registro do operador de transporte multimodal:**Este campo deverá ser preenchido com o número de registro do operador de transporte multimodal junto à ANTT. O mesmo será utilizado para gerar o registro D170, campo 09 do SPED FISCAL.

**Filial é SCP:**Para que a filial seja considerada SCP o parâmetro Filial é SCP deverá ser marcado e o código da filial sócio ostensivo informado.

**Filial SCP transmite REINF através da Filial Matriz**: Para habilitar esta opção é necessário marcar "Filial é SCP".

**Programa de Aquisição de Alimentos (PPA):**Para que o usuário possa indicar se a filial está inscrita ou não no PAA (Programa de Aquisição de Alimentos).

Para atender à legislação do CT-e OS o usuário deve preencher os campos Termo de Autorização de Fretamento e Número de Registro Estadual no **Cadastro da Filial** em **Anexos | Dados Fiscais |** Aba **Dados Adicionais**.

Demonstrativo de Caixa
