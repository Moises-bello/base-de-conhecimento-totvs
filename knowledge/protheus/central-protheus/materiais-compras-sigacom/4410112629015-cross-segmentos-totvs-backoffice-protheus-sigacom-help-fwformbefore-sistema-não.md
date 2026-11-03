---
article_id: 4410112629015
category: Materiais - Compras (SIGACOM)
content_hash: b5d68f84e2edef8c25ecabbb08ed48fa225c1e31335e5e823f34bef8d78dc68a
fetched_at: '2026-06-28T22:41:18.918521+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP FWFORMBEFORE -
  Sistema não permite excluir comprador do Grupo de Compras.
type: support-article
updated_at: '2022-10-26T13:59:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410112629015-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-FWFORMBEFORE-Sistema-n%C3%A3o-permite-excluir-comprador-do-Grupo-de-Compras
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: 00:03:00 min**Ocorrência****Ao excluir um comprador no Grupo de Compras**, ocorre o HELP FWFORMBEFORE abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410112543639/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Todas as versões  
  
**Solução**

Para correção deste incidente, acesse a tabela **SX9** > Filtrar pelo campo **X9\_DOM = SAJ** > Deletar todos registros.

Este ajuste deletará o relacionamento da tabela (**X9\_DOM**) **SAJ**com as tabelas (**X9\_CDOM**) **SS4, SY1, SC1, SC8, SCY, SAI, SB1 e SC7**.Através deste ajuste, foi criado duas tratativas para o processo de exclusão, sendo:

1º) Exclusão do comprador dentro do cadastro do Grupo de Compras

Deverá permitir a exclusão, desde que, não seja deletado todos os compradores do Grupo. Deverá ter pelo menos um comprador no grupo de Compras.

2º) Exclusão do Grupo de Compras

Se o Grupo de Compras (o qual estará tentando excluir) tiver relacionamento com alguma das tabelas abaixo, o sistema não permitirá a exclusão. As tabelas passíveis de relacionamento são:

**SS4** → Descrição Genérica do Produto

**SY1** → Compradores

**SC1** → Solicitação de Compras

**SC8** → Cotação

**SCY** → Histórico Pedidos de Compras

**SAI** → Solicitantes

**SB1** → Produtos

**SC7**→ Pedido de Compra

**Mais informações:**

Este ajuste ocorreu para atender releases inferiores a 27. A partir desta release, o dicionário já será criado de forma correta!

**OBSERVAÇÃO**

Caso a mensagem seja exibida na **exclusão de um Aprovador do Grupo de Aprovações**, neste caso já é necessário verificar se esse grupo já foi processado pelo sistema.

A mensagem é exibida devido tentar excluir um cadastro, o qual já foi selecionado e utilizado no sistema, ou seja, o cadastro está vinculado em outra(s) Tabela(s), de modo que excluí-lo causaria uma quebra de integridade entre os dados das tabelas.

Exemplos: Tentar excluir um cadastro de Cliente que já fora vinculado em um Pedido de Vendas. Excluir um cadastro de Fornecedor que já fora vinculado em um Doc de Entrada. Excluir um Solicitante/ Comprador/ Aprovador/ Perfil de aprovação/ Grupo de aprovação que já fora vinculado em um Pedido ou Solicitação de Compras, Etc. Nestes casos, de fato, não é possível excluir o cadastro.

Veja todos os detalhes aqui: [Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Help FWFORMBEFORE - Problema: Violação de Integridade. Foi encontrada referência na tabela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7144060258711-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Help-FWFORMBEFORE-Problema-Viola%C3%A7%C3%A3o-de-Integridade-Foi-encontrada-refer%C3%AAncia-na-tabela?source=search)

O sistema apresenta o help , pois, há uma validação na tabela SX9 de relacionamentos do Protheus com os campos abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/0u9ZIUfUIar6UQpp1iE8HTIAa/?name=image.png)

O aprovador que está tentando excluir possui algum documento aprovado com esse grupo , por isso não é possível realizar a exclusão, de fato.

No cadastro do aprovador é possível consultar os documentos aprovados por esse aprovador desde que os campos Tip Aprov = Aprovador e limite Auto = sim no grupo de aprovação.

![](https://totvssuporte.zendesk.com/attachments/token/y316WpOV1eCPc4GFipoGfqket/?name=image.png)

Acesse Cadastro do Aprovador MATA095>selecione o aprovador >Outras ações>Consulta Saldo será demonstrado os documentos aprovados pelo aprovador.

![](https://totvssuporte.zendesk.com/attachments/token/mrfeHtSmhTXK9nvSHpFCfTruG/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/USnPykB9WjhOzxy9ARATWgvbJ/?name=image.png)

Uma outra forma de consultar é na tabela DBM

![](https://totvssuporte.zendesk.com/attachments/token/pfn9oXEp7nSDlvj1tgRBjogzb/?name=image.png)

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
