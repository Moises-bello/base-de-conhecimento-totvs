---
article_id: 38748120049559
category: Meu RH - Pagamento
content_hash: b855353163915754d7d326bc9b3a26d2d221bfd79e5ae00c37f6929dfe354b41
fetched_at: '2026-06-28T22:47:33.834989+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: RH - RM - Meu RH - Comportamento do Informe de Rendimentos para funcionários
  transferidos
type: support-article
updated_at: '2026-03-05T18:00:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38748120049559-RH-RM-Meu-RH-Comportamento-do-Informe-de-Rendimentos-para-funcion%C3%A1rios-transferidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38748142938007) Tempo aproximado para leitura: **00:03:50 min**  
  
**Dúvida**  
Qual é o comportamento para geração e visualização do Informe de Rendimentos para funcionários que possuem transferência?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.27  
  
**Solução**  
1. Transferência entre **Filiais da mesma Coligada** no ano de **2025**

Quando o funcionário foi transferido entre **filiais que pertencem à mesma coligada** durante o ano de 2025, o comportamento do **Informe de Rendimentos no Meu RH** será o seguinte:

* Para que o **Informe de Rendimentos seja gerado corretamente**, é **obrigatório gerar a DIRF informando o CPF do funcionário quando é gerado apenas para uma pessoa, ou gerar para todos os funcionários (incluindo D-Demitido).**
* Ao informar o CPF, o sistema irá **localizar todos os vínculos existentes**, incluindo:

  + Chapas **demitidas**
  + Chapa **ativa**
* Após a geração da DIRF:

  + O **Informe de Rendimentos ficará disponível apenas na Chapa Ativa** no Meu RH.
  + Esse informe irá **consolidar todas as verbas** referentes aos vínculos do funcionário, tanto do período **demitido** quanto do período **ativo**.

**Observação importante**  
Caso a **transferência tenha ocorrido em 2026**, o comportamento muda:

* O **Informe de Rendimentos será armazenado no vínculo Demitido**, e não na Chapa Ativa.

---

2. Transferência entre **Coligadas diferentes** no ano de **2025**

Quando o funcionário teve transferência entre **coligadas diferentes** (ou seja, **empresas com CNPJ distintos**) durante o ano de 2025, o sistema adota um comportamento diferente:

* Será gerado **um Informe de Rendimentos para cada vínculo** do funcionário.
* Isso ocorre porque cada coligada possui um **CNPJ/empresa diferente**, impossibilitando a unificação das informações.
* Dessa forma:

  + Cada vínculo (chapa) terá **seu próprio Informe de Rendimentos**.
  + As verbas **não serão consolidadas em um único informe**, diferentemente do cenário descrito no item 1.

#### **Importante**:

Nos casos em que foram criados cadastros para o mesmo funcionário com códigos de pessoa distintos, é necessário realizar o processo de unificação descrito [AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014630691-RH-RM-RHU-Unificar-pessoas).

Em seguida, deve-se associar o mesmo usuário a todas as chapas do funcionário e, no momento do acesso ao Meu RH, o usuário poderá escolher qual chapa acessar por meio do recurso de contexto - [Trocar contexto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028833431-RH-RM-Meu-RH-Altera%C3%A7%C3%A3o-de-contexto).
