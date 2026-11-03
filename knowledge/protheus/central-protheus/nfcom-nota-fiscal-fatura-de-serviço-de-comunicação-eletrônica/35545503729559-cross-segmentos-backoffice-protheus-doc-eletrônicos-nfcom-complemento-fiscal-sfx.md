---
article_id: 35545503729559
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: d296b551eb4118945fea90c395c48d8d4b783c26da0f71f47c26a5a63f7700d6
fetched_at: '2026-06-28T22:39:55.088646+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM  - Complemento
  Fiscal (SFX) x XML
type: support-article
updated_at: '2025-10-23T19:23:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35545503729559-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Complemento-Fiscal-SFX-x-XML
---

**Dúvida**  
Quais são os campos necessários e obrigatórios para o preenchimento no Complemento Fiscal da NFCOM?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Abaixo segue a relação de campos obrigatórios para geração correta do XML da NFCOM:

|  |  |  |
| --- | --- | --- |
| **Campos SFX** | **Tags XML** | **Observações** |
| FX\_TIPOREC | <tpFat> | **0** - Faturamento Normal;  **1** - Faturamento centralizado;  **2** - Cofaturamento |
| FX\_ESTCONT | <iCodAssinante> | Código único de Identificação do assinante |
| FX\_TPASSIN | <tpAssinante> | **1** - Comercial; **2** - Industrial; **3** - Residencial/Pessoa Física; **4** - Produtor Rural; **5** - Órgão da administração pública estadual direta e suas fundações e autarquias, quando mantidas pelo poder público estadual e regidas por normas de direito público, nos termos do Convênio ICMS 107/95; **6** - Prestador de serviço de telecomunicação responsável pelo recolhimento do imposto incidente sobre a cessão dos meios de rede do prestador do serviço ao usuário final, nos termos do Convênio ICMS 17/13; **7** - Missões Diplomáticas, Repartições Consulares e Organismos Internacionais, nos termos do Convênio ICMS 158/94; **8** - Igrejas e Templos de qualquer natureza; **99** - Outros não especificados anteriormente |
| FX\_TIPSERV | <tpServUtil> | **1** - Telefonia; **2** - Comunicação de dados;  **3** - TV por Assinatura; **4** - Provimento de acesso à Internet;  **5** - Multimídia;  **6** - Outros;  **7** - Vários |
| FX\_NUMCONT | <nContrato> | Número do Contrato do assinante |
| FX\_DINCONT | <dContratoIni> | Data de início do contrato |
| FX\_DFICONT | <dContratoFim> | Data de término do contrato |
| FX\_TERMINA | <NroTermPrinc> | Em se tratando de plano de prestação de serviço telefônico corporativo, familiar ou similares, informar o número do terminal telefônico principal do plano. |
| FX\_AREATER | <cUFPrinc> | Código da UF de habilitação do terminal - Utilizar a Tabela do IBGE de código de unidades da federação. |
| FX\_GRPCLAS + FX\_CLASSIF | <cClass> | Tabela de Classificação de Item da NFCom |

Manual Oficial da Sefaz: <https://dfe-portal.svrs.rs.gov.br/NFCOM/ConsultaSchema>
