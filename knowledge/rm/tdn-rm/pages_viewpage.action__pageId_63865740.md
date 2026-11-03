---
content_hash: 1be4d7d9816a3da8d241ad9ba9f46069c3a01505f284d08bcd448ba6ef04140f
fetched_at: '2026-06-29T00:11:06.993331+00:00'
page_id: '63865740'
product: rm
source: tdn-rm
title: Geração de Guias Tributos Retidos - CSRF, PISRF e COFINSRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63865740
version: 26
---

|  |  |
| --- | --- |
| **Produto** | TOTVS Gestão Fiscal |
| **Versão** | 11.52 |
| **Processo** | Geração de Guia a partir de Lançamentos Financeiros |
| **Data da publicação** | 28/06/2013 |

 Através dessa documentação é possível que o usuário tenha melhor entendimento em relação a geração da guias  no [TOTVS Gestão Fiscal](https://tdn.totvs.com/pages/viewpage.action?pageId=198948859) de valores retidos do [TOTVS Gestão Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=198948854).

Os tributos retidos serão [apurados](https://tdn.totvs.com/pages/viewpage.action?pageId=422545773) no  desde que haja lançamentos financeiros com retenção de tributos no T[OTVS Gestão Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=198948854) com [código de receita](https://tdn.totvs.com/pages/viewpage.action?pageId=421388788), base, alíquota, valor do tributo retido e também que esteja com o status de "[baixado](https://tdn.totvs.com/pages/viewpage.action?pageId=421388668)".

        

**LANÇAMENTO FINANCEIRO**

* Sera gerado através do lançamento financeiro que possui tributos retido.

* Na baixa do lançamento financeiro que possui o tributo retido será gerado um lançamento automaticamente com o valor do tributo a ser apurado

O lançamentos financeiro pode ser também rastreado através do processo [Rastreabilidade do Lançamento](https://tdn.totvs.com/pages/viewpage.action?pageId=421388752)

 **PROCESSO DE GERAÇÃO DA GUIA**

* Antes de qualquer procedimento, observe se o status do período de apuração do tributo esteja "Encerrado"

 ***Observação***: a guia só será gerada na filial Matriz definida nos parâmetros do TOTVS Gestão Fiscal

* Basta selecionar o período de apuração do tributo e executar o processo de "Geração de Guias a partir de Lançamentos Financeiros"

* Será apresentada a tela para informar os dados da "Geração da Fatura"

* Após a execução do processo é possível visualizar o valor apurado e a guia gerada

 **Atenção** aos possíveis erros do processo:

 Verifique:

Se o lançamento financeiro gerou retenção do tributo apurado?

O processo já foi executado?

A data da baixa do lançamento financeiro condiz com a data do período de apuração selecionado?

O TOTVS Gestão Fiscal está integrado com o TOTVS Gestão Financeira?

O parâmetro "Lançamentos serão Faturados no RM Liber" está habilitado?

Na linha do tributo retido no lançamento financeiro possui código de receita?

Os lançamentos financeiros gerados ao baixar o lançamento de origem possui o mesmo tipo contábil?

Ao contrário o sistema apresentará a seguinte mensagem:

Para maiores informações:

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
