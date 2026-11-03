---
article_id: 360019924212
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: a4e939cc7483d4f6f91c288e1e31e111b9055a204b8e98433753db81efc31e4b
fetched_at: '2026-06-28T22:38:45.091147+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Tamanho da
  numeração de notas fiscais
type: support-article
updated_at: '2024-04-26T17:25:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019924212-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Tamanho-da-numera%C3%A7%C3%A3o-de-notas-fiscais
---

**Dúvida**

Preparação de nota fiscal com mais de 6 dígitos de numeração.  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões

**Solução**

É necessário possuir **6 ou 9 dígitos** para Emissão do Documento de saída. Este é um controle de Numeração do ERP Protheus.

A numeração oficial da NF é o número de retorno do SEFAZ após transmissão. Esses procedimentos atendem às legislações atuais que tratam emissão de nota.

O sistema somente trabalha a numeração interna do ERP com 6 ou 9 dígitos, conforme orientação de Ajuste SINIEF, desta forma, para as notas com 6 dígitos, complete com três vezes o '0' (na esquerda), o formato atual é 9 dígitos.

**Antes:** 009120 (6 dígitos)

**Depois:** 000009120 (9 dígitos)

Para realizar a **configuração** da **numeração de nota fiscal e série** é necessário acessar o **Módulo** **Configurador**e seguir o procedimento.

1 - Base de Dados -> Dicionário -> Bases de Dados -> Grupo de Campos -> Documento de entrada/saída

* Configure para Tamanho 9

**OBSERVAÇÃO:** Caso seja configurado dígitos diferentes de 6 ou 9, será apresentado invés da numeração, **'\*\*\*\*\*\*'**, simbolizando que deve ser corrigido a série para tamanho 6 ou 9.

2 - Verificar como está configurado o parâmetro: **MV\_TPNRNFS** = Define o tipo de controle da numeração dos Documentos de Saída

* Se = 1 - SX5
* Se = 2 - SXE/SX
* Se = 3 - SD9

3 - Ajustar na SX5:

 Base de Dados -> Dicionário -> Bases de Dados -> Tabelas Genéricas  -> Séries de N. Fiscais-> (editar) -> Itens -> Escolher a Série e  Informar nos campos Descrição / Desc Spanish/ Des English, a numeração de acordo com a quantidade de digito (tamanho) : Ex De: 6 - 000001 / Para: 9 - 000000001

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102465453)

Para os demais configurações do parâmetro consulte documentação completa sobre assunto a seguir.

**Saiba mais:**

**[Configuração de numeração de Notas Fiscais com mais de 6 dígitos](https://tdn.totvs.com/x/NIojDw)**
