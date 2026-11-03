---
content_hash: 1a485ef169c73c6ba073fc990aa406045d59ef37944657a095b4d4541406afae
fetched_at: '2026-06-29T00:09:26.066161+00:00'
page_id: '423938242'
product: rm
source: tdn-rm
title: Razão Auxiliar Parametrizável para SPED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938242
version: 3
---

Na geração do SPED Contábil temos a forma de escrituração "Z- Razão Auxiliar" que pode ser gerada quando a empresa opta pela forma de escrituração "R - Diário com Escrituração Resumida", neste caso a escrituração "Z- Razão Auxiliar" será anexa a escrituração "R - Diário com Escrituração Resumida".  
   
O Razão Auxiliar é um relatório de layout aberto e não tem um padrão pré definido, por este motivo quando o mesmo foi implementado no módulo contábil foi proposta a sua criação no RM Gerador Delphi integrada a um processo que complementava a parametrização do relatório e que posteriormente seria enviado para o SPED Contábil.  
   
Devido à grande complexidade do processo no RM Gerador, foi implementada a parametrização do relatório dentro do próprio cadastro da escrituração contábil afim de simplificar a utilização/geração do Relatório Razão Auxiliar que será entregue ao SPED Contábil através dos registros I500/I510/I550/I555 mantendo a flexibilidade na estruturação e composição do relatório.  
   
**PARAMETRIZAÇÃO DO RELATÓRIO**  
• Origem das informações do relatório: O relatório poderá ser parametrizado baseado nas informações dos Lançamentos Contábeis, através de uma consulta SQL customizada pelo usuário e por meio do RAS (Razão Auxiliar de Subconta).  
   
- Lançamentos Contábeis: Ao selecionar essa opção, o sistema habilita os campos disponíveis para serem utilizados na   estrutura do relatório. Cabe ao usuário parametrizar os campos que serão utilizados. É possível adicionar e remover qualquer campo disponível respeitando sempre a quantidade de caracteres. Existe a possibilidade de parametrização "Padrão", onde é criada uma parametrização padrão automaticamente para o relatório;   
- Consulta SQL Customizada: O relatório será baseado na consulta SQL criada pelo o usuário. A partir dos campos disponíveis (que serão carregados conforme o SQL) o usuário deverá selecionar os campos que irão compor o relatório;

* RAS (Razão Auxiliar de Subconta): As informações para composição do relatório serão buscadas nos Lançamentos de Detalhamento do RAS. Mais informações referente ao RAS  
     
  • Filtro complementar: Disponível apenas para opção "Lançamentos Contábeis".  Será disponibilizado um filtro complementar que poderá ser usado pelo usuário, caso queira restringir os dados que serão processados.  
     
  • Campos do Relatório Razão: São os campos que foram selecionados para serem apresentados no relatório. Tais informações como nome do campo (no caso de consulta SQL), descrição, tipo e tamanho da coluna podem ser editados conforme necessidade do usuário.  
     
  • Totalizar Campos: Neste campo o usuário seleciona a partir dos campos que irão compor o relatório qual campo deverá ser totalizado no relatório.  
     
  Exemplo: Para o relatório padrão o sistema selecionará automaticamente os campos "Valor Débito" e "Valor Crédito" e neste caso durante a geração deste relatório o sistema vai somar estes valores conforme os agrupadores dos totalizadores.  
     
  • Campos Agrupadores dos totalizadores: Neste campo o usuário seleciona a partir dos campos que irão compor o relatório qual campo será o agrupador dos totalizadores.  
     
  Exemplo: Para o relatório padrão o sistema selecionará automaticamente o campo "Conta Contábil", neste caso durante o processamento do relatório o sistema vai totalizar os valores dos campos definidos em "Totalizar Campo(s)" por Conta Contábil.  
     
  • Importar parametrização de outra escrituração: Através deste botão é possível parametrizar o relatório conforme a parametrização de uma outra escrituração já cadastrada.  
     
  **GERAÇÃO DO RAZÃO AUXILIAR**  
  A geração é realizada dentro dos processos da própria escrituração contábil.  
     
  • Tipo Saída: No momento da geração do relatório é possível escolher entre dois tipos de saída: Visualizar relatório e Arquivo.  
  - Visualizar relatório: Será mostrado um Preview do relatório conforme o layout de parametrização criado;  
  - Arquivo: O relatório será gerado em um arquivo, já no padrão do layout do SPED Contábil. Este arquivo deverá ser informado em uma das etapas durante o processo de geração do arquivo do SPED Contábil.  
     
  • Selecionar Coligada/Filial: Identifica as Filiais que serão consideradas durante o processamento do relatório, se não for informada nenhum filtro serão consideradas todas as Filiais.  
     
  **OBSERVAÇÕES**  
  • Será gerado o detalhamento apenas para as conta contábeis que estiverem cadastradas na aba "Contas que recebem lançamentos globais". Lembrando que ser for definido uma conta sintética o sistema vai considerar todas as contas analíticas filhas;  
  • O processamento deste relatório será baseado nos dados desagrupados, ou seja, quando o lançamento contábil estiver agrupado o sistema deve gerar as informações neste relatório de forma desagrupada;  
  • As informações apresentadas no relatório serão baseadas no período identificado no cadastro da escrituração contábil correspondente;  
  • Quando a origem do relatório é "Consulta SQL Customizada" algumas informações serão de responsabilidade do usuário identificar na consulta SQL, tais como: - Contas Contábeis - Período Desta forma para esta opção o sistema não vai considerar as datas e nem as contas identificadas no cadastro da escrituração contábil.
