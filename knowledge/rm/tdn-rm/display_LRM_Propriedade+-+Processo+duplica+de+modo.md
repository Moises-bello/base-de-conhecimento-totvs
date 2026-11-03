---
content_hash: 6363e728223bd85439ee10c2320d11b24d96ebad409a16c9f0ea5b9ee884e5ce
fetched_at: '2026-06-29T00:09:45.904295+00:00'
page_id: '435100055'
product: rm
source: tdn-rm
title: Propriedade - Processo duplica de modo
type: documentation
url: https://tdn.totvs.com/display/LRM/Propriedade+-+Processo+duplica+de+modo
version: 32
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      Este tutorial descreve o comportamento da propriedade “Processo duplica de modo” existente para o Controle Tabela.

# Propriedade "Processo duplica de modo":

---

      Para exemplificarmos o resultado das opções dessa propriedade, utilizaremos o seguinte relatório:

falseComo Criar1ª - Acessando a propriedade

      Para uso desta propriedade, é necessário selecionar no controle Tabela qual a célula que receberá as definições.

      Selecionada a célula, tecle F4 para acessar a Grade de Propriedades do controle.

2ª - Valor: "Deixar"

      O valor “*Deixar*” é o default da propriedade. Este valor não acarretará alterações nas células exibidas no relatório.

3ª - Valor: "Mesclar"

      Quando atribuído “*Mesclar*”, sempre que o registro repetir, em sequência, seu valor, as células serão mescladas.

false

Em versões que ***antecedem a 12.1.19***, quando utilizado o valor “*Mesclar*”, algumas células poderão gerar seu valor em branco após células mescladas. Esta situação é decorrente da versão da ***DevExpress*** (*componente de terceiros*) utilizada nas versões abaixo da mencionada. Nas versões acima este empecilho não mais ocorrerá, pois fazemos uso de uma versão mais recente da ***DevExpress***.

Para solucionar esta situação são necessárias duas alterações em seu relatório.

1ª – Selecione o controle tabela e tecle F4 para acessar suas propriedades. Altere o valor da propriedade “*Comportamento | Ancorar*” para “*Ambos*”.

2ª - Essa alteração impedirá que as células expandam e apresentem todo o conteúdo da célula. Necessário então, aumentar a altura do grupo para que comporte as informações.

4ª - Valor: "Suprimir" e "Suprimir e Encolher"

      Quando atribuído o valor “*Suprimir*” ou "*Suprimir e Encolher*" a célula que repetir o valor da célula anterior/acima será removida.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Propriedade Processo Duplica de Modo

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
