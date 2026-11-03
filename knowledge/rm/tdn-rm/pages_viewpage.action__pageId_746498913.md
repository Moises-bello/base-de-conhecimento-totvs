---
content_hash: 148cca3dda33df13d98cceaf99f3dfa8c24da3e0b8d664e35867e636111e1625
fetched_at: '2026-06-29T00:11:32.339835+00:00'
page_id: '746498913'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Relatórios - Vacância
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=746498913
version: 13
---

Este relatório está disponível a partir da versão **12.1.2306****,**utilizando a nova estrutura do **Smart View.**Para saber mais sobre o Smart View e como instalá-lo**, [clique aqui!](https://tdn.totvs.com.br/pages/viewpage.action?pageId=626926739)**

Um relatório de vacância de shopping é um documento que fornece uma visão geral das unidades de lojas vazias ou não ocupadas em um determinado shopping center. Este relatório é uma ferramenta essencial para os proprietários e gerentes de shopping centers, pois ajuda a identificar as áreas do shopping que precisam de mais atenção para atrair novos inquilinos e aumentar a receita. Em geral, o relatório de vacância de shopping é um recurso importante para avaliar o desempenho e as oportunidades de investimento em um shopping center.

Este relatório irá exibir por mês o percentual de vacância de cada shopping. Ele possui os seguintes filtros:

* Data início: a partir de qual competência será exibido os dados
* Data fim: até qual competência será exibido os dados
* Empreendimento: lista com os shoppings que serão retornados na análise (caso não esteja vinculado a visão de Empreendimentos)

Para os shoppings terem as suas vacâncias analisadas, o módulo de condomínio deverá estar integrado ao módulo de aluguel. O sistema irá percorrer todas as subunidades (lojas) do empreendimento (shopping) e analisar a sua integração com os imóveis (aluguel). Somente será considerado os imóveis com data de cadastro menor que a competência analisada.

Para determinar se um imóvel está ocupado ou não, o relatório analisa a existência do imóvel em algum contrato de locação na competência da análise.

Exemplo de como o relatório exibe as informações:

## **Como Acessar o Relatório**

---

Existem algumas formas de visualizar o relatório, dependendo de suas permissões e da configuração do sistema.

#### **Método 1: Acesso Direto (Requer Permissão)**

1. Navegue até o menu: `Shopping > Relatórios > SmartView`.
2. Selecione o relatório.

> **Nota:** O acesso a este menu é controlado por permissões. Caso a opção não esteja visível, por favor, contate o administrador do sistema para solicitar a liberação.

#### **Método 2: Acesso via Cadastro de Empreendimento**

1. Navegue até o menu: `Condomínio > Manutenção de Empreendimento > Empreendimento > Anexos > Relatórios`.
2. Selecione o relatório.

**O que fazer se o relatório não estiver listado?**

Caso o relatório não apareça nesta lista, você pode vinculá-lo manualmente seguindo os passos abaixo:

1. No Anexo Relatórios do empreendimento, clique no botão **"Inserir Relatório"**.
2. Siga as instruções do assistente de configuração (Wizard).
3. Na etapa **"Vínculo de Campos"**, configure o vínculo da seguinte forma:

   * **Nome do Campo:** `CODEMPREENDIMENTO`
   * **Valor:** `Empreendimento`
4. Conclua o assistente para salvar a configuração.
