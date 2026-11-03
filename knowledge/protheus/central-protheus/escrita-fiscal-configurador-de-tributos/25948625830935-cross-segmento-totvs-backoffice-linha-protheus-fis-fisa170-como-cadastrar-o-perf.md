---
article_id: 25948625830935
category: Escrita Fiscal - Configurador de Tributos
content_hash: 8269748df9105873807f30da56dd627fce55396ff9cdbf930bf764869dc78947
fetched_at: '2026-06-28T22:39:17.292955+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como cadastrar
  o perfil de participante ou dar Manutenção?
type: support-article
updated_at: '2024-11-22T19:26:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25948625830935-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-cadastrar-o-perfil-de-participante-ou-dar-Manuten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25948596055447) Tempo aproximado para leitura: 03:00**min** **Dúvida**Como cadastrar o perfil de participante?  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**Ao fazer o cadastro de Participantes temos a opção de escolher fornecedores ou clientes, onde podemos:

1a) Incluir de forma manual ,selecionando cada participante no SA1 ( cadastro de clientes ) ou SA2 ( cadastro de Fornecedores )

2a) Podemos  usar a opção TODOS para clientes e fornecedores

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25948625806487)

3a) podemos usar Facilitador

2.2.7.1[Facilitador do cadastro de perfi](https://tdn.totvs.com.br/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10#CFGTRIBConfiguradordeTributos12.1.22.10-Facilitadordocadastrodeperfil)

<https://tdn.totvs.com.br/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10#CFGTRIBConfiguradordeTributos12.1.22.10-CadastrodePerfilTribut%C3%A1riodeParticipante>

4a) Usar o parâmetro **MV\_FACAUTO = .T.**

O sistema vai perguntar se quer a inclusão do cadastro na regra existente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28002198557463)

Sendo demonstrado para cadastro de clientes , fornecedores e produtos

5a) Podemos usar  a rotina  FISA164 -  ExecAuto (execução automática)

<https://tdn.totvs.com/pages/releaseview.action?pageId=788607214>
