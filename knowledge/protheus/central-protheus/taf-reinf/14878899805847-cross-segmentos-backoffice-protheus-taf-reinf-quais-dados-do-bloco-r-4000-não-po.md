---
article_id: 14878899805847
category: TAF - REINF
content_hash: f99049674e1bcb9aafe75d5026b560fdc64d43150c95b809ff8addb79f40c2e7
fetched_at: '2026-06-28T22:41:34.762456+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - REINF - Quais dados do bloco
  R-4000 não possuem tratamento no extrator? '
type: support-article
updated_at: '2023-06-02T21:04:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14878899805847-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Quais-dados-do-bloco-R-4000-n%C3%A3o-possuem-tratamento-no-extrator
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04****:00 min****Dúvida** Quais dados da serie R-4000 não possuem tratamento no extrator?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12.

**Solução**

Algumas informações dos eventos do bloco  R-4000 da EFD-REINF não são tratadas pelas rotinas dos módulos do Backoffice Protheus, e consequentemente o Extrator Fiscal não envia esses dados para o TAF.

Portanto será necessário que essas informações  sejam inseridas diretamente no TAF, para  enviar  na EFD- Reinf.

Segue a lista de algumas  informações que o extrator fiscal não levará para o TAF no  layout 2.1.1:

1- **Valor da contribuição do Funpresp (tag vlrPatrocFunp do evento R-4010)**

Quando ocorrer uma dedução de base do IRPF do tipo FUNPRESP, a informação relativa ao "Valor da contribuição do ente público patrocinador da Fundação de Previdência do Servidor Público (Funpresp)", caso exista, deverá ser informada diretamente no TAF, através da rotina Fatura/Recibo (**TAFA448**)

**2- Data da moléstia grave atribuída pelo laudo - (tag dtLaudo do evento R-4010)**

Quando ocorrer uma isenção de IRPF do tipo "6 - Pensão, aposentadoria, reforma por moléstia grave ou acidente em serviço", caso seja necessário informar a data do laudo da moléstia grave, deve ser informada diretamente no TAF, através da rotina  Participantes (**TAFA053**)

**3- Cadastro e pagamentos para FCI (fundos ou clubes de investimentos)**

O cadastro de FCI serve como base para geração das informações do evento R-1050 ( **Tabela de Entidades Ligadas**) . Este cadastro pode ser preenchido de forma manual na rotina Cadastro FCI Scp    (**TAFA536**).

**4- Plano privado coletivo empresarial de assistência à saúde**

Este cadastro pode ser preenchido de forma manual na rotina  Cadastro do plano de saúde (**TAFA538**), e será utilizado para o preenchimento das informações de reembolso médico e/ou coparticipação apresentados no evento R-4010 quando for necessário apresentar as informações da operadora do plano privado coletivo empresarial de assistência à saúde.

Já os pagamentos (reembolso) pode ser preenchido de forma manual na rotina  Reembolso PLS (**TAFA539**).

**5- Informações de rendimentos decorrentes de processos judiciais ou RRA (Rendimento Recebido Acumuladamente)**

Quando houver pagamentos de títulos a pagar provenientes de um processo judicial ou RRA, após a integração do pagamento através do Extrator Fiscal, será necessário complementar os dados relativos ao: processo, despesas com advogados e custos judiciais. Para isso, insira os dados na rotina  Despesas Processuais/RRA (**TAFA541**) e o número de processo deve ser amarrado a um rendimento (pagamento ou fatura) para que as informações relacionadas ao processo Judicial e/ou RRA sejam apresentadas no evento R-4010 e R-4020.

6- **Pagamento/crédito a beneficiários não identificados (evento R-4040)**

Esse evento serve para o contribuinte informar os pagamentos em que não será possível identificar o beneficiário. Caso houver a necessidade, é necessário inserir os dados do evento no TAF,  na rotina Pagamento/crédito a beneficiários não identificados (**TAFA542)**
