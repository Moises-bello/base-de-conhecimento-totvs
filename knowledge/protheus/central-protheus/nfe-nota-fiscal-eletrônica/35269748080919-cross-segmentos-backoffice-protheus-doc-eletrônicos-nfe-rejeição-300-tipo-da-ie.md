---
article_id: 35269748080919
category: NFe - Nota Fiscal Eletrônica
content_hash: 61e9412c88d7917b92b80a921c17ddf089fbd69af35496949a037afef3ffc5be
fetched_at: '2026-06-28T22:40:06.917658+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Rejeição 300:
  Tipo da IE do Destinatário difere de Não Contribuinte no cadastro da UF'
type: support-article
updated_at: '2025-09-29T14:04:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35269748080919-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Rejei%C3%A7%C3%A3o-300-Tipo-da-IE-do-Destinat%C3%A1rio-difere-de-N%C3%A3o-Contribuinte-no-cadastro-da-UF
---

**Dúvida**  
Como realizar todas as atualizações e configurações para de adequar a **Nota Técnica 2024.003 v1.06?**  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões

**Causa**

A Rejeição 300 ocorre porque cadastrou o destinatário da nota fiscal como "não contribuinte"  ([indIEDest=9](https://www.google.com/search?safe=active&sca_esv=47975ecff811ba0d&rlz=1C1CHBD_pt-PTBR1073BR1073&q=indIEDest%3D9&sa=X&ved=2ahUKEwjViPWijP6PAxXiFLkGHbEKMhwQxccNegQIHRAB&mstk=AUtExfAZAPaRD2KPne6rmPh5KivDj-ELH5LkyXJWFdHFrAEh9GyQom3Kc2iCTW3zK-ZiZ2I973qaGgvA1U0Jhw5tILVR8ZaI8V00llf6EQxy4ngw2FGbfboMB2nDICujwHmTagq-Yo1Y9vzhGLlAS_Mk959kAl-2gTOgLzmWbDQhAqBxlWf9E1lWECVogj4SJxezA7AV&csui=3)), mas o sistema da Secretaria da Fazenda (SEFAZ) da Unidade Federativa (UF) dele o classifica como um contribuinte com Inscrição Estadual (IE) ativa. 

**Solução**

Para resolver, é preciso acessar  ao cadastro do cliente e alterar a opção para o tipo de contribuinte correto, confirmando a Inscrição Estadual, ou então, verificar a informação com o próprio cliente para assegurar a sua classificação cadastral na SEFAZ. 

Acesse ao **Cadastro Centralizado de Contribuintes (CCC)** para verificar qual a situação da IE do destinatário.

<https://dfe-portal.svrs.rs.gov.br/nfe/ccc> 

Após a confirmação do tipo da IE no site da Sefaz CCC, faça as alterações no cadastro do cliente SA1.

1=Contribuinte ICMS (informar a IE do destinatário);

2=Contribuinte isento de Inscrição no cadastro de Contribuintes do ICMS;

9=Não Contribuinte, que pode ou não possuir Inscrição Estadual no Cadastro de Contribuintes do ICMS;

Para gerar a tag indIEDest = 1 é necessário que os campos estejam preenchidos:

A1\_INSCR = preenchido

A1\_CONTRIB =SIM

A1\_IENCONT = Em branco

Para gerar a tag indIEDest = 2 é necessário que os campos estejam preenchidos:

A1\_INSCR = Em branco ou ISENTO

A1\_CONTRIB (ABA FISCAIS) = SIM (é contribuinte só não tem Inscrição)

A1\_IENCONT (ABA OUTROS) = Em branco

Para gerar a tag indIEDest = 9 é necessário que os campos estejam preenchidos:

Se tiver inscrição e precisar destacar no XML

A1\_INSCR = Inscrição estadual

A1\_CONTRIB (ABA FISCAIS) = Não

A1\_IENCONT (ABA OUTROS) = Sim

Se tiver inscrição e não puder destacar no XML

A1\_INSCR = Inscrição estadual

A1\_CONTRIB (ABA FISCAIS) = Não

A1\_IENCONT (ABA OUTROS) = Não

Se não tiver inscrição

A1\_INSCR = Em branco

A1\_CONTRIB (ABA FISCAIS) = Não

A1\_IENCONT (ABA OUTROS) = Não
