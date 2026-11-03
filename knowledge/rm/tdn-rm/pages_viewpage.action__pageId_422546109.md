---
content_hash: 829fe597d205c614029b5f535006e4ad83065a877acebc88f0b9420a6da0eb48
fetched_at: '2026-06-29T00:09:23.726727+00:00'
page_id: '422546109'
product: rm
source: tdn-rm
title: Natureza de Operação do ISS (NFS-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546109
version: 2
---

Devido a diversidade de códigos existente entre prefeituras, foi criado o cadastro com intuito de atender a NFS-e. A tabela default possui situações mapeadas como sendo as situações mais comuns utilizadas pelo usuário. Os dados serão gravados no tributo ISS do movimento de NFS-e que será gerado no XML da mesma. Caso seja criada uma nova coligada, será necessário executar o processo "Incluir Cadastro de Naturezas de Operação da NFS-e Default" deste cadastro.  
Criada a tela "Natureza de Operação do ISS" onde o usuário visualiza as naturezas de operação do ISS que foram cadastradas para a coligada. Nesta tela o usuário somente visualiza os campos não sendo possível as seguintes ações:

* Incluir um novo registro;
* Editar os registrados cadastrados;
* Excluir.

Criada a tela de anexo "Codificação para a Natureza de operação do ISS" onde o usuário pode cadastrar uma codificação que esta relacionada a "Natureza de Operação do ISS" para a coligada. Nesta tela o usuário pode realizar seguintes ações:

* Incluir somente uma Codificação para a Natureza de Operação do ISS por filial;
* Editar;
* Excluir.

***Observação*.:** Caso seja criada uma nova coligada é necessário executar este processo para a inclusão das naturezas de operação do ISS default da NFS-e.

**Codificação para a Natureza de Operação do ISS**

O usuário seleciona a "Natureza de Operação do ISS" e ao clicar no botão incluir da tela de anexo "Codificação para a Natureza de operação do ISS" será salvo um único registro por "Natureza de Operação do ISS".  
Segue abaixo exemplo de cadastro para a natureza de operação do ISS no modelo "Padrão ABRASF".

***Observação*.:** Valores mostrados abaixo serão utilizados como exemplo, os valores corretos serão de responsabilidade de cada prefeitura.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **ID** | **Descrição** | **NatOp - No Mun.** | **NatOp - Fora Mun.** | **NatOp - Exterior** |
| 1 | Tributada | 1 | 2 | - |
| 2 | Isenta | 3 | 3 | 3 |
| 3 | Imune | 4 | 4 | 4 |
| 4 | Não Incidência | - | - | - |
| 5 | Exigibilidade Suspensa por decisão judicial | 5 | 5 | 5 |
| 6 | Com Deduções/Materiais | 6 | 6 | 6 |
| 7 | Devolução/Simples Remessa | - | - | - |
| 8 | ISS Fixo | - | - | - |
| 9 | Retido pelo Tomador | - | - | - |

***Exemplo*:** Ao incluir um movimento de Saída/Entrada na aba de Tributação, o campo de "Natureza de Operação do ISS" do tributo ISS será preenchido com "1" se Operação Tributada dentro do Município e "2" se Operação Tributada Fora do Município.
