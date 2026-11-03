---
content_hash: 528dd5bf43690a58a55ac6e3405e10b1afb3969301f5ff806bf9cf093a77ea7e
fetched_at: '2026-06-29T00:08:16.483639+00:00'
page_id: '247171246'
product: rm
source: tdn-rm
title: ER SAUHRM02-333 Controle e Pedido de Exames - Parâmetros para Nova Integração
  PACS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=247171246
version: 2
---

|  |
| --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo** **extremamente** **técnico.** |

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | TOTVS Gestão Hospitalar - RM | Módulo | Parâmetros Gerais |
| Segmento Executor | Saúde |  |  |
| Projeto¹ | R\_SAU\_HRM1617 | IRM¹ | SAUHRM02-1045 |
| Requisito¹ | SAUHRM02-333 | SubTarefa¹ | SAUHRM02-1047 |
| Chamado² | TUTQH0 |  |  |
| Release de Entrega Planejada |  | Réplica |  |
| País | (x  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

# \_Toc355276661\_Toc355276662Objetivo

Criação de nova tela de parâmetros para possibilitar a configuração de mais um PACS no hospital.  
 Nesta nova tela de parâmetros será permitido o cadastro das informações de integração por **modalidade de exames** **e Unidade de atendimento.**  
 Também será alterada a URL da tela principal de parâmetros para possibilitar sua montagem em tempo de execução.

# \_Toc355276664Definição da Regra de Negócio

RN001 – Alteração do campo de endereço de visualização da Imagem. Para utilização deste, deverão ser criadas variáveis para que o sistema monte a URL em tempo de execução conforme PACIENTE e EXAME selecionados. Atualmente o sistema utiliza as seguintes informações para montagem da URL: - Acesionnumber, codpacientente e prontuário. Na tela 1 existe um exemplo de URL já montada.   
 RN002 –Nos parâmetros gerais criar um botão para chamada de tela para permitir configurações por modalidade.   
 RN003– Criar tela para permitir configurações por modalidade e unidade de atendimento(SZCONFIGMODIMAGEM).Nesta tela será possível a criação de parâmetros que permitirão ao cliente a utilização de mais de um PACS no hospital.   
 RN004 - No momento de realizar as integrações ou visualização das imagens o sistema deverá verificar se o exame pertence a uma modalidade cadastrada nos novos parâmetros, caso sim deverá utilizar esse cadastro. Se não existir configuração específica para a modalidade do exame o mesmo deve utilizar a parametrização já existente hoje. Desta forma não afetará a parametrização de clientes antigos.

# Fora do Escopo

* Outras informações que não estiverem descritas neste documento;.

|  |  |  |  |
| --- | --- | --- | --- |
| Rotinas Envolvidas |  |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Integração | Inclusão | Opções/Parametros/Parâmetros Gerais/"Unidade Diagnóstico II/ Carestream |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

# \_Toc355276665Protótipo de Tela

\_Toc355276666

|  |  |
| --- | --- |
| **Regras da Interface** |  |
|  |  |
| **RI-001** | Tela 1 – Criação de novo campo de parâmetros para Endereço de visualização da imagem, que possibilitará a configuração de mais um PACS no hospital. |
| **RI-002** | Tela 2 – Botão para chamada de tela para permitir configurações por modalidade (SZCONFIGMODIMAGEM). |
| **RI-003** | TELA 3 – Para configuração por Modalidade e Unidade de Atendimento. Estas são as mesmas informações que constam na tela principal com acréscimo da unidade de atendimento.     \_GoBack     Cabeçalho quando tipo de integração WebService. |

# \_Toc355276667Fluxo do Processo

# Dicionário de Dados

* Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

* Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

* Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

* Não necessário para o desenvolvimento deste requisito.
