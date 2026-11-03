---
content_hash: 106ab69775ea94e0c2447da6b138bc3bdb0e65d1c5ddc7f17fda20bb383130f3
fetched_at: '2026-06-29T00:06:00.198840+00:00'
page_id: '195299963'
product: rm
source: tdn-rm
title: RMFIS00012_04 - Estrutura do Registro L210 (apenas para Lucro Real)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=195299963
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: 11.82.38 e superiores** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 29/07/2015 |

Este Registro apresenta a composição dos custos dos produtos de fabricação própria vendidos e custos dos serviços prestados no período para as empresas que utilizam o inventário permanente.

**Como será tratado no módulo contábil?**

As informações a serem geradas neste registro serão controladas pelo recurso do “Plano Paralelo” e mapeamento para as contas contábeis, ou seja, ao gerar a ECF o sistema vai gerar o registro L210 baseado nas contas paralelas e os valores serão calculados conforme as contas contábeis mapeadas.

**Importação da Tabela Dinâmica**

Disponibilizaremos o arquivo “**L210\_ INFORMATIVO DE COMPOSIÇÃO DE CUSTOS.txt**” contendo os itens da tabela dinâmica do registro L210 que deverá ser importado pelo usuário utilizando o recurso de importação de contas paralelas via arquivo TXT, disponível na visão do plano paralelo.

**Dicas:**

* Cadastrar a capa do Plano de Contas Paralelo com máscara igual a “##”
* Ao importar desmarcar a opção “Identificar/Atualizar máscara automaticamente”
* Marcar a opção “Não validar níveis da máscara”
* No campo “Instituição Responsável” do cadastro do plano de contas paralelo, selecionar a opção “Outras Estruturas”.

**Procedimentos:**

1. O usuário deverá mapear a conta contábil a respectiva conta paralela que representa a composição do custo conforme características de sua empresa.
2. No Anexo "Parâmetros Escrituração Contábil Fiscal" - Parâmetros Contábeis, na aba “Lucro Real” informar o plano paralelo que representa o “Informativo de Composição de Custos”.

**Processamento do registro na geração da ECF:**

* O sistema calculará o valor a ser gerado baseado nos saldo das contas contábeis associada às contas paralelas que representa o informativo de composição de custo.
* Será considerado o saldo da conta contábil antes do encerramento, ou seja, desconsidera todos os histórico de fechamento.
* Serão gerados valores sempre absolutos, ou seja, se o valor processado for negativo será enviado positivo (regra do manual do layout).
* Serão gerados somente as contas paralelas que a data de vigência esteja entre o período da escrituração.
