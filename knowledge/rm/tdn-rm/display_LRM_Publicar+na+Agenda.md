---
content_hash: c82df37db4f6c05153b819a5cd1b4a23a203fb23af5534ed3329ff7c24ade6fa
fetched_at: '2026-06-29T00:08:58.051402+00:00'
page_id: '359466137'
product: rm
source: tdn-rm
title: Publicar na Agenda
type: documentation
url: https://tdn.totvs.com/display/LRM/Publicar+na+Agenda
version: 6
---

Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão do que é e como funciona a funcionalidade "Publicar na Agenda".

# Introdução:

---

       O assistente de publicação de dados na agenda é utilizado para ajudar o usuário a publicar os dados da visão na agenda de compromissos, respeitando as permissões e filtro utilizado na visão. Essa funcionalidade está disponível na opção de "Exportar dados da visão".

falseObservação:

A funcionalidade de "Publicar na Agenda" estará disponível somente se houver um campo "Data" na visão.

# Passo a Passo:

---

 Segue abaixo o passo a passo da execução de um exemplo (Visão de lançamentos):

falseInstalação em N camadas (App Server)1º Passo:

Acesse a visão de Lançamentos e crie um filtro qualquer (é necessário que o filtro retorne um registro).

Como exemplo foi criado um filtro que referencia o laçamento 6750

|  |
| --- |

2º Passo:

Após a criação do filtro, acesse "Exportar dados da visão | Publicar na Agenda".

3º Passo:

Em seguida será aberto um "Assistente de Publicação de Dados", como mostra a imagem abaixo:

|  |
| --- |

4º Passo:

Ao clicar em "Avançar", será solicitado ao usuário a seleção da coluna de "Data" que determinará a data e horário do compromisso. Imagem demonstrativa:

|  |
| --- |

5º Passo:

Ao avançar novamente o processo, na tela de "Detalhes da Fonte de Dados" defina:

* Uma descrição para a fonte de dados
* A cor da fonte de dados
* A descrição do compromisso

|  |
| --- |

Em seguida clique em avançar e execute o processo.

6º Passo:

Finalizado a execução do processo, é necessário acessar os menus "Gestão | Agenda". Ao ser aberta a visão, selecione a fonte de dados criada anteriormente (Data de Previsão de Baixa - Lançamento 6750), agrupe o compromisso por data ou fonte e clique em "Atualizar". Os dados da visão devem ser gravados na agenda de compromissos, trazendo corretamente os parâmetros passados na tela de "Detalhes da Fonte de Dados" (4º Passo). Imagem demostrativa abaixo:

|  |
| --- |

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Publicar na Agenda

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
