---
article_id: 360055246873
category: Materiais - Compras (SIGACOM)
content_hash: b24a965eaec61c9b8734ce0c76a58a0d7b6e041201ed111765719afa23952816
fetched_at: '2026-06-28T22:41:19.925830+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Erro
  COM024 - (CT-e)
type: support-article
updated_at: '2024-05-27T18:13:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055246873-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Erro-COM024-CT-e
---

**Dúvida**

Como corrigir o erro COM024 no Importador de XML ou Totvs Colaboração  
  
**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

A partir do dia 22/11/2019, foi implementado o campo CKO\_MSGERR. Este campo será utilizado para armazenar detalhes específicos do erro.

**Implementação do Campo CKO\_MSGERR**

**Descrição do Campo:**

* **Nome do Campo:** CKO\_MSGERR
* **Tipo de Campo:** MEMO
* **Finalidade:** Armazenar detalhes do erro COM024 para facilitar o diagnóstico e a resolução de problemas.

**Criação do Campo no Configurador:**

Para criar o campo CKO\_MSGERR, siga as etapas abaixo:

a. Acesse o Configurador do Totvs Backoffice Protheus.

b. Navegue até o módulo SIGACOM e selecione a tabela correspondente onde o campo será adicionado.

c. Siga os passos para adicionar um novo campo:

* **Passo 1:** Clique em "Adicionar Campo".
* **Passo 2:** Preencha as propriedades do campo conforme indicado  
  **- Nome do Campo:** CKO\_MSGERR  
  **- Descrição:** Detalhes do Erro COM024  
  **- Tipo de Dados:** MEMO  
  **- Tamanho:** Deixe o padrão para tipo MEMO

d. Salve as alterações.

**Utilização do Campo:**

* Durante a execução das rotinas de importação de XML, qualquer ocorrência do erro COM024 será registrada no campo CKO\_MSGERR.
* O conteúdo do campo incluirá uma descrição detalhada do erro, permitindo uma análise mais precisa e rápida por parte da equipe técnica.

***Saiba Mais :***

[7179858 DMANMAT02-22747 DT Totvs Colaboração Importador XML gravar detalhe do erro COM024](https://tdn.totvs.com/pages/releaseview.action?pageId=521639797)

[Códigos de Erros Totvs Colaboração | Importador XML](https://tdn.totvs.com/pages/releaseview.action?pageId=271663193)

[MP - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
