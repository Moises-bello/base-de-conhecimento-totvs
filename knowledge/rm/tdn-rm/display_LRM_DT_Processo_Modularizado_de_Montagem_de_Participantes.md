---
content_hash: 809c9297002220be0ec4823fe7176407caae0783314cbc47ff106a813ae6f7e8
fetched_at: '2026-06-29T00:06:27.179980+00:00'
page_id: '231899449'
product: rm
source: tdn-rm
title: DT_Processo_Modularizado_de_Montagem_de_Participantes
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Processo_Modularizado_de_Montagem_de_Participantes
version: 1
---

# Processo Modularizado de Montagem de Participantes

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Versões/Release:** | *12.1.4* |

## Descrição

O Processo Modularizado de Montagem de Participantes tem como objetivo fornecer uma infraestrutura para criação e manipulação de estrutura hierárquica e genérica de avaliadores e seus avaliados. Essa estrutura pode ser utilizada em qualquer módulo do sistema que possui estrutura de avaliadores/avaliados.

## Procedimento para Utilização

**1 – Montagem da estrutura de Avaliador/Avaliado**

A montagem da estrutura de Avaliador/Avaliado pode ser feita das seguintes formas: Automática, Manual ou através de Importação de arquivo XML. Nos tipos de montagem Automática e Manual os avaliados são carregados baseados nos parâmetros de Elegibilidade:

Estrutura de lotação: Considera todos os participantes que estejam lotados em seção com chefia direta do Avaliador. Exceto quando a opção “Supervisores” estiver marcada e o participante pertencer a uma equipe.   
Estrutura de hierarquia: Considera os participantes que são chefes de seções diretamente abaixo da seção com chefia do Avaliador. Exceto quando a opção “Supervisores” estiver marcada e o participante pertencer a uma equipe.   
Supervisores: Serão considerados como Avaliados do supervisor, qualquer participante que faça parte da equipe no qual o mesmo é supervisor, independente da seção e da chefia onde o participante esteja lotado.

**1.1 – Tipo de montagem:** **Automática**

A montagem automática é realizada em uma única etapa com a seleção dos participantes em foco pelas informações de Pessoas, Funcionários, Chefes ou Supervisores. Serão carregados todos os selecionados. Os participantes secundários serão carregados automaticamente ao final do processo.

**1.2 – Tipo de montagem: Manual**

   A montagem manual é realizada em duas etapas:   
  1.2.1 – Primeira etapa: seleção dos participantes em foco pelas informações de Pessoas, Funcionários, Chefes ou Supervisores.   
  1.2.2 – Segunda etapa: seleção manual dos participantes em foco na “grid” à direita, arrastando e soltando na árvore da esquerda. Os participantes secundários serão carregados automaticamente durante essa etapa do processo.

**1.3 – Tipo de montagem: Importação XML**

A montagem por importação de XML carregará toda a estrutura Avaliador/Avaliado através do arquivo XML ao finalizar o processo. A estrutura do arquivo deve estar de acordo com o padrão abaixo. Tal estrutura pode ser exportada ao clicar no ícone “Exportar XML”.

**Atenção**

Participante em foco: determina quais são os personagens principais e secundários, com as seguintes opções:   
- Foco nos avaliadores: determina que os avaliadores serão os personagens principais e os avaliados serão os personagens secundários.   
- Foco nos avaliados: contrário ao item anterior.

O padrão é considerar o Foco nos Avaliadores, ficando os Avaliados como secundários.   
Clicando com o botão direito sobre o participante é possível “Excluir participante” ou “Visualizar dados da pessoa”.

Em caso de dúvidas consulte o help do aplicativo ou entre em contato pelo Help Desk.
