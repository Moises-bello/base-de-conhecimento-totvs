---
article_id: 41488864919959
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: ab95ba61d0bd1c6ae932df9e623d80be263c5b6e40603ed6ade95df87c1aa552
fetched_at: '2026-06-28T22:39:09.775162+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Microsiga Protheus) - SIGAEST - Cadastro
  de Características de Produtos ESTA012
type: support-article
updated_at: '2026-06-25T18:06:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41488864919959-Cross-Segmento-TOTVS-Backoffice-Linha-Microsiga-Protheus-SIGAEST-Cadastro-de-Caracter%C3%ADsticas-de-Produtos-ESTA012
---

O cadastro de Características de Produto (ESTA012) no TOTVS Backoffice SIGAEST permite centralizar e padronizar atributos como cor e tamanho, otimizando buscas. Controlado pelas tabelas D4V (configurações gerais) e D4W (itens/valores), o cadastro exige definir nome, tipo (lista, consulta, livre, número), tipo de seleção (única ou múltipla) e seção para organização visual, garantindo integridade e flexibilidade no gerenciamento do catálogo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41488864909079) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**   
Como realizar o cadastro, a parametrização e a padronização de características de produtos através da rotina ESTA012? 

**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Microsiga Protheus) - SIGAEST - A partir da versão 12.1.2510 

**Solução**   
O cadastro de **Características de Produto (ESTA012)** centraliza e padroniza as classificações dos itens no sistema, assegurando a integridade e a flexibilidade no gerenciamento do catálogo. Por meio desta funcionalidade, as propriedades dos produtos (como cor, voltagem, material e tamanho) tornam-se atributos estruturados que otimizam os filtros de pesquisa e a busca avançada no dia a dia operacional.

A gestão dessas características é controlada internamente por duas tabelas principais do sistema:

* **D4V**: Armazena o cabeçalho e as configurações gerais da característica de produto.
* **D4W**: Armazena os itens e valores predefinidos da lista de opções da característica.

**Passos**

Para cadastrar uma nova característica de produto, siga o procedimento abaixo:

1. Acesse o módulo **Estoque e Custos (SIGAEST)**.
2. Siga o caminho de menu: **Atualizações** -> **Cadastros** -> **Produtos** -> **Características de Produto**.
3. Clique na opção **Incluir**. O sistema abrirá a tela "Características de Produto - Incluir".
4. No campo **Nome** (D4V\_NOME), insira a descrição da característica. Este campo é obrigatório, único e não aceita duplicidades ou variações em plural/singular (ex: Cor/Cores).
5. No campo **Tipo** (D4V\_TIPO), defina a modalidade de preenchimento do dado:

* **Lista de opções**: Para criar um grupo fechado de opções (ex: Branco, Preto, Azul). É obrigatório incluir pelo menos um item/valor válido nesta lista.
* **Consulta Padrão**: Para vincular uma consulta de sistema (SXB) existente (ex: Consulta SA2 de Fornecedores). O preenchimento da consulta correspondente é obrigatório.
* **Livre**: Permite a digitação de texto aberto pelo usuário. *(Nota: Recomenda-se evitar o uso excessivo para manter a eficiência dos filtros de pesquisa)*.
* **Número**: Destinado a valores puramente numéricos (ex: Espessura, dimensões).

6. No campo **Tipo de Seleção** (D4V\_TPSEL), informe se a aplicação do atributo aceitará seleção **Única** ou **Múltipla**. A opção "Múltipla" permite vincular mais de um valor ao mesmo produto e só estará disponível para os tipos "Lista de opções" ou "Consulta Padrão".
7. No campo **Seção** (D4V\_SECAO), selecione o agrupador visual e lógico para organizar a exibição na tela. O sistema disponibiliza seções padrão como Comerciais, Logísticos, Fiscais/Financeiros, E-commerce, Aplicações e Técnicos (customizáveis via Configurador).
8. Confirme as informações preenchidas para salvar o registro no banco de dados.

**Saiba Mais**

[Cadastro de características de produtos (ESTA012 - SIGAEST)](https://tdn.totvs.com/x/HuxqP)
