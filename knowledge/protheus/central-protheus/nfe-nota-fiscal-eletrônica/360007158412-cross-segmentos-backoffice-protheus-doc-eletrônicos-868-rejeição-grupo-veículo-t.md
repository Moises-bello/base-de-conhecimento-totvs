---
article_id: 360007158412
category: NFe - Nota Fiscal Eletrônica
content_hash: 541da52d36eb53cbbd29b03030e109575bcdb5e0cf72550ca3e618aca7eb89c8
fetched_at: '2026-06-28T22:40:00.044137+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 868 Rejeição :
  Grupo veículo transporte e reboque não devem ser informados'
type: support-article
updated_at: '2024-11-11T20:58:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007158412-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-868-Rejei%C3%A7%C3%A3o-Grupo-ve%C3%ADculo-transporte-e-reboque-n%C3%A3o-devem-ser-informados
---

**Dúvida**

Como solucionar a rejeição abaixo :

868 Rejeição : Grupo veículo transporte e reboque não devem ser informados ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Exemplo o XML gerou conforme abaixo **emitente e destinatário da mesma UF:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069622694)

* No XML  foi gerada as TAGs **de veículo ou reboque ou os dois** conforme o exemplo abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16999068027031)

* A **critério da UF** pode ocorrer a rejeição 868 devido gerar as TAGS **<veicTransp> e <reboque>** no XML.

Para operação **interestadual** não gerar a informação pois há um tratamento  no fonte do NFESEFAZ **(RDMAKE da NFe)** e para operações internas há um **parâmetro.**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar****MV\_INTTRAN = .F.** **Não gera as TAGS** para operações Internas

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069625334)

2. Após isso, exclua a nota e gere novamente.

* **Saiba mais:**

No Danfe no **quadro Transportador/Volumes transportados**em operações dentro do mesmo Estado só será levado o conteúdo do grupo das TAGS transp se preenchido os campos C5\_TRANSP, C5\_TPFRETE e C5\_VEICULO.

* **Impressão no Danfe:**

A Placa que não for destacada no XML não será levado para o Danfe.

Caso seja uma solicitação da Sefaz do seu estado, poderá utilizar um padrão para gerar a mensagem em informações complementares, como exemplo ***C5\_MENNOTA.***

Obs: Como informado na validação abaixo a rejeição 868 pode ocorrer também em operações internas a critério da UF, em alguns caso em que a nota é emitida em **contingencia.**

* ***Validação da Sefaz:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16999047656599)

**Transmissão habilitada Contingência:**

**Caso ocorra a rejeição 868 ao emitir a nota em contingencia com tipo operação interna, deve gerar a nota sem o grupo transportador, veiculo transporte e reboque ou seja não preencha os campos C5\_TRANSP, C5\_TPFRETE e C5\_VEICULO.**

Caso seja necessário fazer um MDFe para essa nota, poderá incluir o veiculo e transportadora aos a autorização da nota pela rotina **Faturamento - Expedições**, selecione a nota e depois clique em **Manutenção**

![](https://totvssuporte.zendesk.com/attachments/token/gjZyjj7QW2RUILiwnOCLft4DP/?name=image.png)
