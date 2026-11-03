---
content_hash: 6e84bdffd6bd098ad1dc8779fda538494258615a954631476daf30c45507baf7
fetched_at: '2026-06-29T00:10:07.750774+00:00'
page_id: '452719428'
product: rm
source: tdn-rm
title: Processo Modularizado de Montagem de Participantes
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+Modularizado+de+Montagem+de+Participantes
version: 3
---

**Processo Modularizado de Montagem de Participantes**

O Processo Modularizado de Montagem de Participantes tem como objetivo fornecer uma infraestrutura para criação e manipulação de estrutura hierárquica e genérica de avaliadores e seus avaliados. Essa estrutura pode ser utilizada em qualquer módulo do sistema que possui estrutura de avaliadores/avaliados.

**1 – Montagem da estrutura de Avaliador/Avaliado**

A montagem da estrutura de Avaliador/Avaliado pode ser feita das seguintes formas: Automática, Manual ou pela Importação de arquivo XML.

Nos tipos de montagem Automática e Manual os avaliados são carregados baseados nos parâmetros de Elegibilidade:

Estrutura de lotação: Considera todos os participantes que estejam lotados em seção com chefia direta do Avaliador. Exceto quando a opção "Supervisores" estiver marcada e o participante pertencer a uma equipe.

Estrutura de hierarquia: Considera os participantes que são chefes de seções diretamente abaixo da seção com chefia do Avaliador. Exceto quando a opção "Supervisores" estiver marcada e o participante pertencer a uma equipe.

Supervisores: Serão considerados como Avaliados do supervisor, qualquer participante que faça parte da equipe no qual o mesmo é supervisor, independente da seção e da chefia onde o participante esteja lotado.

**Atenção:**

- Se o parâmetro "Tipo de Gestão Hierárquica" (Configurações|Parametrizador|Preferências) estiver definido "Por Posição" ao configurar uma avaliação de desempenho será considerado a Gestão de Hierarquia ativa no sistema e as opções acima de elegibilidade serão desconsideradas. Apenas estará disponível o filtro de seleção de funcionário dentre as opções de elegibilidade. - O filtro "Avaliadores" deverá retornar líderes conforme Gestão de Hierarquia ativa.  
Maiores informações sobre a Gestão de Hierarquia consulte o Help.

**1.1 – Tipo de montagem: Automática**

A montagem automática é realizada em uma única etapa com a seleção dos participantes em foco pelas informações de Pessoas, Funcionários, Chefes ou Supervisores. Serão carregados todos os selecionados. Os participantes secundários serão carregados automaticamente ao final do processo.

**1.2 – Tipo de montagem: Manual**

A montagem manual é realizada em duas etapas:

    1.2.1 – Primeira etapa: seleção dos participantes em foco pelas informações de Pessoas, Funcionários, Chefes ou Supervisores.

    1.2.2 – Segunda etapa: seleção manual dos participantes em foco na "grid" à direita, arrastando e soltando na árvore da esquerda. Os participantes secundários serão carregados automaticamente durante essa etapa do processo.

**1.3 – Tipo de montagem: Importação XML** A montagem por importação de XML carregará toda a estrutura Avaliador/Avaliado através do arquivo XML ao finalizar o processo. A estrutura do arquivo deve estar de acordo com o padrão abaixo. Tal estrutura pode ser exportada ao clicar no ícone "Exportar XML". <?xml version="1.0" encoding="UTF-8"?> <participantes> <participante>     <codcoligadaavaliador>1</codcoligadaavaliador>     <chapaavaliador>00001</chapaavaliador>     <codtipoavaliador>2</codtipoavaliador>     <codcoligadaavaliado>7</codcoligadaavaliado>     <chapaavaliado>00015</chapaavaliado> </participante> <participante>     <codcoligadaavaliador>6</codcoligadaavaliador>     <chapaavaliador>00015</chapaavaliador>     <codtipoavaliador>1</codtipoavaliador>     <codcoligadaavaliado>6</codcoligadaavaliado>     <chapaavaliado>00015</chapaavaliado> </participante> <participante>     <codcoligadaavaliador>1</codcoligadaavaliador>     <chapaavaliador>00001</chapaavaliador>     <codtipoavaliador>2</codtipoavaliador>     <codcoligadaavaliado>1</codcoligadaavaliado>     <chapaavaliado>00003</chapaavaliado> </participante> <participante>     <codcoligadaavaliador>1</codcoligadaavaliador>     <chapaavaliador>00003</chapaavaliador>     <codtipoavaliador>1</codtipoavaliador>     <codcoligadaavaliado>1</codcoligadaavaliado>     <chapaavaliado>00003</chapaavaliado> </participante> <participante>     <codcoligadaavaliador>1</codcoligadaavaliador>     <chapaavaliador>00001</chapaavaliador>     <codtipoavaliador>2</codtipoavaliador>     <codcoligadaavaliado>1</codcoligadaavaliado>     <chapaavaliado>00004</chapaavaliado> </participante> </participantes>

**Atenção**

Participante em foco: determina quais são os personagens principais e secundários, com as seguintes opções:

  - Foco nos avaliadores: determina que os avaliadores serão os personagens principais e os avaliados serão os personagens secundários.

  - Foco  nos avaliados: contrário ao item anterior. O padrão é considerar o Foco nos Avaliadores, ficando os Avaliados como secundários. Clicando com o botão direito sobre o participante é possível "Excluir participante" ou "Visualizar dados da pessoa".

**Observação**  
A tabela VADTPAVALIADOR contém os dados do código tipo avaliador utilizado na montagem do arquivo XML:  
1 - ProprioAvaliado  
2 - Gestor  
3 - Subordinado  
4 - Cliente  
5 - Fornecedor  
6 - Funcionario  
7 - Outro
