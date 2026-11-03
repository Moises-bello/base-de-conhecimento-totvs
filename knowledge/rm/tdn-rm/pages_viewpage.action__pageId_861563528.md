---
content_hash: c6c6f355ec4ecc3f42734d15950b5a7b751690d88b70453cc41bf8288f7760b9
fetched_at: '2026-06-29T00:11:55.467918+00:00'
page_id: '861563528'
product: rm
source: tdn-rm
title: Configurações para encontrar Local de Estoque ao criar uma requisição de paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=861563528
version: 6
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

PainelVisão Geral

## **01. VISÃO GERAL**

Esta documentação visa explicar como é pesquisado o valor default para o campo "Local de Estoque", ao criar uma requisição de paciente, via integração com PEP ou menu Movimentação de Estoque, conforme cada configuração do ambiente.

O usuário conectado deverá ter permissão de acesso ao local de estoque encontrado como default.

Esta permissão é configurada no menu “Ambiente / Parâmetros / Gestão Hospitalar/Estoque” nos itens “Local de Estoque – Permissão por Usuário” OU “Local de Estoque – Permissão por Perfil” (para versões a partir de 12.1.2406). E no menu “Parâmetros Gerais / Estoque” para versões anteriores.

Tabela onde fica gravado as permissões ao local de estoque, nos Parâmetros Gerais de Requisição: SZPARAMGERALREQUISICAO

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

### **Configurações de Ambiente – na ordem onde será pesquisado**

1 - Buscar Local de Estoque pelo Centro de Custo do Leito, quando paciente Interno e ocupa um Leito:

#### **1 - Buscar** **Local de Estoque pelo Centro de Custo do Leito, quando paciente Interno e ocupa um Leito:**

Ocorrerá se marcaro campo **“Busca local de estoque a partir do centro de custo do leito”** no menu “Ambiente / Parâmetros / Gestão Hospitalar” (para versões a partir de 12.1.2406). Ou no menu “Parâmetros Gerais / Estoque” para versões anteriores.

Primeiro buscará o centro de custo do leito e em seguida, pesquisará o local de estoque na unidade de atendimento que tenha este centro de custo.

SELECT SZUNIDATEND.CODLOC

WHERE SZUNIDATEND.CODCCUSTO = :**CODCCUSTO**

Exemplo: paciente no leito 101 unidade de atendimento 1. Irá buscar o local de estoque da unidade atendimento 2

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Unidade Atendimento | Local Estoque Unid.Atend | Centro Custo Unid. Atendimento | Leito | Centro Custo Leito |
| 1 | 01.001 | 140 | 101 | 142 |
| 2 | 01.002 | 142 | 102 | 150 |

2 - Buscar Local de Estoque pelos Parâmetros por Estação de Trabalho:

#### **2 - Buscar Local de Estoque pelos Parâmetros por Estação de Trabalho: tabela SZPARAMESTACAO**

Na aba “Estoque” o campo “Código local de Estoque”.

3 - Buscar Local de Estoque no Cadastro da Unidade de Atendimento do paciente:

#### **3 - Buscar Local de Estoque no Cadastro da Unidade de Atendimento do paciente: tabela SZUNIDATEND.**

Caso não esteja configurado o local de estoque em nenhum item acima, será utilizado o local de estoque da unidade de atendimento.

Atendimento Externo : buscará pela unidade de atendimento do paciente.

Atendimento Interno: buscará a unidade de atendimento do Leito do paciente, caso exista. Se não tiver preenchido no leito, então buscará a unidade de atendimento do paciente.

SELECT SZUNIDATEND.CODLOC

WHERE SZUNIDATEND.IDUNIDATEND = :**IDUNIDATEND\_ATUAL**

Use esse box para destacar informações relevantes e/ou de destaque.IMPORTANTE!

## **05. TABELAS UTILIZADAS**

Coloque o link das tabelas relacionadas
