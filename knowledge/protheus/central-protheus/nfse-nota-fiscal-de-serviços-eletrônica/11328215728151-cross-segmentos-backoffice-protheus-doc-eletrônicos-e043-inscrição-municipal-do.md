---
article_id: 11328215728151
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d136a0d0d5cf929b13c1f529252de4156e1df8ebe562b033cb30a367b65803e3
fetched_at: '2026-06-28T22:39:56.230310+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - E043 - Inscrição
  Municipal do Prestador do Serviço não encontrada na base de dados (Brasília)
type: support-article
updated_at: '2025-06-02T12:10:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11328215728151-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-E043-Inscri%C3%A7%C3%A3o-Municipal-do-Prestador-do-Servi%C3%A7o-n%C3%A3o-encontrada-na-base-de-dados-Bras%C3%ADlia
---

**Ocorrência**Como corrigir a rejeição E043?  
Vale ressaltar que ela pode ser apresentada de outras formas, porém todas com o mesmo padrão de tratativa:  
  
***E043** - Inscrição Municipal do Prestador do Serviço não encontrada na base de dados do município.*  
***E157** - Usuário não tem autorização para solicitar o serviço. A pessoa física ou jurídica, identificada pelo CPF ou CNPJ.*  
***L090** - Usuário não tem autorização para solicitar o serviço.*  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeições ocorrem exclusivamente por dois motivos:  
  
**1.** Contribuinte não possuir a liberação para o uso do sistema Webservice da prefeitura;  
**2.** Os dados de IM/CNPJ no XML estão incorretos.  
  
**Solução**Para o **item 1**, é preciso **solicitar autorização** para o uso do ambiente via WebService através do e-mail: [suporte@notaeletronica.com.br](mailto:suporte@notaeletronica.com.br) ou Tel.: (67) 3041-2075.  
  
Para o **item 2,** é preciso verificar os dados de **Inscrição Municipal e CNPJ** no Cadastro da Filial (SIGACFG), após isso refazer o Wizard.cfg por COMPLETO, assim as informações serão atualizadas nas tabelas do TSS, bastando apenas retransmitir a nota.
