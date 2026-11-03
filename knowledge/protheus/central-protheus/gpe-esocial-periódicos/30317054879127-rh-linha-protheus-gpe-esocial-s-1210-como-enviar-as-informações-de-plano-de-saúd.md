---
article_id: 30317054879127
category: GPE - eSocial - Periódicos
content_hash: 471328e365b28661a0764ea934e3a2791275e03fb32910b54c3d8221ee1cbd63
fetched_at: '2026-06-28T22:45:07.385207+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Como enviar as informações de
  plano de saúde/odonto para o S-1210
type: support-article
updated_at: '2026-06-24T16:00:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30317054879127-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-enviar-as-informa%C3%A7%C3%B5es-de-plano-de-sa%C3%BAde-odonto-para-o-S-1210
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30317054827543) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como enviar ao eSocial no evento S-1210 as informações de plano de saúde/odonto, como mensalidade, coparticipação e reembolso?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
A partir do leiaute S-1.3 se tornou obrigatório o envio do grupo **infoIRComplem** que são informações relacionadas à retenção na fonte, aos rendimentos tributáveis e não tributáveis, deduções e/ou isenções, entre outros no evento S-1210.  
Nesse grupo teremos a tag **planSaude** onde serão levas as informações de plano de saúde coletivo,  identificacando o fornecedor responsavel (operadora de saude/odonto), natureza e incidencia para IRRF especificas, valores e dependentes/agregados.  
  
**Assista** **nosso treinamento** completo sobre Plano de saúde no S-1210: [**Webinar TOTVS | Suporte Responde - Plano de saúde para o eSocial S-1210**](https://www.youtube.com/watch?v=lo2RMo3jeG0)  
  
Dessa forma precisamos realizar os seguintes cadastros no sistema:  
  
**1º** Cadastro do **fornecedor** nas **tabelas S016 e S017** contendo **CNPJ** e **registro ANS** ativo  
**Atenção:** o cadastro de verba para os fornecedores deve obrigatóriamente ser diferente da verba de desconto funcionario e o CNPJ não pode se repetir, no saiba mais veja as documentações dos identificadores para fornecedores;  
Acesse: Atualizações - definição cálculo - manuntenção de tabelas  
**2º** Informar a **natureza 9219 e incidencia 67 no campo IncIRRF**, nas verbas de mensalidade e para **reembolso a natureza é 1405 com incidencia 67 no campo IncIRRF;**  
**3º** Cadastrar o **tipo de plano de saúde;**  
**4º** **Associar** o tipo de plano **ao funcionário e dependentes/agregados** na rotina **Planos de Saúde Ativos;**  
**5º** Para **coparticipação e reembolso**, os valores devem ser informados na rotina GPEA003 Co-participação/reembolso;  
**6º** Criar o **roteiro PLA**, que deve ser calculado e integrado, para que os registros sejam levados às tabelas RHP e RHS.  
  
As verbas de mensalidade, parte empresa, reembolso e coparticipação **devem ser diferentes**. Não pode ter uma verba para varios cadastros.  
  
Para obter mais **informações** sobre cadastro do tipo do **plano de saúde**, cálculo do roteiro PLA e lançamento de coparticipação, acesse nosso material de apoio e se necessário **acione nosso suporte de Benefícios.**  
  
Após as informações estarem cadastradas corretamente, garanta que todos os dependentes/agregados possuem **CPF**, realize o cálculo da folha de pagamento e a geração dos eventos periódicos.  
  
Em casos de lançamentos realizados pelo **modulo 84 (TAF)**, se houver erro **MODEL\_T8E,** por favor veja nosso artigo:

* [RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1210 - Não é permitido informar dados sem referência superior. O formulário Info. Relac. Retenção Na Fonte (MODEL\_T8E) precisa ser preenchido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30280365481367-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1210-N%C3%A3o-%C3%A9-permitido-informar-dados-sem-refer%C3%AAncia-superior-O-formul%C3%A1rio-Info-Relac-Reten%C3%A7%C3%A3o-Na-Fonte-MODEL-T8E-precisa-ser-preenchido)

Para a rejeição ao enviar o S-1210, com codigo de **ocorrência 8 Descrição: Grupo 'Plano de saúde coletivo' deve ser preenchido**, verifique por favor o artigo a seguir:

* [RH - Linha Protheus - GPE - eSocial - S-1210 - RET 8: Grupo 'Plano de saude coletivo' deve ser preenchido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29454128905751-RH-Linha-Protheus-GPE-eSocial-S-1210-RET-8-Grupo-Plano-de-saude-coletivo-deve-ser-preenchido)

**Material de Apoio**  
[Manual do Cálculo de Benefícios](https://tdn.totvs.com/pages/releaseview.action?pageId=904043923)  
[Alerta no lançamento manual de valores de Plano de Saúde](https://tdn.totvs.com/pages/releaseview.action?pageId=918420026)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - Lançamento e cálculo de coparticipação/reembolso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004324382-RH-Linha-Protheus-GPE-Lan%C3%A7amento-e-c%C3%A1lculo-de-coparticipa%C3%A7%C3%A3o-reembolso)  
[RH - Linha Protheus - GPE - Cadastro das verbas referente a assistência médica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057700074-RH-Linha-Protheus-GPE-Cadastro-das-verbas-referente-a-assist%C3%AAncia-m%C3%A9dica)  
[RH - Linha Protheus - GPE - Cadastro das verbas referente ao plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057689734-RH-Linha-Protheus-GPE-Cadastro-das-verbas-referente-ao-plano-odontol%C3%B3gico)  
[Boletim Técnico Leiaute S-1.2 Plano de Saúde, Coparticipação e Reembolso](https://tdn.totvs.com/pages/releaseview.action?pageId=790651360)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
