---
article_id: 360060708093
category: Integrações Outros BackOffice
content_hash: 4744f0ad5d0f2605c014ccef3ec5a29187bbe8e3216bca34bd4f522fa9b00f62
fetched_at: '2026-06-28T22:46:42.193911+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: 'RM - FOP - Integração RM Labore x BackOffice Protheus: Erro no CUSTOMERVENDOR'
type: support-article
updated_at: '2021-10-15T13:20:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060708093-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Erro-no-CUSTOMERVENDOR
---

**Ocorrência**Ao realizar a integração dos Fornecedores do Protheus para o RM Folha de Pagamento através do Adapter CUSTOMERVENDOR, é retornado a mensagem de erro: **"****is not a valid value for Int32. Index was outside the bounds of the array."**  
**Ambiente**RM - Folha de Pagamento - A partir da 12.1  
 **Solução**No RM Folha de Pagamento, deverá acessar o módulo de integração, em Mensagem Única | Integrações | Selecionar a Integração | Anexos | Parâmetros da Integração.   
  
Deverá ser editado o parâmetro RH\_CODCLASSIFICPAIS, alterar para valor 1 e tipo Numérico/Inteiro.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000442661/mceclip0.png)
