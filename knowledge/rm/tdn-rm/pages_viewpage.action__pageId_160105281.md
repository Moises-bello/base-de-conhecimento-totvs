---
content_hash: 43b471838fdbf80b5475dd505f15bf0d9b1639f7e78ff9fc338d16ece2ab5c02
fetched_at: '2026-06-29T00:05:56.941250+00:00'
page_id: '160105281'
product: rm
source: tdn-rm
title: Permissão aos menus do Gerador de Saídas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=160105281
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | Gerador de Saídas |
| **Subprocesso** | **:** | Permissão aos menus do Gerador de Saídas |
| **Data da publicação** | **:** | 04/09/2014 |

Para conceder permissão aos menus do Gerados de Saídas, acesse a MDI (RM.exe, localizado em C:\totvs\CorporeRM\RM.Net), com usuário **Supervisor** no sistema **G** (Serviços Globais, Integração e RM Inteligência de Negócios).

Para confirmar quais usuários possuem permissão ao codsistema G, segue abaixo exemplo de consulta sql para ser executada no banco de dados:

SELECT \* FROM GPERMIS  
WHERE SUPERVISOR = 1   
AND CODSISTEMA = 'G'  
AND CODCOLIGADA = 1

**Nota:** altere os parâmetros da consulta sql conforme desejado.

Selecione o contexto Serviços Globais:

Selecione o Menu "Perfis", na aba Segurança:

Conceda permissão para o Menu Gerador de Saída, no sistema Integração:

Associe o perfil liberado ao usuário que deseja conceder permissão ao Gerador de Saídas.

Atenção

Atenção,

Para **importar** um Layout de Gerador de Saídas é necessário possuir a permissão somente em **Importar Layout**, onde a permissão de Incluir não é necessária.

Para maiores informações:

Icon

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha);
