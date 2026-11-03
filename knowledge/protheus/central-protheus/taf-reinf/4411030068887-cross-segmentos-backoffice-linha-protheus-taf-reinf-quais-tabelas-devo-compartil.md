---
article_id: 4411030068887
category: TAF - REINF
content_hash: 51f75455a8a5b23b0302a41312f2c1c89b9a18f0f488c92164773fd686e51aa2
fetched_at: '2026-06-28T22:41:33.400374+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: CROSS Segmentos -  Backoffice Linha Protheus - TAF - REINF - Quais tabelas
  devo compartilhar no TAF para geração da EFD Reinf?
type: support-article
updated_at: '2024-11-19T12:32:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411030068887-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-Quais-tabelas-devo-compartilhar-no-TAF-para-gera%C3%A7%C3%A3o-da-EFD-Reinf
---

**Dúvida**

Quais tabelas devo compartilhar no TAF para geração da EFD Reinf?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -TAF - Todas as versões  
  
**Solução**

Para realizar o compartilhamento das tabelas da empresa matriz é necessário compartilhar as tabelas utilizando o modulo Configurador através do menu Base de Dados → Dicionário → Base Dados, será apresentado uma uma lista de tabelas, clique em pesquisar (ícone de uma lista com uma lupa) e selecione a tabela a ser compartilhada, clique no botão Buscar e após o sistema posicionar na tabela clique no botão Editar ( ícone de uma lista com um lápis), será aberto uma tela com as propriedades da tabela, altere as propriedades Ac. Filial, Ac. Unidade para 1 - Compartilhado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411034014871)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411029920151)

Tabelas TAF relacionadas aos cadastros de geração da EFD Reinf:

**R-1000**

* C1E, C1F, CR9, CRM, CUW e CZR (O S-1000 deve ser compartilhado entre todas as Empresas, Unidades e Filiais, certifique-se que este compartilhamento esteja definido)**(TAFA050 - T001) - Complemento de Empresa**
* **Atenção:** caso o ambiente não possuir gestão de empresas, ou seja, se houver **2 ou mais grupos de empresas diferentes**, cada grupo precisa olha para a sua própria tabela, onde o **grupo 01** precisa ter a **C1E010** e o **grupo 02** a **C1E020**. Ou seja, **não deve ser compartilhada** a tabela de um grupo entre todos os grupos de empresa, pois pode ocasionar problemas nas rotinas no TAF.

**R-1070**

* C1G e T5L**(TAFA051 - T001AB) - Processo Referenciado**

**R-20XX (Todos os eventos apurados a partir de movimentos e cadastros)**

* C1H **(TAFA053 - T003) - Participantes**
* C1J **(TAFA055 - T005) - Unidade de Medida**
* C1L **(TAFA057 - T007) - Itens - Produtos/Serviços**
* C1O **(TAFA060 - T010) - Plano de Contas**
* C1P **(TAFA061 - T011) - Centro de Custo**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411034052631)**

**Informações adicionais:**

[TAF - REINF - Tabelas utilizadas na Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016286891-TAF-REINF-Tabelas-utilizadas-na-Reinf?source=search)

<https://tdn.totvs.com/display/public/TAF/TAF0160+Tabelas+para+compartilhamento+-+EFD+Reinf>
