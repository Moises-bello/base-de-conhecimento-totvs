---
article_id: 37496812676759
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 14ba4c86894a3b659de3a248d56c6eca7c20e4c3200472e385656796321aeb34
fetched_at: '2026-06-28T22:39:58.669175+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE São Paulo/SP
  : Erros mapeados no novo layout da NFSE'
type: support-article
updated_at: '2026-02-24T17:49:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37496812676759-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-S%C3%A3o-Paulo-SP-Erros-mapeados-no-novo-layout-da-NFSE
---

**Dúvida**  
Desde 01/01/2026 entrou em produção um novo layout da NFSE para a prefeitura de São Paulo-SP.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Todas as atualizações para o novo layout de São Paulo-SP estão disponiveis no material abaixo:  
[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE São Paulo/SP (IBS e CBS)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37221035991575-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-S%C3%A3o-Paulo-SP-IBS-e-CBS)  
  
Abaixo listamos todos os erros mapeados até o momento para a transmissão da nota:  
  
**Erro: Cod 1002** **- Versão do Schema XML Incorreto. A Versão 2 (Campos IBS/CBS) somente e aceita pelo endereço específico.**  
**R:** Essa rejeição ocorre porque a prefeitura alterou a url do webservice, para atualizar as urls do TSS [clique aqui.](https://suporte.totvs.com/portal/p/10098/download?e=1232131)  
  
**Erro Cod 1001** **- XML não compatível com Schema.The element 'RPS' has invalid child element 'cLocPrestacao'. List of possible elements expected: 'NCM, NBS'.**  
**R:** O erro ocorre porque está sendo transmitida uma NFSE com cálculo de IBS/CBS, e nesse caso é obrigatório o envio do NBS, que deve ser preenchido no cadastro do produto, no campo B5\_NBS.  
Após preencher esse campo, é necessário gerar uma nova nota para transmissão.  
Se tiver dúvidas sobre qual NBS utilizar, recomendamos entrar em contato com a prefeitura para obter essa informação.  
  
**Falha de schema:** **The element 'RPS' has invalid child element 'ValorIPI'. List of possible elements expected.**  
R: Essa falha é devido à ausência da TAG ValorFinalCobrado. Esse erro acontece quando há mais de um item na nota e eles não estão sendo aglutinados.  
[Veja aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021832371-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Falha-de-schema-Element-Servico-is-not-expected-Expected-is-Prestador) como realizar a aglutinação dos itens.  
  
**Falha de schema:****The element 'RPS' has incomplete content. List of possible elements expected: 'IBSCBS'.**  
R: Esse erro ocorre porque a prefeitura está esperando as informações de IBS/CBS na versão 2.0. Para o ambiente de produção, o envio das TAGs no momento é opcional, mas para homologação é necessário enviar os dados de IBS/CBS.

Produção

Para corrigir, é necessário criar o parâmetro MV\_RTCNFSE na SPED000 do TSS com uma data posterior à obrigatoriedade da prefeitura para o IBS/CBS. Por exemplo:  
  
**MV\_RTCNFSE =** '01/**04**/2026'

Agora caso deseje enviar as TAG's de IBS e CBS, basta alterar o parâmetro para uma data inferior à atual, e as informações serão geradas, exemplo:  
  
**MV\_RTCNFSE =** '01/**01**/2026'  
  
**Falha de schema:** **Element '{http://www.prefeitura.sp.gov.br/nfe}indDest': This element is not expected. Expected is ( {http://www.prefeitura.sp.gov.br/nfe}cIndOp )**  
R: O erro acontece porque a NFSE está sendo transmitida com cálculo de IBS/CBS, e, nesse cenário, é obrigatório enviar o **Código de Indicadores de Operação**, que deve ser preenchido no cadastro do configurador ( **Regra de Escrituração** ), no campo **CJ2\_INDOP**.

[**Passo a Passo para correção do erro IndOP aqui.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37280831407511-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-NFSE-Falha-de-Schema-Element-http-www-prefeitura-sp-gov-br-nfe-indDest-This-element-is-not-expected-Expected-is-http-www-prefeitura-sp-gov-br-nfe-cIndOp)

Após preencher esse campo, por favor, gere uma nova nota para transmissão.
