---
article_id: 29805178646807
category: Gestão de Transportes (TMS)
content_hash: 3e51e70f6c774d82a7a755137ae56d00dee1c94e7536cde28c902ddaa8bc16a7
fetched_at: '2026-06-28T22:45:33.471697+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Valor Informado para Frete a Pagar
type: support-article
updated_at: '2025-02-07T16:39:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29805178646807-Log%C3%ADstica-Linha-Protheus-TMS-Valor-Informado-para-Frete-a-Pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29805130218775) Tempo aproximado para leitura: **00:02:10 min** **Dúvida**Como utilizar o componente de frete do tipo **61 - Valor Informado** no frete a pagar no **TOTVS Logística TMS**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O componente de frete do tipo **61 - Valor Informado** é utilizado para serviços com valor unitário fixo, como ajudantes, diárias, taxas ou qualquer outro item definido pelo cliente. Por exemplo, se um ajudante ou qualquer outro item, custar R$ 200 e há três ajudantes na viagem, então, o Sistema multiplicará a quantidade deste item pelo valor unitário deste componente configurado na **Tabela de Frete a Pagar.**  
Este é o conceito de uso do **Valor Informado**, mas, caso o cliente deseje informar o valor de frete a pagar fechado por viagem, independentemente de quantidade de ajudantes, diárias, taxas, etc, então, deve-se utilizar o conceito de **Frete Informado** conforme detalhes no **Saiba Mais**.   
  
Para utilizar o componente **61 - Valor Informado** para frete a pagar, é necessário:   
  
Cadastrar o componente de frete do tipo **61 - Valor informado** na rotina **TMSA030 - Componentes de Frete**:

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29825759309847)

Vincule o componente cadastrado na tabela de frete a pagar em **TMSA130 - Configuração da tabela de frete**:

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29825735126807)

Configure o valor a calcular do componente em **TMSA790 - Tabela de frete a pagar**:

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29825735128855)

Vincule a tabela de frete ao contrato do fornecedor em **TMSA800 - Contrato do fornecedor**:

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29825735129751)

Com os cadastros efetuados, basta preencher o valor informado na viagem.

* Se utilizar **viagem modelo 2**, informe a quantidade de Valor Informado no complemento da viagem, em **Outras Ações/ Val.Inf.** :

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29825759317527)

* Se utiliza **viagem modelo 3**, informe a quantidade de Valor Informado acessando a aba **Recursos/Valor Inf.**:

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29825759318807)

Após gerar a viagem, quando for gerar o contrato de carreteiro em **TMSA250 - Contrato de carreteiro**, o valor informado será calculado no contrato e destacado nos componentes do contrato de carreteiro gerado:

![7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29825736554519)

**Saiba mais**[Logística - Linha Protheus - TMS - Frete Informado para Frete a Pagar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29808346366103-Log%C3%ADstica-Linha-Protheus-TMS-Frete-Informado-para-Frete-a-Pagar)Tabela de Frete a Pagar: [Tabela de Frete a Pagar (TMSA790 - SIGATMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=542152688)
