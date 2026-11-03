---
article_id: 23948760944663
category: Alterações Globais
content_hash: 954f44ecf07d0fe476b4720c67ed4c3883a0ecb8c6926b9e97a5a4029e27b64e
fetched_at: '2026-06-28T22:46:27.039583+00:00'
product: rm
section_id: 6045417448343
source: central-rm
title: RH - RM - PTO - Menu Cartão de Ponto
type: support-article
updated_at: '2026-03-16T12:26:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23948760944663-RH-RM-PTO-Menu-Cart%C3%A3o-de-Ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23948745060247) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Detalhes do menu de processo global de utilização do cartão de ponto.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões

**Solução**

No caminho **Cadastros | Alterações Globais | Cartão de Ponto**, pode ser realizado, alterações sobre o uso do cartão de ponto, permitindo que os funcionários participem de todo o processo de coleta de marcações e apuração de ponto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29033889768983)

Atualmente, por padrão, os novos funcionários não utilizam cartão de ponto, então é necessário executar o processo de utilizar o cartão de ponto, para que sejam realizadas a coleta e tratativas do ponto do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23949640642839)

Nessa tela é utilizada para identificar se o funcionário utiliza ponto no período atual, utiliza o ponto parcialmente no período atual, ou não utiliza ponto no período atual.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29033857671319)

**Observações:**  Na coluna utiliza ponto no período atual, a legenda:

* Bolinha azul: Utiliza ponto no período atual/ativo
* Bolinha contorno azul fundo branco:  utiliza ponto parcialmente no período atual/ativo
* Bolinha vermelha: não utiliza ponto no período atual/ativo

Através do menu **Processos**, é possível alterar o status do funcionário no ponto, podendo optar pelos itens do menu.

* **Utiliza Cartão de Ponto**: Abrirá uma tela para ser informada a data de quando os funcionários selecionados na visão passarão a bater ponto e ser considerado em todo o processo de apuração.
* **Deixar de Utilizar Cartão de Ponto:**Abrirá uma tela para ser informada a data de quando os funcionários selecionados na visão deixarão de bater ponto e não ser mais considerados no processo de apuração.

**Observações:**

**1)** Se existe algum movimento no período anterior, não poderá fazer NENHUMA exclusão.  
**2)** A tabela AHSTUTILIZAPONTO - histórico de utilização de cartão de ponto, somente será preenchida para os novos funcionários, após executar o processo de utilizar o cartão de ponto.

**3)** Validar se é necessário excluir item do histórico caso necessite utilizar em todo período atual.

**4)** O sistema passou a validar a data do histórico de utilização do cartão de ponto ao inserir batidas.

**Exemplo**: Funcionário possui os seguintes históricos:

Data início utiliza cartão     - 01/09/2021

Deixou de utilizar o cartão - 06/09/2011

Voltou a utilizar o cartão    - 10/09/2021

**No menu anexo:** Histórico de utilização de cartão de ponto Visão que mostra os períodos em que o funcionário utilizou ou não cartão de ponto. Há uma opção de exclusão para permitir desfazer possíveis erros de lançamento.

**Saiba mais**  
[RH - RM - PTO - Utilizar cartão de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004113861-RH-RM-PTO-Utilizar-cart%C3%A3o-de-ponto)

[RH - RM - PTO - Excluir Histórico de Utilização do Cartão de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024457232)

[Cartão de Ponto](https://tdn.totvs.com/pages/releaseview.action?pageId=452719087)
