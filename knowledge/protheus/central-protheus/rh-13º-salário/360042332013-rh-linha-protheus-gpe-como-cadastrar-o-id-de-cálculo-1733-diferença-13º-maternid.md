---
article_id: 360042332013
category: RH - 13º salário
content_hash: 5e23c7238c695f6ea8be6196737d9ad0f01f6bec81011195d7c1ac82d27f1bc8
fetched_at: '2026-06-28T22:44:00.529064+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar o ID de Cálculo 1733 - Diferença
  13º Maternidade Negativo
type: support-article
updated_at: '2026-03-03T16:58:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042332013-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-de-C%C3%A1lculo-1733-Diferen%C3%A7a-13%C2%BA-Maternidade-Negativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18738466435863) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como cadastrar o ID de Cálculo 1733 - Diferença 13º Maternidade Negativo?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Em Atualizações > Definições de Cálculo > Verbas:

1. **Incluir >** Preencha o código da verba conforme disponibilidade
2. **Descrição:** Diferença de 13o. negativa - Maternidade
3. **Percentual:** 100%
4. **Identificador** **de cálculo:** 1733
5. **Tipo Código:** Desconto
6. **Tipo da verba:** Valor

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38773717764503)

Esta verba trata-se da **diferença** **de 13º** para empregados que estão afastados por licença **maternidade** e receberam o **id 0040**. Antes desta atualização o sistema gerava para estas matriculas o **valor da diferença** no id **0348**. Foi necessário a inclusão deste identificador para atender as exigências do eSocial, onde o sistema irá **separar** os valores que tratam da maternidade das demais diferenças.  
  
A separação dos valores é efetuada através da verificação da configuração do campo **RV\_NATUREZ**: a diferença das verbas configuradas com natureza **4051** serão geradas nos novos Ids de cálculo; já a diferença das demais verbas serão geradas nos Ids antigos (0028 ou 0348).  
  
**Observação:** A configuração das Verbas e as Incidências Tributárias é algo particular de cada Empresa e que deve ser analisado em conjunto com o departamento Jurídico e Contábil  
  
Mais informações relacionadas podem ser encontradas no link a seguir: [DT Complemento 13º Salário - Criação dos IDs de Cálculo 1732 e 1733](https://tdn.totvs.com/pages/viewpage.action?pageId=528450030)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Complemento de 13º Salário Maternidade - Id de Cálculo 1732 e 1733](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042554093-RH-Linha-Protheus-GPE-Complemento-de-13%C2%BA-Sal%C3%A1rio-Maternidade-Id-de-C%C3%A1lculo-1732-e-1733?source=search)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXkGzzAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTA3MjA0MjM5NTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZG8tY29tcGxlbWVudG8tZGUtMTMlQzIlQkEGOwhUOg5zZWFyY2hfaWRJIik4NzRkNTNhZC1mMjFmLTRiZmMtYjQyZC04ZTI0MTFhMTA5OTIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIm5SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUXVhaXMgc8OjbyBhcyBkb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGFvIGPDoWxjdWxvIGRvIGNvbXBsZW1lbnRvIGRlIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--ed4e25a62bb71593b5abc3ca6fcc96028826c1d3)  
[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)
