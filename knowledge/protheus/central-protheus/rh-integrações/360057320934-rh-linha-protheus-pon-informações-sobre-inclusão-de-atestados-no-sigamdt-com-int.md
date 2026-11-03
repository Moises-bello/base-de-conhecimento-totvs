---
article_id: 360057320934
category: RH - Integrações
content_hash: ae25e6bf59386aed059df025a73757280fc9c99948fa3dbe938712076df15683
fetched_at: '2026-06-28T22:44:47.542621+00:00'
product: protheus
section_id: 32419269542935
source: central-protheus
title: RH - Linha Protheus - PON - Informações sobre inclusão de atestados no SIGAMDT
  com integração no SIGAPON
type: support-article
updated_at: '2025-06-16T17:43:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057320934-RH-Linha-Protheus-PON-Informa%C3%A7%C3%B5es-sobre-inclus%C3%A3o-de-atestados-no-SIGAMDT-com-integra%C3%A7%C3%A3o-no-SIGAPON
---

**Dúvida**Como configurar a  integração do atestado médico com  ponto eletrônico SIGAMDT x SIGAPON?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Certifique-se do conteúdo do seu parâmetro **MV\_PONMES e MV\_PAPONTA**, pois o lançamento realizado precisa estar **dentro do período de ponto em aberto**.  
  
Ajuste o conteúdo dos **parâmetros** abaixo.  
MV\_NG2ABON: Códigos de Abono que podem ser informados pelo programa de Atestado Médico.  
MV\_MDTGPE = S  
MV\_NGMDTAF = S  
MV\_NG2AFAS = Incluir os códigos de ausência.  
MV\_NG2IPON = 1  
  
Após **lançar** o **atestado medico,** deve ser verificado no módulo SIGAPON - cadastro do funcionário -> **pré abono**.  
Nesta rotina, deverá ter o **lançamento do atestado** porem **utilizado** estará como **não** e o ***flag*** deve estar com **G**  
Ao realizar a rotina leitura/apontamento/marcação **reapontando** as marcações, será atualizado nos **lançamentos do funcionário o abono cadastrado** e, na rotina de pré-abono o campo utilizado = SIM.  
  
**Saiba Mais**  
[RH - Linha Protheus - MDT - Integração do Atestado Médico com o Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025162074-RH-Linha-Protheus-MDT-Integra%C3%A7%C3%A3o-do-Atestado-M%C3%A9dico-com-o-Ponto-Eletr%C3%B4nico#:~:text=Ap%C3%B3s%20lan%C3%A7ar%20o%20atestado%20m%C3%A9dico,Cadastro%20do%20funcion%C3%A1rio%20%3E%20Pr%C3%A9%20abono.)
