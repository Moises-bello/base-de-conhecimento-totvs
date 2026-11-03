---
article_id: 12072778950423
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: f7ce17f25ca23679869241afce4abde36fc0435a3e83759d334bc856bd3378d3
fetched_at: '2026-06-28T22:42:01.173717+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro 1601 no Sped Fiscal quando não há integração com o módulo
  SIGALOJA?
type: support-article
updated_at: '2023-02-14T19:31:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12072778950423-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-1601-no-Sped-Fiscal-quando-n%C3%A3o-h%C3%A1-integra%C3%A7%C3%A3o-com-o-m%C3%B3dulo-SIGALOJA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida:**

 Como gerar o registro **1601** no Sped Fiscal quando não há integração com o módulo SIGALOJA?  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão 12.1.25  
  
**Solução**

Para gerar o registro **1601** sem o módulo **SIGALOJA** somente com ponto de entrada **SPED1601**, segue exemplo abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=651921344>

Para facilitar o entendimento do **ponto de entrada SPED1601,** segue **exemplo** prático das configurações que foram realizadas com base no **exemplo** do ponto ponto de entrada padrão,  disponibilizado pelo produto.

O código da administradora financeira  deve ser o mesmo constante no cadastro de cliente (tabelas SA1/SAE)

Ao criar um cadastro na **SAE - Administradora Financeira,** o sistema cria esse  mesmo cadastro na tabela SA1, para preencher os dados e gerar o registro 0150 corretamente

**Procedimento para cadastro**

1 - Cadastre as Administradoras Financeiras:

**Campo Tipo Adminstr**=CC - para cartão de crédito, CD para cartão de débito, PX - PIX e PD Pagto Digital.

**Campo Rede Destino** =Selecione a empresa administradora – esse campo é responsável para geração do registro 1601 unificado das administradoras financeiras.

**Importante:**

Ao criar um cadastro na SAE, o sistema cria o mesmo na tabela SA1, para preencher os dados e gerar o registro 0150 corretamente

**Campo Tipo Admins** (AE\_TIPO) - informe de acordo com o cadastro

**Rede Destino (AE\_REDE**), informe a rede para que o sistema gere corretamente. Caso não exista, efetue o cadastro na tabela genérica L9 via configurador.

**Campo Cod. Cliente - AE\_CODCLI/Loja ClienteAE\_LOJCLI** com o código do cliente referente a administradora financeira.

**Importante:**

No cadastro de cliente, **todas** as administradoras devem possuir o cadastro completo.

**Exemplo didático**

Acesse o Modulo 05 (SIGAFAT) e realize o cadastro da ADM Financeira

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12418510867479)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12418480507415)

Condição de pagamento.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12418533019159)

Pedido de venda:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12418534141335)

TXT Gerado

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12418570832279)

Importante ressaltar que os testes exemplificados acima foram realizados com base no exemplo do **Ponto de Entrada SPED1601** disponibilizado pelo produto.

Realize as devidas alterações/customizações conforme a operação fiscal e necessidade da empresa.
