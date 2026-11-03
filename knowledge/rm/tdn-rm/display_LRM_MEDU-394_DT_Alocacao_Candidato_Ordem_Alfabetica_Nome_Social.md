---
content_hash: b7ffd5fed970cdf296ae2f17d05728e24b8d22a6793843ec5b1995829f016947
fetched_at: '2026-06-29T00:08:21.477049+00:00'
page_id: '268825919'
product: rm
source: tdn-rm
title: MEDU-394_DT_Alocacao_Candidato_Ordem_Alfabetica_Nome_Social
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-394_DT_Alocacao_Candidato_Ordem_Alfabetica_Nome_Social
version: 111
---

# ALOCAR CANDIDATOS EM LOCAIS DE PROVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Processo Seletivo** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de candidatos através do portal* | *N/A* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Dados do candidato** | *N/A* | | *Inscrição de candidatos *através do portal** | *N/A* | | *Cadastro de candidatos através do portal* | *N/A* | | *Dados pessoais *através do portal** | *N/A* | |
| **Cadastros Iniciais:** | *Nome social cadastrado nos dados da pessoa* |
| **Parâmetro(s):** | - |
| **Ponto de Entrada:** | *Portal do processo seletivo:*   * *Portal do processo seletivo | Cadastro de candidato* * *Portal do processo seletivo | Cadastro de responsáveis* * *Portal do processo seletivo | Acesso usuário | Dados pessoais* * *Dados do candidato* |
| **Chamados Relacionados** | **N/A** |
| **Requisito (ISSUE):** | - |
| **País(es):** | - |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *PPESSOA*  *SPSLOCALETAPAINSCRITO* |
| **Sistema(s) Operacional(is):** | - |

## Descrição

Ao executar o processo de 'Alocar candidatos em locais de prova' é possível utilizar o nome do candidato em ordem alfabética para alocação, porém com a inclusão do campo nome social, a ordenação não reconhece este campo, o que pode gerar dúvidas na alocação, sendo assim, foi feito um ajuste no processo de alocação para que se selecionado a opção para alocar por ordem alfabética também possa considerar o nome social, caso o nome social esteja preenchido para o candidato e a opção para considerar o nome social na ordem alfabética esteja selecionada.

## Procedimento para Implantação

```
A opção para alocar candidatos pelo nome em ordem alfabética utilizando também o campo 'nome social' estará disponível a partir da versão 12.1.15 sendo necessário selecionar as opções conforme necessidade.
```

**Observação**: por padrão a opção para considerar o nome social estará desabilitada e só será habilitada se a opção para alocar por ordem alfabética for selecionada.

## Procedimento para Utilização

## Sistema

Ao executar o processo de alocar candidatos em locais de prova será exibida uma nova opção 'Considerar nome social na ordem alfabética', está opção ficará desabilitada e só estará disponível para seleção se a opção 'Alocar candidatos por ordem alfabética' for marcada.

divs
