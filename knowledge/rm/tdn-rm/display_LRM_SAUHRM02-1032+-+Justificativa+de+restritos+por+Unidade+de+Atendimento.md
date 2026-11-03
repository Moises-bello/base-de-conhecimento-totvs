---
content_hash: 43dd10ae66b3db2279c8f5bb4740a148ecd1764e6c000de29f000fa7244bd52a
fetched_at: '2026-06-29T00:08:32.059571+00:00'
page_id: '273982388'
product: rm
source: tdn-rm
title: SAUHRM02-1032 - Justificativa de restritos por Unidade de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/SAUHRM02-1032+-+Justificativa+de+restritos+por+Unidade+de+Atendimento
version: 1
---

|  |
| --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |

Nenhuma anotação efetuada a mão ou rasura no documento será considerada válida.

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| **Produto** | GESTÃO HOSPITALAR - RM | **Módulo** | Cadastro |
| **Segmento Executor** | Saúde |  |  |
| **Projeto¹** |  | **IRM¹** |  |
| **Requisito¹** | SAUHRM02-1031 | **SubTarefa¹** | 1. SAUHRM02-1032 |
| **Chamado²** |  |  |  |
| **Release de Entrega Planejada** | Não definido | **Réplica** | Não necessário |
| **País** | **(**X **) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador**   **(  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_.** |  |  |
| **Outros** |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

Criar configuração por unidade de atendimento para que no momento da prescrição médica o sistema solicite uma justificativa para o medicamento em questão.  
\_Toc355276664

# Definição da Regra de Negócio

**RN001 –** Deverá ser criado um anexo **em unidades de Atendimentos** para informar quais produtos irão requerer a justificativa;
  
**RN002** – Se o medicamento inserido neste cadastro não necessitar mais de Justificativa o sistema deverá permitir a exclusão do mesmo deste cadastro;
  
**RN003 –** A o prescrever um medicamento o sistema deverá verificar neste cadastro a necessidade ou não da justificativa;
  
**RN004** **–** A justificativa a ser preenchida é a já existente no sistema.

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Cadastros | Inclusão | Cadastros > Uso Geral > Unidades de Atendimentos >Anexos |
|  |  |  |

# \_Toc355276665Protótipo de Tela

As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema, devem ser utilizadas apenas para exemplificar a forma de iteração que os usuários possuirão ao acessar o HIS, o fluxo de negócio e a forma em que os dados e informações serão manipuladas.  
\_Toc355276666

|  |
| --- |
| **Protótipos** |
| Tela 1 – Em Anexos criação da Opção de Justificativa Medicamentos Restritos |
| Tela 2 – Tela Para Inclusão do medicamento que terá Justificativa\_GoBack |
| Tela 3 – Ao prescrever o Item que foi cadastrado no **"Medicamentos para requerimento de Justificativa**" o sistema apresentará a tela de Justificativa. |

|  |  |
| --- | --- |
|  | **Regras de Interface** |
| **RI-001** | Na tela 2 – No cadastro **"Medicamentos para requerimento de Justificativa**" a seleção deverá trazer somente medicamentos   Na Tela 3 - No momento da prescrição médica ao prescrever um medicamento que estiver neste cadastro o sistema deverá solicitar a Justificativa |

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
