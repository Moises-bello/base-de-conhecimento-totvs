---
article_id: 360021956892
category: Financeiro - Integrações (SIGAFIN)
content_hash: ef3c0af433277a1beae2df9a325a181eec50b60e0d6e6c6b6a00c0653ec4a3fa
fetched_at: '2026-06-28T22:38:18.556488+00:00'
product: protheus
section_id: 1500001539241
source: central-protheus
title: MP - SIGAFIN - Integração Participante x Reserve
type: support-article
updated_at: '2021-04-28T15:14:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021956892-MP-SIGAFIN-Integra%C3%A7%C3%A3o-Participante-x-Reserve
---

**Dúvida**É possível integrar Participantes do Cadastro de pessoas(APDA020) com o Reserve para quando o colaborador for fazer uma viagem?

**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.  
  
   
**Solução**Sim, para isso é necessário que os seguintes campos estejam preenchidos:

| RD0 |
| --- |
| RD0\_NOME |
| RD0\_EMAIL |
| RD0\_CODIGO |
| RD0\_DDD |
| RD0\_DDI |
| RD0\_SEXO |
| RD0\_LOGINR |
| RD0\_IDRESE |
| RD0\_EMPANT |
| RD0\_FILANT |
| RD0\_CIC |
| RD0\_DTNASC |
| RD0\_NVLCAR |
| RD0\_CC |
| RD0\_FONE |
| RD0\_DVIAGE |
| RD0\_PERMAD |
| RD0\_APROPC |
| RD0\_APSUBS |
| RD0\_FORNEC |
| RD0\_LOJA |

**Importante**- A integração **não** ocorrerá caso o campo **Disp Viage (RD0\_DVIAGE)**esteja com o conteúdo **1=Não viaja**.  
  
- No Cadastro de Pessoas, temos a aba **Viagem** com alguns campos específicos para o processo de viagem. Abaixo, destaco os principais campos:  
**Nível Cargo**(RD0\_NVLCAR): Define o nível de cargo deste participante, conforme cadastro da tabela FL3;  
**Login Reserv**(RD0\_LOGINR):Login do participante/passageiro no Sistema Reserve;  
**ID Reserve**(RD0\_IDRESE):Código deste participante no Reserve. Este campo é preenchido automaticamente no momento da integração.  
**Perm.Adto**(RD0\_PERMAD):Este campo determina se o participante pode ou não solicitar um adiantamento para a viagem;  
**Aprovador**(RD0\_APROPC): Define quem será o aprovador no processo de viagem deste participante;  
**Substituto**(RD0\_APSUBS):Permite definir um substituto para aprovações no processo de viagem deste participante;  
**Fornecedor**(RD0\_FORNEC):Código do fornecedor vinculado ao participante.
