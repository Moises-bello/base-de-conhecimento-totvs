---
content_hash: 2da876f6028529564d958be79bc38f04d3a0e0d6163c1384782c813d30da77d3
fetched_at: '2026-06-29T00:08:31.927028+00:00'
page_id: '273975232'
product: rm
source: tdn-rm
title: ER SAUHRM02-985 Substituição de prestador na conta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273975232
version: 2
---

|  |
| --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |

Nenhuma anotação efetuada a mão ou rasura no documento será considerada válida.

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| **Produto** | Gestão hospitalar RM | **Módulo** | Faturamento |
| **Segmento Executor** | Saúde |  |  |
| **Projeto¹** | R\_SAU\_HRM1617 | **IRM¹** | SAUHRM02-984 |
| **Requisito¹** | SAUHRM02-985 | **SubTarefa¹** | SAUHRM02-986 |
| **Chamado²** | 692872 |  |  |
| **Release de Entrega Planejada** | Não definido | **Réplica** | Não necessário |
| **País** | **(**X **) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador**   **(  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_.** |  |  |
| **Outros** |  |  |  |

# \_Toc355276661\_Toc355276662Objetivo

Permitir a apresentação do hospital como prestador na conta hospitalar, mantendo a indicação do médico responsável pelo atendimento.  
 \_Toc355276664

# Definição da Regra de Negócio

**RN001 –** Possibilitar a indicação do hospital como prestador na seção de honorários da conta do paciente (***substituição de prestador na conta***).   
 **RN002 –** A aplicação será automática, configurável e deverá respeitar os seguintes critérios:

* + - Especialidade do atendimento;
    - Unidade;
    - Tipo de atendimento;
    - Convênio;
    - Tipo de procedimento.   
       **RN003 –** Cabe ressaltar que as regras de repasse não serão influenciadas por esta alteração.  
       Esta regra deve somente será para a substituição de prestador, e não afetando os critérios de repasse já existentes no sistema (Ver telas RI005).

      |  |  |  |
      | --- | --- | --- |
      | Rotinas Envolvidas |  |  |
      | **Rotina** | **Tipo de Operação** | **Opção de Menu** |
      | Cadastros | Inclusão | Cadastros > Faturamento > Substituição de prestador na conta |
      | Faturamento | Inclusão | Elaboração da conta |
      | Lançamento nas guias\Autorização | Alteração | Atendimento > Pronto atendimento/Ambulatório > Registro de atendimentos externos |
      | Autorização\ Pedidos de exames | Alteração | Atendimento > Pronto atendimento/Ambulatório > Registro de atendimentos externos |
      | Registro de informações cirúrgicas | Alteração | Cuidados com o paciente > Centro cirúrgico > Registro de informações cirúrgicas |

      # \_Toc355276665Protótipo de Tela

      As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema, devem ser utilizadas apenas para exemplificar a forma de iteração que os usuários possuirão ao acessar o HIS, o fluxo de negócio e a forma em que os dados e informações serão manipuladas.

      ## \_Toc355276666Configuração de Ordenação de Leitos por Unidade

      |  |  |
      | --- | --- |
      | **Função** | Consiguração para substituição de prestador na conta |
      | **Objetivo** | Permitir a parametrização da regra de substituição de prestador |
      | **Módulo** | Faturamento |
      | **Menu** | Cadastros > Faturamento > Configuração de substituição de prestador na conta |

      |  |  |
      | --- | --- |
      |  | **Regras de Interface** |
      | **RI-001** | Criar um item de menu chamado SUBSTITUIÇÃO DE PRESTADOR NA CONTA em CADASTRO>>>FATURAMENTO, abaixo do ítem REGRA PARA LANÇAMENTO DENTRO OU FORA DA CONTA, conforme imagem: |
      | **RI-003** | \_GoBackA inclusão de uma nova regra para substituição se dará a partir da tela iluastrada a seguir.   Esta tela deverá ser dividida em duas abas, onde o usuário definirá os parâmetros para a substituição e posteriormente à que convênios a regra se aplica. |
* Deverá ser possível que o usuário selecione a opção TODOS para as todas as opções em tela.|

  |  |  |
  | --- | --- |
  | **RI-004** | A seguir, exemplificação de como o processo se desenvolverá a partir das alterações solicitatas: |

1. **Configuração da regra de substituição:**
2. **Atendimento com enquadramento nos parêmetros:**   
      
    **Atendimento com os parâmetros definidos na regra**
3. **Consulta registro na conta:**   
      
       
    |   

   # \_Toc355276667Fluxo do Processo

   Não necessário para o desenvolvimento deste requisito.

   # Dicionário de Dados

   Não necessário para o desenvolvimento deste requisito.

   # Grupo de Perguntas

   Não necessário para o desenvolvimento deste requisito.

   # **Consulta Padrão**

   Não necessário para o desenvolvimento deste requisito.

   # Estrutura de Menu

   Não necessário para o desenvolvimento deste requisito.

   # Assinaturas

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   | Nome | Cargo | Data | Ação | Assinatura |
   | Cleber Silveira | Analista de Negócio |  | Autor |  |
   | Ricardo Gomes de Lima | Analista de Negócio |  | Revisor |  |
   | Joji Tamekuni | Líder de Equipe de Desenvolvimento |  | Aprovador |  |
   | Fernanda Sírio | Consultora Especialista |  | Aprovadora |  |
   | Mariana Cruz | Líder de Equipe de Engenharia |  | Aprovadora |  |
   | Daniel Solari | Coordenador de Desenvolvimento |  | Revisor |  |
