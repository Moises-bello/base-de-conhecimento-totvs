---
content_hash: cb71bb9765be9fb6b4f4f712164d07073cbbc1d24bfa967bea27be22bb7d9503
fetched_at: '2026-06-29T00:11:13.122072+00:00'
page_id: '656326989'
product: rm
source: tdn-rm
title: Menu Gerencial
type: documentation
url: https://tdn.totvs.com/display/LRM/Menu+Gerencial
version: 12
---

#FF9000Gráficos

Neste menu são apresentados gráficos prontos com informações referentes a vendas, atendimento de clientes, estoque de unidades e conversão de vendas por tipo de mídia.

#FF9000Comissões

Aqui também encontra-se o menu de comissão onde será possível definir uma situação para a comissão de propostas vendidas. A finalidade desta tela é demonstrar ao corretor se uma determinada comissão já está disponível para ser faturada ou não.

As propostas que aparecerão neste menu devem ser parametrizadas através do menu *Backend > Globais > Situação de propostas.* As situações que tiverem a opção “Visível no menu corretor e comissão.

As propostas visíveis neste menu podem ter suas situações alteradas, manualmente, de acordo com a situação atual da comissão daquela proposta. Como padrão temos duas situações, sendo “Liberada ou Bloqueada”, mas estas situações podem ser substituídas ou mesmo acrescidas através do menu *Backend > Globais > Situação da proposta.*

Para se alterar a situação atual da comissão de uma proposta, basta no menu Gerencial > comissão, selecionar a situação desejada para aquela proposta na coluna NOVA SITUAÇÂO.

#FF9000Relatórios

É possível no Portal de Imóveis criar uma extração de dados das tabelas existentes no banco de dados. As opções para a visualização destes dados agrupados serão visíveis através deste menu *Gerencial > Relatórios.*

Para se criar estas visões é necessário ter noções da linguagem SQL para a criação dos scripts de extração dos dados. A criação dos relatórios deve ser feita através do menu *Backend > Relatórios*. Após acessá-lo podemos editar um relatório existente ou criar um novo.

Ao adicionar um novo relatório será solicitado o nome deste e o script em linguagem de programação SQL para a extração dos dados das tabelas do Portal de Imóveis. Para conhecer as tabelas existentes e os nomes dos campos para a construção do script SQL para a extração dos dados basta selecionar a opção “Visualizar tabelas”.

Atenção

A partir da versão 12.1.2402, o Portal de Imóveis passou a suportar bases de dados Oracle. Para garantir a compatibilidade e o correto funcionamento das consultas SQL, é necessário atentar-se a um detalhe importante relacionado ao uso de aliases.

**Orientações para Consulta:**

1. **Uso de Aliases:**

   * Ao utilizar aliases para colunas em suas consultas SQL, **certifique-se de que todos os aliases estejam em letras minúsculas**.
   * Esta prática é essencial para evitar possíveis conflitos e problemas de reconhecimento de colunas ao executar as consultas.
2. **Exemplo:**

   ```
   SELECT 
       nome          AS empreendimento,        
       data_entrega  AS entrega
   FROM 
       empreendimento
   ```

   * Certifique-se de que os aliases (`empreendimento` e `entrega`) estejam em minúsculas como demonstrado acima.
3. **Impacto:**

   * Consultas que não seguirem essa recomendação podem resultar em erros de execução ou retorno incorreto de dados.

Após criar o script SQL a próxima parte será definir parâmetros para o relatório e definir os nomes reais das colunas que serão apresentadas.

Após salvo o relatório, este será apresentando no menu *Gerenciais > Relatórios* e poderá ser selecionado para impressão.

O resultado do relatório pode ser impresso (abrirá uma nova aba no Browser com a visualização do relatório) ou baixado um arquivo CSV para abertura através do EXCEL.

### Inserindo relatórios do RM na visão gerencial dos relatórios

---

A partir da versão 12.1.2205, estamos disponibilizando também uma opção que permite selecionar um RM Reports para compor os relatórios gerenciais. Desta forma, serão apresentados os parâmetros deste relatório, possibilitando a confecção dos filtros da mesma forma que é realizado

Para usar um relatório do RM, basta seguir os passos abaixo:

Acessar *Backend > Relatórios*. e clicar em Adicionar.

Na tela de inclusão de relatórios, Dar um título para o relatório e clicar em RM Reports como mostra a figura abaixo.

Ao clicarmos em "selecionar" serão listados todos os relatórios do RM.

**Observação:** No intuito de facilitar e filtrar os relatórios importantes do RM para o Portal de Imóveis, existe um tipo específico para esses relatórios no RM, **1021 - Portal de Imóveis.**

A partir da versão 12.1.35, foi criado um filtro que permite filtrar por tipo de relatório como mostra a imagem abaixo:

Ao selecionarmos o relatório do RM, neste exemplo, utilizamos o relatório PortaldeImoveis\_Propostas. Este relatório já foi confeccionado no RM e irá trazer o parâmetro de ID da proposta, para que seja selecionado em sua execução.

É importante salientar que a consulta SQL atrelada à este relatório deve ter uma conexão direcionada externamente ao banco do Portal de Imóveis.

Para aprender como fazer isso, consulte a documentação aqui → [Configuração de Banco de Dados Externo](https://tdn.totvs.com/pages/viewpage.action?pageId=59900202)

Estando o nosso relatório parametrizado no RM, o Portal de Imóveis irá apresentar os parâmetros do mesmo, caso existam:

Neste caso foi definido no RM Reports o parâmetro de ID da proposta.

Este parâmetro não pode ser alterado diretamente no Portal de Imóveis. Para que novos parâmetros ou consultas sejam inseridas, deveremos criar na própria estrutura do RM Reports.

Para fins de exemplo, este relatório simples possui a consulta SQL abaixo: que listará as propostas de acordo com o ID:

sql

Para entender como são criados os reports dentro do RM, favor verificar o link abaixo:

[RM Reports](https://tdn.totvs.com/display/LRM/RM+Reports)

Estando o relatório parametrizado no RM e salvo no Portal de Imóveis, basta acessarmos o mesmo no menu *Frontend / Gerencial / Relatórios.*

Escolhemos no drop down o relatório e executamos de acordo com os parâmetros selecionados, clicando no botão "Imprimir".

O relatório será gerado numa nova guia. É importante desabilitar o bloqueio de pop-ups do navegador, para que a guia seja aberta corretamente.
