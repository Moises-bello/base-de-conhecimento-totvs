---
content_hash: c7f247122a98c07a8abb79bfcc02a5837e083fc1e9e278d77f3bf5b3507eaf1e
fetched_at: '2026-06-29T00:08:20.717346+00:00'
page_id: '268585062'
product: rm
source: tdn-rm
title: TVYUDM_DT_Auto_Declaracao_CorRaca
type: documentation
url: https://tdn.totvs.com/display/LRM/TVYUDM_DT_Auto_Declaracao_CorRaca
version: 115
---

# CADASTRO DE CANDIDATOS E RESPONSÁVEIS - PORTAL DO PROCESSO SELETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Processo Seletivo - Portal** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de candidatos através do portal* | *N/A* | | *Cadastro de responsáveis *através do portal** | *N/A* | | *Dados pessoais *através do portal** | *N/A* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Inscrição de candidatos *através do portal** | *N/A* | |
| **Cadastros Iniciais:** | *Configuração dos parâmetros de dados pessoais para que seja definido se o campo nome social será visível e obrigatório para candidatos e responsáveis* |
| **Parâmetro(s):** | * + *Parâmetros do sistemas | Portal | Pessoa | Informações básicas | Candidato | Cor / Raça - Visível*   + *Parâmetros do sistemas | Portal | Pessoa | *Informações básicas | Candidato | Cor / Raça* - Obrigatório*   + *Parâmetros do sistemas | Portal | Pessoa | *Informações básicas | Responsáveis | Cor / Raça* - Visível*   + *Parâmetros do sistemas | Portal | Pessoa | *Informações básicas | Responsáveis | Cor / Raça* - Obrigatório* |
| **Ponto de Entrada:** | *Portal do processo seletivo:*   * *Portal do processo seletivo | Cadastro de candidato* * *Portal do processo seletivo | Cadastro de responsáveis* * *Portal do processo seletivo | Acesso usuário | Dados pessoais* |
| **Chamados Relacionados** | **N/A** |
| **Requisito (ISSUE):** | - |
| **País(es):** | - |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *PPESSOA*  *PCORRACA* |
| **Sistema(s) Operacional(is):** | - |

## Descrição

No cadastro de candidatos, é exibido o campo "cor/raça" (se configurado para exibir), na lista de opções de cor/raça, é exibido o item "Não informado", porém, este tipo não pode ser aceito, pois o candidato, quando virar um aluno precisa se auto declarar e o "não informado" não atende este declaração, que depois será enviada para CENSO ESCOLAR, sendo assim, o tipo "não informado" não será exibido na lista de cor/raça, para que no ato do cadastro do candidato, ele já preencha a opção correta. É permitido ainda que o candidato "não declare" sua cor/raça, sendo assim, existe o item "Não declarado", porém para que fique em conformidade com o processo seletivo, o texto desse item para o portal do processo seletivo foi alterado para "Não desejo declarar", sendo que nos demais cadastros da pessoa acessadas pela aplicação desktop, continuará como "Não declarado".

## Procedimento para Implantação

```
A alteração do item "Não declarado" para "Não desejo declarar" e a remoção do item "Não informado" do campo  "Cor / Raça" no portal do processo seletivo estará disponível a partir da versão 12.1.14.
```

```
Se o campo não estiver visível no portal do processo seletivo é necessário ativar os parâmetros do  campo conforme necessidade para que este se torne visível.
```

## Procedimento para Utilização

## Sistema

Configuração dos parâmetros que definem o campo como visível e obrigatório para candidatos e responsáveis:

### Portal do processo seletivo

Exibição do campo no cadastro de candidato no portal do processo seletivo:

Exibição do campo no dados pessoais no portal do processo seletivo:

divs
