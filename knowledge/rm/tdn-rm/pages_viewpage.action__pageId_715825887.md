---
content_hash: 6499af2e1098d44a6e2e016bfecedf02671c36beb616bb259bca99ca9d0f15e3
fetched_at: '2026-06-29T00:11:26.152198+00:00'
page_id: '715825887'
product: rm
source: tdn-rm
title: Alterações do Layout 2022 - Versão 2.1.1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715825887
version: 95
---

#f5f5f5#363636

Foi publicado no [Diário Oficial da União](https://www.in.gov.br/en/web/dou/-/ato-declaratorio-executivo-cofis-n-60-de-6-de-julho-de-2022-413730315), de 08/07/2022, [Ato Declaratório Executivo COFIS nº 60, de 6 de julho de 2022](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?naoPublicado=&idAto=124862&visao=anotado), que aprova a versão 2.1.1 dos leiautes dos arquivos que compõem a Escrituração Fiscal Digital de Retenções e Outras Informações Fiscais - EFD-Reinf (Eventos R-4000), que será exigida para os eventos ocorridos a partir da competência de março de 2023.

Com os Eventos R-4000 a Receita Federal inicia uma nova Fase na obrigação, a inclusão de outros tributos federais como PIS, COFINS, CSLL e o IRRF, completando assim a Evolução da REINF e mantendo a mesma escritura de eventos.

Devem ser declarados nos eventos R-4000 todas Retenções na fonte (IR, CSLL, COFINS, PIS/PASEP) incidentes sobre os pagamentos diversos efetuados a pessoas físicas e jurídicas.

#f5f5f5#363636Registros01lefttrue01\_1Visão Geral dos Registros

**Tipos de Registros:**

**[R-1000](https://tdn.totvs.com/display/LRM/Eventos+Cadastrais)** - Informações do contribuinte  
**[R-1050](https://tdn.totvs.com/display/LRM/Eventos+Cadastrais)** - Tabela de entidades ligadas   
**[R-1070](https://tdn.totvs.com/display/LRM/Eventos+Cadastrais)** - Tabela de processos administrativos/judiciais  
**[R-2010](https://tdn.totvs.com/pages/viewpage.action?pageId=715830617)** - Retenção de contribuição previdenciária - serviços tomados  
**[R-2020](https://tdn.totvs.com/pages/viewpage.action?pageId=715830650)** - Retenção de contribuição previdenciária - serviços prestados  
**[R-2030](https://tdn.totvs.com/pages/viewpage.action?pageId=715830674)** - Recursos recebidos por associação desportiva  
**[R-2040](https://tdn.totvs.com/pages/viewpage.action?pageId=715830693)** - Recursos repassados para associação desportiva  
**[R-2050](https://tdn.totvs.com/pages/viewpage.action?pageId=715830706)** - Comercialização de produção  
**[R-2055](https://tdn.totvs.com/pages/viewpage.action?pageId=715830721)** - Aquisição de produção rural  
**[R-2060](https://tdn.totvs.com/pages/viewpage.action?pageId=715830735)** - Contribuição previdenciária sobre a receita bruta - CPRB  
**[R-2098](https://tdn.totvs.com/pages/viewpage.action?pageId=525012579)** - Reabertura dos eventos da série R-2000  
**[R-2099](https://tdn.totvs.com/pages/viewpage.action?pageId=521640172)** - Fechamento dos eventos da série R-2000  
**R-3010** - Receita de espetáculos desportivos  
**[R-4010](https://tdn.totvs.com/pages/viewpage.action?pageId=733184530)** - Pagamentos/créditos a beneficiário pessoa física  
**[R-4020](https://tdn.totvs.com/pages/viewpage.action?pageId=733190896)** - Pagamentos/créditos a beneficiário pessoa jurídica  
**R-4040** - Pagamentos/créditos a beneficiários não identificados  
**[R-4080](https://tdn.totvs.com/pages/viewpage.action?pageId=733190928)** - Retenção no recebimento  
**R-4099** - Fechamento/reabertura dos eventos da série R-4000  
**[R-9000](https://tdn.totvs.com/pages/viewpage.action?pageId=522009449)** - Exclusão de eventos  
**R-9001** - Bases e tributos - contribuição previdenciária  
**R-9005** - Bases e tributos - retenções na fonte  
**[R-9011](https://tdn.totvs.com/pages/viewpage.action?pageId=727915628)** - Consolidação de bases e tributos - Contribuição previdenciária  
**[R-9015](https://tdn.totvs.com/pages/viewpage.action?pageId=727912988)** - Consolidação das retenções na fonte

true1R-100001\_1true01\_2R-1000

Os dados deste Registro são montados com base no cadastro de Filiais. Para mais informações acesse:

Informações do Contribuinte

| Registro/Campo | Registro Pai | ALTERAÇÕES |
| --- | --- | --- |
| dtTransfFinsLucr | infoCadastro | Criado a tag <dtTransfFinsLucr> |
| dtObito | infoCadastro | Campo não é gerado |
| indUniao | infoCadastro | Criado a tag <indUniao> Indicativo de entidade vinculada à União. |

true2R-105002\_1true02\_1R-1050

Os dados deste Registro são montados com base no cadastro de Filiais. Para mais informações acesse:

Tabela de entidades ligadas

| Registro/Campo | Registro Pai | ALTERAÇÕES |
| --- | --- | --- |
| tpEntLig | ideEntLig | Criado a tag <tpEntLig> |
| cnpjLig | ideEntLig | Criado a tag <cnpjLig> |
| iniValid | ideEntLig | Criado a tag <iniValid> |
| fimValid | ideEntLig | Criado a tag <fimValid> |

true3R-205503\_1true03\_1R-2055

Os dados deste Registro são montados com base nos lançamentos fiscais de entrada que possuem o Tributo FUNRURAL informado. Para mais informações acesse:

Aquisição de produção rural

| Registro/Campo | Registro Pai | ALTERAÇÕES |
| --- | --- | --- |
| ~~retifS1250~~ | ~~ideEvento~~ | ~~Indicativo de retificação de informação enviada ao ambiente nacional do eSocial.~~ **Campo retirado no novo layout** |

true4R-209904\_1true04\_1R-2099

Este registro é enviado para fechamento dos eventos periódicos. Para mais informações acesse:

Fechamento dos eventos da série R-2000

| Registro/Campo | Registro Pai | ALTERAÇÕES |
| --- | --- | --- |
| ~~compSemMovto~~ | ~~infoFech~~ | ~~Informar a primeira competência a partir da qual não houve movimento, cuja situação perdura até a competência atual.~~ **Campo retirado no novo layout** |

true04\_1R-9011

Alteração do cadastro do Evento R-5011/R-9011.

Para mais informações acesse:

9015R-9015

Criado o Cadastro do Evento R-9015

Para mais informações acesse:

R-4010R-4010

**R-4010 - Pagamentos/créditos a beneficiário pessoa física**

Neste registro serão informados os pagamentos e créditos que os contribuintes efetuarem sobre as contratações de serviço sem vínculo empregatício (pessoa física), para o recolhimento do IR. 

Teremos um evento para cada registro do beneficiário. Para mais  informações acesse:

R-4020R-4020

**R-4020 - Pagamentos/créditos a beneficiários não identificados**

Dever ser declarado os pagamentos/créditos sobre os pagamentos de serviços de pessoas jurídicas.

Será gerado um evento para cada registro de beneficiário. Para mais  informações acesse:

R-4080R-4080

**R-4080 - Retenção no recebimento**

São para empresas prestadoras de serviços com atividades previstas em legislação que efetuam a sua própria retenção. Ou seja, esse registro será transmitido pelos beneficiários dos rendimentos e não pelos contratantes, como, por exemplo, agências de propaganda e publicidade.

Para mais informações acesse:

R-4099R-4099

**R-4099 - Fechamento/Reabertura dos eventos da série R-4000**

É aquele pelo qual se informa o encerramento ou reabertura (se o movimento estiver fechado) da transmissão dos eventos periódicos da série R-4000 na EFD Reinf em determinado período de apuração.

Para mais informações acesse: 

#f5f5f5#363636CadastrosIDcadastrosleftLançamento Fiscal

Criado o campo '**Natureza de Rendimento'** no Lançamento Fiscal - Situação Tributaria \Outros Tributos do Lançamento ou Item do Lançamento.

Para mais informações acesse:

Movimento

Criado o campo **'Natureza de Rendimento'** no Movimento\Tributos do Movimento ou do Item**.**

Para mais informações acesse:

Cadastro Parâmetros de Processos

Foi adicionado no cadastro de Parâmetros de Processos opções para configurar a geração dos Eventos da EFD-Reinf.

Lançamento Financeiro

Criado o campo **'Natureza de Rendimento'** no Lançamento Financeiro pasta Valores| Valores IRRF e Valores de Retenções.

Para mais informações acesse:

#f5f5f5#363636ProcessoIDProcessosleftTransmissão e Consulta

Os processos de Transmitir e Consultar Eventos periódicos foram ajustado para os Eventos do bloco 40.

Para mais informações acesse:

Exclusão

Criado o Processo de Exclusão para os Eventos R-4010, R-4020 e R-4080.

Para mais informações acesse:

#f5f5f5#363636TSS (TOTVS Service SOA)

Para a versão 2.1.1 da EFD Reinf o TSS também liberou várias atualizações. Antes de iniciar os testes, faça atualização do TSS conforme o link abaixo.

* [Atualização do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)
#f5f5f5#363636Outras informações


* [Parâmetros de Processo - EFD REINF](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588#1-5)
* Documentação RM: [EFD-REINF](https://tdn.totvs.com/display/LRM/EFD-Reinf)
* Layout disponível pela RFB: [SPED EFD\_REINF](http://sped.rfb.gov.br/projeto/show/1196)
* [Importação de Eventos R-1000](https://tdn.totvs.com/pages/viewpage.action?pageId=721011043)
* [Natureza de Rendimento](https://tdn.totvs.com/display/LRM/Natureza+de+Rendimentos)
* [Lançamento Financeiro - Fluxus -  (Anexo Evento Periódico)](https://tdn.totvs.com/pages/viewpage.action?pageId=736982006)
* [Fechamento dos Eventos Periódicos.](https://tdn.totvs.com/pages/viewpage.action?pageId=521640172)
* [Reabertura dos Eventos Periódicos.](https://tdn.totvs.com/pages/viewpage.action?pageId=525012579)
* [Relatório - Objeto de Negócio da EFD-REINF para o TReports (Bloco 40)](https://tdn.totvs.com/pages/viewpage.action?pageId=747314339)
