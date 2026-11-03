---
content_hash: 870deff10faf4695e73ed085b500abdb763b028ef603f7c0f7d3cb16c0a986b2
fetched_at: '2026-06-29T00:10:05.716231+00:00'
page_id: '452719298'
product: rm
source: tdn-rm
title: Organograma
type: documentation
url: https://tdn.totvs.com/display/LRM/Organograma
version: 2
---

**Organograma**   
O organograma é uma ferramenta para representar graficamente a estrutura hierárquica de uma organização. Diversas informações hierárquicas presentes nos cadastros do Gestão de Pessoas são utilizadas para gerar diferentes tipos de organogramas: por **Função**, por **Seção**, por **Seção x Função** e por **Chefes e Supervisores**.  
**Barra de Ferramentas**

1. **Seletor de Organograma**: Utilizado para selecionar o tipo do organograma.
2. **Imprimir**: Abre a tela de impressão do organograma.
3. **Exportar para Arquivo**: Abre a tela de exportação do organograma para arquivos de diversos formatos.
4. **Atualizar**: Recarrega completamente o organograma. Importante perceber que o organograma será remontado uma vez que essa opção for chamada, pode demorar dependendo do volume de dados mostrados pelo organograma.
5. **Expandir Todos os Nodos**: Ativa o modo de expansão completa do organograma. É importante notar que uma vez apertado sempre todos os organogramas serão exibidos completamente expandidos. Aperte o botão **Retrair Todos Os Nodos** para voltar para o comportamento padrão. Outro ponto importante a se notar que quanto maior o número de nodos a se mostrar o tempo de exibição pode aumentar drasticamente quando este botão for pressionado.
6. **Retrair Todos Os Nodos**: Ativa o comportamento padrão de mostrar todos os organogramas completamente retraídos. A exibição de um organograma com essa opção ativada é muito mais rápida.
7. **Zoom +:** Aumenta o zoom na tela do organograma (Dica: Utilize Ctrl mais a roda do mouse para dar zoom no organograma).
8. **Zoom -:** Diminui o zoom na tela do organograma (Dica: Utilize Ctrl mais a roda do mouse para dar zoom no organograma).
9. **Estrutura de Árvore:** Ativa o layout de árvore para o organograma.
10. **Estrutura em Cascata:** Ativa o layout em cascata para o organograma.
11. **Opções de Exibição:** Abre a tela de configuração da exibição dos nodos do organograma.
12. **Filtros Rápidos:** Opções de filtro prontos para o organograma.
13. **Filtros Avançado:** Abre a tela de filtros avançados do organograma.

**Organograma Por Função**  
Utiliza as informações de subordinação de funções presentes no respectivo cadastro. Ao cadastrar uma função acesse a aba "Funções Subordinadas" e preencha o campo "Chefia" para sinalizar a função que possui uma relação de chefia com a função sendo cadastrada.  
  
De acordo com o cadastro acima a **Função 00021** está subordinada a **Função 00003** e será mostrada no organograma da seguinte forma (em Vermelho):  
  
Uma característica importante da montagem do organograma por função é que é necessário que existam funções que não possuam chefes, funções que o campo chefia mostrado na primeira imagem não esteja preenchido, as chamadas Funções Raiz. Isso acontece, pois, o Organograma Por Função é montado a partir das raízes se movendo para os filhos recursivamente. Dessa forma, se uma função pai não estiver configurada para aparecer no organograma nenhuma de suas funções filhas também aparecerão.  
Outra característica é que todas as funções cadastradas sem chefes serão consideradas como Funções Raiz e aparecerão no primeiro nível da árvore do organograma. As Funções Raiz estão mostradas em destaque na imagem anterior (Azul).  
Os filtros rápidos do Organograma Por Função permitem configurar para mostrar os funcionários alocados em cada função (demitidos ou não) e mostrar as funções inativas:  
  
**Organograma por Seção**  
O Organograma por Seção apresenta a estrutura hierárquica de seções de acordo com a estrutura definida pelas quebras de seção. Para entender como funciona as quebras de seções favor verificar a documentação de seções do Folha de Pagamento.  
  
Os filtros rápidos do Organograma Por Seção permitem configurar para mostra os funcionários alocados em cada seção (demitidos ou não) e seções desativadas.  
  
**Organograma Por Seção x Função**  
O Organograma por Seção x Função apresenta a união das informações do Organograma Por Função e o Organograma Por Seção. Esse organograma é montado mostrando toda a hierarquia de seções e as funções dos funcionários alocados em cada seção.  
  
Os filtros rápidos do **Organograma Por Seção x Função** são os mesmos de ambos os **Organogramas Por Função** e **por Seção**.  
  
**Organograma Por Chefes e Supervisores**  
O Organograma Por Chefes e Supervisores mostra a hierarquia de chefes e supervisores da organização. As informações que são utilizadas para gerar dependem do tipo de gestão hierárquica configurada. Se configurada para utilizar a **Gestão Hierárquica por Seção** as informações utilizadas serão as mesmas da tela de Chefes e Supervisores. Se configura para utilizar a **Gestão Hierárquica por Posição** as informações utilizadas serão as mesmas da tela de Painel de Hierarquia.  
O organograma é montado mostrando todos os chefes e supervisores e a relação de chefia entre eles. A relação de chefia entre chefes é ligada diretamente a posição ou a seção que os chefes estão alocados. Essas relações podem ser verificadas e configuradas na tela de Chefes e Supervisores ou no Painel de Hierarquia.  
  
Os filtros rápidos deste organograma permitem mostrar os subordinados diretos de cada chefe (demitidos ou não).  
  
**Filtros Avançados**  
A tela de filtros avançados permite criar filtros clássicos do sistema RM para o organograma:  
  
Os filtros podem ser criados para Funcionários, Seção ou Funções. É importante destacar que os filtros são aplicados as consultas que retornam os dados do organograma e não ao organograma já montado. É importante destacar essa característica pois, por exemplo, no organograma de funções se uma função pai é filtrada nenhuma de suas filhas será adicionada já que as filhas só aparecem se as funções que são suas superiores são adicionadas.  
Essa tela permite criar e deletar os filtros e com cada mudança realizada o organograma será recarregado do servidor.

⚠️ **Ponto de Atenção:**  
Ao utilizar uma **base de dados parametrizada** para **[Hierarquia por Posição](https://tdn.totvs.com/pages/viewpage.action?pageId=655858368)**, a aplicação de **filtros avançados** afetará apenas os resultados nas hierarquiasde **[nível múltiplo](https://tdn.totvs.com/pages/viewpage.action?pageId=655446495)**.
