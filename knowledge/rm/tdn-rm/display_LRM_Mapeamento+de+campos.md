---
content_hash: e96611ad246c3f5734c35769c98b0a29a6e399d3bc3c709fc727011dc80be91e
fetched_at: '2026-06-29T00:10:30.396424+00:00'
page_id: '519728738'
product: rm
source: tdn-rm
title: Mapeamento de campos
type: documentation
url: https://tdn.totvs.com/display/LRM/Mapeamento+de+campos
version: 48
---

R-1000R-1000falseinfoCadastrolefttrue0ideContri

### ideContri

| Elemento | Origem RM |
| --- | --- |
| tpInsc | Gera com 1 se a Filial possuir CNPJ e gera com 2 se a Filial possuir CPF |
| nrInsc | Regra de geração associada ao campo **Filial é Órgão Público** - Cadastro da Filial | Anexos | Dados Fiscais  - Gerado com CNPJ completo quando a filial for Órgão Público. - Gerado com os 8 primeiros dígitos (Raiz) do CNPJ quando a filial não for Órgão Público. imagem |

true0evtInfoContri

### evtInfoContri

xmlinfoCadastro...]]>

Foi realizado ajuste na montagem do XML na geração da tag <evtInfoContri> de forma que sejam acrescentados 3 zeros à direita caso o CGC da filial seja CPF.

Disponível a partir da versão 12.1.28

Filiais

Para filiais que sejam **Órgãos Públicos**, a tag **<evtInfoContri>** será gerada com o CNPJ da filial contendo 14 dígitos. Nas demais filiais, a tag será gerada com o CNPJ raíz (8 primeiros dígitos).

0infoCadastro

### infoCadastro

xmlinfoCadastro
st
123
123
123
123
{...}
{...}
{...}
]]>

**Origem de dados**

| **Elemento do XML** | **Origem** |
| --- | --- |
| classTrib | DFILIAL.CLASSIFTRIBUTARIA |
| indEscrituracao | DFILIAL.EMPOBRIGADAECD |
| indDesoneracao | DFILIAL.DESONERACAOFOLHACPRB |
| indAcordoIsenMulta | DFILIAL.ACORDOINTISENCAOMULTA |
| indSitPJ | Selecionado na execução do processo de transmissão do evento. |
| indUniao | Gerado a partir do campo **Empresa Vinculada a União** Localizado no cadastro da Filial | Anexos | Dados Fiscais  Se o campo preenchido com **Nenhum** a Tag <IndUniao> NÃO será gerada. Se o campo preenchido com **Não** a Tag <IndUniao> será gerada com zero. **<IndUniao>0</IndUniao>** Se o campo preenchido com **Sim** a Tag <IndUniao> será gerada com Um. **<IndUniao>1</IndUniao>** Imagem Cadastro da Filial | Anexos | Dados Fiscais | Pasta Tipo Estabelecimento    DFILIAL.TIPOORGAOPUBLICO |
| dtObito | Data do óbito do contribuinte, se falecido. Não é gerado |
| dtTransfFinsLucr | DFILIAL.CLASSIFTRIBUTARIA Regra Gerar somente se no histórico (tabela DFILIALLOG) estiver o código referente a classificação "Entidade Beneficiente/Isenta" e no cadastro atual estiver a classificação "PJ em Geral" |

1contato

### contato

xmlcontato
str1234
str1234
str1234
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| nmCtt | DFILIAL.NOMECONTADOR |
| cpfCtt | DFILIAL.CPFCONTADOR |
| foneFixo | DFILIAL.DDDCONTADOR + DFILIAL.TELCONTADOR |
| foneCel | DFILIAL.DDDCELCONTADOR + DFILIAL.CELULARCONTADOR |
| email | DFILIAL.EMAILCONTADOR |

2softHouse

### softHouse

xmlsoftHouse
str1234
str1234
str1234
str1234
str1234
]]>

### Origem de dados Dados do Responsável pelo Software, geração automática com valores fixos.

| Elemento do XML | Origem |
| --- | --- |
| cnpjSoftHouse | 53113791001285 |
| nmRazao | TOTVS S.A. |
| nmCont | Eduardo Pires |
| telefone | 3121229000 |
| email | [desenvolvimento-dfe-rm@totvs.com.br](mailto:desenvolvimento-dfe-rm@totvs.com.br) |

3infoEFR

### infoEFR

xmlinfoEFR
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| ideEFR | Se o campo abaixo estiver preenchido, então este campo deve ser preenchido com "N" |
| cnpjEFR | DFILIAL.CNPJENTEFEDERATIVO |

R-1050falsetpEntLigleft0tpEntLig

### tpEntLig

xmltpEntLig
4
str1234
1999-05
1999-05
]]>

Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpEntLig | Campo gerado fixo 4 - Sociedade em conta de participação(SCP) |
| cnpjLig | GFILIAL.CNPJ |
| iniValid | Campo "Início do Período" do Cadastro do Evento |
| fimValid | Campo "Fim do Período"  do Cadastro do Evento |

R-1070falseinfoCadastroleft0ideProcesso

### ideProcesso

xmlideProcesso
5
str1234
1999-05
1999-05
5
{...}
{...}
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpProc | DPROCESSOJUDICIAL.TIPOPROCESSO |
| nrProc | DPROCESSOJUDICIAL.NUMERO |
| iniValid | Campo "Início do Período" do Cadastro do Evento |
| fimValid | Campo "Fim do Período"  do Cadastro do Evento |
| indAutoria | DPROCESSOJUDICIAL.TERCEIRO Se este campo estiver marcado, então preencher este campo com "2". |

1infoSusp

### infoSusp

xmlinfoSusp
str1234
str1234
2012-12-13
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| codSusp | DTRIBDISCUTIDOSPROCJUDICIAL.IDTRIBDISCUTIDOS |
| indSusp | DTRIBDISCUTIDOSPROCJUDICIAL.CODINDICSUSPEXIG |
| dtDecisao | DTRIBDISCUTIDOSPROCJUDICIAL.DATADECISAO |
| indDeposito | DTRIBDISCUTIDOSPROCJUDICIAL.CODINDICDEPMONT |

2dadosProcJud

### dadosProcJud

xmldadosProcJud
st
str1234
str1
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| ufVara | DPROCESSOJUDICIAL.CODETD |
| codMunic | DPROCESSOJUDICIAL.CODMUNICIPIO |
| idVara | DPROCESSOJUDICIAL.VARA |
