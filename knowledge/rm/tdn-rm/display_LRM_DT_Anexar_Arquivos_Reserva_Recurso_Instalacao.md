---
content_hash: 57ad86a39cc4122dfec72280371154c1e193007246f94ccb843e4f39cb8e6ae2
fetched_at: '2026-06-29T00:08:27.328997+00:00'
page_id: '271407048'
product: rm
source: tdn-rm
title: DT_Anexar_Arquivos_Reserva_Recurso_Instalacao
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Anexar_Arquivos_Reserva_Recurso_Instalacao
version: 2
---

# ANEXAR ARQUIIVOS Á RESERVA DE RECURSO E INSTALAÇÃO

## 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| ****Segmento Executor:**** | Educacional | | |
| **Módulo:** | TOTVS Educacional | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Reserva de recurso e instalação | Reserva de recurso e instalação |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Processo de reserva de recurso | Processo de reserva de recurso*.* | | Processo de reserva de instalação | Processo de reserva de instalação | | Reserva de recurso | Reserva de recurso | | Reserva de instalação | Reserva de instalação | | Portal - reserva de recurso | Portal - reserva de recurso | | Portal - reserva de instalação | Portal - reserva de instalação | | | |
| **Requisito (ISSUE):** | EDUEDU001-705 | | |
| **País:** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

 Incluir arquivos à reserva de recurso e instalação através do processo de reserva ou pelo cadastro da reserva.

### Definição da Regra de Negócio

# Parametrização

No sistema, acessar: **Módulo Educacional | Configurações | Parâmetros  -> 15.01 - Secretária > Geral 7/7**

* Defina qual o tipo de armazenamento, as extensões de aquivos permitidas e o tamanho máximo de armazenamento (kb).

# Anexar arquivos à reserva no sistema

Acessar:****Módulo Educacional | Atividades acadêmicas | Infra-estrutura | Reserva de recurso e instalação****

Selecionar uma atividade agendada, executar o Processo de reserva de recurso ou o Processo de reserva de instalação:

* Informar o solicitante
* Definir os horários
* Escolher o recurso ou instalação
* Incluir informações adicionais
* Anexar arquivos, nesta etapa é possível incluir "N" arquivos à reserva de acordo com o parametrizado no sistema.

Para visualizar o arquivo vinculado à reserva: Selecionar à atividade agendada e ir em anexo reserva de recurso ou reserva de instalação, editar a reserva e ir anexo Arquivos anexos. 

**Importante**

Em Arquivos anexos o usuário poderá visualizar o arquivo anexado através do processo, incluir novos arquivos de acordo com o parametrizado nos parâmetros ou excluir um arquivo.

# Anexar arquivos à reserva no portal

Logar no portal educacional com perfil de professor ir em Reservar recurso ou Reservar instalação e clicar em "Fazer reserva". Incluir as informações da reserva e em arquivos anexo adicionar o arquivo e salvar a reserva.Após incluir a reserva é exibida a lista de reservas do professor, para visualizar o arquivo  anexado basta clicar em (+). Caso queira adicionar novos arquivos, clicar em "Enviar arquivo".

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Reserva de recurso | [Criação] | Atividades acadêmicas -> Infra-estrutura - > Reserva de recurso e instalação ->Processo reserva de recurso | - |
| Reserva de instalação | [Criação] | Atividades acadêmicas -> Infra-estrutura - > Reserva de recurso e instalação -> Processo reserva de instalação | - |
| Reserva de recurso | [Criação] | Atividades acadêmicas -> Infra-estrutura - > Reserva de recurso e instalação ->Reserva de recurso -> Anexar arquivos | - |
| Reserva de instalação | [Criação] | Atividades acadêmicas -> Infra-estrutura - > Reserva de recurso e instalação ->Reserva de instalação -> Anexar arquivos | - |
| Reserva de recurso Portal | [Criação] | Portal educacional - > Reservar recurso | - |
| Reserva de recurso Portal | [Criação] | Portal educacional - > Reservar instalação | - |
