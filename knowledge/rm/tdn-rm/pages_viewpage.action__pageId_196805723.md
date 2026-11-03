---
content_hash: 639eb88f8e5845239fb1fa6215515a5b2ba8d0b2d2fa84016c9a5276461a7fc8
fetched_at: '2026-06-29T00:06:00.393483+00:00'
page_id: '196805723'
product: rm
source: tdn-rm
title: ER_Inclusão_Tabela_TLOC_Filtro_Por_Perfil_E_Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=196805723
version: 4
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | PDR\_CP\_MOV006 | **IRM1** | PCREQ-6352 |
| **Requisito1** | PCREQ-6375 | **Subtarefa1** | PDR\_CP\_MOV006-842 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Permitir que o usuário defina Filtro por Perfil e Filtro por Usuário para a tabela de Local de Estoque.

### Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Filtro por Usuário | Inclusão | Serviços Globais\Segurança\Usuários\Anexos\Filtro por Usuário | - |
| Filtro por Perfil | Inclusão | Serviços Globais\Segurança\Perfis\Anexos\Filtro por Perfil | - |
| Local de Estoque | Envolvida | BackOffice\Gestão de Estoque, Compras e Faturamento\Cadastros\Locais de Estoque | - |

O Local de Estoque trata-se de uma entidade principal para o correto controle de estoque. É criado conforme local de armazenagem dos produtos nas filiais e tem a sua importância dentro do Gestão de Estoque, Compras e Faturamento, pois  todo o  saldo dos produtos estará vinculado à filial/local de estoque da empresa, permitindo assim a obtenção de informações por local de estoque ou consolidados.

Visando melhorar a segurança será permitido definir filtros por perfil e usuário para esta entidade. Ao definir um **Filtro por Usuário** ou **Filtro por Perfil**, quando o usuário acessar o cadastro de Local de Estoque e demais pontos do sistema que possuírem a informação de Local de Estoque, será respeitado os filtros definidos por usuário e/ou perfil.

**Exemplo**O usuário “José” possui um filtro associado para a tabela de Local de Estoque (TLOC), onde ele só pode ver os locais de estoque da Filial 1 (TLOC.CODFILIAL = 1). 

Ao entrar no cadastro de Local de Estoque e selecionar um filtro com todos os registros, serão trazidos somente os locais de estoque da Filial 1, ou seja, não serão apresentados os dados de nenhuma outra filial.

As condições dos filtros criados só poderão conter campos da tabela principal envolvida no processo, sendo assim ao incluir no cadastro de Movimento um novo registro, no campo local de estoque serão apresentados somente os locais de estoque da Filial 1. Se houver movimentos com locais de estoque de outras filiais, o usuário poderá visualizar, pois neste caso a tabela principal é a TMOV e o filtro deve ser feito considerando esta tabela.

Esta mesma regra é aplicada nos demais pontos do sistema, onde existir a informação de Local de Estoque.

**Tabelas Utilizadas**

* TLOC - Local de Estoque
* GFILTROUSUARIO - Filtro por Usuário
* GFILTROPERFIL - Filtros associados aos Perfis

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
