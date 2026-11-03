---
article_id: 360016073632
category: Financeiro - Contas a Pagar
content_hash: d4d7e0871cc68a0baeeb676d11761b0e7a96adae62adee8bd28ca5eaacc736e2
fetched_at: '2026-06-28T22:38:06.967697+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Como incluir
  contas a pagar com rateio externo e visualizá-lo
type: support-article
updated_at: '2026-03-02T14:25:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016073632-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Como-incluir-contas-a-pagar-com-rateio-externo-e-visualiz%C3%A1-lo
---

**Dúvida**  
Como incluir contas a pagar com rateio (aba contábil) e visualizá-las?   
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contas a Pagar (FINA050 / FINA750) -  Todas as Versões.  
  
**Solução**  
Para que o rateio no módulo de Contas a Pagar seja executado corretamente utilizando o cadastro de *Rateio Externo* (aba Contábil), é imprescindível que o *Lançamento Padrão 511 – Inclusão de títulos a pagar com rateio* esteja devidamente cadastrado e com o status *Ativo*. Qualquer outra configuração impedirá a execução adequada do rateio externo.

A contabilização do título, seja no modo *online* ou *offline*, é responsável pelo abastecimento das informações na tabela **CV4 – Rateios**.

No módulo **Contas a Pagar (FINA050/FINA750)**, ao incluir um novo título:

Na aba *Contábil*, habilite o campo *Rateio* marcando a opção "Sim" e confirme a inclusão do título.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38015470358679)

Selecione o tipo de rateio (*Digitado* ou *Pré-configurado*) e preencha as Contas Contábeis ou Centros de Custo com os valores a serem rateados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38015429695255)

Quando utilizado o rateio do tipo *Digitado*, os percentuais ou valores informados devem obrigatoriamente totalizar 100% para que o título seja incluído com sucesso.

**Para consultar os dados do rateio:**

Acesse a rotina **Contas a Pagar (FINA050)**, selecione o título desejado, clique em *Outras Ações* e escolha a opção ***Visualizar Rateio***.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38015429696023)

Serão apresentadas as informações referentes ao rateio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38015470360599)

Alternativamente, verifique diretamente na tabela **CV4 – Rateio** se os campos estão devidamente preenchidos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38015429697815)

#### **Importante**

Na rotina **CTBA080 – Lançamento Padrão**, valide se o ***Lançamento Padrão 511*** está com o campo *Status* definido como **Ativo**. Caso contrário, será necessário realizar a alteração.

Caso seja exibido o *help* **NORATEIO**, isso indica que o processo acima não foi corretamente executado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33407137870999)  
  
**Saiba mais**  
[Rateio Externo Contas a Pagar](https://tdn.totvs.com/display/public/PROT/FIN0036_LPAD_Rateio_Externo_Contas_a_Pagar)
