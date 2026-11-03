---
content_hash: e5070cfc9ad83ed26a66913ada95176eda81e5c4c9d63b4e838a7aabeff206cb
fetched_at: '2026-06-29T00:08:13.298479+00:00'
page_id: '243662294'
product: rm
source: tdn-rm
title: SAUHRM01-395_COPIA_CAMPOS_ENDERECO_PACIENTE
type: documentation
url: https://tdn.totvs.com/display/LRM/SAUHRM01-395_COPIA_CAMPOS_ENDERECO_PACIENTE
version: 2
---

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | GESTÃO HOSPITALAR - RM | Módulo | REGISTROS DE ATENDIMENTOS EXTERNOS |
| Segmento Executor | Saúde |  |  |
| Projeto¹ | R\_SAU\_HRM1516 | IRM¹ | SAUHRM01-392 |
| Requisito¹ | SAUHRM01-395 | SubTarefa¹ | SAUHRM01-488 |
| Chamado² |  |  |  |
| Release de Entrega Planejada | Não definido | Réplica | Não necessário |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

No registro de atendimento de pacientes externos, se vários membros de uma mesma família forem atendidos e estes residirem no mesmo local, o atendente poderá copiar em memória do sistema o endereço de um dos membros da família e replicar para os demais cadastros.   
 **RN001** – Após digitação do endereço do paciente o atendente poderá clicar com o botão direto e o sistema abrirá um menu suspenso com as opções de "Copiar Endereço" e "Colar Endereço".  
 **RN002** – No registro de um novo paciente o atendente terá que efetuar a cópia novamente para subscrever os dados copiados anteriormente.   
 **RN003 –** Caso haja necessidade de sair da tela Registro de atendimentos Externos os dados terão que ser copiados novamente para a memória do sistema.

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Registro de Atendimento Externo | Alteração | Atendimento/Pronto Atendimento /Ambulatório/Registro de atendimentos externos |

# Escopo Negativo

Não haverá cadastro para guardar os atendimentos copiados. Após o atendente sair da tela de atendimentos externos as informações em memoria serão descartadas.  
 \_GoBack

# \_Toc355276665Protótipo de Tela

As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema.  
 Tela – Os Campos sinalizados nos quadros em vermelhos serão copiados em memória e posteriormente colados.

|  |  |
| --- | --- |
| **RI-001** | Se não existirem dados em memória para serem colados a opção de "Colar" não ficará habilitado no menu suspenso. |
| **RI-002** | Se o atendente sair da tela de Registro de Atendimentos Externos os dados em memória serão perdidos. Haverá necessidade de cópia novamente. |
|  |  |

# \_Toc355276667Fluxo do Processo

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.
