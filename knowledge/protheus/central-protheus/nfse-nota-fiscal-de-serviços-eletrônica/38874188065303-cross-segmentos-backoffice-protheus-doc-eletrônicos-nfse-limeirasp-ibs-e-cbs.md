---
article_id: 38874188065303
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d4fd863dce857ab36662658404d6180978f3e7ccee7b4a4eb5b57e1314f73ffc
fetched_at: '2026-06-28T22:39:58.657656+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE Limeira/SP
  (IBS e CBS)
type: support-article
updated_at: '2026-03-18T22:59:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38874188065303-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Limeira-SP-IBS-e-CBS
---

**Dúvida**  
Como realizar o destaque de IBS e CBS no XML da prefeitura de Limeira/SP?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões

**Solução**  
  
**ATUALIZAÇÕES**  
**PROTHEUS**  
Expedição continua Protheus com os fontes atualizados até o dia 26/02:  
12.1.2410: <https://suporte.totvs.com/portal/p/10098/download#detail/1171486>   
12.1.2510: <https://suporte.totvs.com/portal/p/10098/download?e=1224039>

NFSEXMLENV 18/03/2026:

12.1.2410:<https://r.totvs.io/p/1242974>  (Aplicar pacote PTM e compilar no RPO do Protheus).  
12.1.2510:<https://r.totvs.io/p/1242975> (Aplicar pacote PTM e compilar no RPO do Protheus).

Precisamos que os fontes sejam atualizados conforme indicado nesta interação. A expedição continua: -> NFSEXMLENV.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39141844568471)

**TSS**  
12.1.2410:<https://r.totvs.io/p/1240314>

12.1.2510:<https://r.totvs.io/p/1240311>

Dentro desse pacote, há alguns arquivos importantes: 

* .xsd deve ser informado na pasta SCHEMAS
* .tssnewnfse.json na pasta SYSTEM

Boletim Tecnico para apoio : <https://tdn.totvs.com/pages/releaseview.action?pageId=1042920231>

Depois derealizadas as atualizações, ao acessar a rotina FISA022 deverá informar as opções relacionadas ao modelo nacional:

Modelo de Transmissão deve está configurado igual à Prefeitura 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38874194440983)

Após isso, deverá alterar a versão de layout para **'2.04'**, tanto em **homologação** quanto **produção**:

Importante preencher o Token Prefeitura, caso tenha dúvidas deverá contactar a prefeitura

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38874188062743)

Abaixo listamos todas rejeições mapeadas até o momento para a transmissão da nota:

**E90 Numero do RPS invalido. Informe um número de RPS que corresponda a sequência utilizada pelo prestador do serviço.**

 Informe um número de RPS que siga a sequência correta esperada pela Prefeitura. Por exemplo, se o último RPS foi 001148, tentar enviar o 001150 causará erro, pois a Prefeitura aguarda o 001149.

**EI29 Prestador não vinculado com o Subitem do serviço prestado Só é possível usar Subitens dos serviços vinculados ao prestador.**

No portal da Prefeitura, verifique o campo **Selecione o serviço / atividade compatível** e informe o código correspondente no campo B1\_CODISS (exemplo: 14.01).

**EI87 Código tributacao nacional invalido. O campo código tributacao nacional deverá ter tamanho máximo de 5 caracteres.**

**EI88 Código tributacao nacional inexistente. Consulte a legislação vigente para saber o código tributacao nacional do serviço que deverá ser informado.**

No portal, no campo **Selecione o serviço nacional**, escolha o código e informe no B1\_TRIBMUN (exemplo: 140101).

[NFSe - Possibilidades de montagem de Código de Serviço, Código de Tributação e CNAE (NFSEXMLENV e NFSEXMLNAC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061751034-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Possibilidades-de-montagem-de-C%C3%B3digo-de-Servi%C3%A7o-C%C3%B3digo-de-Tributa%C3%A7%C3%A3o-e-CNAE-NFSEXMLENV-e-NFSEXMLNAC?source=search)
