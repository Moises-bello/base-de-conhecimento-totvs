---
article_id: 360057828454
category: MDT - Atendimento Médico
content_hash: 06965d4c47f0e69737a2c7f9c9e6b5310b63e7223f3f125e53856e8613dcffb1
fetched_at: '2026-06-28T22:44:21.420102+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Os campos R8_NMMED, R8_IDEOC, R8_CRMMED são dependentes,
  se um for preenchido todos devem ser
type: support-article
updated_at: '2025-07-25T19:48:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057828454-RH-Linha-Protheus-MDT-Os-campos-R8-NMMED-R8-IDEOC-R8-CRMMED-s%C3%A3o-dependentes-se-um-for-preenchido-todos-devem-ser
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27598342395287)**Tempo aproximado para leitura: 00:01:00 min**Ocorrência**Ao confirmar um atestado medico (**MDTA685**) no modulo Medicina e Segurança do Trabalho ocorre a seguinte mensagem:  
**Problema**: Os campos R8\_NMMED, R8\_IDEOC, R8\_CRMMED são dependentes, se um for preenchido todos devem ser.   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100295133)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho  - Todas as versões  
  
**Causa**Essa mensagem ocorre nos casos que está sendo integrado o afastamento com o modulo Gestão de Pessoal (SIGAGPE), e aos campos do cadastro de Emitentes **Ent. Classe** (TNP\_ENTCLA), **Num. Ent.** (TNP\_NUMENT) e **UF Ent.** (TNP\_UF) responsáveis por alimentar os campos **R8\_NMMED**, **R8\_IDEOC**, **R8\_CRMMED** não estão preenchidos ou estão com informação incorreta.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o cadastro de Emitente no Módulo 35 (SIGAMDT) no caminho: Atualizações > Atendimento Médico > Médico Emitente de Atestado **(****MDTA680)**;  
  
2. Verifique se os campos **Ent. Classe** (TNP\_ENTCLA), **Num. Ent.** (TNP\_NUMENT) e **UF Ent.** (TNP\_UF) estão preenchidos;  
  
3. Deve ser observado também o campo **Ent. Classe** (TNP\_ENTCLA), para integrar o afastamento com o SIGAGPE só é possível ser os 3 primeiros dígitos foram CRM, CRO ou RMS.  
Exemplo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100296813)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[MP - MDT - Como criar novos tipos (funções) de emitentes de atestados médicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056243514-MP-MDT-Como-criar-novos-tipos-fun%C3%A7%C3%B5es-de-emitentes-de-atestados-m%C3%A9dicos?source=search)  
[MP - MDT - Seleção de quais emitentes serão liberados para a geração de atestados médicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044452334-MP-MDT-Sele%C3%A7%C3%A3o-de-quais-emitentes-ser%C3%A3o-liberados-para-a-gera%C3%A7%C3%A3o-de-atestados-m%C3%A9dicos?source=search)
