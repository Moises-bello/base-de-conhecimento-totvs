---
content_hash: 8efc227c7f9e1bf8207cef88024a7ca47becc60872182a0897be07541529f4af
fetched_at: '2026-06-29T00:05:53.202480+00:00'
page_id: '1068198815'
product: rm
source: tdn-rm
title: 'Perspectiva de códigos de tributação: Incidência ou Emitente'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1068198815
version: 8
---

# Conteúdo

1Conteúdononenone

# 1. Sobre

Esta atualização permite parametrizar qual perspectiva deve ser utilizada para preenchimento das tags referentes ao código de serviço municipal e ao código de serviço federal.

# 2. Versões para atualização

A solução está disponível a partir dos patches:

Data: 

Biblioteca RM

* 12.1.2506.317
* 12.1.2510.244
* 12.1.2602.157

# 3. Detalhe da Alteração

Criado o parâmetro: Códigos de trib. pelo Mun. Emitente, em: anexos - Dados Fiscais Município, no cadastro de municípios. Também foram criados os campos referentes as perspectivas Incidência e Emitente, em: anexos - Tributos do Produto por Município , no cadastro do serviço.

Exemplo preenchimento Parametro

Ao marcar o parâmetro nos dados fiscais do município, será considerado os códigos de tributação municipal e federal, na perspectiva Emitente. Neste cenário, os campos do xml serão sempre gerados considerando o município da filial emitente e buscando o código do campo referente a perspectiva do emitente.

Exemplo preenchimento dos campos

Ao desmarcar o parâmetro nos dados fiscais do município, será considerado os códigos de tributação municipal e federal, na perspectiva Incidência. Neste cenário, os campos do xml serão gerados considerando o município de incidência, preenchido no Movimento, e o xml irá considerar os campos referente a incidência

Exemplo preenchimento dos camposComportamento Padrão

O parâmetro Códigos de trib. pelo Mun. Emitente por default fica desmarcado, ou seja, gera os campos no xml a partir da perspectiva da incidência do ISS.

# 4. Layouts de NFS-e afetados

Layout TSS:

Layout TPF:

Layout NFS-e Nacional:
