---
article_id: 5839815125399
category: NFe - Nota Fiscal Eletrônica
content_hash: e3f9202a536a1a87259e2acfd6e3206c9c52062ddfed4b6b6a8f0819435be5e0
fetched_at: '2026-06-28T22:40:05.392490+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 848 Rejeição: Transporte
  próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador difere do
  CNPJ Base ou CPF do Destinatário'
type: support-article
updated_at: '2025-06-18T14:49:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5839815125399-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-848-Rejei%C3%A7%C3%A3o-Transporte-pr%C3%B3prio-por-conta-do-Destinat%C3%A1rio-e-CNPJ-Base-ou-CPF-do-Transportador-difere-do-CNPJ-Base-ou-CPF-do-Destinat%C3%A1rio
---

**Dúvida**Como solucionar a rejeição 848 Rejeição: Transporte próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Destinatário ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

* **Conforme a nota técnica do link abaixo:**

[Nota Técnica 2016.002 - v 1.61 (publicada em 10/09/2018)](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=zfWxcJtOf98=)

Ao clicar no link acima será aberto um PDF com NT.

**Página 51**

**0=**Contratação do Frete por conta do Remetente (CIF);

**1=**Contratação do Frete por conta do Destinatário (FOB);

**2=**Contratação do Frete por conta de Terceiros;

**3=**Transporte Próprio por conta do Remetente;

**4=**Transporte Próprio por conta do Destinatário;

**9=**Sem Ocorrência de Transporte.

**Novas opções:**

* **R = Por conta remetente**(Corresponde opção 3 )
* **D = Por conta destinatário**(Corresponde opção 4 )

**"C"**= **0=**Contratação do Frete por conta do Remetente (CIF);

**"F"** =**1=**Contratação do Frete por conta do Destinatário (FOB);

**"T"=** **2=**Contratação do Frete por conta de Terceiros;

**"R"** =**3=**Transporte Próprio por conta do Remetente;

**"D"** =**4=**Transporte Próprio por conta do Destinatário;

**"S"** = **9=**Sem Ocorrência de Transporte

1. Verifique se a modalidade do frete correta no campo é opção **4=**Transporte ***Próprio por conta do Destinatário;*  Se não*****altere no campo F1\_TPFRETE Tipo Frete.***

![20210712_171640.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896737709207)

2. Após isso, exclua a nota e gere novamente.

*3.* Se caso opção de modalidade do frete for 4 no campo ***F1\_TPFRETE Tipo Frete,*** Acessar Cadastro de Contribuinte da UF ***(Chave: UF Retirada , IE Retirada)*****Cadastro Centralizado de Contribuinte (CCC)**[Clique Aqui](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc) e verificar o CNPJ correto da transportadora e alterar no cadastro da transportadora no campo ***CNPJ A4\_CGC.***

5. Após isso, exclua a nota e gere novamente.

***Observação 1:*** Regra de validação não se aplica quando ***CNPJ/CPF*** do transportador não for informado.

1. Se não houver um  ***CNPJ/CPF*** transportador, retire o conteúdo do  ***CNPJ/CPF no campo*** ***A4\_CGC vinculado no campo F1\_TRANSP***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12435391175703)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12435405427223)

![CNPJ.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12435501085591)

2. Após isso, exclua a nota e gere novamente.

**Caso 2**: Emitida uma NF-e, modelo 55,**de Saída (tpNF=1)** com modalidade do frete igual a 4 (Grupo: transp, campo: modFrete = 4), se o CNPJ ou CPF do transportador (CNPJ ou CPF do grupo “transporta”) for diferente do CNPJ ou CPF do Destinatário (CNPJ ou CPF do grupo “emit”), retornará **Rejeição 848.**

Após isso, exclua a nota e gere novamente.

**Referência:**

[NT 2021.004 v1.20 – Regras de Validação e Novos Campos](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=gv5XFF3hh0Y=)

Se for NF-e de entrada ***(tpNF=0) e Modalidade do Frete = 4 (id: X02,* campo: modFrete),** o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser IGUAL ao CNPJ Base  
(id: C02, campo: CNPJ) ou CPF do Destinatário (id: C03, campo: CPF) ***Observação: Regra de validação não se aplica quando CNPJ/CPF do transportador não for informado.***
