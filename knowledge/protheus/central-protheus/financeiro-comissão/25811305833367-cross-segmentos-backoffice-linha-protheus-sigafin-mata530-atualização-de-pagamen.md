---
article_id: 25811305833367
category: Financeiro - Comissão
content_hash: fda6b5821d1051dd8d27d32ec6e004f5425c18b837b4140687a412d7cad9f505
fetched_at: '2026-06-28T22:37:50.836002+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MATA530 - Atualização
  de Pagamento de Comissões
type: support-article
updated_at: '2026-02-03T17:25:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25811305833367-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATA530-Atualiza%C3%A7%C3%A3o-de-Pagamento-de-Comiss%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25828605356055) Tempo aproximado para leitura: **00:05 min**

**Ocorrência**

O que validar para realizar o pagamento das comissões?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**

Para que o pagamento das comissões seja efetuado, é necessário validar as seguintes informações principais:

Acesse o módulo **Financeiro**, **Atualizações**, **Cadastros**>**Vendedores**> Preencher as informações do **Vendedor** na aba V**endas**, e o campo **Pagamento de Comissão.**

**%Pg na Emis**: Este campo define o percentual do valor da comissão a ser pago na emissão do título.

**%Pg na Baix:** Este campo indica o percentual do valor da comissão a ser pago na baixa do título.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25811296027159)

As comissões podem ser pagas conforme a configuração no **Cadastro de Vendedores**, na aba "**Pagamento de Comissão**", onde é possível definir a "**Forma Pgto**". O pagamento das comissões pode ser gerado utilizando as seguintes opções:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25811305790999)

**1º S – Contas a Pagar**

O sistema gera o valor da comissão como um **título no Contas a Pagar**. Para isso, é necessário vincular um **fornecedor** e uma **loja.**

![Gravar_2024_08_21_15_05_38_826.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25811305793047)

Após a baixa do título, é gerada a comissão na **Manutenção de Comissões.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25829720116759)

**Importante**

**MV\_TPCOMIS = O (online)**

A comissão é gerada automaticamente (após a emissão ou a baixa) sem necessidade de ser realizada a rotina de **Recalc. Comissão (FINA440)**.

**MV\_TPCOMIS = B (batch)**

**Comissão off-line:** O cálculo da comissão somente será gerado após processada a rotina de **Recalc. Comissão (FINA440)**.

**2º F - Folha de Pagamento**

Para mais informações, siga o link: [Comissão F - Folha de Pagamento](https://tdn.totvs.com/pages/releaseview.action?pageId=286010234)

**3º N - Sem interface**

Para esta opção, o sistema grava as **comissões na Tabela SE3** normalmente. No entanto, ao gerar a **Atualização de Pagamento de Comissões (MATA530**), ele apenas preenche a data do pagamento da **comissão (E3\_DATA)**, sem criar registros adicionais.

Dessa forma, é possível visualizar as comissões na rotina "**Manutenção das Comissões" (MATA490)** e no **Relatório de Comissões (MATR540)**, sem que haja integração com outros módulos.

Ao executar a rotina de **Atualização de Pagamento de Comissões (MATA530**), é necessário habilitar o campo indicado para que a **comissão** seja gerada no **Contas a Pagar**. Caso contrário, o registro não será gerado na **SE2**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25811305802647)

**Importante**

Para identificação do registro da **comissão no Pagar,** será gerado o prefixo “**COM**” em nome do **fornecedor** vinculado ao **vendedor,** somando todos os valores de comissões do período.

**Saiba mais**

[HELP: BXNAOCANC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17102292867991-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-HELP-BXNAOCANC?source=search)

[Validações Comissão](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528#Rec%C3%A1lculodeComiss%C3%B5es(FINA440SIGAFIN)-Comiss%C3%A3oOn-lineouOff-line)
