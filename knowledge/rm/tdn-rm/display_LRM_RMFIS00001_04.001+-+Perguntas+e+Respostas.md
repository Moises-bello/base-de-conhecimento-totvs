---
content_hash: 9855869288d0ad9cf711b733a90e08cac0cfc71f87285fa5d41cd37daee0ad82
fetched_at: '2026-06-29T00:06:00.267888+00:00'
page_id: '195300244'
product: rm
source: tdn-rm
title: RMFIS00001_04.001 - Perguntas e Respostas
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00001_04.001+-+Perguntas+e+Respostas
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: todas** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 27/07/2015 |

**Como gerar as informações sobre o L210?**

O Registro L210 – Informativo da Composição de Custos será gerado a partir do Plano de Contas Paralelo da Gestão Contábil.

A estrutura do registro L210 está disponível no Portal do Cliente – Downloads e Atualizações (<https://suporte.totvs.com/download>) arquivo: [PLANOREFERENCIAL\_ATUAL.ZIP](https://suporte.totvs.com/download#13).

Passo a passo:

* Acesse a Nova MDI | BackOffice | Gestão Contábil | Cadastros | Paralelo
* Crie a estrutura do Plano de Contas, clicando em “Incluir”
* Preencha as informações solicitadas e na instituição responsável selecione “**Outras Estruturas**”
* Salve.
* Execute o processo “**Importação de Contas via arquivo TXT**”.
* Associe as Contas Contábeis às linhas da estrutura importada, através do Anexo “**Contas Paralelas**”

Essa estrutura deve ser associada nos Parâmetros Contábeis do Anexo “**Parâmetros – Escrituração Contábil Fiscal**” do Cadastro da Filial.
