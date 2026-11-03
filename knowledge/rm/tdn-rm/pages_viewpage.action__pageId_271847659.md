---
content_hash: 4334f8296e8cac658912d10c354553269273659c5baae0f28fac00e607cf4df3
fetched_at: '2026-06-29T00:08:28.737988+00:00'
page_id: '271847659'
product: rm
source: tdn-rm
title: Configuração de Gráfico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271847659
version: 23
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      O objetivo deste documento é auxiliar usuários na configuração de um Gráfico utilizando como fonte de dados uma consulta SQL. É através do Assistente de Configuração que configura-se títulos, cores, tipo, legendas e textos em um gráfico.

Recomendamos que ao criar novos Gráficos utilize o tipo '**Drill Down**' e não o '**Padrão**'.

O tipo 'Padrão' é mantido no RM apenas para manter compatibilidade com sistemas legados. Com o gráfico 'Drill Down' é possível criar gráficos de várias formas e com mais opções de customização. O Drill Down é indicado mesmo para criação de gráficos simples, por isso o exemplo deste documento é baseado em gráfico Dril Down.

# Como Configurar:

---

      Selecione o gráfico desejado e acesse o menu *Processos > Assistente de Configuração de Gráfico.*

      O Assistente de Configuração apresenta opções de **Construção** e de **Apresentação**.

      Veja a seguir um exemplo de criação de Gráfico em Barra:

false

**CONFIGURAÇÕES DE CONSTRUÇÃO**

Assistente de ConfiguraçãoCenárioCenárioCenário

**Exemplo:**

O objetivo deste exemplo é criar um gráfico de barras que exiba as sete seções com menor custo de salários. Para isso, utilizaremos uma Consulta SQL na tabela PFUNC que retornará os seguintes dados:

Esses dados devem ser representados em um gráfico de Barra.

Tipo de GráficoTipo de GráficoTipo de Gráfico

**Tipo de Gráfico**

Nessa tela deve ser selecionado qual o tipo de gráfico será construído. Selecione o tipo **Barra** e clique em **Próximo**.

AparênciaAparênciaAparência

**Aparência**

Customize a paleta de cores e selecione um estilo para o seu gráfico.

Para visualizar o resultado de uma alteração feita nas configurações de um gráfico, basta acessar novamente a opção **Aparência**.

SériesSériesSéries

**Séries**

O sistema cria automaticamente algumas séries. Neste exemplo, utilizaremos apenas uma série. Por isso, selecione a **Séries2** e clique em **Remover**.

No canto lateral da direita existem outras opções para customização da série. Por enquanto, neste exemplo, não faremos alterações nela.

O nome da série será exibido na legenda do gráfico. Basta alterar o nome 'Séries1' para Salário.

DadosDadosDados

**Dados**

Essa tela possui três abas de configuração: **Pontos**, **Binding de Séries** e **Série auto-criada**.

Na aba Binding de Séries faremos a seguinte configuração:

Após configurar a **Propriedade do Agrupamento** e a **Propriedade do Valor,** acesse a aba **Pontos** e visualize os dados que serão utilizados na representação do gráfico:

---

****CONFIGURAÇÕES DE APRESENTAÇÃO****

ApresentaçãoGráficoGráficoGráfico

**Gráfico**

Configure a aparência do gráfico, como cor de fundo, estilo de preenchimento, imagem de fundo, bordas, entre outros. Utilize também as abas apresentadas no canto direito da tela.

DiagramaDiagramaDiagrama

**Diagrama**

Comoestamos construindo um gráfico de Barras, podemos inverter os eixos; para isso, marque a opção **Inverter** presente na tela.

PainéisPainéisPainéis

**Painéis**

Configure a aparência do painel do gráfico, que é a área destacada em vermelho na imagem abaixo. Pode-se alterar cores, sombra, bordas, entre outros.

EixosEixosEixos

**Eixos**

Por padrão o sistema gera uma escala automaticamente para os eixos. Para alterá-la, assim como customizar aparência, elementos, rótulos, entre outros, utilize as abas do canto direito da tela.

SériesSériesSéries

**Séries**

Para gráficos que possuem mais de uma série, é possível customizar sua aparência, bordas, sombras e indicadores. Essas configurações não serão alteradas neste exemplo.

Rótulo de PontoRótulo de PontoRótulo de Ponto

**Rótulo de Ponto**

Para exibir os rótulos no gráfico, que estão indicados em vermelho na imagem abaixo, marque a opção **Visível.** A partir de então será possível customizar cores, conteúdo a ser exibido no rótulo, linhas, aparência, sombra, entre outros.

Para configurar o conteúdo a ser exibido no rótulo, acesse a aba **Opções de Ponto.**

Títulos de GráficoTítulos de GráficoTítulos de Gráfico

**Títulos de Gráfico**

Para colocar títulos no gráfico, clique em **Adicionar,** informe o título e faça a configuração de posição, aparência, fonte, cor, tamanho, entre outros, através da aba **Geral**.

LegendaLegendaLegenda

**Legenda**

A legenda pode ser ocultada, customizada em cores, aparência, bordas, sombras, entre outros.

AnotaçãoAnotaçãoAnotação

**Anotação**

É possível adicionar anotações no gráfico, como no exemplo abaixo. Podem ser adicionadas imagens também.

Para customizar as anotações basta navegar entre as abas apresentadas no canto direito da tela.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.44 ou Superiores

false

**Processo:** Criação de Gráfico do tipo 'Drill Down'

falsefalse

**Status:** Finalizado

false

**Data:** 22/02/2017

false

**Autores:**
