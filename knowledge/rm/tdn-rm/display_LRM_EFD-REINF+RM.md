---
content_hash: c1d752ce94aad0670843224ee93a16e3453a955d3844a255c96cc80e75446d2e
fetched_at: '2026-06-29T00:08:55.458037+00:00'
page_id: '349183651'
product: rm
source: tdn-rm
title: EFD-REINF RM
type: documentation
url: https://tdn.totvs.com/display/LRM/EFD-REINF+RM
version: 36
---

Novidades EFD Reinf

A partir da versão 12.1.27 a linha RM também gera os eventos da REINF e realiza a transmissão, [clique aqui](http://transmite a Reinf) para mais informações.

solidPrincipais assuntosConceitos Básicos

## Conceito EFD-REINF

A Escrituração Fiscal Digital das Retenções e Informações das Contribuições Previdenciárias Substituída (EFD-REINF), nasceu dentro do eSocial, como uma necessidade da Receita Federal do Brasil (RFB) de controlar as retenções dos tributos federais de forma única e ao mesmo tempo aproveitar uma estrutura inovadora. Dentro do projeto do Sistema Público de Escrituração Digital (SPED), o envio das informações seria de modo segmentado, através de eventos codificados em linguagem XML, como já ocorre na NF-e. Porém, com a dimensão que tomou o eSocial, aliado a grande dificuldade dos departamentos ligados as Relações Humanas de compreenderem os preceitos dos pagamentos realizados por Tomadores e Prestadores de serviços, bem como nosso complexo quadro normativo relacionados aos tributos federais, a EFD-REINF foi retirada do layout do eSocial. Agora, cada obrigação tem a sua própria estrutura e segue o seu próprio layout para se integrarem através de um sistema de gerenciamento de pagamentos, denominado DCTF-WEB. Este sistema será o responsável pela emissão das Guias de Pagamentos dos Tributos Federais, que a princípio terão sob sua ótica apenas as Contribuições Previdenciárias.

A EFD-REINF abarca todas as retenções do contribuinte sem relação com o trabalho, bem como as informações sobre a receita bruta para a apuração das contribuições previdenciárias substituídas. A nova escrituração substituirá as informações contidas em outras obrigações acessórias, tais como o módulo da EFD-Contribuições que apura a Contribuição Previdenciária sobre a Receita Bruta (CPRB).

São objetivos da EFD-REINF:

* Simplificar o cumprimento de obrigações; e
* Aprimorar a qualidade de informações previdenciárias, fiscais e tributárias prestadas pelos contribuintes substituindo o envio de diversas declarações, formulários, termos e documentos.

As informações referentes a períodos anteriores à implantação da EFD-REINF devem ser enviadas pelos sistemas utilizados à época.

## Contribuintes obrigados

* Empresas sujeitas a Contribuição Previdenciária sobre a Receita Bruta
* Empresas obrigadas a Retenções de impostos como IR, CSLL, COFINS, PIS/PASEP, incidentes sobre os pagamentos diversos feitos a pessoas jurídicas;
* Empresas que prestam ou contratam serviços realizados por cessão de mão de obra ou empreitada
* Produtor rural pessoa jurídica e agroindústria quando sujeitos a contribuição previdenciária substitutiva sobre a receita bruta proveniente da comercialização da produção rural
* Associações desportivas que mantenham equipe de futebol profissional valores para promover espetáculos desportivos
* Entidades promotoras de eventos envolvendo associação desportiva ligada a clubes de futebol profissionais

## O que deve ser declarado na EFD-REINF

* Retenções na fonte (IR, CSLL, COFINS, PIS/PASEP)
* Serviços Tomados (Cessão de Mão de Obra ou Empreitada Total e Parcial)
* Serviços Prestados (Cessão de Mão de Obra e Empreitada Total e Parcial)
* Recursos Recebidos ou Repassados por Associação Desportiva
* Comercio de Produção Agroindústria PJ
* Apuração de CPRB
* Recursos Recebidos de Entidades Promotoras de Eventos Desportivos

## Obrigatoriedade e periodicidade

A obrigatoriedade da EFD-REINF foi escalonada e distribuída da seguinte forma:

* Maio de 2018

  + Empresas que faturam igual ou acima de 78.000.000,00

* Novembro de 2018

  + Empresas que faturam abaixo de 78.000.000,00

A EFD-REINF será transmitida mensalmente, de acordo com a periodicidade dos seus eventos, que estão definidos assim:

**Eventos de Tabela (Iniciais)**

|  |  |  |
| --- | --- | --- |
| R-1000 | Informações do Contribuinte | No início do período e sempre que houver alterações |
| R-1070 | Tabela de Processos Administrativos/Judiciais | 15 do mês subsequente ou antes do envio de qualquer evento no qual o processo tenha sido informado |

**Eventos Periódicos**

|  |  |  |
| --- | --- | --- |
| R-2010 | Retenção Contribuição Previdenciária – Prestadores de Serviço | 15 do mês subsequente |
| R-2020 | Retenção Contribuição Previdenciária - Tomadores de Serviço | 15 do mês subsequente |
| R-2030 | Recursos recebidos por Associação Desportiva | 15 do mês subsequente |
| R-2040 | Recursos repassados para Associação Desportiva | 15 do mês subsequente |
| R-2050 | Comercialização da produção por Produtor Rural PJ/Agroindústria | 15 do mês subsequente |
| R-2060 | Contribuição Previdenciária sobre a Receita Bruta - CPRB | 15 do mês subsequente |
| R-2070 | Retenção na Fonte - IR, CSLL, COFINS, PIS/PASEP - Pagamentos Diversos | 15 do mês subsequente |
| R-2098 | Reabertura dos eventos periódicos | 15 do mês subsequente |
| R-2099 | Fechamento dos eventos periódicos | 15 do mês subsequente |

**Eventos Não Periódicos**

|  |  |  |
| --- | --- | --- |
| R-3010 | Receita de espetáculo desportivo | Até o segundo dia subsequente ao do evento |
| R-5011 | Informação das bases e dos tributos consolidado por contribuinte | Evento de retorno enviado automaticamente com a totalização das bases e tributos consolidados por contribuinte a cada transmissão |
| R-9000 | Exclusão de eventos | Sempre que houver exclusão que torne sem efeitos qualquer um dos eventos |

## Penalidades

As sanções até este momento são as previstas para o próprio projeto SPED e pelas normas dos tributos federais. Não há penalidade prevista exclusivamente para a não entrega da EFD-REINF até o momento.

## Manual do Contribuinte x Versão do layout

A RFB ainda não disponibilizou o Manual do Contribuinte, somente o Manual de Orientação e o layout que podem ser acessados nos links abaixo:

* + - [Layout EFD REINF](http://sped.rfb.gov.br/pasta/show/2133);
    - [Manual de Orientação](http://sped.rfb.gov.br/pasta/show/2225).

## Transmissão do Arquivo

O contribuinte gera um arquivo eletrônico, assinado digitalmente, para garantir a integridade dos dados e a autoria do emissor. O arquivo eletrônico é transmitido e será emitido um protocolo de recebimento que será enviado ao empregador / contribuinte. A EFD-Reinf não funciona por meio de um Programa *off-line* Gerador de Declaração (PGD) ou Validador e Assinador (PVA), ou seja, não possui um aplicativo para download no ambiente do contribuinte que importe o arquivo e faça as validações antes de transmitir.

O arquivo pode ser gerado de duas formas: pelo sistema de propriedade do contribuinte ou contratado de terceiros, assinado digitalmente e transmitido por meio de*webservice,*recebendo um protocolo de entrega (Comprovante).

## Certificado

O certificado digital utilizado no sistema EFD-Reinf deverá ser emitido por Autoridade Certificadora credenciada pela Infraestrutura de Chaves Públicas Brasileira – ICP-Brasil.

O certificado digital deverá ser do tipo A1 ou A3. Certificados digitais de tipo A1 ficam armazenados no próprio computador a partir do qual ele será utilizado. Certificados digitais do tipo A3 são armazenados em dispositivo portátil inviolável do tipo *smart* card ou *token*, que possuem um chip com capacidade de realizar a assinatura digital.

 Os certificados digitais serão exigidos em dois momentos distintos:

1. 1. 1. Transmissão: antes de ser iniciada a transmissão de solicitações ao sistema EFD-Reinf, o certificado digital do solicitante é utilizado para garantir a segurança do tráfego das informações na INTERNET. Para que um certificado seja aceito na função de transmissor de solicitações este deverá ser do tipo e-CNPJ (e-PJ).
      2. Assinatura de documentos: Os eventos poderão ser gerados por qualquer estabelecimento da empresa ou seu procurador, mas o certificado digital assinante destes deverá pertencer a Matriz ou ao representante legal desta ou ao procurador/substabelecido, outorgado por meio de procuração eletrônica e não-eletrônica. Os certificados digitais utilizados para assinar os eventos enviados à EFD-REINF deverão estar habilitados para a função de assinatura digital, respeitando a Política do Certificado. Está previsto para o projeto o uso de Procuração Eletrônica da RFB

  
Manuais importantes

* [Manual do TAF](http://tdn.totvs.com/pages/viewpage.action?pageId=271650454)
* [Integração RM x TAF](http://tdn.totvs.com/pages/viewpage.action?pageId=336404337)
solidDúvidas GeraisNo primeiro momento, a entrega da EFD Reinf estava para Jan/2018, onde podemos consultar essa prorrogação para Maio/2018?

No site do sped existe uma nota publicada sobre a prorrogação da entrega do Reinf para o primeiro grupo de contribuintes – empresas com faturamento superior a 78 milhões - para Maio/2018  
<http://sped.rfb.gov.br/pagina/show/2414>

Quais os eventos do Reinf que devem ser entregues a partir de Maio/2018?

Todos os eventos, exceto o R-2070 que ainda não tem prazo para entrada em produção. 

As guias de pagamento serão geradas pela DCTF web?

A DCTF Web é o sistema da Receita federal que irá consolidar as informações recebidas do REINF e do e-Social para gerar as guias de pagamentos.  
Irá consolidar os dados e apresentar para o contribuinte os valores compensados (terá a integração com o per/dcomp), creditos, suspensão por processo judicial ou adm e débitos a pagar pelo contribuinte.   
Depois irá gerar a guia de pagamento da contribuição previdenciária com base nas informações prestadas.

Clubes de futebol terão a obrigatoriedade do evento R-3010?

Somente se o clube for classificado como associação desportiva ou federação desportiva que mantém clube de futebol devem enviar este evento.

Onde devo informar os dados da receita de Espetáculo Desportivo no RM?

Essas informações devem ser inseridas diretamente no cadastro criado no TAF.

Sou obrigado a ter o TAF para o REINF?

Sim. Assim como o E-Social, a entrega dos dados para o REINF para a Receita, será feita através do TAF.  
O TOTVS Gestão Fiscal irá alimentar a base do TAF com as informações de notas e títulos através do Gerador de Saídas.   
A partir disso, o TAF irá consolidar essas informações e realizar o envio à Receita via TSS.

Podemos utilizar o mesmo TSS para envio de NF-e, e-Social e Reinf?

A versão do TSS a ser utilizada para o REINF deve ser release 12.1.17 ou superior e versão 3.0.

O que preciso fazer para realizar a integração com o TAF?

As implementações foram realizados nos Releases de mercado 12.1.18 e 12.1.19 e na Release 12.1.20 (prevista para 06 de abril).

Será necessário:

* + Atualizar sua Biblioteca para o Patch Específico 12.1.18.194 ou 12.1.19.147, ou superiores.
  + Executar o script da Reinf disponível no [RM Atualizador](http://tdn.totvs.com/display/public/rm/Atualizador++V.12).
  + Importar o Layout do Gerador de Saídas criado especificamente para a integração com o TAF, disponível na pasta de Objetos Gerenciais.
  + Sanear os cadastros inerentes à esta rotina (Cadastros de Filiais,Processos Judiciais/Administrativos, Cliente/Fornecedor e Produtos/Serviços).

Para geração dos registros referentes à segunda entrega (R-2030, R-2040, etc) será necessário, além dos passos relatados acima:

* + Atualizar sua Biblioteca para o Patch Específico 12.1.18.208 ou 12.1.19.169 ou 12.1.20.107, ou superiores.
  + Executar o script da Reinf disponível no [RM Atualizador](http://tdn.totvs.com/display/public/rm/Atualizador++V.12).
  + Executar o script para geração dos eventos R-2030 e R-2040, de nome NU.2018.03\_04, disponível no [RM Executor de Scripts](http://tdn.totvs.com/display/public/rm/%5BLegado%5D+-Executor+de+Scripts+RM)

**IMPORTANTE!** Será necessário regerar o arquivo \_broker.dat. Para isso 1) pare o serviço do Host, 2) delete o arquivo \_broker.dat na pasta RM.Net e 3) reinicie o serviço do Host.

solidBase de Conhecimentotruetrue

Lista de alterações realizadas no sistema:

* [Cadastro de Filiais / Anexo Dados Fiscais - Campos novos](http://tdn.totvs.com/display/LRM/FISCAL01-908+DT+Reinf+-+Cadastro+de+Filiais)
* [Cadastro de Filiais - Histórico de Alteração](http://tdn.totvs.com/display/LRM/FISCAL01-909+DT+Log+do+Cadastro+da+Filial)
* [Cadastro de INSS/PJ - Campos Novos](http://tdn.totvs.com/pages/viewpage.action?pageId=287078794)
* [Cadastro de Cliente/Fornecedor - Campos novos](http://tdn.totvs.com/pages/viewpage.action?pageId=286519272)
* [Cadastro de Processos Judiciais/Administrativos - Campos novos](http://tdn.totvs.com/pages/viewpage.action?pageId=286223366)
* [Cadastro de Processos Judiciais/Administrativos - Anexo](http://tdn.totvs.com/display/LRM/FISCAL01-1027+REINF+Anexo+Tributos+Discutidos+Processo+Judicial)
* [Cadastro de Processos Judiciais/Administrativos - Histórico de alteração](http://tdn.totvs.com/display/LRM/FISCAL01-911+DT+REINF+-+Log+Processo+Judicial)
* [Cadastro de Produtos/Serviços, Anexo Dados Fiscais - Campos novos](http://wikihelp.totvs.com.br/WikiHelp/EST/Est.DadosFiscaisProduto.aspx)
* [Cadastro de Projetos - Campos novos](http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.EdicaoProjeto.aspx)
* [Integração com Nucleus - Escrituração (INSS e Funrural)](http://tdn.totvs.com/pages/viewpage.action?pageId=347445276)
* [Lançamento Fiscal](http://tdn.totvs.com/display/LRM/FISCAL01-1583+DT+REINF+Memoria+Calculo+Tributo+Item+Lancamento+Fiscal)
* [Apuração do Tributo FUNRURAL](http://tdn.totvs.com/pages/viewpage.action?pageId=307832540)
* [Alteração na apuração do INSS](http://tdn.totvs.com/display/LRM/FISCAL01-2338+DT+Tributos+Itens+INSS)
* [Integração RM x TAF - WebService](http://tdn.totvs.com/pages/viewpage.action?pageId=336404337)
solidAtualizado recentemente

6truesidebarREINF\_RM

BeigesolidLegislação - EFD-REINF

```
 Consultoria de Segmentos
```

###### [IN RFB nº 1701](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=anotado&idAto=81226) - Institui a Escrituração Fiscal

###### Digital de Retenções e Outras Informações

###### Fiscais (EFD-Reinf).

###### [IN RFB nº 1767](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=anotado&idAto=88696#1836552) - Faseamento do e-Social

solidBeigePacotes de Atualização

**RM 12.1.18 e 12.1.19**

* Data de Liberação do Pacote:

**02/04 - 1ª Entrega**

* + Extrator Fiscal - Linha RM
  + Apuração dos Eventos - TAF
    - R-1000
    - R-1070
    - R-2010
    - R-2020
    - R-9000
  + Monitor de transmissão dos eventos para o Governo - TAF

**04/05 - Entrega Final**

* + Apuração dos Eventos - TAF
    - R-2030
    - R-2040
    - R-2050
    - R-2060
    - R-2098
    - R-2099
    - R-3010
    - R-5001

**RM 12.1.20**

* Data de Liberação do Pacote:

**13/04 - 1ª Entrega**

* + Extrator Fiscal - Linha RM
  + Apuração dos Eventos - TAF
    - R-1000
    - R-1070
    - R-2010
    - R-2020
    - R-9000
  + Monitor de transmissão dos eventos para o Governo - TAF

**04/05 - Entrega Final**

* + Apuração dos Eventos
    - R-2030
    - R-2040
    - R-2050
    - R-2060
    - R-2098
    - R-2099
    - R-3010
    - R-5001

solidLinks principais

 Home - TAF:

[TAF](http://tdn.totvs.com/display/TAF)

[Guia de instalação e configuração - TAF (TOTVS Automação Fiscal) e TSS (TOTVS Service SOA)](http://tdn.totvs.com.br/pages/releaseview.action?pageId=331868191)

[Guia de atualização via TOTVS Developer Studio - TAF (TOTVS Automação Fiscal) e TSS (TOTVS Service SOA)](http://tdn.totvs.com/pages/releaseview.action?pageId=344461282#UPDDISTReUPDTAF--2050426759)

 Home - TSS:

[TSS](http://tdn.totvs.com/display/TSS)

[Como utilizar o REINF no TSS](http://tdn.totvs.com/pages/viewpage.action?pageId=347443982)

solidSaiba mais

**Comunidade R@ Fiscal**

Abrange os temas: rotinas legais, apuração de tributos e projetos do SPED como Sped Fiscal e EFD Contribuições.

[Acesse aqui](http://fluig.totvs.com/portal/p/10097/subject/rfiscal) a Comunidade R@ Fiscal.

**Comunidade **TAF - TOTVS Automação Fiscal****

Focado em todos os temas envolvendo o TAF para a entregas das obrigações fiscais, seja ela Fiscal, RH-eSocial ou Contábil-ECF.

[Acesse aqui](http://fluig.totvs.com/portal/p/10097/subject/taftotvsautomacaofiscal) a Comunidade TAF - TOTVS Automação Fiscal

solidOutros links

 Sobre o Ciclo de Vida de Software - TOTVS:

[Informações gerais](https://suporte.totvs.com/portal/p/10098/ciclodevida)

[Linha RM](https://suporte.totvs.com/portal/p/10098/rm)

[Calendário das Releases](https://suporte.totvs.com/portal/p/10098/rel)

[Perguntas Frequentes](https://suporte.totvs.com/portal/p/10098/ciclodevidafaq)
