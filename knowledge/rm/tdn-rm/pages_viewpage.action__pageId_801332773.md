---
content_hash: fe913b1387c494cd1dc8fbf2e3d42b935de1419db89639175a312b66d35d04b8
fetched_at: '2026-06-29T00:11:43.056898+00:00'
page_id: '801332773'
product: rm
source: tdn-rm
title: Cadastro de Diagnóstico de Enfermagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=801332773
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Permissões de acesso (Perfil do usuário)**
   1. **Inserir**
   2. **Excluir**
   3. **Editar**
3. **Cadastro de Diagnóstico de Enfermagem**
   1. **Versão/Edição**
   2. **Domínio**
   3. **Classe**
   4. **Diagnóstico**
   5. **Informações relacionadas ao diagnóstico**
      1. **Características**
      2. **Fatores de Risco**
      3. **Populações em Risco**
      4. **Condições Associadas**
      5. **Fatores Relacionados**
4. **Detalhes Técnicos**
   1. **Tabelas envolvidas**
   2. **Importação de dados**

Cadastro de Diagnóstico de EnfermagemVisão Geral

## **01. VISÃO GERAL**

Permite realizar o cadastro dos diagnósticos de enfermagem de acordo com a sua classe e domínio, agrupando-os através de diferentes versões/edições.

Permissões de acesso (Perfil do usuário)

## **02. PERMISSÕES DE ACESSO (PERFIL DO USUÁRIO)**

As permissões de acesso para o cadastro de diagnóstico de enfermagem fica localizada em: Hospitais e Clínicas / Cadastros / Cuidados com o Paciente / Processo de Enfermagem / **Cadastro de Diagnóstico de Enfermagem**:

1. **Inserir**: permite a inserção de novos registros.
2. **Excluir**: permite a exclusão de registros já existentes.
3. **Editar**: permite a edição de registros já existentes.
4. **IMPORTANTE:** para permitir apenas a **visualização** dos registros, basta habilitar apenas a permissão para o **Cadastro de Diagnóstico de Enfermagem**.
Cadastro de Diagnóstico de Enfermagem

## **03. CADASTRO DE DIAGNÓSTICO DE ENFERMAGEM**

O menu para acesso ao cadastro de diagnóstico de enfermagem fica localizado em: Cadastros / Cuidados com o Paciente / Processo de Enfermagem / **Cadastro de Diagnóstico de Enfermagem.**

O diagnóstico de enfermagem é agrupado através da versão/edição da publicação, e encontra-se dividido de acordo com a sua classe e domínio. Dessa forma, para se cadastrar um diagnóstico, é necessário primeiro cadastrar uma versão, e então o domínio e a classe a qual esse diagnóstico pertence.

1. **Versão/Edição**:
2. **Domínio**,cadastro anexado à Versão/Edição:
3. **Classe**,cadastro anexado ao Domínio:
4. **Diagnóstico**,cadastro anexado à Classe:
5. **Informações relacionadas ao diagnóstico (Características, Fatores de Risco, Populações em Risco, Condições Associadas, Fatores Relacionados)**,cadastros anexados ao Diagnóstico:
Detalhes Técnicos

## **04. DETALHES TÉCNICOS**

**a. Tabelas envolvidas**:

* + SZCADDIAGENFVERSAO (Versão/Edição)
  + SZCADDIAGENFDOMINIO (Domínio)
  + SZCADDIAGENFCLASSE (Classe)
  + SZCADDIAGENFDIAGNOSTICO (Diagnóstico)
  + SZCADDIAGENFCARACTERISTICA (Características)
  + SZCADDIAGENFFATORRISCO (Fatores de risco)
  + SZCADDIAGENFFATORRELACIONADO (Fatores relacionados)
  + SZCADDIAGENFPOPULACAORISCO (Populações em risco)
  + SZCADDIAGENFCONDICAOASSOCIADA (Condições associadas)

**b. Importação de dados:**

* + Foi realizado a importação direta da versão **12 Edição dos Diagnósticos de Enfermagem (2021 - 2023)** para que já exista um cadastro padrão.
