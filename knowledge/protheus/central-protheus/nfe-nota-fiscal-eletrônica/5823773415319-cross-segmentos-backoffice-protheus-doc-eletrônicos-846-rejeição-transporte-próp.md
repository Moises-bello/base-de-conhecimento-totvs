---
article_id: 5823773415319
category: NFe - Nota Fiscal Eletrônica
content_hash: 268ff706b67c935e82fb6ec055cdc71ba6c084554e5741ae58a2e0caf345e524
fetched_at: '2026-06-28T22:40:05.369272+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 846 Rejeição: Transporte
  próprio por conta do Remetente e CNPJ Base ou CPF do Transportador difere do CNPJ
  Base ou CPF do Remetente'
type: support-article
updated_at: '2025-06-18T14:49:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5823773415319-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-846-Rejei%C3%A7%C3%A3o-Transporte-pr%C3%B3prio-por-conta-do-Remetente-e-CNPJ-Base-ou-CPF-do-Transportador-difere-do-CNPJ-Base-ou-CPF-do-Remetente
---

**Dúvida**Como solucionar a 846 Rejeição: Transporte próprio por conta do Remetente e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Remetente ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1. Verifique se a modalidade do frete correta no campo é opção ***3=****Transporte Próprio por conta do Remetente;** **e altere no campo F2\_TPFRETE Tipo Frete.***

**0=**Contratação do Frete por ***conta do Remetente (CIF);***

**1=**Contratação do Frete por ***conta do Destinatário (FOB);***

**2=**Contratação do Frete por ***conta de Terceiros;***

**4=**Transporte ***Próprio por conta do Destinatário;***

***9=Sem Ocorrência de*** Transporte;

![Tipo_frete.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12435803312151)

2. Após isso, exclua a nota e gere novamente.

*3.* Se caso opção de modalidade do frete for 3 no campo ***F2\_TPFRETE Tipo Frete.*** Acessar Cadastro de Contribuinte da UF ***(Chave: UF Retirada , IE Retirada)*****Cadastro Centralizado de Contribuinte (CCC)**[Clique Aqui](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc) e verificar o CNPJ correto da transportadora e alterar no cadastro da transportadora no campo ***CNPJ A4\_CGC.***

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12436105886743)

5. Após isso, exclua a nota e gere novamente.

***Observação 1:*** Regra de validação não se aplica quando ***CNPJ/CPF*** do transportador não for informado.

1. Se não houver um  ***CNPJ/CPF*** transportador, retire o conteúdo do  ***CNPJ/CPF no campo*** ***A4\_CGC vinculado no campo F2\_TRANSP***

![transp_cnpj.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12436204241943)

2. Após isso, exclua a nota e gere novamente.

* ***Validação da Sefaz:***

![846_rejeicao_NT_2021.004.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5912653442071)
